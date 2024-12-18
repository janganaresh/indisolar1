from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Add a secret key for sessions

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nari@2058",  # Replace with your MySQL password
    database="newusers"
)

# Route to render the login.html page
@app.route('/')
def index():
    return render_template('login.html')

# Route for user login verification
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Users WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()

    if user:
        session['username'] = user['name']  # Store the username in the session
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"})

# Route for user creation
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    cursor = connection.cursor()
    try:
        query = "INSERT INTO Users (name, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, password))
        connection.commit()
        return jsonify({"success": True, "message": "User created successfully"})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error creating user: {e}"})

# Route for the home page
@app.route('/home')
def home():
    if 'username' in session:  # Check if the user is logged in
        return render_template('home.html', username=session['username'])
    return redirect(url_for('index'))

# Route for logging out
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)  # Remove the username from the session
    return redirect(url_for('index'))

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

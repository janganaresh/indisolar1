# Flask User Authentication System

This is a Flask-based web application for user registration and login. It includes functionalities for creating new users, verifying user credentials, and redirecting to a personalized home page after successful login. The application connects to a MySQL database to store and retrieve user information.

## Features

- **User Registration**: Allows users to create a new account by providing their name, email, and password.
- **Login System**: Users can log in using their email and password.
- **Session Management**: User sessions are managed to provide personalized content on the home page.
- **Responsive UI**: The interface is mobile-friendly, ensuring proper display on devices of various screen sizes.
- **Logout Functionality**: Allows users to securely log out of the application.

## Project Structure

. ├── app.py # Main Flask application ├── templates/ # Folder containing HTML templates │ ├── login.html # Login page │ ├── home.html # Home page for logged-in users ├── static/ # Static files (CSS, JS) │ ├── styles.css # Custom styles for the application │ ├── scripts.js # Custom JavaScript functionality ├── README.md # Project documentation


## Prerequisites

- Python 3.10 or above
- MySQL database
- Flask (`pip install flask`)
- MySQL Connector for Python (`pip install mysql-connector-python`)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository

Usage

1.Register a User:
Navigate to the registration page (via the /create_user API or add functionality in the UI).
Provide your name, email, and password.

2.Login:
Enter your registered email and password on the login page.

3.Home Page:
Upon successful login, you'll be redirected to a home page that displays a welcome message and a logout button.

4.Logout:
Click the logout button to end the session and return to the login page.

Technologies Used

Backend: Flask (Python)
Frontend: HTML, CSS, JavaScript
Database: MySQL
Session Management: Flask Sessions

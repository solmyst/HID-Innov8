

# Project Name

## Overview
This project was developed by Aaryan Mehta, Anush Gupta, Arpita Garg, and Ayushman Rathi as part of the Innove8 Hackathon, a 24-hour hackathon held on 17-18 October. The goal of the hackathon was to build innovative solutions within a constrained time frame.

The project is a full-stack web application with a backend built using Python and Django, and a frontend powered by HTML, CSS, and JavaScript. Data is managed using MySQL, and APIs are utilized to fetch and manipulate data from the database..

## Features
- **Backend**: 
  - Python with Django framework: This is the backbone of the project, handling server-side operations and managing routing.
  - JavaScript for handling dynamic functionality and asynchronous operations in the backend.
  - API integration: The application uses APIs to interact with the MySQL database, fetching and sending data as needed.

- **Frontend**:
  - HTML: Structure and layout of the web pages.
  - CSS: Styling and design for an enhanced user experience.
  - JavaScript: Adds interactivity and manages client-side logic.

- **Database**:
  - MySQL: A relational database used to store and manage user and application data.

## Framework
The wireframe for this project can be viewed at Visily Wireframe. This wireframe provides a visual blueprint of the user interface and application flow.

## Setup Instructions

### Prerequisites
- Python 3.x
- Django 3.x
- MySQL
- Node.js (for JavaScript dependency management if required)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Install the Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the MySQL database:
    - Install and start MySQL.
    - Create a database:
      ```sql
      CREATE DATABASE your_database_name;
      ```
    - Update the `settings.py` file with your MySQL credentials:
      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'your_database_name',
              'USER': 'your_username',
              'PASSWORD': 'your_password',
              'HOST': 'localhost',
              'PORT': '3306',
          }
      }
      ```

4. Run migrations to set up the database schema:
    ```bash
    python manage.py migrate
    ```

5. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

6. (Optional) Install any JavaScript dependencies (if applicable):
    ```bash
    npm install
    ```

### Usage
- Access the web application by visiting `http://localhost:8000` in your browser.
- The API endpoints can be accessed at `/api/` for various CRUD operations with the MySQL database.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

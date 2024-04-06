# To-Do List Web Application
This project is a simple to-do list web application built using Django, a high-level Python web framework. It allows users to create, view, update, and delete tasks to manage their daily activities effectively.

## Features
- **User Authentication**: Users can sign up and log in securely to access their to-do lists.
- **CRUD Operations**: Users can create, read, update, and delete tasks.
- **Task Prioritization**: Tasks can be prioritized based on urgency or importance.
- **Responsive Design**: The application is responsive and can be accessed on various devices.
- **Database**: Must be use MySQL Database for perform CRUD Operation.

## Installation
1. Clone this repository:
- https://github.com/nagesh882/to-do-list-project.git

2. Navigate to the project directory:
- cd to_do_list_project

3. Create a virtual environment (optional but recommended):
- python -m venv venv

4. Activate the virtual environment For Windows:
- venv\Scripts\activate

5. Install the project dependencies:
- pip install django
- pip install mysqlclient
- pip install django-autoslug

6. Apply migrations to create the database schema:
- python manage.py makemigrations
- python manage.py migrate

7. Run the development server:
- python manage.py runserver

8. Access the application in your web browser at `http://localhost:8000`.

## Usage
1. Create a new account or log in if you already have an account.
2. Once logged in, you will be redirected to the home page where you can view your to-do list.
3. To add a new task, click on the "Add Task" button and fill out the task details.
4. To edit or delete a task, click on the respective task and choose the desired action.
5. Tasks can be marked as complete by checking the checkbox next to them.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

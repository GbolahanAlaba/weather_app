
# **Simple Weather API**

## **Overview**

This project is a Django-based application utilizing Django Rest Framework (DRF) to create a basic weather API that interacts with a SQL database to store and retrieve weather data. The API allows users to add new weather data and retrieve weather data for a specific city.

## **Prerequisites**

- `Python 3.11.3`
- `Django 5.0.7`
- `Django Rest Framework (DRF) 3.15.2`
- `SQLite or any other preferred database`


## **Installation**
Clone the Repository


git clone https://github.com/GbolahanAlaba/sokosq-technical-assessment
cd your-repo-name
Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies

Install the required dependencies using pip:

bash
Copy code
pip install -r requirements.txt


Run Migrations

Apply the migrations to set up your database schema:
`python manage.py migrate`


Run the Development Server
Start the development server to verify everything is set up correctly:

`python manage.py runserver`
You should now be able to access the application at http://127.0.0.1:8000/.


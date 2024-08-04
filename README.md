
# **Simple Weather API**

## **Overview**

This project is a Django-based application utilizing Django Rest Framework (DRF) to create a basic weather API that interacts with a SQL database to store and retrieve weather data. The API allows users to add new weather data and retrieve weather data for a specific city.

## **Prerequisites**

- `Python 3.x`
- `Django 3.x or later`
- `Django Rest Framework (DRF) 3.x or later`
- `PostgreSQL or any other preferred database`


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
Database Setup

Update your database settings in settings.py. For example, if you're using PostgreSQL, it should look something like this:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Run Migrations

Apply the migrations to set up your database schema:

bash
Copy code
python manage.py migrate
Create a Superuser

Create a superuser to access the Django admin:

bash
Copy code
python manage.py createsuperuser
Run the Development Server

Start the development server to verify everything is set up correctly:

bash
Copy code
python manage.py runserver
You should now be able to access the application at http://127.0.0.1:8000/.
>>>>>>> 676051c5182551c053df9c31b5e024a7fc6e70a4

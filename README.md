API Endpoints
Here is a brief overview of the main API endpoints:

POST /weather: Add new weather data.
GET /weather/{city}: Retrieve weather data for a specific city.

Database Schema
Table: weather
Columns:
id (Primary Key, Integer, Auto Increment)
city (Text)
date (Date)
temperature (Float)
description (Text)
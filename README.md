# **Simple Weather API**

## **Objective**

Create a basic weather API using Python that interacts with a SQL database to store and retrieve weather data. The API allows users to add new weather data and retrieve weather data for a specific city.

## **Requirements**

### **API Endpoints**

- **`POST /weather`**: Add new weather data.
- **`GET /weather/{city}`**: Retrieve weather data for a specific city.

### **Database Schema**

- **Table**: `weather`
  - **Columns**:
    - `id` (Primary Key, Integer, Auto Increment)
    - `city` (Text)
    - `date` (Date)
    - `temperature` (Float)
    - `description` (Text)

## **Environment**

- Use any HTTP server or API framework of your choice (Flask, aiohttp, FastAPI, LiteStar, or Django REST framework).
- Use SQLite for the database.

# Historical Weather Data REST API

This application is a RESTful API that provides historical weather data, specifically temperature, for various cities. The app is built using Python, Django, Django REST Framework, and PostgreSQL for data storage.

## Features

- Retrieve historical temperature data for specific cities (stations) in Europe.
- Supports querying data by:
  1. **Station ID** for all historical data.
  2. **Station ID and Year** for all temperature data for a specific year.
  3. **Station ID, Year, and Month** for monthly temperature data.
  4. **Station ID and Date** for temperature data for a specific date.
- Built-in documentation webpage to guide users on how to interact with the API.
- PostgreSQL is used as the backend database, with data imported from CSV files located in the `data` folder.
- API can be accessed via tools such as `curl`, `httpie`, `Postman`, or web browsers (API platforms are recommended).

## Getting Started

### Requirements

- Python 3.x
- Django 5.x
- Django REST Framework
- PostgreSQL

Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

### Setting Up Environment Variables
In the `/mysite/settings.py` file, the database configuration is set up using environment variables. Make sure to find and replace the following placeholders with your actual database credentials:
```python
SECRET_KEY = env("SECRET_KEY") # Replace with your Django secret key
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DB_NAME"),  # Replace with your PostgreSQL database name
        'USER': env("DB_USER"),  # Replace with your PostgreSQL database user
        'PASSWORD': env("DB_PASSWORD"),  # Replace with your PostgreSQL password
        'HOST': env("DB_HOST"),  # Replace with your PostgreSQL host (e.g., localhost)
        'PORT': env("DB_PORT"),  # Replace with your PostgreSQL port (e.g., 5432)
    }
}
```
- SECRET_KEY: Your Django secret key.
- NAME: PostgreSQL database name.
- USER: PostgreSQL database username.
- PASSWORD: PostgreSQL database password.
- HOST: PostgreSQL database host (usually localhost).
- PORT: PostgreSQL database port (usually 5432).

### Database Setup
Make sure you have PostgreSQL installed and running. Create the database and set up the tables:
```bash
python manage.py migrate
```

### Running the Application
To start the development server, run:
```bash
python manage.py runserver
```
The app will be available at http://127.0.0.1:8000/.

## API Documentation
The root domain (http://127.0.0.1:8000/) serves a documentation webpage where you can find:

- A list of available API endpoints.
- Usage instructions with examples.
- A searchable table of available weather stations, where you can look up data by STAID (station ID).

## API Endpoints
1. Get all historical data for a specific station:
- URL: `http://127.0.0.1:8000/v1/api/<station-id>/`
- Example: http://127.0.0.1:8000/v1/api/43/
- Returns a JSON object with Date and TG (temperature).

2. Get yearly data for a specific station:
- URL: `http://127.0.0.1:8000/v1/api/yearly/<station-id>/<year: YYYY>/`
- Example: http://127.0.0.1:8000/v1/api/yearly/43/1958/
- Returns temperature data for each day of the specified year.

3. Get monthly data for a specific station:
- URL: `http://127.0.0.1:8000/v1/api/yearly/<station-id>/<year-month: YYYY-MM>/`
- Example: http://127.0.0.1:8000/v1/api/yearly/43/1958-02/
- Returns temperature data for each day of the specified month.

4. Get daily data for a specific station:
- URL: `http://127.0.0.1:8000/v1/api/<station-id>/<date: YYYY-MM-DD>/`
- Example: http://127.0.0.1:8000/v1/api/43/1958-02-05/
- Returns the temperature for the specified date.

## Notes:
- If the temperature (TG) is `-999.9`, it means the data for that day is missing.
- If an empty list `[ ]` is returned, the station or date may not be available.

## Contributing
Contributions to this project are welcome! Please follow the steps below:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -am 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Open a Pull Request.

## License
- This project is licensed under the MIT License.
- You can now copy and paste this directly into your `README.md` file.
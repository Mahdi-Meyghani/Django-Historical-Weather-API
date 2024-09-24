# Historical Weather Data REST API

This app is built using Python and Django, providing a REST API for accessing historical weather data for cities (stations) across The Earth! Developers can retrieve temperature data through various endpoints, allowing for flexible queries.

## Features

- Access historical weather data for specific stations (cities) using their unique station IDs.
- Query data for a specific day or year, including monthly data.
- Documentation available for easy reference on usage and available endpoints.

## API Endpoints

1. **Get all temperature data for a specific station:**
- GET `http://localhost:8000/v1/api/{station ID}` 
- Example: http://127.0.0.1:8000/v1/api/10

2. **Get temperature data for a specific station on a specific day:**
- GET ` http://localhost:8000/v1/api/{station ID}/{date: YYYY-MM-DD}` 
- Example: http://127.0.0.1:8000/v1/api/10/1992-05-19

3. **Get all temperature data for a specific year:**
- GET `http://localhost:8000/v1/api/yearly/{station ID}/{year: YYYY}` 
- Example: http://127.0.0.1:8000/v1/api/yearly/10/1992

4. **Get all temperature data for a specific month on a specific year:**
- GET `http://localhost:8000/v1/api/yearly/{station ID}/{year: YYYY}-{month: MM}` 
- Example: http://127.0.0.1:8000/v1/api/yearly/10/1992-10

## Documentation

Comprehensive documentation is available at the main URL: `http://127.0.0.1:8000`

This includes details on how to use the API, URL formats, examples, and a list of all available stations.

## Project Structure
```commandline
.
├── data
│   ├── stations.txt
│   ├── TG_STAID000001.txt
│   ├── TG_STAID000002.txt
│   ├── ..................
│   ├── TG_STAID000099.txt
│   └── TG_STAID000100.txt
├── db.sqlite3
├── LICENSE
├── manage.py
├── mysite
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
└── weather_api
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   ├── __init__.py
    ├── models.py
    ├── templates
    │   ├── documentation.html
    │   └── error_500.html
    ├── tests.py
    ├── urls.py
    └── views.py
```

## Requirements

Make sure to install the required packages listed in `requirements.txt`:
```commandline
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing 🤝

We welcome contributions! If you'd like to help out, please follow these steps:

1. **Fork the repository** 🍴
2. **Create a new branch** 🌿
   ```bash
   git checkout -b feature/YourFeatureName
3. **Make your changes** ✨
4. **Commit your changes** 📝
   ```bash
   git commit -m "Add some feature"
5. **Push to the branch** 🚀
   ```bash
   git push origin feature/YourFeatureName
6. **Open a Pull Request** 🔄

Thank you for considering contributing to this project! Every bit helps! 😊


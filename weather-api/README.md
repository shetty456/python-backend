# FastAPI Weather API with Redis Caching

This is a FastAPI-based Weather API that caches responses using Redis for improved performance. The project is managed with Poetry and includes test cases using `pytest`.

---

## **Features**
- Fetch weather data using an external API.
- Cache responses in Redis with a **12-hour timeout** to reduce API calls.
- Health check endpoint (`/health`).
- Unit tests using `pytest` and `fastapi.testclient`.

---

## **Project Structure**

```
weather-api/               # Root project directory
│── app/                   # Main application folder
│   ├── main.py            # FastAPI application
│   ├── __init__.py        # Makes `app` a package
│   ├── tests/             # Test cases
│   │   ├── __init__.py    # Makes `tests` a package
│   │   ├── test_app.py    # Test cases for API
│── .env                   # Environment variables
│── pyproject.toml         # Poetry project file
│── poetry.lock            # Poetry dependencies lock file
│── README.md              # Project documentation
```

---

## **Setup and Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-repo/weather-api.git
cd weather-api
```

### **2. Install Poetry (if not installed)**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### **3. Install Dependencies**
```bash
poetry install
```

### **4. Set Up Environment Variables**
Create a `.env` file in the root directory and add:

```
WEATHER_API_BASE_URL=https://api.weatherprovider.com
WEATHER_API_KEY=your_api_key_here
REDIS_URL=redis://localhost:6379
```

---

## **Running the Application**

### **1. Start Redis**
Ensure Redis is running:
```bash
redis-server
```

### **2. Run FastAPI Server**
```bash
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### **3. Test API Endpoints**
Visit in your browser or use `curl`:
```bash
curl -X GET "http://localhost:8000/health"
curl -X GET "http://localhost:8000/weather/london"
```

---

## **Running Tests**

### **1. Run Tests with Poetry**
```bash
poetry run pytest -v
```

### **2. Check Python Path (if ImportError occurs)**
```bash
poetry run python -c "import app.main; print('Module found!')"
```

---

## **Endpoints**
| Method | Endpoint           | Description |
|--------|-------------------|-------------|
| GET    | `/`               | Root endpoint |
| GET    | `/health`         | Health check |
| GET    | `/weather/{city}` | Fetch weather data (caches for 12 hours) |

---

## **Troubleshooting**
### **1. Fix Import Errors in Tests**
If you see `ModuleNotFoundError: No module named 'app'`, try:
```bash
touch app/__init__.py
```

### **2. Redis Not Running**
Ensure Redis is installed and running:
```bash
redis-server
```

---

## **Contributing**
Pull requests are welcome! Open an issue if you find a bug or have a suggestion.

---

## **License**
This project is licensed under the MIT License.


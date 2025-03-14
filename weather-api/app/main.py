from fastapi import FastAPI, Depends
from dotenv import load_dotenv
import os
import requests
from redis import Redis
import json

# Load environment variables from .env file
load_dotenv()
WEATHER_API_BASE_URL = os.getenv('WEATHER_API_BASE_URL')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI with Poetry!"}


REDIS_URL = "redis://localhost:6379"
redis_client = Redis.from_url(REDIS_URL, decode_responses=True)
CACHE_TIMEOUT = 12 * 60 * 60  # 12 hours in seconds (43,200 sec)

def set_cache(key: str, value: dict, ttl: int = CACHE_TIMEOUT):
    print(key)
    """Stores data in Redis with an expiration time."""
    redis_client.setex(key, ttl, json.dumps(value))

def get_cached_data(key: str):
    """Retrieves data from cache if available, otherwise returns None."""
    cached_data = redis_client.get(key)
    if cached_data:
        return json.loads(cached_data)
    return None

def delete_cache(key: str):
    """Deletes a key from the cache."""
    redis_client.delete(key)

def flush_cache():
    """Clears the entire Redis cache."""
    redis_client.flushall()

# Dependency injection
def get_redis():
    try:
        yield redis_client
    finally:
        redis_client.close()


@app.get("/health")
def check_health():
    return {"message": f"Hello, FastAPI health is fine, {redis_client.ping()}"}


@app.get("/weather/{city_name}")
def read_weather_by_city_name(city_name:str):
    # todo: implement third party api here
    # add redis for caching
    # can add a util function for fetching the weather
    if not WEATHER_API_KEY:
        raise ValueError("Token in missing. Please set it in the .env file")
    
    # weather api endpoint
    url = f"{WEATHER_API_BASE_URL}/{city_name}/?key={WEATHER_API_KEY}"
    print(f"Fetching data from: {url}")

    # check in redis 
    # if present in redis, return else hit the api
    cached_data = get_cached_data(city_name)
    
    if cached_data:
        print("this is cached data")
        return cached_data

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for HTTP errors (4xx, 5xx)
        set_cache(city_name, response.json())
        return {"data": response.json(), "status_code": response.status_code}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed", "status_code": getattr(e.response, "status_code", 500)}
    except ValueError:
        return {"error": "Invalid JSON response", "status_code": response.status_code if response else 500}

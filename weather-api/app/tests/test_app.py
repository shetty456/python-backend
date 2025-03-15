import pytest
from fastapi.testclient import TestClient
from app.main import app, set_cache, get_cached_data, delete_cache

client = TestClient(app)

# Mock Redis for testing (optional)
class MockRedis:
    def __init__(self):
        self.store = {}

    def setex(self, key, ttl, value):
        self.store[key] = value

    def get(self, key):
        return self.store.get(key)

    def delete(self, key):
        if key in self.store:
            del self.store[key]

mock_redis = MockRedis()

@pytest.fixture
def override_redis():
    """Override Redis functions with mock for testing"""
    global redis_client
    redis_client = mock_redis
    yield
    redis_client = None  # Reset after tests

def test_read_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI with Poetry!"}

def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert "Hello, FastAPI health is fine" in response.json()["message"]

def test_cache_functions(override_redis):
    """Test caching functionality"""
    test_key = "test_city"
    test_value = {"temperature": 25, "weather": "sunny"}

    set_cache(test_key, test_value)
    cached_data = get_cached_data(test_key)

    assert cached_data == test_value  # Cached value should match the set value

    delete_cache(test_key)
    assert get_cached_data(test_key) is None  # Cache should be empty after deletion

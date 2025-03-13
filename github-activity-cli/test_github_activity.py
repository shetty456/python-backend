import pytest
from unittest.mock import patch, MagicMock
from main import fetch_github_user_activity


@pytest.fixture
def mock_requests_get():
    with patch("requests.get") as mock_get:
        yield mock_get


def test_valid_user_with_activity(mock_requests_get):
    """Test case: Valid GitHub user with recent activity"""
    mock_requests_get.return_value = MagicMock(
        status_code=200,
        json=lambda: [
            {"type": "PushEvent", "repo": {"name": "user/repo1"}},
            {"type": "ForkEvent", "repo": {"name": "user/repo2"}}
        ]
    )

    result = fetch_github_user_activity("valid_user")
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["type"] == "PushEvent"


def test_valid_user_no_activity(mock_requests_get):
    """Test case: Valid GitHub user with no recent activity"""
    mock_requests_get.return_value = MagicMock(status_code=200, json=lambda: [])

    result = fetch_github_user_activity("inactive_user")
    assert result is None


def test_user_not_found(mock_requests_get):
    """Test case: GitHub user does not exist (404)"""
    mock_requests_get.return_value = MagicMock(status_code=404)

    result = fetch_github_user_activity("nonexistent_user")
    assert result is None


def test_rate_limit_exceeded(mock_requests_get):
    """Test case: API rate limit exceeded (403)"""
    mock_requests_get.return_value = MagicMock(status_code=403)

    result = fetch_github_user_activity("rate_limited_user")
    assert result is None


def test_internal_server_error(mock_requests_get):
    """Test case: GitHub API internal server error (500)"""
    mock_requests_get.return_value = MagicMock(status_code=500)

    result = fetch_github_user_activity("server_error_user")
    assert result is None

import pytest

from core.api_client import APIClient


@pytest.fixture
def api_client():
    return APIClient("https://httpbin.org/")

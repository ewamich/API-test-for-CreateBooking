import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com/"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def headers():
    return {"Content-Type": "application/json"}

def create_booking(base_url, booking_data):
    response = requests.post(f"{base_url}/booking", json=booking_data)
    return response
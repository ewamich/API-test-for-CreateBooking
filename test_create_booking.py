import requests
import pytest

# Test data for booking
valid_booking = {
    "firstname": "Janko",
    "lastname": "Muzykant",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2025-10-23",
        "checkout": "2025-10-25"
    },
    "additionalneeds": "Breakfast"
}


@pytest.mark.parametrize("booking_data", [valid_booking])
def test_create_booking(base_url, booking_data):
    response = requests.post(f"{base_url}/booking", json=booking_data)

    assert response.status_code == 200
    response_body = response.json()
    assert response_body['bookingid'] is not None
    assert response_body['booking']['firstname'] == booking_data['firstname']
    assert response_body['booking']['lastname'] == booking_data['lastname']


@pytest.mark.parametrize("invalid_data", [
    {},  # Empty data
    {"firstname": "John"},  # Missing required fields
])
def test_create_booking_invalid_data(base_url, invalid_data):
    response = requests.post(f"{base_url}/booking", json=invalid_data)

    assert response.status_code == 400 or response.status_code == 500

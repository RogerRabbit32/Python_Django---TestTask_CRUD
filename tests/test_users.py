import pytest

from rest_framework.test import APIClient


@pytest.mark.parametrize(
    "username, password, email, expected_status, expected_result",
    [
        # Successful registration
        ("admin", "Mypass12345", "admin@mail.com", 201, True),
        # Failed registration: username not provided
        (None, "Mypass12345", "admin2@mail.com", 400, False),
        # Failed registration: password not provided
        ("admin", None, "admin2@mail.com", 400, False),
        # Failed registration: username and password are same
        ("admin2", "admin2", "admin2@mail.com", 400, False),
        # Failed registration: username and password are similar
        ("admin2", "iamadmin2", "admin2@mail.com", 400, False),
        # Failed registration: password is entirely literal
        ("admin2", "iamthebest", "admin2@mail.com", 400, False)
    ]
)
@pytest.mark.django_db
def test_register_user(username, password, email, expected_status, expected_result):
    url = "/api/auth/users/"
    client = APIClient()
    response = client.post(url, format='json', data={
                "username": username,
                "password": password,
                "email": email
        }
    )
    assert response.status_code == expected_status
    response_json = response.json()
    if expected_result is True:
        assert "id" in response_json
        assert response_json["username"] == username

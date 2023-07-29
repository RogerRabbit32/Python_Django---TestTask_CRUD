import pytest

from rest_framework.test import APIClient


@pytest.fixture
def test_access_token():
    url = "/api/auth/users/"
    client = APIClient()
    client.post(url, format='json', data={
        "username": "admin",
        "password": "mypass12345"
    }
                           )
    url = "/api/auth/token/login/"
    client = APIClient()
    response = client.post(
        url, data={
            "username": "admin",
            "password": "mypass12345"
        }
    )
    assert response.status_code == 200
    response_json = response.json()
    assert "auth_token" in response_json
    return response_json["auth_token"]


@pytest.fixture
def test_another_access_token():
    url = "/api/auth/users/"
    client = APIClient()
    client.post(url, format='json', data={
        "username": "admin2",
        "password": "my2pass12345"
    }
                           )
    url = "/api/auth/token/login/"
    client = APIClient()
    response = client.post(
        url, data={
            "username": "admin2",
            "password": "my2pass12345"
        }
    )
    assert response.status_code == 200
    response_json = response.json()
    assert "auth_token" in response_json
    return response_json["auth_token"]


def test_unauthorized_access():
    url = "/api/posts/"
    client = APIClient()
    response = client.post(
        url,
        format='json',
        data={"title": "Test title", "body": "Test text"},
    )
    assert response.status_code == 401


@pytest.mark.parametrize(
    "title, body, expected_status, expected_result",
    [
        # Successful post creation
        ("Test title", "Test text", 201, True),
        # Failed post creation: no title
        (None, "Test text", 400, False),
        # Failed post creation: no text
        ("Test title", None, 400, False)
    ]
)
@pytest.mark.django_db
def test_create_and_delete_post(title, body, expected_status, expected_result, test_access_token):
    url = "/api/posts/"
    client = APIClient()
    response = client.post(
        url,
        format='json',
        data={"title": title, "body": body},
        headers={"Authorization": f"Token {test_access_token}"}
    )
    assert response.status_code == expected_status
    response_json = response.json()
    if expected_result is True:
        assert "id" in response_json
        assert response_json["user"] == "admin"

        # Unauthorized deletion of another's post
        post_id = response_json["id"]
        url = f"/api/posts/{post_id}/"
        response = client.delete(url, headers={"Authorization": f"Token {test_another_access_token}"})
        assert response.status_code == 401

        # Successful deletion of own post
        post_id = response_json["id"]
        url = f"/api/posts/{post_id}/"
        response = client.delete(url, headers={"Authorization": f"Token {test_access_token}"})
        assert response.status_code == 204

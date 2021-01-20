import cerberus
import pytest
import requests


def test_get_posts(base_url):
    response = requests.get(base_url + "posts/")

    schema = {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    }

    validate = cerberus.Validator()

    assert response.status_code == 200
    assert validate.validate(response.json()[0], schema)


@pytest.mark.parametrize("post_id, user_id", [(33, 4), (4, 1), (77, 8)])
def test_get_post_by_id(base_url, post_id, user_id):
    response = requests.get(base_url + f"posts/{post_id}")

    schema = {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    }

    validate = cerberus.Validator()
    assert response.status_code == 200
    assert response.json().get("userId") == user_id
    assert validate.validate(response.json(), schema)


@pytest.mark.parametrize("post_id", [1, 33, 44])
def test_comments_by_post_id(base_url, post_id):
    response = requests.get(base_url + f"comments?postId={post_id}")
    print(response.json())

    schema = {
        "postId": {"type": "number"},
        "id": {"type": "number"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "body": {"type": "string"}
    }

    validate = cerberus.Validator()
    assert response.status_code == 200
    assert response.json()[0].get("postId") == post_id
    assert validate.validate(response.json()[0], schema)


def test_post(base_url):
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = requests.post(base_url + "posts", data)

    assert response.status_code == 201


def test_delete(base_url):
    response = requests.delete(base_url + "posts/1")

    assert response.status_code == 200

import cerberus
import pytest
import requests


def test_random_random_image(base_url):
    response = requests.get(base_url + "api/breeds/image/random")

    schema = {
        "message": {"type": "string", "required": True},
        "status": {"type": "string", "required": True}
    }

    validate = cerberus.Validator()
    # assert response.status_code == 200
    assert validate.validate(response.json(), schema)


def test_multiple_random_image(base_url):
    response = requests.get(base_url + "api/breeds/image/random/3")

    schema = {
        "message": {"type": "list",
                    "items": [{"type": "string"}, {"type": "string"}, {"type": "string"}], "required": True},
        "status": {"type": "string", "required": True}
    }

    validate = cerberus.Validator()
    assert response.status_code == 200
    assert validate.validate(response.json(), schema)


def test_image_by_breed_status(base_url):
    response = requests.get(base_url + "api/breed/hound/images")
    assert response.status_code == 200


@pytest.mark.parametrize("breed", ["affenpinscher", "african", "akita"])
def test_image_by_breed(base_url, breed):
    response = requests.get(base_url + f"api/breed/{breed}/images")

    schema = {
        "message": {"type": ["list", "string"], "required": True},
        "status": {"type": "string", "required": True}
    }

    validate = cerberus.Validator()
    assert response.status_code == 200
    assert validate.validate(response.json(), schema)


@pytest.mark.parametrize("breed", ["affenpinscher", "african", "akita"])
def test_image_by_breed(base_url, breed):
    response = requests.get(base_url + f"api/breed/{breed}/images/random")

    schema = {
        "message": {"type": ["list", "string"], "regex": r".*\.jpg", "required": True},
        "status": {"type": "string", "required": True}
    }

    validate = cerberus.Validator()
    assert response.status_code == 200
    assert validate.validate(response.json(), schema)

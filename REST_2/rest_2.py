import cerberus
import pytest
import requests


def test_get_breweries(base_url):
    response = requests.get(base_url + "breweries/")

    schema = {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": "string"},
        "address_2": {'nullable': True},
        "address_3": {'nullable': True},
        "city": {"type": "string"},
        "state": {"type": "string"},
        "county_province": {'nullable': True},
        "postal_code": {"type": "string"},
        "country": {"type": "string"},
        "longitude": {"type": "string"},
        "latitude": {"type": "string"},
        "phone": {"type": "string"},
        "website_url": {"type": "string"},
        "updated_at": {"type": "string"},
        "created_at": {"type": "string"}
    }

    validate = cerberus.Validator()
    assert response.status_code == 200
    assert validate.validate(response.json()[0], schema)


@pytest.mark.parametrize("brewery_id", [10, 200, 426, 5494])
def test_get_brewery(base_url, brewery_id):
    response = requests.get(base_url + f"breweries/{brewery_id}")

    schema = {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": "string"},
        "address_2": {'nullable': True, "type": "string"},
        "address_3": {'nullable': True, "type": "string"},
        "city": {"type": "string"},
        "state": {"type": "string"},
        "county_province": {'nullable': True, "type": "string"},
        "postal_code": {"type": "string"},
        "country": {"type": "string"},
        "longitude": {"type": "string"},
        "latitude": {"type": "string"},
        "phone": {"type": "string"},
        "website_url": {"type": "string"},
        "updated_at": {"type": "string"},
        "created_at": {"type": "string"}
    }

    validate = cerberus.Validator()
    assert response.status_code == 200
    assert validate.validate(response.json(), schema)


@pytest.mark.parametrize("name", ["Avondale Brewing Co", "Grand Canyon Brewing Company", "Dragoon Brewing Co"])
def test_search_by_name(base_url, name):
    response = requests.get(base_url + f"breweries/search?query={name}")

    schema = {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": "string"},
        "address_2": {'nullable': True, "type": "string"},
        "address_3": {'nullable': True, "type": "string"},
        "city": {"type": "string"},
        "state": {"type": "string"},
        "county_province": {'nullable': True, "type": "string"},
        "postal_code": {"type": "string"},
        "country": {"type": "string"},
        "longitude": {"type": "string"},
        "latitude": {"type": "string"},
        "phone": {"type": "string"},
        "website_url": {"type": "string"},
        "updated_at": {"type": "string"},
        "created_at": {"type": "string"}
    }

    validate = cerberus.Validator()
    assert response.status_code == 200
    assert validate.validate(response.json()[0], schema)
    assert response.json()[0].get("name") == name


@pytest.mark.parametrize("brewery_type", ["planning", "brewpub", "micro"])
def test_search_by_type(base_url, brewery_type):
    response = requests.get(base_url + f"breweries?by_type={brewery_type}")

    schema = {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": "string"},
        "address_2": {'nullable': True, "type": "string"},
        "address_3": {'nullable': True, "type": "string"},
        "city": {"type": "string"},
        "state": {"type": "string"},
        "county_province": {'nullable': True, "type": "string"},
        "postal_code": {"type": "string"},
        "country": {"type": "string"},
        "longitude": {"type": "string"},
        "latitude": {"type": "string"},
        "phone": {"type": "string"},
        "website_url": {"type": "string"},
        "updated_at": {"type": "string"},
        "created_at": {"type": "string"}
    }

    validate = cerberus.Validator()
    assert response.status_code == 200
    assert validate.validate(response.json()[0], schema)
    assert response.json()[0].get("brewery_type") == brewery_type


@pytest.mark.parametrize("city", ["Alameda", "Phoenix", "North Little Rock"])
def test_search_by_city(base_url, city):
    response = requests.get(base_url + f"breweries?by_city={city}")

    schema = {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": "string"},
        "address_2": {'nullable': True, "type": "string"},
        "address_3": {'nullable': True, "type": "string"},
        "city": {"type": "string"},
        "state": {"type": "string"},
        "county_province": {'nullable': True, "type": "string"},
        "postal_code": {"type": "string"},
        "country": {"type": "string"},
        "longitude": {"type": "string"},
        "latitude": {"type": "string"},
        "phone": {"type": "string"},
        "website_url": {"type": "string"},
        "updated_at": {"type": "string"},
        "created_at": {"type": "string"}
    }

    validate = cerberus.Validator()
    assert response.status_code == 200
    assert validate.validate(response.json()[0], schema)
    assert response.json()[0].get("city") == city

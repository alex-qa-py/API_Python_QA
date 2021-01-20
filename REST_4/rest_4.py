import requests


def test_status_code(base_url, status):
    response = requests.get(base_url)
    assert response.status_code == int(status)

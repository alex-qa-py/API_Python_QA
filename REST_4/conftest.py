import pytest


def pytest_addoption(parser):
    parser.addoption("--url", required=True, default="ya.ru")
    parser.addoption("--status_code", required=True, default="200")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def status(request):
    return request.config.getoption("--status_code")

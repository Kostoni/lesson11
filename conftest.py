import pytest

from src.webdriverfactory import WebDriverFactory


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help='Browser type'
    )
    parser.addoption(
        "--app_url", default="http://localhost", help='Opencart url'
    )


@pytest.fixture(scope='module')
def app_url(request):
    return request.config.getoption('--app_url')


@pytest.fixture(scope='module')
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture()
def webdriver(browser):
    wd = WebDriverFactory.get(browser)
    yield wd
    wd.close()

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    url = "https://testdev.emversity.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit
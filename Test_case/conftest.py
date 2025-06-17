import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Global variable to store the driver instance
driver = None

@pytest.fixture(scope="class")
def setup(request):
    global driver
    if driver is None:
        options = Options()
        options.add_argument("--use-fake-ui-for-media-stream")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
    
    if hasattr(request, "param"):
        driver.get(request.param)  
    
    request.cls.driver = driver
    yield
    

@pytest.fixture(scope="session", autouse=True)
def teardown():
    yield
    # Quit the driver only after all tests are complete
    global driver
    if driver:
        driver.quit()
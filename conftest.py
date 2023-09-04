import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options,
                              service_args=['--connect-timeout=30'])
    yield driver
    driver.quit()

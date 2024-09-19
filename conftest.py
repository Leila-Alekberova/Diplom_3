import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(params=['chrome'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()

    else:
        raise ValueError(f"Неизвестный браузер: {request.param}")
    yield driver
    driver.quit()
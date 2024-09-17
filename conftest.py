import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(params=['chrome']) #на firefox не работает, у меня все тесты падают, если будет нужно, я разкомментирую
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
 #   elif request.param == 'firefox':
#        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Неизвестный браузер: {request.param}")
    yield driver
    driver.quit()
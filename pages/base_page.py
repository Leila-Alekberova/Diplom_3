import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Открытие ссылки
    def open_page(self, url):
        self.driver.get(url)

    # Получение ссылки страницы
    def current_url(self):
        return self.driver.current_url

    # Нахождение элемента
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    # Ожидание, пока элемент не станет невидимым
    def wait_until_element_invisibility(self, locator):
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(locator))

    # Ожидание наличия элемента на странице
    def wait_element_present(self, locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
    # Нахождение элемента с ожиданием

    def find_element_with_wait(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    # Клик на  элемент
    def click_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator)).click()

    # Ожидание, когда элемент станет видимым на странице
    def wait_visibility_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    # Ожидание, когда несколько элементов станут видимыми на странице
    def wait_visibility_elements(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))

    # Ожидание, когда элемент станет кликабельным
    def wait_clickable_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))


    # Перетащить элемент
    def drag_and_drop_on_element(self, locator_one, locator_two):
        draggable = self.find_element_with_wait(locator_one)
        droppable = self.find_element_with_wait(locator_two)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()


    # Ввести текст в поле
    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    # Отображение текста элемента
    def find_element_text(self, locator):
        result = self.driver.find_element(*locator).text
        return result


    

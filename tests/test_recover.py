from data import Urls
from data import TestUser
from helpers import CorrectUser
import allure
import pytest
from pages.recover_page import RecoverPageLocator
from locators.profile_page_locator import ProfilePageLocator
from locators.main_page_locator import MainPageLocators
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.recover_page import RecoverPage
from conftest import driver

class TestRecoverPassword:

    @allure.title("Нажатие на кнопку показать или скрыть пароль")
    def test_show_input_password(self, driver):
        page = RecoverPage(driver)
        page.open_page(Urls.GET_LOGIN)
        page.click_recover_link()
        page.input_email_user(CorrectUser.email)
        page.click_recover_button()
        page.wait_visibility_element(RecoverPageLocator.BUTTON_SAVE_PASS)
        page.input_password_user(CorrectUser.password)
        page.show_pass()
        password = page.active_input_pass()
        assert password.is_displayed() is True


    @allure.title("Переход а страницу восстановления пароля")
    def test_go_recover_page(self, driver):
        page = RecoverPage(driver)
        page.open_page(Urls.GET_LOGIN)
        page.click_recover_link()
        current_url = page.current_url()
        assert current_url == Urls.GET_FORGOT_PASS

    @allure.title("Ввод почты в блоке с восстановлением пароля")
    def test_enter_email(self, driver):
        page = RecoverPage(driver)
        page.open_page(Urls.GET_LOGIN)
        page.click_recover_link()
        page.input_email_user(CorrectUser.email)
        current_url = page.current_url()
        assert current_url == Urls.GET_FORGOT_PASS

    @allure.title("Ввод почты и нажатие кнопки 'Восстановить' в блоке с восстановлением пароля")
    def test_enter_email_and_click_button(self, driver):
        page = RecoverPage(driver)
        page.open_page(Urls.GET_LOGIN)
        page.click_recover_link()
        page.input_email_user(CorrectUser.email)
        page.click_recover_button()
        page.wait_visibility_element(RecoverPageLocator.BUTTON_SAVE_PASS)
        current_url = page.current_url()
        assert current_url == Urls.GET_RESET_PASS


import allure
import pytest
from data import Urls
from locators.profile_page_locator import ProfilePageLocator
from locators.main_page_locator import MainPageLocators
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from conftest import driver

class TestProfile:
    @allure.title("Переход в профиль пользователя из хедера страницы")
    def test_go_profile(self, driver):
        profile = MainPage(driver)
        profile.open_page(Urls.MAIN_URL)
        profile.wait_visibility_element(MainPageLocators.BUTTON_PROFILE)
        profile.click_profile()
        profile.wait_visibility_element(ProfilePageLocator.BUTTON_ENTER)
        page = profile.current_url()
        assert page == Urls.GET_LOGIN

    @allure.title("Переход в историю заказов")
    def test_go_order_list(self, driver):
        page = MainPage(driver)
        page.open_login_page()
        page.auth_user()
        order_list = ProfilePage(driver)
        order_list.wait_visibility_element(MainPageLocators.BUTTON_CONSTRUCTOR)
        order_list.click_profile()
        order_list.click_order_list()
        current_url = order_list.current_url()
        assert current_url == Urls.GET_ORDER_LIST

    @allure.title("Логаут профиля")
    def test_logout(self, driver):
        page = MainPage(driver)
        page.open_login_page()
        page.auth_user()
        profile = ProfilePage(driver)
        profile.click_profile()
        profile.exit_profile()
        profile.wait_visibility_element(ProfilePageLocator.BUTTON_ENTER)
        button = profile.find_element_text(ProfilePageLocator.BUTTON_ENTER)
        assert button == "Войти"


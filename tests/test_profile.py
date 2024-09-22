import allure
import pytest
from data import Urls
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from conftest import driver

class TestProfile:
    @allure.title("Переход в профиль пользователя из хедера страницы")
    def test_go_profile(self, driver):
        page = MainPage(driver)
        page.open_page(Urls.MAIN_URL)
        profile = ProfilePage(driver)
        profile.click_profile()
        profile.wait_visibility_button_profile()
        page = profile.current_url()
        assert page == Urls.GET_LOGIN

    @allure.title("Переход в историю заказов")
    def test_go_order_list(self, driver):
        profile = ProfilePage(driver)
        profile.open_login_page()
        profile.auth_user()
        order_list = ProfilePage(driver)
        order_list.click_profile()
        order_list.click_order_list()
        current_url = order_list.current_url()
        assert current_url == Urls.GET_ORDER_LIST

    @allure.title("Логаут профиля")
    def test_logout(self, driver):
        profile = ProfilePage(driver)
        profile.open_login_page()
        profile.auth_user()
        profile.click_profile()
        profile.exit_profile()
        profile.wait_visibility_button_enter()
        current_url = profile.current_url()
        assert current_url == Urls.GET_LOGIN


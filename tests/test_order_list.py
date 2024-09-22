import allure
import pytest
import unittest
from data import Urls
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.order_list_page import OrderListPage
from conftest import driver


class TestOrderList:
    @allure.title("Открытие всплывающего окна с заказом и его деталями")
    def test_order_detailes(self, driver):
        page = OrderListPage(driver)
        page.open_main_page()
        page.click_order_list()
        page.wait_visibility_title()
        page.open_details_order()
        page.wait_visibility_popup()
        assert page.find_title_popup().is_displayed()

    @allure.title("Отображение созданного нового заказа пользователя в истории заказов")
    def test_user_order_in_order_list(self, driver):
        profile = ProfilePage(driver)
        profile.open_login_page()
        profile.auth_user()
        profile.wait_visibility_button_profile()
        profile.click_order_list()
        page = MainPage(driver)
        page.click_constructor()
        page.add_bun_in_order()
        page.create_order()
        page.wait_visibility_button_popup()
        page.click_close_popup_order()
        page.click_profile()
        profile.click_order_list_user()
        profile.wait_visibility_number_order_user()
        number = profile.find_number_order_user()
        profile.click_order_list()
        order = OrderListPage(driver)
        order.wait_visibility_title()
        number_in_order_list = order.find_order_from_order_list(number)
        assert number in number_in_order_list


    @allure.title("Увеличение счетчика 'Выполнено за все время' при создании нового заказа")
    def test_increase_counter_all_time(self, driver):
        profile = ProfilePage(driver)
        profile.open_login_page()
        profile.auth_user()
        profile.wait_visibility_button_profile()
        page = OrderListPage(driver)
        page.click_order_list()
        all_orders_before = OrderListPage(driver)
        all_orders_before.wait_visibility_all_count_order()
        all_orders_before.get_all_day_orders()
        order = MainPage(driver)
        order.click_constructor()
        order.add_bun_in_order()
        order.create_order()
        order.wait_visibility_button_popup()
        order.click_close_popup_order()
        page.click_order_list()
        page.wait_visibility_title()
        all_orders_after = OrderListPage(driver)
        all_orders_after.get_all_day_orders()
        assert all_orders_before != all_orders_after

    @allure.title("Увеличение счетчика 'Выполнено за 'Сегодня' при создании нового заказа")
    def test_increase_counter_today(self, driver):
        profile = ProfilePage(driver)
        profile.open_login_page()
        profile.auth_user()
        profile.wait_visibility_button_profile()
        page = OrderListPage(driver)
        page.click_order_list()
        today_orders_before = OrderListPage(driver)
        today_orders_before.wait_today_orders()
        today_orders_before.get_today_orders()
        order = MainPage(driver)
        order.click_constructor()
        order.add_bun_in_order()
        order.create_order()
        order.wait_visibility_button_popup()
        order.click_close_popup_order()
        page.click_order_list()
        page.wait_visibility_title()
        today_orders_after = OrderListPage(driver)
        today_orders_after.get_today_orders()
        assert today_orders_after != today_orders_before

    @allure.title("Отображение созданного заказа в разделе 'В работе'")
    def test_order_in_work(self, driver):
        profile = ProfilePage(driver)
        profile.open_login_page()
        profile.auth_user()
        profile.wait_visibility_button_profile()
        order = MainPage(driver)
        order.click_constructor()
        order.add_bun_in_order()
        order.create_order()
        order.wait_visibility_button_popup()
        number = OrderListPage(driver)
        number.wait_visibility_number_order()
        number_user = number.get_number_order_in_popup()
        number.click_exit_button()
        order.click_order_list()
        order_list = OrderListPage(driver)
        order_in_work = order_list.get_order_list_in_work()
        assert number_user in order_in_work



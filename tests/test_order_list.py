import allure
import pytest
import unittest
from data import Urls
from locators.profile_page_locator import ProfilePageLocator
from locators.main_page_locator import MainPageLocators
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from locators.order_list_locator import OrderListLocator
from pages.order_list_page import OrderListPage
from conftest import driver


class TestOrderList:
    @allure.title("Открытие всплывающего окна с заказом и его деталями")
    def test_order_detailes(self, driver):
        page = OrderListPage(driver)
        page.open_page(Urls.MAIN_URL)
        page.click_element(MainPageLocators.BUTTON_ORDER_LIST)
        page.wait_visibility_element(OrderListLocator.TITLE_ORDER_LIST)
        page.open_details_order()
        page.wait_visibility_element(OrderListLocator.POPUP_ORDER_DETAILS)
        assert page.find_element_with_wait(OrderListLocator.POPUP_ORDER_DETAILS).is_displayed()

    @allure.title("Отображение созданного нового заказа пользователя в истории заказов")
    def test_user_order_in_order_list(self, driver):
        page = MainPage(driver)
        page.open_login_page()
        page.auth_user()
        page.click_order_list()
        page.click_constructor()
        page.add_bun_in_order()
        page.create_order()
        page.wait_visibility_element(MainPageLocators.BUTTON_CLOSE_ORDER_POPUP)
        page.click_close_popup_order()
        page.click_profile()
        page.click_order_list_user()
        q = ProfilePage(driver)
        q.wait_visibility_element(ProfilePageLocator.NUMBER_FIRST_ORDER)
        number = q.find_number_order_user()
        q.click_order_list()
        w = OrderListPage(driver)
        w.wait_visibility_element(OrderListLocator.TITLE_ORDER_LIST)
        number_in_order_list = w.find_order_from_order_list(number)
        assert number in number_in_order_list


    @allure.title("Увеличение счетчика 'Выполнено за все время' при создании нового заказа")
    def test_increase_counter_all_time(self, driver):
        page = MainPage(driver)
        page.open_login_page()
        page.auth_user()
        page.click_order_list()
        all_orders_before = OrderListPage(driver)
        all_orders_before.wait_visibility_element(OrderListLocator.ALL_COUNT_ORDER)
        all_orders_before.get_all_day_orders()
        page.click_constructor()

        page.add_bun_in_order()
        page.create_order()
        page.wait_visibility_element(MainPageLocators.BUTTON_CLOSE_ORDER_POPUP)
        page.click_close_popup_order()
        page.click_order_list()
        page.wait_visibility_element(OrderListLocator.TITLE_ORDER_LIST)

        all_orders_after = OrderListPage(driver)

        all_orders_after.get_all_day_orders()
        assert all_orders_before != all_orders_after

    @allure.title("Увеличение счетчика 'Выполнено за 'Сегодня' при создании нового заказа")
    def test_increase_counter_today(self, driver):
        page = MainPage(driver)
        page.open_login_page()
        page.auth_user()
        page.click_order_list()
        today_orders_before = OrderListPage(driver)
        today_orders_before.wait_visibility_element(OrderListLocator.TODAY_COUNT_ORDER)
        today_orders_before.get_today_orders()
        page.click_constructor()
        page.add_bun_in_order()
        page.create_order()
        page.wait_visibility_element(MainPageLocators.BUTTON_CLOSE_ORDER_POPUP)
        page.click_close_popup_order()
        page.click_order_list()
        page.wait_visibility_element(OrderListLocator.TITLE_ORDER_LIST)
        today_orders_after = OrderListPage(driver)
        today_orders_after.get_today_orders()
        assert today_orders_after != today_orders_before

    @allure.title("Отображение созданного заказа в разделе 'В работе'")
    def test_order_in_work(self, driver):
        page = MainPage(driver)
        page.open_login_page()
        page.auth_user()
        page.click_constructor()
        page.add_bun_in_order()
        page.create_order()
        order_page = OrderListPage(driver)
        order_page.wait_clickable_exit_button()
        order_page.wait_visibility_element(OrderListLocator.NUMBER_ORDER_IN_POPUP)
        number = OrderListPage(driver)
        number_user = number.get_number_order_in_popup()
        order_page.click_exit_button()
        page.click_order_list()
        order_list = OrderListPage(driver)
        order_in_work = order_list.get_order_list_in_work()
        assert number_user in order_in_work



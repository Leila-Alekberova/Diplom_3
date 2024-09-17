from locators.main_page_locator import MainPageLocators
from locators.profile_page_locator import ProfilePageLocator
from pages.base_page import BasePage
from locators.order_list_locator import OrderListLocator

from data import Urls

import allure

class OrderListPage(BasePage):

    @allure.step("Открываем детали заказа в списке заказов")
    def open_details_order(self):
        self.click_element(OrderListLocator.LINK_ORDER)

    @allure.step("Поиск заказа по номеру в ленте заказов")
    def find_order_from_order_list(self, order):
        one = OrderListLocator.NUMBER_ORDER[0]
        locator = OrderListLocator.NUMBER_ORDER[1]
        locator = locator.format(order)
        return self.find_element_text((one, locator))

    @allure.step("Проверка, есть ли заказ в общей ленте заказов")
    def check_order_in_order_list(self, order):
        return self.find_order_from_order_list(order, OrderListLocator.ALL_ORDERS)


    @allure.step("Ожидание, когда кнопка закрытия заказа станет кликабельной")
    def wait_clickable_exit_button(self):
        self.wait_clickable_element(OrderListLocator.BUTTON_EXIT)

    @allure.step("Нажатие кнопки закрытия заказа")
    def click_exit_button(self):
        self.click_element(OrderListLocator.BUTTON_EXIT)

    @allure.step("Ожидание отображения количества заказов, выполненных сегодня")
    def wait_today_orders(self):
        self.wait_visibility_element(OrderListLocator.TODAY_COUNT_ORDER)

    @allure.step("Получение количества заказов, выполненных сегодня")
    def get_today_orders(self):
        self.find_element_text(OrderListLocator.TODAY_COUNT_ORDER)

    @allure.step("Ожидание отображения количества заказов, выполненных за все время")
    def wait_all_day_orders(self):
        result = self.wait_visibility_element(OrderListLocator.ALL_COUNT_ORDER)
        return result

    @allure.step("Получение количества заказов, выполненных за все время")
    def get_all_day_orders(self):
        result = self.find_element(OrderListLocator.ALL_COUNT_ORDER).text
        return result

    @allure.step("Получение номера заказа в поп-апе")
    def get_number_order_in_popup(self):
        self.wait_until_element_invisibility(OrderListLocator.DEFAULT_NUMBER_ORDER_IN_POPUP)
        res = self.find_element_text(OrderListLocator.NUMBER_ORDER_IN_POPUP)
        return res

    @allure.step("Получение списка заказов 'В работе'")
    def get_order_list_in_work(self):
        self.wait_element_present(OrderListLocator.TEXT_ORDER_IN_WORK)
        self.wait_until_element_invisibility(OrderListLocator.TEXT_ORDER_IN_WORK)
        result = self.find_element(OrderListLocator.NUMBER_ORDERS_IN_WORK).text
        return result


    # Получение списка номеров заказов
    def get_order_numbers(self):
        by, value = OrderListLocator.NUMBER_ORDER_IN_POPUP
        order_numbers = self.driver.find_elements(by, value)
        return [order.text for order in order_numbers]
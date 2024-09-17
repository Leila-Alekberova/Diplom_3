from locators.main_page_locator import MainPageLocators
from locators.profile_page_locator import ProfilePageLocator
from pages.base_page import BasePage

import allure

class ProfilePage(BasePage):
    @allure.step("Переход в профиль пользователя")
    def click_profile(self):
        self.click_element(MainPageLocators.BUTTON_PROFILE)

    @allure.step("Выход их профиля")
    def exit_profile(self):
        self.click_element(ProfilePageLocator.BUTTON_EXIT)

    @allure.step("Переход в историю заказов")
    def click_order_list(self):
        self.click_element(MainPageLocators.BUTTON_ORDER_LIST)

    @allure.step("Нажатие кнопки 'История заказов'")
    def get_user_order_list(self):

        self.click_element(ProfilePageLocator.LINK_ORDER_HISTORY)
        return self.find_element_text(ProfilePageLocator.LINK_ORDER_HISTORY).get_attribute('class')

    @allure.step("Получение первого заказа пользователя")
    def find_number_order_user(self):
        return self.find_element_text(ProfilePageLocator.NUMBER_FIRST_ORDER)





from locators.profile_page_locator import ProfilePageLocator, LoginPageLocator
from pages.base_page import BasePage
from helpers import CorrectUser
import allure
from data import Urls

class ProfilePage(BasePage):
    @allure.step("Переход в профиль пользователя")
    def click_profile(self):
        self.click_element(ProfilePageLocator.BUTTON_PROFILE)

    @allure.step("Ожидание отображения кнопки 'Личный кабинет'")
    def wait_visibility_button_profile(self):
        self.wait_visibility_element(ProfilePageLocator.BUTTON_PROFILE)

    @allure.step("Ожидание отображения кнопки 'Войти'")
    def wait_visibility_button_enter(self):
        self.wait_visibility_element(ProfilePageLocator.BUTTON_ENTER)

    @allure.step("Получение текста кнопки 'Войти'")
    def find_element_text_button_enter(self):
        self.find_element_text(ProfilePageLocator.BUTTON_ENTER)

    @allure.step("Выход их профиля")
    def exit_profile(self):
        self.click_element(ProfilePageLocator.BUTTON_EXIT)

    @allure.step("Переход в историю заказов")
    def click_order_list(self):
        self.click_element(ProfilePageLocator.BUTTON_ORDER_LIST)

    @allure.step("Нажатие кнопки 'История заказов'")
    def get_user_order_list(self):

        self.click_element(ProfilePageLocator.LINK_ORDER_HISTORY)
        return self.find_element_text(ProfilePageLocator.LINK_ORDER_HISTORY).get_attribute('class')

    @allure.step("Получение первого заказа пользователя")
    def find_number_order_user(self):
        return self.find_element_text(ProfilePageLocator.NUMBER_FIRST_ORDER)
    @allure.step("Ожидание отображения первого заказа пользователя")
    def wait_visibility_number_order_user(self):
        self.wait_visibility_element(ProfilePageLocator.NUMBER_FIRST_ORDER)

    @allure.step("Ввод почты пользователя")
    def input_email(self, email):
        self.send_keys(LoginPageLocator.FIELD_EMAIL, email)

    @allure.step("Ввод пароля пользователя")
    def input_password(self, password):
        self.send_keys(LoginPageLocator.FIELD_PASSWORD, password)

    @allure.step("Нажатие кнопки 'Войти'")
    def click_login_button(self):
        self.click_element(LoginPageLocator.BUTTON_LOGIN)

    @allure.step("Переход в историю заказов пользователя")
    def click_order_list_user(self):
        self.click_element(ProfilePageLocator.BUTTON_HISTORY)

    @allure.step("Получение номера заказов пользователя")
    def get_orders_user(self):
        orders = []
        element = self.find_element_with_wait(ProfilePageLocator.ORDER_LIST_USER)
        return orders.append(element)

    @allure.step("Авторизация пользователя")
    def auth_user(self):
        email = CorrectUser.email
        password = CorrectUser.password
        self.input_email(email)
        self.input_password(password)
        self.click_login_button()


    @allure.step("Переход на страницу авторизации пользователя")
    def open_login_page(self):
        self.open_page(Urls.GET_LOGIN)


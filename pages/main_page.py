from pages.base_page import BasePage
import allure
from locators.main_page_locator import MainPageLocators
from locators.profile_page_locator import LoginPageLocator, ProfilePageLocator
from locators.order_list_locator import OrderListLocator
from selenium.webdriver import ActionChains
from data import Urls
from helpers import CorrectUser


class MainPage(BasePage):

    @allure.step("Переход в конструктор по кнопке в хедере")
    def click_constructor(self):
        self.click_element(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step("Переход в ленту заказов")
    def click_order_list(self):
        self.click_element(MainPageLocators.BUTTON_ORDER_LIST)

    @allure.step("Переход в личный кабинет")
    def click_profile(self):
        self.click_element(MainPageLocators.BUTTON_PROFILE)


    @allure.step("Клик на ингредиент 'Флюоресцентная булка R2-D2'")
    def click_bun(self):
        self.click_element(MainPageLocators.BUN_INGREDIENT)

    @allure.step("Клик на ингредиент 'Соус Spicy-X'")
    def click_sause(self):
        self.click_element(MainPageLocators.SAUSE_INGREDIENT)

    @allure.step("Клик на ингредиент 'Мясо бессмертных моллюсков Protostomia'")
    def click_stuffing(self):
        self.click_element(MainPageLocators.STUFFING_INGREDIENT)

    @allure.step("Клик на поп-ап для закрытия карточки ингредиента")
    def click_close_popup(self):
        self.click_element(MainPageLocators.BUTTON_CLOSE_POPUP)


    @allure.step("Клик на поп-ап для закрытия заказа")
    def click_close_popup_order(self):
        self.wait_until_element_invisibility(MainPageLocators.ELEMENT_COVER)
        self.click_element(MainPageLocators.BUTTON_CLOSE_ORDER_POPUP)

    @allure.step("Добавить булку в заказ")
    def add_bun_in_order(self):
        self.drag_and_drop_on_element(MainPageLocators.BUN_INGREDIENT, MainPageLocators.ORDER_TO)

    @allure.step("Добавить соус в заказ")
    def add_sause_in_order(self):
        self.drag_and_drop_on_element(MainPageLocators.SAUSE_INGREDIENT)

    @allure.step("Добавить начинку в заказ")
    def add_stuffing_in_order(self):
        self.drag_and_drop_on_element(MainPageLocators.STUFFING_INGREDIENT)

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def create_order(self):
        self.click_element(MainPageLocators.BUTTON_CREATE_ORDER)

    @allure.step("Переход на страницу авторизации пользователя")
    def open_login_page(self):
        self.open_page(Urls.GET_LOGIN)

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
        element = self.find_element_with_wait(OrderListLocator.ORDER_LIST_USER)
        return orders.append(element)


    @allure.step("Получение номера нового заказа")
    def find_new_order(self):
        return self.find_element_text(OrderListLocator.NUMBER_NEW_ORDER)

    @allure.step("Авторизация пользователя")
    def auth_user(self):
        email = CorrectUser.email
        password = CorrectUser.password
        self.input_email(email)
        self.input_password(password)
        self.click_login_button()

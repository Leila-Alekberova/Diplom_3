from locators.profile_page_locator import RecoverPageLocator
from pages.base_page import BasePage
from data import Urls
import allure

class RecoverPage(BasePage):
    @allure.step("Нажать на кнопку 'Восстановить пароль'")
    def click_recover_link(self):
        self.click_element(RecoverPageLocator.LINK_RECOVER_PASS)

    @allure.step("Ввод почты в поле 'Email'")
    def input_email_user(self, email):
        self.send_keys(RecoverPageLocator.INPUT_EMAIL, email)

    @allure.step("Нажать кнопку 'Восстановить'")
    def click_recover_button(self):
        self.click_element(RecoverPageLocator.BUTTON_RECOVER_PASS)

    @allure.step("Нажать кнопку 'Показать/скрыть пароль'")
    def show_pass(self):
        self.click_element(RecoverPageLocator.BUTTON_SHOW_PASS)

    @allure.step("Ввод пароля в поле 'Пароль'")
    def input_password_user(self, password):
        self.send_keys(RecoverPageLocator.INPUT_PASS, password)

    @allure.step("Ожидание активности поля 'Пароль'")
    def active_input_pass(self):
        return self.find_element_with_wait(RecoverPageLocator.INPUT_ANIMATED)

    @allure.step("Переход на страницу авторизации пользователя")
    def open_login_page(self):
        self.open_page(Urls.GET_LOGIN)

    @allure.step("Ожидание отображения кнопки 'Сохранить'")
    def wait_visibility_button_save(self):
        self.wait_visibility_element(RecoverPageLocator.BUTTON_SAVE_PASS)



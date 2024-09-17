from faker import Faker


class TestUser:
    @staticmethod
    def create_fake_user():
        fake = Faker()
        registration_fake_user ={
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return registration_fake_user

    @staticmethod
    def create_email():
        fake = Faker()
        registration_fake_email = {
            "email": fake.email()}
        return registration_fake_email

    @staticmethod
    def create_password():
        fake = Faker()
        registration_fake_password = {
            "password": fake.password()}
        return registration_fake_password

    @staticmethod
    def create_name():
        fake = Faker()
        registration_fake_name = {
            "password": fake.name()}
        return registration_fake_name

class Urls:
    MAIN_URL = "https://stellarburgers.nomoreparties.site"
    GET_PROFILE = "https://stellarburgers.nomoreparties.site/account/profile"
    GET_ORDER_HISTORY = "https://stellarburgers.nomoreparties.site/account/order-history"
    GET_LOGIN = "https://stellarburgers.nomoreparties.site/login"
    GET_FORGOT_PASS = "https://stellarburgers.nomoreparties.site/forgot-password"
    GET_RESET_PASS = "https://stellarburgers.nomoreparties.site/reset-password"
    GET_ORDER_LIST = "https://stellarburgers.nomoreparties.site/feed"

class Handlers:
    CREATE_USER = "/api/auth/register"
    LOGIN_USER = "/api/auth/login"
    LOGOUT_USER = "/api/auth/logout"
    DELETE_USER = '/api/auth/user'
    EDIT_USER = "/api/auth/user"

    UPDATE_TOKEN = "/api/auth/token"

    CREATE_ORDER = "/api/orders"
    GET_ORDERS = "/api/orders"

    GET_INGREDIENTS = "/api/ingredients"

    headers = {"Content-Type": "application/json"}


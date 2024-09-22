class Urls:
    MAIN_URL = "https://stellarburgers.nomoreparties.site"
    GET_PROFILE = f"{MAIN_URL}/account/profile"
    GET_ORDER_HISTORY = f"{MAIN_URL}/account/order-history"
    GET_LOGIN = f"{MAIN_URL}/login"
    GET_FORGOT_PASS = f"{MAIN_URL}/forgot-password"
    GET_RESET_PASS = f"{MAIN_URL}/reset-password"
    GET_ORDER_LIST = f"{MAIN_URL}/feed"



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


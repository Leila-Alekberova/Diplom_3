from selenium.webdriver.common.by import By

class RecoverPageLocator:

    LINK_RECOVER_PASS = (By.XPATH, ".//a[text() = 'Восстановить пароль']") # Гиперссылка "Восстановить пароль"
    INPUT_EMAIL = (By.XPATH, ".//label[text() = 'Email']/../input")  # Инпут почты для восстановления
    INPUT_PASS = (By.XPATH, '//input[@type="password"]') # Инпут пароля для восстановления
    BUTTON_RECOVER_PASS = (By.XPATH, '//button[text()="Восстановить"]') # Кнопка "Восстановить" на странице восстановления пароля
    BUTTON_SHOW_PASS = (By.XPATH, '//div[contains(@class,"icon-action")]') # Кнопка "Показать/скрыть" пароль
    INPUT_ANIMATED = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                           '"input_status_active")]') # Поле "Пароль" активное
    INPUT_ANIMATED_2 = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")
    BUTTON_SAVE_PASS = (By.XPATH, '//button[text()="Сохранить"]') # Кнопка 'Сохранить' на странице восстановления пароля

class ProfilePageLocator:

    BUTTON_EXIT = (By.XPATH, ".//button[text() = 'Выход']")  # кнопка 'Выход'
    TITLE_PROFILE = (By.XPATH, '//a[text()="Профиль"]')  # Заговок 'Профиль' в хедере страницы
    BUTTON_ENTER = (By.XPATH, ".//button[text()='Войти']") # Кнопка "Войти"
    BUTTON_HISTORY = (By.XPATH, "//a[@href='/account/order-history']") # Кнопка 'История заказов' пользователя
    LINK_ORDER_HISTORY = (By.XPATH, '//a[text()="История заказов"]') #История заказов в профиле пользователя
    NUMBER_NEW_ORDER = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    NUMBER_FIRST_ORDER = (By.XPATH, '(//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")])[last()]') # Номер первого с конца заказа в истории заказов пользователя
    BUTTON_PROFILE = (By.XPATH, '//p[text()="Личный Кабинет"]')  # кнопка "Личный Кабинет" в хэдере страницы
    BUTTON_ORDER_LIST = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')  # кнопка "Лента заказов" в хэдере страницы
    ORDER_LIST_USER = (By.XPATH, '//div[@class="OrderHistory_textBox__3lgbs mb-6"]//p[@class="text '
                                 'text_type_digits-default"]')  # Список заказов пользователя

class LoginPageLocator:
    FIELD_EMAIL = (By.XPATH, ".//input[@name='name']")  # Поле 'Email' на странице авторизации
    FIELD_PASSWORD = (By.XPATH, ".//input[@name='Пароль']")  # Поле 'Пароль' на странице авторизации
    BUTTON_LOGIN =(By.XPATH, '//button[contains(text(), "Войти")]')  # Кнопка 'Войти' на странице авторизации
    INPUT_EMAIL_LOGIN = (By.XPATH, ".//label[text() = 'Email']/../input")  # Инпут почт

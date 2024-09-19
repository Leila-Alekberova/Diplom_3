from selenium.webdriver.common.by import By

class OrderListLocator:
    LINK_ORDER = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'  # Ссылка на заказ из списка заказов
    ORDER_LIST_LOCATOR = [By.XPATH, ".//ul/li/a/div[1]/p[1]"] # Список заказов
    TITLE_ORDER_LIST = By.XPATH, '//h1[text()="Лента заказов"]' # Заголовок "Лента заказов"
    POPUP_ORDER_DETAILS = (By.XPATH, '//p[text()="Cостав"]') # Поп-ап с текстом "Состав"
    BUTTON_EXIT = (By.CSS_SELECTOR, "[class= 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    TODAY_COUNT_ORDER = (By.XPATH, "//div[contains(@class, 'OrderFeed_ordersData')]/div[last()]/p[last()]") # Количество заказов, выполненных сегодня
    ALL_COUNT_ORDER = (By.XPATH, ".//p [@class='OrderFeed_number__2MbrQ text text_type_digits-large']") # Количество заказов, выполненных за все время
    ORDER_LIST_USER = (By.XPATH, '//div[@class="OrderHistory_textBox__3lgbs mb-6"]//p[@class="text '
                                'text_type_digits-default"]')  # Список заказов пользователя
    NUMBER_ORDER = (By.XPATH, '//p[text()="{}"]')  # номер заказа из Ленты заказов
    NUMBER_ORDER_FROM_LOCATOR = By.XPATH, '//p[text()="{}"]' # Поиск номера заказа по локатору
    ALL_ORDERS = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, "
                                       "'text_type_digits-default')]")
    NUMBER_ORDER_IN_POPUP = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")  # Номер заказа в поп-апе
    NUMBER_ORDERS_IN_WORK = (By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]') # Номер заказа 'В работе'
    DEFAULT_NUMBER_ORDER_IN_POPUP = (By.XPATH, '//h2[text()="9999"]') # Дефолтный номер заказа в поп-апе
    TEXT_ORDER_IN_WORK = (By.XPATH, '//li[text()="Все текущие заказы готовы!"]') # В блоке 'В работе' все заказы готовы
    BUTTON_ORDER_LIST = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')  # кнопка "Лента заказов" в хэдере страницы


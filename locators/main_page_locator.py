from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_PROFILE = (By.XPATH, '//p[text()="Личный Кабинет"]')  # кнопка "Личный Кабинет" в хэдере страницы
    BUTTON_CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')  # кнопка "Конструктор" в хэдере страницы
    BUTTON_ORDER_LIST = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')  # кнопка "Лента заказов" в хэдере страницы

    TITLE_CONSTRUCTOR = (By.XPATH, '//h1[text()="Соберите бургер"]')  # заголовок "Соберите бургер"
    TITLE_BUN = (By.XPATH, '//span[@class="text text_type_main-default" and .="Булки"]') # заголовок "Булки"
    TITLE_SAUSE = (By.XPATH, '//span[@class="text text_type_main-default" and .="Соусы"]')  # заголовок "Соусы"
    TITLE_STUFFING = (By.XPATH, '//span[@class="text text_type_main-default" and .="Начинки"]')  # заголовок "Начинки"

    BUN_INGREDIENT = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')  # ингредиент "Флюоресцентная булка R2-D3"
    SAUSE_INGREDIENT = (By.XPATH, '//p[text()="Соус Spicy-X"]')  # ингредиент "Соус Spicy-X"
    STUFFING_INGREDIENT = (By.XPATH, '//p[text()="Мясо бессмертных моллюсков Protostomia"]')  # ингредиент "Мясо бессмертных моллюсков Protostomia"
    BUTTON_CLOSE_POPUP = (By.XPATH, '//button[contains(@class, "Modal_modal__close_modified")]')  # Кнопка закрытия поп-апа
    BUTTON_CLOSE_ORDER_POPUP = (By.XPATH, '//button[contains(@class, "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK")]')  # Кнопка закрытия поп-апа заказа
    BUTTON_CREATE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]') # кнопка "Оформить заказ"
    ORDER_TO = (By.XPATH, '//div[contains (@class, "constructor-element_pos_bottom")]') # Место, куда перетаскивается ингредиент для заказа
    ELEMENT_COVER = (By.XPATH, "//*[contains(@class, 'Modal_modal__loading')]"
                               "/following::div[@class='Modal_modal_overlay__x2ZCr']") # Перекрывающий элемент



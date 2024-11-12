from selenium.webdriver.common.by import By

class TestLocators:
    #поле ввода имени при регистрации
    INPUT_REGISTRATION_USER_NAME = [By.XPATH, '//label[text()="Имя"]/following-sibling::input']

    #поле ввода email при регистрации
    INPUT_REGISTRATION_EMAIL = [By.XPATH, '//label[text()="Email"]/following-sibling::input']

    #поле ввода пароля при регистрации
    INPUT_REGISTRATION_USER_PASSWORD = [By.XPATH, '//label[text()="Пароль"]/following-sibling::input']

    #кнопка "Зарегистрироваться" в окне регистрации
    BUTTON_REGISTRATION = [By.XPATH, '//button[text()="Зарегистрироваться"]']

    #форма авторизации "Вход" после завершения регистрации
    FORM_LOGIN_AFTER_REGISTRATION = [By.XPATH, '//h2[text() = "Вход"]']

    #Текст "Некорректный пароль" при вводе некорректного пароля
    INCORRECT_PASSWORD = [By.XPATH, '//p[text() = "Некорректный пароль"]']

    #Кнопка "Войти в аккаунт" на главной странице
    BUTTON_LOGIN_ON_MAIN_PAGE = [By.XPATH, '//button[text() = "Войти в аккаунт"]']

    #поле ввода email на странице авторизации
    INPUT_EMAIL_ON_LOGIN_PAGE = [By.XPATH, "//input[@name='name' and @type='text']"]

    # поле ввода пароля на странице авторизации
    INPUT_PASSWORD_ON_LOGIN_PAGE = [By.XPATH, "//input[@name='Пароль' and @type='password']"]

    #кнопка "Оформить заказ" на главной странице для авторизованного пользователя
    BUTTON_MAKE_ORDER_ON_MAIN_PAGE = [By.XPATH, '//button[text() = "Оформить заказ"]']

    #кнопка "Личный кабинет" на главной странице
    BUTTON_PERSONAL_ACCOUNT_ON_MAIN_PAGE = [By.XPATH,  "//a[contains(@class, 'AppHeader_header__link__3D_hX')]//p[text()='Личный Кабинет']"]

    #кнопка "Войти" на странице авторизации
    BUTTON_LOG_IN_ON_LOGIN_PAGE = [By.XPATH, '//button[text() = "Войти"]']

    #кнопка "Войти" в форме регистрации
    BUTTON_LOG_IN_ON_REGISTRATION_PAGE = [By.XPATH, '//a[text() = "Войти"]']

    #кнопка "Войти" в форме восстановления пароля
    BUTTON_LOG_IN_ON_FORGOT_PASSWORD_PAGE = [By.XPATH, '//a[text() = "Войти"]']

    #кнопка "Конструктор" в личном кабинете авторизованного пользователя
    BUTTON_CONSTRUCTOR_FROM_PERSONAL_ACCOUNT = [By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p']

    #логотип Stellar Burgers в личном кабинете авторизованного пользователя
    STELLAR_BURGERS_LOGO = [By.XPATH, '//*[@id="root"]/div/header/nav/div/a']

    #кнопка "Выход" в личном кабинете авторизованного пользователя
    BUTTON_LOG_OUT = [By.XPATH, "//button[text()='Выход']"]

    #раздел Конструктора Булки
    SECTION_BULKI = [By.XPATH, '//span[text()= "Булки"]']

    #Заголовок секции Булки
    BUNS_HEADER = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]']

    #раздел Конструктора Соусы
    SECTION_SAUСES = [By.XPATH, '//span[text()="Соусы"]']

    #заголовок секции Соусы
    SAUCES_HEADER = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]']

    # раздел Конструктора Начинки
    SECTION_FILLINGS = [By.XPATH, '//span[text()="Начинки"]']

    #Заголовок секции Начинки
    FILLINGS_HEADER = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]']


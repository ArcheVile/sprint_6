from selenium.webdriver.common.by import By

# Локаторы главной страницы
LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный Кабинет"
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор"
STELLAR_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип Stellar Burgers

# Локаторы регистрации
REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")  # Ссылка "Зарегистрироваться"
REGISTER_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле Имя
REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле Email
REGISTER_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле Пароль
REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка Зарегистрироваться
REGISTER_ERROR = (By.CLASS_NAME, "input__error_text")  # Ошибка регистрации

# Локаторы входа
EMAIL_INPUT = (By.XPATH, "//input[@name='name' or @name='email']")  # Поле ввода email
PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль' or @name='password']")  # Поле ввода пароля
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка Войти

# Локаторы восстановления пароля
FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")  # Ссылка "Восстановить пароль"

# Локаторы личного кабинета
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка Выход

# Локаторы разделов конструктора
BUN_SECTION = (By.XPATH, "//span[text()='Булки']")  # Раздел "Булки"
SAUCE_SECTION = (By.XPATH, "//span[text()='Соусы']")  # Раздел "Соусы"
FILLING_SECTION = (By.XPATH, "//span[text()='Начинки']")  # Раздел "Начинки"

# Локаторы оформления заказа
ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")  # Кнопка "Оформить заказ"

# Локаторы формы регистрации - ссылка для перехода на страницу входа
LOGIN_LINK_FROM_REGISTER = (By.XPATH, "//a[text()='Войти']")  # Ссылка "Войти"

# Локаторы формы восстановления пароля - ссылка для перехода на страницу входа
LOGIN_LINK_FROM_FORGOT = (By.XPATH, "//a[text()='Войти']")  # Ссылка "Войти"

import pytest
from src.settings import valid_email, valid_password, valid_p_number, not_valid_password, valid_login, valid_ls, ls_l_7, ls_m_7, ls_l_12
from src.fixtures import go_to_rt, go_to_rt_fust, driver, driver_auth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("go_to_rt_fust")
def test_auth_ls_password(driver_auth):
    '''Проверяем авторизацию по лс и паролю.'''
    driver = driver_auth
    # Кликаем на вкладку "Лицевой счёт"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-ls'))).click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).click()
    # Вводим лс
    driver.find_element(By.ID, 'username').send_keys(valid_ls)
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password'))).click()
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    
    # Кликаем на кнопку "Войти"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-login'))).click()

    # Проверяем что мы на странице пользователя странице пользователя
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'lfjrSy')))
        lc = driver.find_element(By.CLASS_NAME, 'lfjrSy')
        text = lc.text

        # Проверяем, соответствует ли текст ожидаемому значению
        expected_text = "Личный кабинет"
        assert text == expected_text, f"Тест прошел успешно, но текст элемента span не верный. Ожидалось '{expected_text}', получено '{text}'"
        
    except Exception as e:
        assert False, f"Не удалось найти элемент lfjrSy или произошла ошибка: {str(e)}"

@pytest.mark.usefixtures("go_to_rt_fust")
def test_auth_ls_fals_password(driver_auth):
    '''Проверяем предупреждение о неверном логине или пароле и отказ в доступе.'''
    driver = driver_auth
    # Кликаем на вкладку "Лицевой счёт"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-ls'))).click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).click()
    # Вводим лс
    driver.find_element(By.ID, 'username').send_keys(valid_ls)
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password'))).click()
    # Вводим неверный пароль
    driver.find_element(By.ID, 'password').send_keys(not_valid_password)
    
    # Кликаем на кнопку "Войти"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-login'))).click()

    # Проверяем предупреждене об ошибке
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'form-error-message')))
        alert = driver.find_element(By.ID, 'form-error-message')
        text = alert.text

        # Проверяем, соответствует ли текст ожидаемому значению
        expected_text = "Неверный логин или пароль"
        assert text == expected_text, f"Тест прошел успешно, но текст элемента span не верный. Ожидалось '{expected_text}', получено '{text}'"

    except Exception as e:
        assert False, f"Не удалось найти элемент form-error-message или произошла ошибка: {str(e)}"
    
@pytest.mark.usefixtures("go_to_rt_fust")
def test_auto_esti_auth_type_ls_to_phone(driver_auth):
    '''Проверяем автоматическая смену типа авторизации с ЛС на вход через телефон и пароль'''
    '''Известная ошибка. Проверка производится исходя из "Стандартная авторизация по логину и паролю" описанному в бриф.
    Лицевой счет состоит из цифр 7 или 12 символов.
    Поле ввода не допускает ввод спец символов. 
    Ввод 11 символов номера телефона будет считатся не верным форматом лс.
    А ввод символа "+" не доступно'''
    driver = driver_auth
    # Кликаем на вкладку "Лицевой счёт"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-ls'))).click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).click()
    # Вводим телефон
    driver.find_element(By.ID, 'username').send_keys(valid_p_number)
    
    # Кликаем на поле пароля для деактивации поля логина
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password'))).click()
    
    # Проверяем что тип поля ввода "Логин".
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'tab_type')))
    type = driver.find_element(By.NAME, "tab_type")
    value = type.get_attribute("value")
    assert value == "PHONE", f"Ожидалось 'PHONE', но получено '{value}'"
    
@pytest.mark.usefixtures("go_to_rt_fust")
def test_auto_esti_auth_type_ls_to_login(driver_auth):
    driver = driver_auth
    '''Проверяем автоматическая смену типа авторизации с ЛС на вход через логин и пароль'''
    '''Известная ошибка. Проверка производится исходя из "Стандартная авторизация по логину и паролю" описанному в бриф.
    Поле ввода не допускает ввод букв и спецсимволов'''
    # Кликаем на вкладку "Лицевой счёт"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-ls'))).click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).click()
    # Вводим логин
    driver.find_element(By.ID, 'username').send_keys(valid_login)
    
    # Кликаем на поле пароля для деактивации поля логина
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password'))).click()
    
    # Проверяем что тип поля ввода "Логин".
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'tab_type')))
    type = driver.find_element(By.NAME, "tab_type")
    value = type.get_attribute("value")
    assert value == "LOGIN", f"Ожидалось 'LOGIN', но получено '{value}'"
    
@pytest.mark.usefixtures("go_to_rt_fust")
def test_auto_esti_auth_type_ls_to_email(driver_auth):
    driver = driver_auth
    '''Проверяем автоматическая смену типа авторизации с ЛС на вход через почту и пароль'''
    '''Известная ошибка. Проверка производится исходя из "Стандартная авторизация по логину и паролю" описанному в бриф.
    Поле ввода не допускает ввод букв и спецсимволов'''
    # Кликаем на вкладку "Лицевой счёт"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-ls'))).click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).click()
    # Вводим почту
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    
    # Кликаем на поле пароля для деактивации поля логина
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password'))).click()
    
    # Проверяем что тип поля ввода "Почта".
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'tab_type')))
    type = driver.find_element(By.NAME, "tab_type")
    value = type.get_attribute("value")
    assert value == "EMAIL", f"Ожидалось 'EMAIL', но получено '{value}'"
    
@pytest.mark.usefixtures("go_to_rt_fust")
def test_ls_less_7(driver_auth):
    '''Проверяем ошибку формата лс при данных <7'''
    '''Известная ошибка.
    Личный счет не может быть меньше 7 символов'''
    driver = driver_auth
    # Кликаем на вкладку "Лицевой счёт"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-ls'))).click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).click()
    # Вводим лс <7
    driver.find_element(By.ID, 'username').send_keys(ls_l_7)
    
    # Кликаем на поле пароля для деактивации поля логина
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password'))).click()

    # Проверяем предупреждене об ошибке
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username-meta')))
        alert = driver.find_element(By.ID, 'username-meta')
        text = alert.text

        # Проверяем, соответствует ли текст ожидаемому значению
        expected_text = "Проверьте, пожалуйста, номер лицевого счета"
        assert text == expected_text, f"Тест прошел успешно, но текст элемента span не верный. Ожидалось '{expected_text}', получено '{text}'"

    except Exception as e:
        assert False, f"Не удалось найти элемент form-error-message или произошла ошибка: {str(e)}"
    
@pytest.mark.usefixtures("go_to_rt_fust")
def test_ls_more_7(driver_auth):
    '''Проверяем ошибку формата лс при данных >7'''
    driver = driver_auth
    # Кликаем на вкладку "Лицевой счёт"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-ls'))).click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).click()
    # Вводим лс >7
    driver.find_element(By.ID, 'username').send_keys(ls_m_7)
    
    # Кликаем на поле пароля для деактивации поля логина
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password'))).click()

    # Проверяем предупреждене об ошибке
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username-meta')))
        alert = driver.find_element(By.ID, 'username-meta')
        text = alert.text

        # Проверяем, соответствует ли текст ожидаемому значению
        expected_text = "Проверьте, пожалуйста, номер лицевого счета"
        assert text == expected_text, f"Тест прошел успешно, но текст элемента span не верный. Ожидалось '{expected_text}', получено '{text}'"

    except Exception as e:
        assert False, f"Не удалось найти элемент form-error-message или произошла ошибка: {str(e)}"
        
pytest.mark.usefixtures("go_to_rt_fust")
def test_ls_less_12(driver_auth):
    '''Проверяем ошибку формата лс при данных >7'''
    driver = driver_auth
    
    # Кликаем на кнопку "Войти с паролем" это заплатка, тест падает на таймауте driver_auth. Такое только с этим тестом. Увеличение времени ожидание не превело к хорошему результату.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'otp-form__back-login-btn'))).click()
    
    # Кликаем на вкладку "Лицевой счёт"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-ls'))).click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).click()
    # Вводим лс <12
    driver.find_element(By.ID, 'username').send_keys(ls_l_12)
    
    # Кликаем на поле пароля для деактивации поля логина
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password'))).click()

    # Проверяем предупреждене об ошибке
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username-meta')))
        alert = driver.find_element(By.ID, 'username-meta')
        text = alert.text

        # Проверяем, соответствует ли текст ожидаемому значению
        expected_text = "Проверьте, пожалуйста, номер лицевого счета"
        assert text == expected_text, f"Тест прошел успешно, но текст элемента span не верный. Ожидалось '{expected_text}', получено '{text}'"

    except Exception as e:
        assert False, f"Не удалось найти элемент form-error-message или произошла ошибка: {str(e)}"
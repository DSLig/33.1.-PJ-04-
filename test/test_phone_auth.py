import pytest
from src.fixtures import go_to_rt, go_to_rt_fust, driver, driver_auth
from src.settings import valid_email, valid_password, valid_p_number, not_valid_password, valid_login, valid_ls, p_number_l
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("go_to_rt_fust")
def test_auth_phone_password(driver_auth):
    '''Проверяем авторизацию по номеру и паролю.'''
    driver = driver_auth
    # Кликаем на вкладку "Телефон"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).click()
    # Вводим телефон
    driver.find_element(By.ID, 'username').send_keys(valid_p_number)
    
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
def test_auth_phone_fals_password(driver_auth):
    '''Проверяем предупреждение о неверном логине или пароле и отказ в доступе.'''
    driver = driver_auth
    # Кликаем на вкладку "Телефон"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).click()
    # Вводим телефон
    driver.find_element(By.ID, 'username').send_keys(valid_p_number)
    
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
def test_auto_esti_auth_type_phone_to_login(driver_auth):
    '''Проверяем автоматическая смену типа авторизации с Телефона на вход через логин и пароль'''
    driver = driver_auth
    # Кликаем на вкладку "Телефон"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    
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
def test_auto_esti_auth_type_phone_to_email(driver_auth):
    driver = driver_auth
    '''Проверяем автоматическая смену типа авторизации с Телефона на вход через почту и пароль'''
    # Кликаем на вкладку "Телефон"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    
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
def test_auto_esti_auth_type_phone_to_ls(driver_auth):
    '''Проверяем автоматическая смену типа авторизации с Телефона на вход через лс и пароль'''
    '''Известная ошибка. Проверка производится исходя из "Стандартная авторизация по логину и паролю" описанному в бриф.
    Из-за того что номер и лс состоит из цифр, и поле ввода,
    в первую очередь, проверяет правельность формата номера 
    и не дает ввести больше 12 символов. 
    Но и не распознает 7 сомволов как ЛС.'''
    driver = driver_auth
    # Кликаем на вкладку "Телефон"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).click()
    # Вводим ЛС
    driver.find_element(By.ID, 'username').send_keys(valid_ls)
    
    # Кликаем на поле пароля для деактивации поля логина
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password'))).click()
    
    # Проверяем что тип поля ввода "ЛС".
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'tab_type')))
    type = driver.find_element(By.NAME, "tab_type")
    value = type.get_attribute("value")
    assert value == "LS", f"Ожидалось 'LS', но получено '{value}'"
    
@pytest.mark.usefixtures("go_to_rt_fust")
def test_meta_error_number(driver_auth):
    '''Проверка  предупреждения о не верном формате номера телефона'''
    driver = driver_auth
    
     # Кликаем на вкладку "Телефон"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).click()
    # Вводим телефон
    driver.find_element(By.ID, 'username').send_keys(p_number_l)
    
    # Кликаем на поле пароля для деактивации поля логина
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password'))).click()
    
    # Проверяем предупреждене об ошибке
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username-meta')))
        alert = driver.find_element(By.ID, 'username-meta')
        text = alert.text

        # Проверяем, соответствует ли текст ожидаемому значению
        expected_text = "Неверный формат телефона"
        assert text == expected_text, f"Тест прошел успешно, но текст элемента span не верный. Ожидалось '{expected_text}', получено '{text}'"

    except Exception as e:
        assert False, f"Не удалось найти элемент username-meta или произошла ошибка: {str(e)}"
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    '''Главная страница сайта'''
    driver = webdriver.Chrome()
    driver.get('https://astrakhan.rt.ru/')
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def driver_auth():
    '''Страница авторизации'''
    driver= webdriver.Chrome()
    driver.get('https://lk.rt.ru/')
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def go_to_rt(driver):
    '''Фикстура для перехода на страницу авторизации с главной сайта'''
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'tmp_resolve_touch_link'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'otp-form__back-login-btn'))).click()
    
@pytest.fixture()
def go_to_rt_fust(driver_auth):
    '''Фикстура для прямого доступа к стринице авторизации'''
    driver = driver_auth
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'otp-form__back-login-btn'))).click()
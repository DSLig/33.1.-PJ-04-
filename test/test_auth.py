import pytest
from src.fixtures import go_to_rt, go_to_rt_fust, driver, driver_auth
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures("go_to_rt")
def test_go_to_rt(driver):
    '''Проверяем доступ к странице авторизации с главной сайта'''
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[@class="what-is__title" and text()="Личный кабинет"]')))
    assert driver.find_element(By.XPATH, '//h2[@class="what-is__title" and text()="Личный кабинет"]'), "Не удалось подтвердить, что мы на странице Личного кабинета"


@pytest.mark.usefixtures("go_to_rt_fust")
def test_go_to_rt_(driver_auth):
    '''Проверяем доступ к странице сайта через ссылку'''
    WebDriverWait(driver_auth, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[@class="what-is__title" and text()="Личный кабинет"]')))
    assert driver_auth.find_element(By.XPATH, '//h2[@class="what-is__title" and text()="Личный кабинет"]'), "Не удалось подтвердить, что мы на странице Личного кабинета"
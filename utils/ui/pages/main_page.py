
import asserts

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import urllib3

from utils.ui.helpers.navigation import NavigationHelper
from utils.ui.locators import LocatorMainPage

http = urllib3.PoolManager(retries=3)
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')


# Class MainPage со следующими методами:
# 1. Методы навигации браузера.
# 2. Проверка урла.

class MainPage(LocatorMainPage):

    # Функции для работы со страницей авторизации и главной страницей

    # Авторизация
    def perform_authorization(self, browser, wait):

        # Настроить браузер
        browser.implicitly_wait(5)
        wait = WebDriverWait(browser, 5)
        browser.set_window_size(1280, 1280)

        NavigationHelper.page_allure(browser)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator_login_field)))

    # Ввести в поле логин
        login_field = browser.find_element(By.CSS_SELECTOR, self.locator_login_field)
        login_field.click()
        login_field.send_keys('Rusla.Yuldashev')
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator_pass_field)))

    # Ввести в поле пароль
        pass_field = browser.find_element(By.CSS_SELECTOR, self.locator_pass_field)
        pass_field.click()
        pass_field.send_keys('yVx435RNw%Jz^y5>')
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator_confirm)))

    # Нажать кнопку Подтвердить
        confirm = browser.find_element(By.CSS_SELECTOR, self.locator_confirm)
        confirm.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator_main_menu_of_page)))

        pass

    # 1. Открыть главную страницу
    def open_main_page(self, browser, wait):
        NavigationHelper.page_main(browser)
        wait = WebDriverWait(browser, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_test_cases_section)))

        pass

    # Открыть страницу для создания suite и тест-кейса
    def open_page_to_create_test_cases(self, browser, wait):
        NavigationHelper.page_create_suite_and_test_cases(browser)
        wait = WebDriverWait(browser, 1)
        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_create_suite_and_test_cases)))

        pass

    # Открыть страницу Запуски
    def open_launch_page(self, browser, wait):
        NavigationHelper.page_launch(browser)
        wait = WebDriverWait(browser, 1)
        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_open_launch_page)))

        pass

    # Обновить страницу
    def refresh_page(self, browser, wait):
        NavigationHelper.page_refresh(browser)

        pass

    # 2. Перейти в раздел Test cases
    def go_to_test_cases_section(self, browser, wait):
        test_cases_section = browser.find_element(By.XPATH, self.locator_test_cases_section)
        test_cases_section.click()

        pass

    # 3. Проверить, что url содержит значение /test-cases
    # url: https://allure.x5.ru/project/123/test-cases
    def check_that_url_contains_value_test_cases(self, browser, wait):
        get_url = browser.current_url
        print("\n")
        print(browser.current_url)
        asserts.assert_in('/test-cases', get_url, 'The fragment /test-cases was not found in the URL')

        pass

    # 4. Вернуться на главную страницу при помощи встроенных инструментов навигации браузера
    def return_to_main_page(self, browser, wait):
        NavigationHelper.page_return_main(browser)

        pass

    # Закрыть браузер
    def close_browser(self, browser, wait):
        NavigationHelper.browser_close(browser)

        pass


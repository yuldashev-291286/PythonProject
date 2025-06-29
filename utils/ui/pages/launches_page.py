
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import urllib3
from selenium.webdriver.support.wait import WebDriverWait

from utils.ui.locators import LocatorLaunchesPage

http = urllib3.PoolManager(retries=3)

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')

from utils.ui.pages.main_page import MainPage

# Реализовать следующие сценарии с использованием PO (имя класса со вспомогательными методами для этих сценариев LaunchesPage):
class LaunchesPage(LocatorLaunchesPage):

    # Первый сценарий:
    # 1. Открыть свои тест-кейсы.
    # 2. Выбрать 2 тест-кейса.
    # 3. Нажать на Bulk Actions -> Выбрать Run.
    # 4. Ввести имя ланча.
    # 5. Создать свой тег ланча.
    # 6. Нажать Submit.
    # 7. Проверить, что появилось окно с подтверждением созданного ланча.

    def run_created_test_cases(self, browser, wait):

        # 2. Выбрать 2 тест-кейса
        # Делаем фильтр по созданному новому тест-кейсу
        search_and_filter_bar = browser.find_element(By.XPATH, self.locator_search_and_filter_bar)
        ActionChains(browser).move_to_element(search_and_filter_bar).click(search_and_filter_bar).send_keys("Новый тест-кейс для проверки ланча").send_keys(Keys.ENTER).perform()

        # Ждем когда список кейсов прогрузится по заданному фильтру
        wait_for_case_list_load = WebDriverWait(browser, 40)
        wait_for_case_list_load.until(EC.presence_of_element_located((By.XPATH, self.locator_new_test_case_found)))

        # Выбираем первый кейс
        select_test_case_first = browser.find_element(By.XPATH, self.locator_select_test_case_first)
        ActionChains(browser).move_to_element(select_test_case_first).click(select_test_case_first).perform()

        # Выбираем второй кейс
        select_test_case_last_second = browser.find_element(By.XPATH, self.locator_select_test_case_second)
        ActionChains(browser).move_to_element(select_test_case_last_second).click(select_test_case_last_second).perform()

        # 3. Нажать на Bulk Actions -> Выбрать Run.

        # Нажать кнопку Запустить
        run_selected_test_case = browser.find_element(By.XPATH, self.locator_run_selected_test_case)
        run_selected_test_case.click()

        # 4. Ввести имя ланча.
        lunch_name = browser.find_element(By.XPATH, self.locator_lunch_name)
        ActionChains(browser).move_to_element(lunch_name).click().send_keys(", Тестовый запуск, Юлдашев Р.А.").perform()

        # 5. Создать свой тег ланча. Не получается создать, так как событие Keys.ENTER для ActionChains не проходит после введения нового значения тега в поле поиска.
        # Выбираем тег из существующих в поле поиска.
        drop_down_list_of_tags = browser.find_element(By.XPATH, self.locator_drop_down_list_of_tags)
        drop_down_list_of_tags.click()

        input_name_tag = browser.find_element(By.XPATH, self.locator_input_name_tag)
        ActionChains(browser).move_to_element(input_name_tag).click().send_keys("new_project").send_keys(Keys.ENTER).perform()

        wait = WebDriverWait(browser, 1)
        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_select_name_tag)))
        select_name_tag = browser.find_element(By.XPATH, self.locator_select_name_tag)
        select_name_tag.click()

        # 6. Нажать Submit.
        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_submit)))
        submit = browser.find_element(By.XPATH, self.locator_submit)
        submit.click()

        # 7. Проверить, что появилось окно с подтверждением созданного ланча.
        wait = WebDriverWait(browser, 15)
        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_notification_run)))
        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_run)))

    pass


    # Второй сценарий:
    # 1. Перейти в Launches.
    # 2. Найти и открыть свой ланч.
    # 3. Проверить, что в Success rate отображается0 %.
    # 4. Перейти в тест-кейсы этого ланча.
    # 5. Открыть первый тест-кейс. Нажать на Failed. Проверить, что у тест-кейса стоит статус Failed.
    # 6. Открыть второй тест-кейс. Нажать на Pass. Проверить, что у тест-кейса стоит статус Pass.
    # 7. Перейти в Overview.
    # 8. Проверить, что в Success rate отображается 50%.
    # 9. Нажать на CloseLaunch.
    # 10. Проверить, что появилось окно о закрытии ланча.

    def check_test_cases_in_launches(self, browser, wait):

        # 2. Найти и открыть свой ланч. Например: Запуск от 25/06/2025 11:26, Тестовый запуск, Юлдашев Р.А.
        run_test_cases = browser.find_element(By.XPATH, self.locator_run_test_cases)
        run_test_cases.click()

        # Ждем, когда откроется страница выбранного запуска
        wait = WebDriverWait(browser, 1)
        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_selected_launch_page)))

        # 3. Проверить, что в Success rate отображается 0%.
        success_rate = browser.find_element(By.CSS_SELECTOR, self.locator_success_rate)
        assert success_rate.text == "0%", "В success rate отображается не 0%"
        print("\n" + success_rate.text)

        # 4. Перейти в тест-кейсы этого ланча.
        test_cases_this_lunch = browser.find_element(By.XPATH, self.locator_test_cases_this_lunch)
        test_cases_this_lunch.click()

        # 5. Открыть первый тест-кейс. Нажать на Failed. Проверить, что у тест-кейса стоит статус Failed.
        test_cases_lunch_one = browser.find_element(By.XPATH, self.locator_test_cases_lunch_one)
        test_cases_lunch_one.click()

        failed = browser.find_element(By.XPATH, self.locator_failed)
        failed.click()

        confirm_failed = browser.find_element(By.XPATH, self.locator_confirm_failed)
        confirm_failed.click()

        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_failed_test_case)))

        failed_test_case = browser.find_element(By.XPATH, self.locator_failed_test_case)
        assert failed_test_case.text == "НЕУСПЕШНЫЙ", "Отсутствует тест-кейс со статусом НЕУСПЕШНЫЙ"
        print("\n" + failed_test_case.text)

        # 6. Открыть второй тест-кейс. Нажать на Pass. Проверить, что у тест-кейса стоит статус Pass.
        test_cases_lunch_two = browser.find_element(By.XPATH, self.locator_test_cases_lunch_two)
        test_cases_lunch_two.click()

        success = browser.find_element(By.XPATH, self.locator_success)
        success.click()

        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_success_test_case)))

        success_test_case = browser.find_element(By.XPATH, self.locator_success_test_case)
        assert success_test_case.text == "УСПЕШНЫЙ", "Отсутствует тест-кейс со статусом УСПЕШНЫЙ"
        print("\n" + success_test_case.text)

        # 7. Перейти в Overview.
        overview_lunch = browser.find_element(By.XPATH, self.locator_overview_lunch)
        overview_lunch.click()

        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_overview)))

        main_page = MainPage()
        main_page.refresh_page(browser, wait)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator_success_rate_after)))

        # 8. Проверить, что в Success rate отображается 50%.
        success_rate_after = browser.find_element(By.CSS_SELECTOR, self.locator_success_rate_after)
        assert success_rate_after.text == "50%", "В success rate отображается не 50%"
        print("\n" + success_rate_after.text)

        # 9. Нажать на CloseLaunch.
        close_lunch = browser.find_element(By.XPATH, self.locator_close_lunch)
        close_lunch.click()

        # 10. Проверить, что появилось окно о закрытии ланча.
        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_notification_closed_launch)))
        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_notification_launch_completed)))



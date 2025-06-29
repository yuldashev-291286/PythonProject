
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import urllib3

http = urllib3.PoolManager(retries=3)
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')

from utils.ui.pages.main_page import MainPage
from utils.ui.pages.case_view_page import CaseViewPage

@pytest.mark.skip
class TestsLaunchesPage:

    # Первый сценарий:
    # 1. Открыть свои тест-кейсы.
    # 2. Выбрать 2 тест-кейса.
    # 3. Нажать на Bulk Actions -> Выбрать Run.
    # 4. Ввести имя ланча.
    # 5. Создать свой тег ланча.
    # 6. Нажать Submit.
    # 7. Проверить, что появилось окно с подтверждением созданного ланча.

    @pytest.mark.skip
    def test_first_scenario(self):

        browser = webdriver.Chrome()
        browser.implicitly_wait(1)
        wait = WebDriverWait(browser, 15)
        browser.set_window_size(1280, 1280)

        main_page = MainPage()
        case_view_page = CaseViewPage()

        # Авторизоваться
        main_page.perform_authorization(browser, wait)

        # 1. Открыть свои тест-кейсы
        main_page.open_page_to_create_test_cases(browser, wait)

        # Создаем два новых тест-кейса для проверки ланча.
        case_view_page.create_test_cases(browser, wait, "Новый тест-кейс для проверки ланча №1")
        case_view_page.create_test_cases(browser, wait, "Новый тест-кейс для проверки ланча №2")

        # 2. Выбрать 2 тест-кейса

        # Делаем фильтр по созданному новому тест-кейсу
        locator_search_and_filter_bar = "//div[@class='_comboBox_1wc1o_16']"
        search_and_filter_bar = browser.find_element(By.XPATH, locator_search_and_filter_bar)
        ActionChains(browser).move_to_element(search_and_filter_bar).click(search_and_filter_bar).send_keys("Новый тест-кейс для проверки ланча").send_keys(Keys.ENTER).perform()

        # Ждем когда список кейсов прогрузится по заданному фильтру
        locator_new_test_case_found = "//div[@class='_tree_14p85_8']//div[@class='test-tree-row'][last()]"
        wait_for_case_list_load = WebDriverWait(browser, 40)
        wait_for_case_list_load.until(EC.presence_of_element_located((By.XPATH, locator_new_test_case_found)))

        # Выбираем первый кейс
        locator_select_test_case_first = "//div[@class='_iconWrapper_1a6ad_42']/ancestor::*[2]/label[@aria-label='Выбрать Новый тест-кейс для проверки ланча №1']"
        select_test_case_first = browser.find_element(By.XPATH, locator_select_test_case_first)
        ActionChains(browser).move_to_element(select_test_case_first).click(select_test_case_first).perform()

        # Выбираем второй кейс
        locator_select_test_case_second = "//div[@class='_iconWrapper_1a6ad_42']/ancestor::*[2]/label[@aria-label='Выбрать Новый тест-кейс для проверки ланча №2']"
        select_test_case_last_second = browser.find_element(By.XPATH, locator_select_test_case_second)
        ActionChains(browser).move_to_element(select_test_case_last_second).click(select_test_case_last_second).perform()

        # 3. Нажать на Bulk Actions -> Выбрать Run.

        # Нажать кнопку Запустить
        run_selected_test_case = browser.find_element(By.XPATH, "//button[@data-testid='button__create-run' and @aria-label='Запустить']")
        run_selected_test_case.click()

        # 4. Ввести имя ланча.
        lunch_name = browser.find_element(By.XPATH, "//input[@class='InputBox__box InputBox__box_base']")
        ActionChains(browser).move_to_element(lunch_name).click().send_keys(", Тестовый запуск, Юлдашев Р.А.").perform()

        # 5. Создать свой тег ланча. Не получается создать, так как событие Keys.ENTER для ActionChains не проходит после введения нового значения тега в поле поиска.
        # Выбираем тег из существующих в поле поиска.
        drop_down_list_of_tags = browser.find_element(By.XPATH, "//div[@class='SelectBox ']")
        drop_down_list_of_tags.click()

        input_name_tag = browser.find_element(By.XPATH, "//input[@class='InputBox__box InputBox__box_small']")
        ActionChains(browser).move_to_element(input_name_tag).click().send_keys("new_project").send_keys(Keys.ENTER).perform()

        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='SelectBoxOptionsList__item-label' and text()='new_project']")))
        select_name_tag = browser.find_element(By.XPATH, "//span[@class='SelectBoxOptionsList__item-label' and text()='new_project']")
        select_name_tag.click()

        # 6. Нажать Submit.
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Отправить']")))
        submit = browser.find_element(By.XPATH, "//button[@aria-label='Отправить']")
        submit.click()

        # 7. Проверить, что появилось окно с подтверждением созданного ланча.
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='Notification']")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Создан']/a[contains(text(),'Запуск от')]")))


    # Второй сценарий:
    # 1. Перейти в Launches.
    # 2. Найти и открыть свой ланч.
    # 3. Проверить, что в Success rate отображается 0%.
    # 4. Перейти в тест-кейсы этого ланча.
    # 5. Открыть первый тест-кейс. Нажать на Failed. Проверить, что у тест-кейса стоит статус Failed.
    # 6. Открыть второй тест-кейс. Нажать на Pass. Проверить, что у тест-кейса стоит статус Pass.
    # 7. Перейти в Overview.
    # 8. Проверить, что в Success rate отображается 50%.
    # 9. Нажать на CloseLaunch.
    # 10. Проверить, что появилось окно о закрытии ланча.

    # После того как тест будет сделан, обязательно пометить его skip, в дальнейшем не использовать его.
    @pytest.mark.skip
    def test_two_scenario(self):

        browser = webdriver.Chrome()
        browser.implicitly_wait(1)
        wait = WebDriverWait(browser, 15)
        browser.set_window_size(1280, 1280)

        main_page = MainPage()

        main_page.perform_authorization(browser, wait)

        # 1. Перейти в Launches.
        main_page.open_launch_page(browser, wait)

        # 2. Найти и открыть свой ланч. Например: Запуск от 25/06/2025 11:26, Тестовый запуск, Юлдашев Р.А.
        run_test_cases = browser.find_element(By.XPATH, "//a[@class='_name_s0uet_21' and contains(text(),'Тестовый запуск, Юлдашев Р.А.')]")
        run_test_cases.click()

        # Ждем, когда откроется страница выбранного запуска
        wait.until(EC.presence_of_element_located((By.XPATH, "//h2[@class='_heading_ns9g6_40']//div[@class='_content_7zz50_6' and contains(text(),'Тестовый запуск, Юлдашев Р.А.')]")))

        # 3. Проверить, что в Success rate отображается 0%.
        success_rate = browser.find_element(By.CSS_SELECTOR, "text._centeredMetricTitle_1qii2_41")
        assert success_rate.text == "0%", "В success rate отображается не 0%"
        print("\n" + success_rate.text)

        # 4. Перейти в тест-кейсы этого ланча.
        test_cases_this_lunch = browser.find_element(By.XPATH, "//span[@class='Tabs__text' and text()='Результаты тестов']")
        test_cases_this_lunch.click()

        # 5. Открыть первый тест-кейс. Нажать на Failed. Проверить, что у тест-кейса стоит статус Failed.
        test_cases_lunch_one = browser.find_element(By.XPATH, "//span[@class='_typography-paragraphs-text-m_skegg_28 _name_1nirb_12' and @title='Новый тест-кейс для проверки ланча №1']")
        test_cases_lunch_one.click()

        failed = browser.find_element(By.XPATH, "//span[@class='_text_1mh1e_790' and text()='Неуспешный']")
        failed.click()

        confirm_failed = browser.find_element(By.XPATH, "//span[@class='_text_1mh1e_790' and text()='Отправить']")
        confirm_failed.click()

        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='_text_j9tew_11 _typography-ui-text-s-ui-bold_skegg_72' and text()='Неуспешный']")))

        failed_test_case = browser.find_element(By.XPATH, "//span[@class='_text_j9tew_11 _typography-ui-text-s-ui-bold_skegg_72' and text()='Неуспешный']")
        assert failed_test_case.text == "НЕУСПЕШНЫЙ", "Отсутствует тест-кейс со статусом НЕУСПЕШНЫЙ"
        print("\n" + failed_test_case.text)

        # 6. Открыть второй тест-кейс. Нажать на Pass. Проверить, что у тест-кейса стоит статус Pass.
        test_cases_lunch_two = browser.find_element(By.XPATH, "//span[@class='_typography-paragraphs-text-m_skegg_28 _name_1nirb_12' and @title='Новый тест-кейс для проверки ланча №2']")
        test_cases_lunch_two.click()

        failed = browser.find_element(By.XPATH, "//span[@class='_text_1mh1e_790' and text()='Успешный']")
        failed.click()

        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='_text_j9tew_11 _typography-ui-text-s-ui-bold_skegg_72' and text()='Успешный']")))

        success_test_case = browser.find_element(By.XPATH, "//span[@class='_text_j9tew_11 _typography-ui-text-s-ui-bold_skegg_72' and text()='Успешный']")
        assert success_test_case.text == "УСПЕШНЫЙ", "Отсутствует тест-кейс со статусом УСПЕШНЫЙ"
        print("\n" + success_test_case.text)

        # 7. Перейти в Overview.
        overview_lunch = browser.find_element(By.XPATH, "//span[@class='Tabs__text' and text()='Обзор']")
        overview_lunch.click()

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='_pieContainer_1qii2_9 _hasLink_1qii2_22']")))
        main_page.refresh_page(browser, wait)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "text._centeredMetricTitle_1qii2_41")))

        # 8. Проверить, что в Success rate отображается 50%.
        success_rate_after = browser.find_element(By.CSS_SELECTOR, "text._centeredMetricTitle_1qii2_41")
        assert success_rate_after.text == "50%", "В success rate отображается не 50%"
        print("\n" + success_rate_after.text)

        # 9. Нажать на CloseLaunch.
        close_lunch = browser.find_element(By.XPATH, "//button[@aria-label='Завершить']")
        close_lunch.click()

        # 10. Проверить, что появилось окно о закрытии ланча.
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='Notification']")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//h5[@class='Notification__title' and text()='Запуск завершен']")))



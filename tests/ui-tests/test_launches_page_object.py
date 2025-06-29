
import pytest
from selenium.webdriver.support.ui import WebDriverWait as wait

import urllib3

from utils.ui.applications import InitBrowser

http = urllib3.PoolManager(retries=3)
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')

from utils.ui.pages.main_page import MainPage
from utils.ui.pages.case_view_page import CaseViewPage
from utils.ui.pages.launches_page import LaunchesPage

@pytest.mark.skip
class TestsLaunchesPageObject:

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

        browser = InitBrowser.init_browser("Chrome")

        main_page = MainPage()
        case_view_page = CaseViewPage()
        launches_page = LaunchesPage()

        # Авторизоваться
        main_page.perform_authorization(browser, wait)

        # 1. Открыть свои тест-кейсы
        main_page.open_page_to_create_test_cases(browser, wait)

        # Создаем два новых тест-кейса для проверки ланча.
        case_view_page.create_test_cases(browser, wait, "Новый тест-кейс для проверки ланча №1")
        case_view_page.create_test_cases(browser, wait, "Новый тест-кейс для проверки ланча №2")

        # 2. Выбрать 2 тест-кейса.
        # 3. Нажать на Bulk Actions -> Выбрать Run.
        # 4. Ввести имя ланча.
        # 5. Создать свой тег ланча.
        # 6. Нажать Submit.
        # 7. Проверить, что появилось окно с подтверждением созданного ланча.
        launches_page.run_created_test_cases(browser, wait)


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

    @pytest.mark.skip
    def test_two_scenario(self):

        browser = InitBrowser.init_browser("Chrome")

        main_page = MainPage()
        launches_page = LaunchesPage()

        main_page.perform_authorization(browser, wait)

        # 1. Перейти в Launches.
        main_page.open_launch_page(browser, wait)

        # 2. Найти и открыть свой ланч.
        # 3. Проверить, что в Success rate отображается 0%.
        # 4. Перейти в тест-кейсы этого ланча.
        # 5. Открыть первый тест-кейс. Нажать на Failed. Проверить, что у тест-кейса стоит статус Failed.
        # 6. Открыть второй тест-кейс. Нажать на Pass. Проверить, что у тест-кейса стоит статус Pass.
        # 7. Перейти в Overview.
        # 8. Проверить, что в Success rate отображается 50%.
        # 9. Нажать на CloseLaunch.
        # 10. Проверить, что появилось окно о закрытии ланча.
        launches_page.check_test_cases_in_launches(browser, wait)



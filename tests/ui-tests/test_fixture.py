
import time

from selenium.webdriver.support.ui import WebDriverWait as wait

import urllib3

from utils.ui.applications import InitBrowser
from utils.ui.pages.main_page import MainPage
from utils.ui.pages.case_view_page import CaseViewPage

http = urllib3.PoolManager(retries=3)
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')

import pytest


class TestsFixture:

    # 2. Фикстура browser, которая принимает параметр с названием браузера (Firefox/Chrome). Должна возвращать указанный браузер 1 раз за сессию.
    # Проверка запуска браузеров, в зависимости от параметра фикстуры: 'Chrome', 'Firefox', 'Edge', 'Ie'.
    @pytest.mark.edit_case
    def test_fixture_name_browser(self, run_browser_from_fixture):
        run_browser_from_fixture.quit()
        print("\nПроверка запуска браузеров 'Chrome', 'Firefox', 'Edge', 'Ie' через фикстуру с параметрами.")


    # 3. Фикстура для авторизации.
    # Авторизация
    @pytest.mark.edit_case
    def test_authorization_fixture(self, authorization_fixture):
        time.sleep(1)
        print("\nПроверка авторизации через фикстуру.")


    # 5. Параметризовать тесты из пункта 4 (минимум 3 набора параметров в каждом тесте)
    names_cases = ["Новый тест-кейс №1", pytest.param("Новый тест-кейс №2", marks=pytest.mark.xfail), "Новый тест-кейс №3"]
    descriptions_cases = ["New test case number one", "New test case number two", "New test case number three"]
    @pytest.mark.parametrize('name_test_case', names_cases, ids=descriptions_cases)
    @pytest.mark.edit_case
    def test_edit_created_test_case_fixture_parametrize(self, name_test_case):
        browser = InitBrowser.init_browser("Chrome")
        main_page = MainPage()
        case_view_page = CaseViewPage()

        main_page.perform_authorization(browser, wait)
        main_page.open_page_to_create_test_cases(browser, wait)

        case_view_page.create_test_cases(browser, wait, name_test_case)
        print("\nСоздан новый тест-кейс.")

        case_view_page.edit_test_case(browser, wait)
        print("\nОтредактирован новый тест-кейс.")

        case_view_page.delete_test_case(browser, wait)
        print("\nУдален ранее созданный тест-кейс.")
        main_page.close_browser(browser, wait)



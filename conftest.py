
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait

from utils.ui.applications import InitBrowser
from utils.ui.pages.main_page import MainPage
from utils.ui.pages.case_view_page import CaseViewPage

import pytest

# 2. Фикстура browser, которая принимает параметр с названием браузера (Firefox/Chrome). Должна возвращать указанный браузер 1 раз за сессию.
@pytest.fixture(params=['Chrome', 'Firefox', 'Edge', 'Ie'])
def value_browser_from_fixture(request):
    return request.param

@pytest.fixture() # module, session, class, function
def run_browser_from_fixture(value_browser_from_fixture):
    if value_browser_from_fixture == 'Chrome':
        return webdriver.Chrome()
    if value_browser_from_fixture == 'Firefox':
        return webdriver.Firefox()
    if value_browser_from_fixture == 'Edge':
        return webdriver.Edge()
    if value_browser_from_fixture == 'Ie':
        return webdriver.Ie()
    else:
        return None


# 3. Фикстура для авторизации.
@pytest.fixture(scope='session') # module, session, class, function
def authorization_fixture():
    browser = InitBrowser.init_browser("Chrome")
    main_page = MainPage()
    main_page.perform_authorization(browser, wait)


# 1. Фикстура создания и удаления тест-кейса (scope module)
# 4. Редактирование тест-кейса (a, b, с - разные тесты): a. Отредактировать название тест-кейса; b. Отредактировать сценарий тест-кейса; c. Отредактировать description тест-кейса.
@pytest.fixture(scope='session') # module, session, class, function
def fixture_test_case():
    browser = InitBrowser.init_browser("Chrome")
    main_page = MainPage()
    case_view_page = CaseViewPage()

    main_page.perform_authorization(browser, wait)
    main_page.open_page_to_create_test_cases(browser, wait)

    case_view_page.create_test_cases(browser, wait)
    print("\nСоздан новый тест-кейс.")

    case_view_page.edit_test_case(browser, wait)
    print("\nОтредактирован новый тест-кейс.")

    yield # Здесь выполняется сам авто-тест

    case_view_page.delete_test_case(browser, wait)
    print("\nУдален ранее созданный тест-кейс.")
    main_page.close_browser(browser, wait)


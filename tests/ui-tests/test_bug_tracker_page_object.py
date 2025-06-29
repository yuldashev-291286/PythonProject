
from selenium.webdriver.support.wait import WebDriverWait as wait

import urllib3

from utils.ui.applications import InitBrowser
from utils.ui.pages.case_list_page import CaseListPage
from utils.ui.pages.main_page import MainPage
from utils.ui.pages.case_view_page import CaseViewPage

http = urllib3.PoolManager(retries=3)
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')


class TestsBugTrackerPageObject:

    # Тест №1. Навигация

    # 1. Открыть главную страницу https://allure.x5.ru/project/123/dashboards
    # 2. Перейти в раздел Test cases
    # 3. Проверить, что url содержит значение /test-cases
    # 4. Вернуться на главную страницу при помощи встроенных инструментов навигации браузера

    def test_navigation_page_object(self):

        browser = InitBrowser.init_browser("Chrome")

        # Шаги для главной страницы
        main_page = MainPage()

        main_page.perform_authorization(browser, wait)
        main_page.open_main_page(browser, wait)
        main_page.go_to_test_cases_section(browser, wait)
        main_page.check_that_url_contains_value_test_cases(browser, wait)

        main_page.return_to_main_page(browser, wait)
        main_page.close_browser(browser, wait)


    # Тест №2. Проверка тест-кейсов Структура

    # 1. Перейти в раздел Test cases
    # 2. Проверить, что выбран вид отображения кейсов Features
    # 3. Проверить, что тест-кейсы на странице отображаются в папках
    # 4. Изменить вид отображения кейсов на Test-cases
    # 5. Проверить, что меняется заголовок на Test-cases. Проверить, что и на странице отображаются тест-кейсы без папок.

    def test_cases_verification_structure_page_object(self):

        browser = InitBrowser.init_browser("Chrome")

        # Шаги для главной страницы
        main_page = MainPage()

        main_page.perform_authorization(browser, wait)
        main_page.open_main_page(browser, wait)
        main_page.go_to_test_cases_section(browser, wait)

        # Шаги для работы со списком кейсов
        case_list_page = CaseListPage()

        case_list_page.features_view_selected_and_cases_in_folders(browser, wait)
        case_list_page.type_test_cases_and_cases_without_folders_is_selected(browser, wait)

        main_page.close_browser(browser, wait)


    # Тест №3. Проверка тест-кейсов Сортировка

    # 1. Перейти в раздел Test cases
    # 2. Изменить вид отображения кейсов на Test-cases
    # 3. Проверить сортировку по возрастанию по полю id

    def test_check_sort_page_object(self):

        browser = InitBrowser.init_browser("Chrome")

        # Шаги для главной страницы
        main_page = MainPage()

        main_page.perform_authorization(browser, wait)
        main_page.open_main_page(browser, wait)
        main_page.go_to_test_cases_section(browser, wait)

        # Шаги для работы со списком кейсов
        case_list_page = CaseListPage()

        case_list_page.view_cases_test_cases_and_check_sort_in_ascending_order_by_id_field(browser, wait)

        main_page.close_browser(browser, wait)


    # Тест №4. Проверка тест-кейсов Фильтрация.

    # 1. Перейти в раздел Test cases
    # 2. Навести курсор на иконку фильтрации. Проверить что появляется попап
    # 3. Нажать на кнопку фильтрации
    # 4. Нажать на +
    # 5. Отфильтровать тест-кейсы по статусу Review и проверить, что фильтрация работает
    # 6. Отфильтровать тест-кейсы по тегу: ввести значение regress. Нажать на Enter. Проверить, что фильтрация работает
    # 7. Сделать комбинированную фильтрацию. Выбрать Layer: UI тест и status: Active
    # 8. Проверить, что фильтрация работает

    def test_case_check_filter_page_object(self):

        browser = InitBrowser.init_browser("Chrome")

        # Шаги для главной страницы
        main_page = MainPage()

        main_page.perform_authorization(browser, wait)
        main_page.open_main_page(browser, wait)
        main_page.go_to_test_cases_section(browser, wait)

        # Шаги для работы со списком кейсов
        case_list_page = CaseListPage()

        case_list_page.filter_test_cases_by_review_status_and_check_that_filter_works(browser, wait)
        case_list_page.filter_cases_by_regress_tag_and_check_what_works(browser, wait)
        case_list_page.make_combined_filter_and_check_what_works(browser, wait)

        main_page.close_browser(browser, wait)


    # Тест №5. Проверка тест-кейса “02 Столбцы с модулем”

    # 1. Проверить заголовок и id тест-кейса
    # 2. Проверить структуру. В тест-кейсе есть блоки: Description, Precondition, Scenario, Expected result, Comments
    # 3. Проверить что отображается картинка в сценарии
    # 4. Перейти в Attachment и проверить что там отображается та же картинка. Проверить по имени файла
    # 5. Проверить что в тегах указан только regress
    # 6. Проверить поле Fields. Feature == "Ермолов Эд", Story == Экран "Рассчитанные цены"

    def test_check_test_case_number_two_columns_with_module_page_object(self):

        browser = InitBrowser.init_browser("Chrome")

        # Шаги для главной страницы
        main_page = MainPage()

        main_page.perform_authorization(browser, wait)
        main_page.open_main_page(browser, wait)
        main_page.go_to_test_cases_section(browser, wait)

        # Шаги для работы с кейсом
        case_view_page = CaseViewPage()

        case_view_page.check_title_and_id_of_test_case(browser, wait)
        case_view_page.check_test_case_structure(browser, wait)
        case_view_page.check_that_picture_is_displayed_in_script_in_attachment(browser, wait)
        case_view_page.check_values_in_tags_and_fields(browser, wait)

        main_page.close_browser(browser, wait)



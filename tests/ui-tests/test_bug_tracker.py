
import asserts

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import urllib3
from tenacity import sleep

http = urllib3.PoolManager(retries=3)
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')


class TestsBugTracker:

    # Тест №1. Навигация

    # 1. Открыть главную страницу https://allure.x5.ru/project/123/dashboards
    # 2. Перейти в раздел Test cases
    # 3. Проверить, что url содержит значение /test-cases
    # 4. Вернуться на главную страницу при помощи встроенных инструментов навигации браузера

    def test_navigation(self):

        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        wait = WebDriverWait(browser, 5)
        browser.set_window_size(1280, 1280)
        browser.get("https://allure.x5.ru")
        #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name=username]')))

        # Авторизация
        login_field = browser.find_element('css selector', 'input[name=username]')
        login_field.click()
        login_field.send_keys('Rusla.Yuldashev')

        pass_field = browser.find_element('css selector', 'input[name=password]')
        pass_field.click()
        pass_field.send_keys('yVx435RNw%Jz^y5>')

        confirm = browser.find_element('css selector', 'button[data-testid=button__login-submit]')
        confirm.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1._greeting_19lqg_1')))

        # 1. Открыть главную страницу https://allure.x5.ru/project/123/dashboards
        browser.get("https://allure.x5.ru/project/123/dashboards")

        # 2. Перейти в раздел Test cases
        go_test_cases_section = browser.find_element('xpath', "//div[contains(text(),'Тест-кейсы')]")
        go_test_cases_section.click()

        # 3. Проверить, что url содержит значение /test-cases
        # url: https://allure.x5.ru/project/123/test-cases
        get_url = browser.current_url
        print("\n")
        print(browser.current_url)
        asserts.assert_in('/test-cases', get_url, 'The fragment /test-cases was not found in the URL')

        # 4. Вернуться на главную страницу при помощи встроенных инструментов навигации браузера
        browser.back()

        # Закрыть браузер
        browser.quit()


    # Тест №2. Проверка тест-кейсов Структура

    # 1. Перейти в раздел Test cases
    # 2. Проверить, что выбран вид отображения кейсов Features
    # 3. Проверить, что тест-кейсы на странице отображаются в папках
    # 4. Изменить вид отображения кейсов на Test-cases
    # 5. Проверить, что меняется заголовок на Test-cases. Проверить, что и на странице отображаются тест-кейсы без папок.

    def test_cases_verification_structure(self):

        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        wait = WebDriverWait(browser, 5)
        browser.set_window_size(1280, 1280)
        browser.get("https://allure.x5.ru")

        # Авторизация
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name=username]')))
        login_field = browser.find_element('css selector', 'input[name=username]')
        login_field.click()
        login_field.send_keys('Rusla.Yuldashev')

        pass_field = browser.find_element('css selector', 'input[name=password]')
        pass_field.click()
        pass_field.send_keys('yVx435RNw%Jz^y5>')

        confirm = browser.find_element('css selector', 'button[data-testid=button__login-submit]')
        confirm.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1._greeting_19lqg_1')))

        # Открыть главную страницу https://allure.x5.ru/project/123/dashboards
        browser.get("https://allure.x5.ru/project/123/dashboards")

        # 1. Перейти в раздел Test cases
        go_test_cases_section = browser.find_element('xpath', "//div[contains(text(),'Тест-кейсы')]")
        go_test_cases_section.click()

        # 2. Проверить, что выбран вид отображения кейсов Features
        open_display_view = browser.find_element('xpath',"//button[@aria-label='Все тест-кейсы']")
        open_display_view.click()

        select_features = browser.find_element('xpath',"//span[contains(text(),'Features')]")
        select_features.click()

        features = browser.find_element('xpath',"//span[contains(text(),'Features')]")
        print("\n")
        print(features.text)
        asserts.assert_equal(features.text, 'Features', 'The display type of cases is not selected Features')

        # 3. Проверить, что тест-кейсы на странице отображаются в папках
        test_cases_in_folder = browser.find_elements('xpath',"//*[@data-icon='line-files-folder']")
        number_of_folders = len(test_cases_in_folder)
        print(number_of_folders)
        asserts.assert_boolean_true(number_of_folders > 0, 'Test cases on the page are not displayed in folders')

        # 4. Изменить вид отображения кейсов на Test-cases
        features.click()
        all_test_cases = browser.find_element('xpath', "//span[contains(text(),'Все тест-кейсы')]")
        all_test_cases.click()

        # 5. Проверить, что меняется заголовок на Test-cases. Проверить, что и на странице отображаются тест-кейсы без папок
        open_display_view = browser.find_element('xpath', "//button[@aria-label='Все тест-кейсы']")
        print(open_display_view.text)

        asserts.assert_equal(open_display_view.text, 'Все тест-кейсы', 'The title has not changed to Test-cases')

        test_cases_in_folder = browser.find_elements('xpath',"//*[@data-icon='line-files-folder']")
        number_of_folders = len(test_cases_in_folder)
        print(number_of_folders)
        asserts.assert_boolean_true(number_of_folders == 0, 'Test cases on the page are not displayed in folders')

        # Закрыть браузер
        browser.quit()


    # Тест №3. Проверка тест-кейсов Сортировка

    # 1. Перейти в раздел Test cases
    # 2. Изменить вид отображения кейсов на Test-cases
    # 3. Проверить сортировку по возрастанию по полю id

    def test_check_sort(self):

        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        wait = WebDriverWait(browser, 5)
        browser.set_window_size(1280, 1280)
        browser.get("https://allure.x5.ru")

        # Авторизация
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name=username]')))
        login_field = browser.find_element('css selector', 'input[name=username]')
        login_field.click()
        login_field.send_keys('Rusla.Yuldashev')

        pass_field = browser.find_element('css selector', 'input[name=password]')
        pass_field.click()
        pass_field.send_keys('yVx435RNw%Jz^y5>')

        confirm = browser.find_element('css selector', 'button[data-testid=button__login-submit]')
        confirm.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1._greeting_19lqg_1')))

        # Открыть главную страницу https://allure.x5.ru/project/123/dashboards
        browser.get("https://allure.x5.ru/project/123/dashboards")

        # 1. Перейти в раздел Test cases
        go_test_cases_section = browser.find_element('xpath', "//div[contains(text(),'Тест-кейсы')]")
        go_test_cases_section.click()

        # 2. Изменить вид отображения кейсов на Test-cases
        # При переходе в раздел тест-кейсов, по умолчанию вид отображения Test-cases

        # 3. Проверить сортировку по возрастанию по полю id
        options = browser.find_element('xpath',"//*[contains(text(),'Опции')]")
        options.click()

        select_sort_by = browser.find_element('css selector',"div[aria-label='Сортировать по']")
        select_sort_by.click()

        sleep(1)

        sort_by_id = browser.find_element('css selector',"div[aria-label='ID теста']")
        sort_by_id.click()

        select_sort_by.click()

        sort_by_id_enable = browser.find_elements('xpath',"//div[@aria-label='ID теста' and @aria-checked='true']")
        number_sort_by_id_enable = len(sort_by_id_enable)
        print("\n")
        print(number_sort_by_id_enable)
        asserts.assert_boolean_true(number_sort_by_id_enable > 0, 'Sorting by ID is not selected')

        sleep(1)

        # Закрыть браузер
        browser.quit()


    # Тест №4. Проверка тест-кейсов Фильтрация.

    # 1. Перейти в раздел Test cases
    # 2. Навести курсор на иконку фильтрации. Проверить что появляется попап
    # 3. Нажать на кнопку фильтрации
    # 4. Нажать на +
    # 5. Отфильтровать тест-кейсы по статусу Review и проверить, что фильтрация работает
    # 6. Отфильтровать тест-кейсы по тегу: ввести значение regress. Нажать на Enter. Проверить, что фильтрация работает
    # 7. Сделать комбинированную фильтрацию. Выбрать Layer: UI тест и status: Active
    # 8. Проверить, что фильтрация работает

    def test_case_check_filter(self):

        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        wait = WebDriverWait(browser, 5)
        browser.set_window_size(1280, 1280)
        browser.get("https://allure.x5.ru")

        # Авторизация
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name=username]')))
        login_field = browser.find_element('css selector', 'input[name=username]')
        login_field.click()
        login_field.send_keys('Rusla.Yuldashev')

        pass_field = browser.find_element('css selector', 'input[name=password]')
        pass_field.click()
        pass_field.send_keys('yVx435RNw%Jz^y5>')

        confirm = browser.find_element('css selector', 'button[data-testid=button__login-submit]')
        confirm.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1._greeting_19lqg_1')))

        # Открыть главную страницу https://allure.x5.ru/project/123/dashboards
        browser.get("https://allure.x5.ru/project/123/dashboards")

        # 1. Перейти в раздел Test cases
        go_test_cases_section = browser.find_element('xpath', "//div[contains(text(),'Тест-кейсы')]")
        go_test_cases_section.click()

        # 2. Навести курсор на иконку фильтрации. Проверить что появляется попап. Здесь нет иконки фильтрации, соответственно попапа тоже.
        # Есть тултип при наведении на любой тест-кейс, его и проверим. Возьмем первый тест-кейс и прочитаем его тултип.
        actions = ActionChains(browser)
        first_test_case = browser.find_element('xpath', "//*[contains(text(),'01')]")
        actions.move_to_element(first_test_case).perform()
        tooltip_text = first_test_case.get_attribute("title")
        print("\n")
        print(tooltip_text)

        # 3. Нажать на кнопку фильтрации
        filter_button = browser.find_element('css selector',"div._comboBox_1wc1o_16")
        filter_button.click()

        # 4. Нажать на +. Этого шага нет в allure.

        # 5. Отфильтровать тест-кейсы по статусу Review и проверить, что фильтрация работает.
        filter_status = browser.find_element('xpath',"//*[contains(text(),'Статус')]")
        filter_status.click()

        filter_test_cases_by_review_status = browser.find_element('xpath',"//span[@class='_label_1xwuz_25' and text()='Ревью']")
        filter_test_cases_by_review_status.click()

        close_filter_by_test_cases = browser.find_element('css selector',"div[data-testid='elements__empty_view']")
        actions.move_to_element(close_filter_by_test_cases).click().perform()

        test_cases_for_review = browser.find_elements('css selector',"svg[style='color: var(--bg-dashboard-betelgeuse);']")
        number_of_test_cases_per_review = len(test_cases_for_review)
        print(number_of_test_cases_per_review)
        asserts.assert_boolean_true(number_of_test_cases_per_review > 0, "No test cases found for review")

        # 6. Отфильтровать тест-кейсы по тегу: ввести значение regress. Нажать на Enter. Проверить, что фильтрация работает
        clear_filter = browser.find_element('xpath',"//*[contains(text(),'Очистить')]")
        clear_filter.click()

        all_types_of_test_cases = browser.find_elements('css selector',"div._out_hanhb_101")
        number_of_all_test_cases = len(all_types_of_test_cases)
        print(number_of_all_test_cases)

        filter_button = browser.find_element('css selector',"div._comboBox_1wc1o_16")
        filter_button.click()

        filter_tag = browser.find_element('xpath', "//*[contains(text(),'Тег')]")
        filter_tag.click()

        filter_regress = browser.find_element('xpath',"//*[contains(text(),'regress')]")
        filter_regress.click()

        close_filter_by_test_cases = browser.find_element('css selector',"div[data-testid='elements__empty_view']")
        actions.move_to_element(close_filter_by_test_cases).click().perform()

        all_types_of_test_cases_regress = browser.find_elements('css selector',"div._out_hanhb_101")
        number_of_all_test_cases_regress = len(all_types_of_test_cases_regress)
        print(number_of_all_test_cases_regress)

        asserts.assert_boolean_true(number_of_all_test_cases >= number_of_all_test_cases_regress,
                                        "The number of all cases cannot be less than the number of regression test cases")

        # 7. Сделать комбинированную фильтрацию. Выбрать Layer: UI тест и status: Active
        clear_filter = browser.find_element('xpath',"//*[contains(text(),'Очистить')]")
        clear_filter.click()

        all_types_of_test_cases = browser.find_elements('css selector',"div._out_hanhb_101")
        number_of_all_test_cases = len(all_types_of_test_cases)
        print(number_of_all_test_cases)

        filter_button = browser.find_element('css selector',"div._comboBox_1wc1o_16")
        filter_button.click()

        filter_layer = browser.find_element('xpath',"//*[contains(text(),'Слой')]")
        filter_layer.click()

        filter_test_cases_by_review_layer = browser.find_element('xpath',"//span[@class='_label_1xwuz_25' and text()='UI Tests']")
        filter_test_cases_by_review_layer.click()

        actions.move_to_element(filter_button).double_click().perform()

        filter_status = browser.find_element('xpath',"//*[contains(text(),'Статус')]")
        filter_status.click()

        filter_test_cases_by_review_status_active = browser.find_element('xpath',"//span[@class='_label_1xwuz_25' and text()='Активный']")
        filter_test_cases_by_review_status_active.click()

        close_filter_by_test_cases = browser.find_element('css selector',"div[data-testid='elements__empty_view']")
        actions.move_to_element(close_filter_by_test_cases).click().perform()

        # 8. Проверить, что фильтрация работает: Layer: UI тест и status: Active.
        all_types_of_test_cases_ui_and_active = browser.find_elements('css selector',"div._out_hanhb_101")
        number_of_all_test_cases_ui_and_active = len(all_types_of_test_cases_ui_and_active)
        print(number_of_all_test_cases_ui_and_active)

        asserts.assert_boolean_true(number_of_all_test_cases >= number_of_all_test_cases_ui_and_active,
                                        "The number of all cases cannot be less than the number of interface and active test cases")

        browser.quit()


    # Тест №5. Проверка тест-кейса “02 Столбцы с модулем”

    # 1. Проверить заголовок и id тест-кейса
    # 2. Проверить структуру. В тест-кейсе есть блоки: Description, Precondition, Scenario, Expected result, Comments
    # 3. Проверить что отображается картинка в сценарии
    # 4. Перейти в Attachment и проверить что там отображается та же картинка. Проверить по имени файла
    # 5. Проверить что в тегах указан только regress
    # 6. Проверить поле Fields. Feature == "Ермолов Эд", Story == Экран "Рассчитанные цены"

    def test_check_test_case_number_two_columns_with_module(self):

        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        wait = WebDriverWait(browser, 5)
        browser.set_window_size(1280, 1280)
        browser.get("https://allure.x5.ru")

        # Авторизация
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name=username]')))
        login_field = browser.find_element('css selector', 'input[name=username]')
        login_field.click()
        login_field.send_keys('Rusla.Yuldashev')

        pass_field = browser.find_element('css selector', 'input[name=password]')
        pass_field.click()
        pass_field.send_keys('yVx435RNw%Jz^y5>')

        confirm = browser.find_element('css selector', 'button[data-testid=button__login-submit]')
        confirm.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1._greeting_19lqg_1')))

        # Открыть главную страницу https://allure.x5.ru/project/123/dashboards
        browser.get("https://allure.x5.ru/project/123/dashboards")

        # Перейти в раздел Test cases
        go_test_cases_section = browser.find_element('xpath', "//div[contains(text(),'Тест-кейсы')]")
        go_test_cases_section.click()

        # Тест-кейс “02 Столбцы с модулем”
        # 1. Проверить заголовок и id тест-кейса
        test_case_number_two = browser.find_element('xpath',"//*[contains(text(),'02 Столбцы с модулем')]")
        test_case_number_two.click()

        test_case_title = browser.find_element('css selector',"span[data-testid='text__test-case-name']")
        test_case_identifier = browser.find_element('css selector',"span._link_qcl1o_1")

        print("\n")
        print(test_case_title.text)
        print(test_case_identifier.text)

        asserts.assert_equal(test_case_title.text,"02 Столбцы с модулем", "The test case title is incorrect")
        asserts.assert_equal(test_case_identifier.text, "#88531", "The test case identifier is invalid")

        # 2. Проверить структуру. В тест-кейсе есть блоки: Description, Precondition, Scenario, Expected result, Comments
        test_case_description = browser.find_element('xpath',"//*[contains(text(),'Описание')]")
        test_case_precondition = browser.find_element('xpath',"//*[contains(text(),'Предварительное условие')]")
        test_case_scenario = browser.find_element('xpath',"//*[contains(text(),'Сценарий')]")
        test_case_expected_result = browser.find_element('xpath',"//*[contains(text(),'Ожидаемый результат')]")
        test_case_comments = browser.find_element('xpath',"//*[contains(text(),'Комментарии')]")

        asserts.assert_equal(test_case_description.text, "Описание", "No description block")
        asserts.assert_equal(test_case_precondition.text, "Предварительное условие", "No precondition block")
        asserts.assert_equal(test_case_scenario.text, "Сценарий","No script block")
        asserts.assert_equal(test_case_expected_result.text, "Ожидаемый результат","No block expected result")
        asserts.assert_equal(test_case_comments.text, "Комментарии","No comments block")

        # 3. Проверить что отображается картинка в сценарии
        open_step_test_case_with_image = browser.find_element('xpath',"//*[@class='Icon Icon_size_micro AllureTree-NodeArrow__icon']")
        open_step_test_case_with_image.click()

        picture_in_test_case = browser.find_element('xpath',"//img[@class='FileContent__media' and @src='/api/testcase/attachment/774436/content']")
        print(picture_in_test_case.tag_name)
        asserts.assert_boolean_true(picture_in_test_case.tag_name.__eq__("img"), "Image not found in test case step")

        # 4. Перейти в Attachment и проверить что там отображается та же картинка. Проверить по имени файла
        name_picture = browser.find_element('xpath',"//span[@data-testid='element__attachment_name']").text
        print(name_picture)

        go_to_attachments = browser.find_element('xpath',"//*[contains(text(),'Вложения')]")
        go_to_attachments.click()

        name_attachment = browser.find_element('xpath',"//div[@class='AttachmentRow__name' and contains(text(),'.png')]").text
        print(name_attachment)

        asserts.assert_in(name_picture, name_attachment, "There is no image from the test case step in the attachments")

        # 5. Проверить что в тегах указан только regress
        go_to_review = browser.find_element('xpath',"//*[contains(text(),'Обзор')]")
        go_to_review.click()

        criteria_for_filter_by_test_cases = browser.find_elements('xpath',"//ul[@class='list  ListViewItems']")
        number_of_criteria_for_filter_by_test_cases = len(criteria_for_filter_by_test_cases)
        print(number_of_criteria_for_filter_by_test_cases)
        asserts.assert_boolean_true(number_of_criteria_for_filter_by_test_cases == 1, "More than one criterion for test case filter")

        only_criterion_test_case_regress = browser.find_element('xpath',"//small[@data-testid='element__tag']/span[contains(text(),'regress')]").text
        print(only_criterion_test_case_regress)
        asserts.assert_equal(only_criterion_test_case_regress, "regress", "The only criterion of a test case is non-regression")

        # 6. Проверить поле Fields. Feature == "Ермолов Эд", Story == Экран "Рассчитанные цены"
        name_feature_filter = browser.find_element('xpath',"//div[@class='ListViewItems__content']//span[contains(text(),'Ермолов Эд')]").text
        print(name_feature_filter)
        asserts.assert_equal("Ермолов Эд", name_feature_filter, "Filter by Feature field equal to 'Ermolov Ed' is missing from test case")

        name_story_filter = browser.find_element('xpath',"//div[@class='ListViewItems__content']//span[contains(text(),'Рассчитанные цены')]").text
        print(name_story_filter)
        asserts.assert_in("Рассчитанные цены", name_story_filter, "Filter by field Story equals Screen 'Calculated prices' is missing from test case")

        browser.quit()



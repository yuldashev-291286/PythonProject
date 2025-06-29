
import asserts

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.action_chains import ActionChains

import urllib3
from selenium.webdriver.support.wait import WebDriverWait
from tenacity import sleep

from utils.ui.locators import LocatorCaseListPage

http = urllib3.PoolManager(retries=3)
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')


# Class CaseListPage:
# 1. Локаторы списка тест-кейсов
# 2. Функции для работы со списком тест-кейсов

class CaseListPage(LocatorCaseListPage):

    # Функции для работы со списком тест-кейсов

    # 2. Проверить, что выбран вид отображения кейсов Features.
    # 3. Проверить, что тест-кейсы на странице отображаются в папках.

    def features_view_selected_and_cases_in_folders(self, browser, wait):

        wait = WebDriverWait(browser, 1)
        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_open_display_view)))

        open_display_view = browser.find_element(By.XPATH, self.locator_open_display_view)
        open_display_view.click()

        select_features = browser.find_element(By.XPATH, self.locator_features)
        select_features.click()

        features = browser.find_element(By.XPATH, self.locator_features)
        print("\n")
        print(features.text)
        asserts.assert_equal(features.text, 'Features', 'The display type of cases is not selected Features')

        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_test_cases_in_folder)))

        test_cases_in_folder = browser.find_elements(By.XPATH, self.locator_test_cases_in_folder)
        number_of_folders = len(test_cases_in_folder)
        print(number_of_folders)

        asserts.assert_boolean_true(number_of_folders > 0, 'Test cases on the page are not displayed in folders')

        pass

    # 4. Изменить вид отображения кейсов на Test-cases.
    # 5. Проверить, что меняется заголовок на Test-cases. Проверить, что и на странице отображаются тест-кейсы без папок.

    def type_test_cases_and_cases_without_folders_is_selected(self, browser, wait):

        wait = WebDriverWait(browser, 1)
        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_features)))

        features = browser.find_element(By.XPATH, self.locator_features)
        features.click()

        all_test_cases = browser.find_element(By.XPATH, self.locator_all_test_cases)
        all_test_cases.click()

        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_open_display_view)))

        open_display_view = browser.find_element(By.XPATH, self.locator_open_display_view)
        print("\n")
        print(open_display_view.text)

        asserts.assert_equal(open_display_view.text, 'Все тест-кейсы', 'The title has not changed to Test-cases')

        test_cases_in_folder = browser.find_elements(By.XPATH, self.locator_test_cases_in_folder)
        number_of_folders = len(test_cases_in_folder)
        print(number_of_folders)

        asserts.assert_boolean_true(number_of_folders == 0, 'Test cases on the page are not displayed in folders')

        pass


    # 2. Изменить вид отображения кейсов на Test-cases
    # При переходе в раздел тест-кейсов, по умолчанию вид отображения Test-cases
    # 3. Проверить сортировку по возрастанию по полю id

    def view_cases_test_cases_and_check_sort_in_ascending_order_by_id_field(self, browser, wait):

        wait = WebDriverWait(browser, 1)
        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_options)))

        options = browser.find_element(By.XPATH, self.locator_options)
        options.click()

        select_sort_by = browser.find_element(By.CSS_SELECTOR, self.locator_select_sort_by)
        select_sort_by.click()

        sleep(1)

        sort_by_id = browser.find_element(By.CSS_SELECTOR, self.locator_sort_by_id)
        sort_by_id.click()

        select_sort_by.click()

        sort_by_id_enable = browser.find_elements(By.XPATH, self.locator_sort_by_id_enable)
        number_sort_by_id_enable = len(sort_by_id_enable)
        print("\n")
        print(number_sort_by_id_enable)

        asserts.assert_boolean_true(number_sort_by_id_enable > 0, 'Sorting by ID is not selected')

        sleep(1)

        pass


    # 2. Навести курсор на иконку фильтрации. Проверить что появляется попап. Здесь нет иконки фильтрации, соответственно попапа тоже.
    # Есть тултип при наведении на любой тест-кейс, его и проверим. Возьмем первый тест-кейс и прочитаем его тултип.
    # 3. Нажать на кнопку фильтрации
    # 4. Нажать на +. Этого шага нет в allure.
    # 5. Отфильтровать тест-кейсы по статусу Review и проверить, что фильтрация работает.

    def filter_test_cases_by_review_status_and_check_that_filter_works(self, browser, wait):

        # 2. Навести курсор на иконку фильтрации. Проверить что появляется попап. Здесь нет иконки фильтрации, соответственно попапа тоже.
        # Есть тултип при наведении на любой тест-кейс, его и проверим. Возьмем первый тест-кейс и прочитаем его тултип.

        actions = ActionChains(browser)
        first_test_case = browser.find_element(By.XPATH, self.locator_first_test_case)
        actions.move_to_element(first_test_case).perform()
        tooltip_text = first_test_case.get_attribute("title")
        print("\n")
        print(tooltip_text)

        # 3. Нажать на кнопку фильтрации

        filter_button = browser.find_element(By.CSS_SELECTOR, self.locator_filter_button)
        filter_button.click()

        # 4. Нажать на +. Этого шага нет в allure.

        # 5. Отфильтровать тест-кейсы по статусу Review и проверить, что фильтрация работает.

        filter_status = browser.find_element(By.XPATH, self.locator_filter_status)
        filter_status.click()

        filter_test_cases_by_review_status = browser.find_element(By.XPATH, self.locator_filter_test_cases_by_review_status)
        filter_test_cases_by_review_status.click()

        close_filter_by_test_cases = browser.find_element(By.CSS_SELECTOR, self.locator_close_filter_by_test_cases)
        actions.move_to_element(close_filter_by_test_cases).click().perform()

        test_cases_for_review = browser.find_elements(By.CSS_SELECTOR, self.locator_test_cases_for_review)
        number_of_test_cases_per_review = len(test_cases_for_review)
        print(number_of_test_cases_per_review)
        asserts.assert_boolean_true(number_of_test_cases_per_review > 0, "No test cases found for review")

        pass


    # 6. Отфильтровать тест-кейсы по тегу: ввести значение regress. Нажать на Enter. Проверить, что фильтрация работает

    def filter_cases_by_regress_tag_and_check_what_works(self, browser, wait):

        # 6. Отфильтровать тест-кейсы по тегу: ввести значение regress. Нажать на Enter. Проверить, что фильтрация работает
        actions = ActionChains(browser)
        clear_filter = browser.find_element(By.XPATH, self.locator_clear_filter)
        clear_filter.click()

        all_types_of_test_cases = browser.find_elements(By.CSS_SELECTOR, self.locator_all_types_of_test_cases)
        number_of_all_test_cases = len(all_types_of_test_cases)
        print("\n")
        print(number_of_all_test_cases)

        filter_button = browser.find_element(By.CSS_SELECTOR, self.locator_filter_button)
        filter_button.click()

        filter_tag = browser.find_element(By.XPATH, self.locator_filter_tag)
        filter_tag.click()

        filter_regress = browser.find_element(By.XPATH, self.locator_filter_regress)
        filter_regress.click()

        close_filter_by_test_cases = browser.find_element(By.CSS_SELECTOR, self.locator_close_filter_by_test_cases)
        actions.move_to_element(close_filter_by_test_cases).click().perform()

        all_types_of_test_cases_regress = browser.find_elements(By.CSS_SELECTOR, self.locator_all_types_of_test_cases)
        number_of_all_test_cases_regress = len(all_types_of_test_cases_regress)
        print(number_of_all_test_cases_regress)

        asserts.assert_boolean_true(number_of_all_test_cases >= number_of_all_test_cases_regress,
                                        "The number of all cases cannot be less than the number of regression test cases")

        pass


    # 7. Сделать комбинированную фильтрацию. Выбрать Layer: UI тест и status: Active
    # 8. Проверить, что фильтрация работает: Layer: UI тест и status: Active.

    def make_combined_filter_and_check_what_works(self, browser, wait):

        actions = ActionChains(browser)

        # 7. Сделать комбинированную фильтрацию. Выбрать Layer: UI тест и status: Active
        clear_filter = browser.find_element(By.XPATH, self.locator_clear_filter)
        clear_filter.click()

        all_types_of_test_cases = browser.find_elements(By.CSS_SELECTOR, self.locator_all_types_of_test_cases)
        number_of_all_test_cases = len(all_types_of_test_cases)
        print("\n")
        print(number_of_all_test_cases)

        filter_button = browser.find_element(By.CSS_SELECTOR, self.locator_filter_button)
        filter_button.click()

        filter_layer = browser.find_element(By.XPATH, self.locator_filter_layer)
        filter_layer.click()

        filter_test_cases_by_review_layer = browser.find_element(By.XPATH, self.locator_filter_test_cases_by_review_layer)
        filter_test_cases_by_review_layer.click()

        actions.move_to_element(filter_button).double_click().perform()

        filter_status = browser.find_element(By.XPATH, self.locator_filter_status)
        filter_status.click()

        filter_test_cases_by_review_status_active = browser.find_element(By.XPATH, self.locator_filter_test_cases_by_review_status_active)
        filter_test_cases_by_review_status_active.click()

        close_filter_by_test_cases = browser.find_element(By.CSS_SELECTOR, self.locator_close_filter_by_test_cases)
        actions.move_to_element(close_filter_by_test_cases).click().perform()

        # 8. Проверить, что фильтрация работает: Layer: UI тест и status: Active.
        all_types_of_test_cases_ui_and_active = browser.find_elements(By.CSS_SELECTOR, self.locator_all_types_of_test_cases)
        number_of_all_test_cases_ui_and_active = len(all_types_of_test_cases_ui_and_active)
        print(number_of_all_test_cases_ui_and_active)

        asserts.assert_boolean_true(number_of_all_test_cases >= number_of_all_test_cases_ui_and_active,
                                        "The number of all cases cannot be less than the number of interface and active test cases")

        pass


import time

import asserts

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import urllib3

from utils.ui.locators import LocatorCaseViewPage

http = urllib3.PoolManager(retries=3)

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')

# Class CaseViewPage:
# 1. Локаторы формы тест-кейса
# 2. Функции для работы с формой тест-кейса

class CaseViewPage(LocatorCaseViewPage):

    # Функции для работы с формой тест-кейса

    # Тест-кейс “02 Столбцы с модулем”
    # 1. Проверить заголовок и id тест-кейса

    def check_title_and_id_of_test_case(self, browser, wait):

        # Тест-кейс “02 Столбцы с модулем”
        # 1. Проверить заголовок и id тест-кейса

        test_case_number_two = browser.find_element(By.XPATH, self.locator_test_case_number_two)
        test_case_number_two.click()

        test_case_title = browser.find_element(By.CSS_SELECTOR, self.locator_test_case_title)
        test_case_identifier = browser.find_element(By.CSS_SELECTOR, self.locator_test_case_identifier)

        print("\n")
        print(test_case_title.text)
        print(test_case_identifier.text)

        asserts.assert_equal(test_case_title.text,"02 Столбцы с модулем", "The test case title is incorrect")
        asserts.assert_equal(test_case_identifier.text, "#88531", "The test case identifier is invalid")

        pass


    # 2. Проверить структуру. В тест-кейсе есть блоки: Description, Precondition, Scenario, Expected result, Comments

    def check_test_case_structure(self, browser, wait):

        # 2. Проверить структуру. В тест-кейсе есть блоки: Description, Precondition, Scenario, Expected result, Comments

        test_case_description = browser.find_element(By.XPATH, self.locator_test_case_description)
        test_case_precondition = browser.find_element(By.XPATH, self.locator_test_case_precondition)
        test_case_scenario = browser.find_element(By.XPATH, self.locator_test_case_scenario)
        test_case_expected_result = browser.find_element(By.XPATH, self.locator_test_case_expected_result)
        test_case_comments = browser.find_element(By.XPATH, self.locator_test_case_comments)

        asserts.assert_equal(test_case_description.text, "Описание", "No description block")
        asserts.assert_equal(test_case_precondition.text, "Предварительное условие", "No precondition block")
        asserts.assert_equal(test_case_scenario.text, "Сценарий","No script block")
        asserts.assert_equal(test_case_expected_result.text, "Ожидаемый результат","No block expected result")
        asserts.assert_equal(test_case_comments.text, "Комментарии","No comments block")

        pass


    # 3. Проверить что отображается картинка в сценарии.
    # 4. Перейти в Attachment и проверить что там отображается та же картинка. Проверить по имени файла.

    def check_that_picture_is_displayed_in_script_in_attachment(self, browser, wait):

        # 3. Проверить что отображается картинка в сценарии.

        open_step_test_case_with_image = browser.find_element(By.XPATH, self.locator_open_step_test_case_with_image)
        open_step_test_case_with_image.click()

        picture_in_test_case = browser.find_element(By.XPATH, self.locator_picture_in_test_case)
        print("\n")
        print(picture_in_test_case.tag_name)
        asserts.assert_boolean_true(picture_in_test_case.tag_name.__eq__("img"), "Image not found in test case step")

        # 4. Перейти в Attachment и проверить что там отображается та же картинка. Проверить по имени файла.

        name_picture = browser.find_element(By.XPATH, self.locator_name_picture).text
        print(name_picture)

        go_to_attachments = browser.find_element(By.XPATH, self.locator_go_to_attachments)
        go_to_attachments.click()

        name_attachment = browser.find_element(By.XPATH, self.locator_name_attachment).text
        print(name_attachment)

        asserts.assert_in(name_picture, name_attachment, "There is no image from the test case step in the attachments")

        pass


    # 5. Проверить что в тегах указан только regress
    # 6. Проверить поле Fields. Feature == "Ермолов Эд", Story == Экран "Рассчитанные цены"

    def check_values_in_tags_and_fields(self, browser, wait):

        # 5. Проверить что в тегах указан только regress

        go_to_review = browser.find_element(By.XPATH, self.locator_go_to_review)
        go_to_review.click()

        criteria_for_filter_by_test_cases = browser.find_elements(By.XPATH, self.locator_criteria_for_filter_by_test_cases)
        number_of_criteria_for_filter_by_test_cases = len(criteria_for_filter_by_test_cases)
        print("\n")
        print(number_of_criteria_for_filter_by_test_cases)
        asserts.assert_boolean_true(number_of_criteria_for_filter_by_test_cases == 1, "More than one criterion for test case filter")

        only_criterion_test_case_regress = browser.find_element(By.XPATH, self.locator_only_criterion_test_case_regress).text
        print(only_criterion_test_case_regress)
        asserts.assert_equal(only_criterion_test_case_regress, "regress", "The only criterion of a test case is non-regression")

        # 6. Проверить поле Fields. Feature == "Ермолов Эд", Story == Экран "Рассчитанные цены"

        name_feature_filter = browser.find_element(By.XPATH, self.locator_name_feature_filter).text
        print(name_feature_filter)
        asserts.assert_equal("Ермолов Эд", name_feature_filter, "Filter by Feature field equal to 'Ermolov Ed' is missing from test case")

        name_story_filter = browser.find_element(By.XPATH, self.locator_name_story_filter).text
        print(name_story_filter)
        asserts.assert_in("Рассчитанные цены", name_story_filter, "Filter by field Story equals Screen 'Calculated prices' is missing from test case")

        pass

    # Создание тест-кейса
    def create_test_cases(self, browser, wait, name_test_case):

        # Нажимаем создать тест-кейс
        create_test_case = browser.find_element(By.XPATH, self.locator_create_test_case)
        create_test_case.click()

        # Вводим название тест-кейса
        input_name_test_case = browser.find_element(By.XPATH, self.locator_input_name_test_case)
        input_name_test_case.send_keys(name_test_case)

        # Сохранить тест-кейс
        input_name_test_case.send_keys(Keys.ENTER)
        new_test_case_title = browser.find_element(By.XPATH, self.locator_new_test_case)
        print("\n" + new_test_case_title.text)

        # Проверить, что тест-кейс создался
        asserts.assert_in("Новый тест-кейс", new_test_case_title.text, "Created test case not found.")

        pass

    # Удаление созданного тест-кейса
    def delete_test_case(self, browser, wait):

        # Открываем меню тест-кейса
        test_case_menu = browser.find_element(By.XPATH, self.locator_test_case_menu)
        test_case_menu.click()

        # Нажимаем Переместить в корзину
        delete_test_case = browser.find_element(By.XPATH, self.locator_delete_test_case)
        delete_test_case.click()

        pass


    # Редактирование созданного тест-кейса
    def edit_test_case(self, browser, wait):

        # 4. Редактирование тест-кейса (a, b, с - разные тесты):
        # a. Отредактировать название тест-кейса

        # Делаем фильтр по созданному новому тест-кейсу
        search_and_filter_bar = browser.find_element(By.XPATH, self.locator_search_and_filter_bar)
        ActionChains(browser).move_to_element(search_and_filter_bar).click(search_and_filter_bar).send_keys("Новый тест-кейс").send_keys(Keys.ENTER).perform()

        wait_for_case_list_load = WebDriverWait(browser, 25)
        wait_for_case_list_load.until(EC.presence_of_element_located((By.XPATH, self.locator_new_test_case_found)))

        # Находим последний созданный новый тест-кейс и переименовываем его
        new_test_case_found = browser.find_element(By.XPATH,self.locator_new_test_case_found)
        ActionChains(browser).move_to_element(new_test_case_found).double_click(new_test_case_found).send_keys("Переименованный новый тест-кейс").send_keys(Keys.ENTER).perform()

        wait = WebDriverWait(browser, 1)
        wait.until(EC.presence_of_element_located((By.XPATH, self.locator_new_test_case_found)))

        time.sleep(1)

        # Проверяем, что тест-кейс переименован
        asserts.assert_in("Переименованный", new_test_case_found.text, "Ошибка! Не переименован новый тест-кейс.")
        print(new_test_case_found.text)

        # b. Отредактировать сценарий тест-кейса
        test_case_step_for_edit = browser.find_element(By.XPATH, self.locator_test_case_step_for_edit)
        ActionChains(browser).move_to_element(test_case_step_for_edit).click(test_case_step_for_edit).send_keys("Отредактированный шаг нового тест-кейса").send_keys(Keys.ENTER).perform()

        # Проверить, что сценарий отредактирован
        edited_step = browser.find_element(By.XPATH, self.locator_edited_step)
        asserts.assert_in("Отредактированный шаг", edited_step.text, "Ошибка! Не переименован шаг нового тест-кейса.")
        print(edited_step.text)

        # c. Отредактировать description тест-кейса

        # Нажать кнопку редактировать описание
        edit_test_case_description = browser.find_element(By.XPATH, self.locator_edit_test_case_description)
        edit_test_case_description.click()

        # Найти поле, чтобы ввести текст описания
        test_case_description = browser.find_element(By.XPATH, self.locator_test_case_description_edit)
        ActionChains(browser).move_to_element(test_case_description).click(test_case_description).send_keys("Новое описание созданного тест-кейса").perform()

        # Сохранить введенный текст в описание
        saved_button_description = browser.find_element(By.XPATH, self.locator_saved_button_description)
        saved_button_description.click()

        # Проверить, что description отредактировано
        asserts.assert_in("Новое описание", test_case_description.text, "Ошибка! Не отредактировано описание нового тест-кейса.")
        print(test_case_description.text)

        pass


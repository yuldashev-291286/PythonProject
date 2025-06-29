
class LocatorMainPage:

    # Локаторы страницы авторизации и главной страницы
    locator_login_field = 'input[name=username]'
    locator_pass_field = 'input[name=password]'
    locator_confirm = 'button[data-testid=button__login-submit]'
    locator_main_menu_of_page = 'h1._greeting_19lqg_1'
    locator_test_cases_section = "//div[contains(text(),'Тест-кейсы')]"

    # Локаторы создание suite и тест-кейсов
    locator_create_suite_and_test_cases = "//div[@class='_toolbar_3eh6g_1 _size-m_3eh6g_10']"

    # Локаторы страницы Запуски
    locator_open_launch_page = "//h2[@class='_heading_ns9g6_40' and text()='Запуски']"


class LocatorLaunchesPage:

    # Локаторы страницы создания тест-кейсов
    locator_search_and_filter_bar = "//div[@class='_comboBox_1wc1o_16']"
    locator_new_test_case_found = "//div[@class='_tree_14p85_8']//div[@class='test-tree-row'][last()]"
    locator_select_test_case_first = "//div[@class='_iconWrapper_1a6ad_42']/ancestor::*[2]/label[@aria-label='Выбрать Новый тест-кейс для проверки ланча №1']"
    locator_select_test_case_second = "//div[@class='_iconWrapper_1a6ad_42']/ancestor::*[2]/label[@aria-label='Выбрать Новый тест-кейс для проверки ланча №2']"
    locator_run_selected_test_case = "//button[@data-testid='button__create-run' and @aria-label='Запустить']"
    locator_lunch_name = "//input[@class='InputBox__box InputBox__box_base']"
    locator_drop_down_list_of_tags = "//div[@class='SelectBox ']"
    locator_input_name_tag = "//input[@class='InputBox__box InputBox__box_small']"
    locator_select_name_tag = "//span[@class='SelectBoxOptionsList__item-label' and text()='new_project']"
    locator_submit = "//button[@aria-label='Отправить']"
    locator_notification_run = "//div[@class='Notification']"
    locator_run = "//div[text()='Создан']/a[contains(text(),'Запуск от')]"

    # Локаторы страницы запуска тест-кейсов
    locator_run_test_cases = "//a[@class='_name_s0uet_21' and contains(text(),'Тестовый запуск, Юлдашев Р.А.')]"
    locator_selected_launch_page = "//h2[@class='_heading_ns9g6_40']//div[@class='_content_7zz50_6' and contains(text(),'Тестовый запуск, Юлдашев Р.А.')]"
    locator_success_rate = "text._centeredMetricTitle_1qii2_41"
    locator_test_cases_this_lunch = "//span[@class='Tabs__text' and text()='Результаты тестов']"
    locator_test_cases_lunch_one = "//span[@class='_typography-paragraphs-text-m_skegg_28 _name_1nirb_12' and @title='Новый тест-кейс для проверки ланча №1']"
    locator_failed = "//span[@class='_text_1mh1e_790' and text()='Неуспешный']"
    locator_confirm_failed = "//span[@class='_text_1mh1e_790' and text()='Отправить']"
    locator_failed_test_case = "//span[@class='_text_j9tew_11 _typography-ui-text-s-ui-bold_skegg_72' and text()='Неуспешный']"
    locator_test_cases_lunch_two = "//span[@class='_typography-paragraphs-text-m_skegg_28 _name_1nirb_12' and @title='Новый тест-кейс для проверки ланча №2']"
    locator_success = "//span[@class='_text_1mh1e_790' and text()='Успешный']"
    locator_success_test_case = "//span[@class='_text_j9tew_11 _typography-ui-text-s-ui-bold_skegg_72' and text()='Успешный']"
    locator_overview_lunch = "//span[@class='Tabs__text' and text()='Обзор']"
    locator_overview = "//div[@class='_pieContainer_1qii2_9 _hasLink_1qii2_22']"
    locator_success_rate_after = "text._centeredMetricTitle_1qii2_41"
    locator_close_lunch = "//button[@aria-label='Завершить']"
    locator_notification_closed_launch = "//div[@class='Notification']"
    locator_notification_launch_completed = "//h5[@class='Notification__title' and text()='Запуск завершен']"


class LocatorCaseViewPage:

    # Локаторы формы тест-кейса
    locator_test_case_number_two = "//*[contains(text(),'02 Столбцы с модулем')]"
    locator_test_case_title = "span[data-testid='text__test-case-name']"
    locator_test_case_identifier = "span._link_qcl1o_1"
    locator_test_case_description = "//*[contains(text(),'Описание')]"
    locator_test_case_precondition = "//*[contains(text(),'Предварительное условие')]"
    locator_test_case_scenario = "//*[contains(text(),'Сценарий')]"
    locator_test_case_expected_result = "//*[contains(text(),'Ожидаемый результат')]"
    locator_test_case_comments = "//*[contains(text(),'Комментарии')]"
    locator_open_step_test_case_with_image = "//*[@class='Icon Icon_size_micro AllureTree-NodeArrow__icon']"
    locator_picture_in_test_case = "//img[@class='FileContent__media' and @src='/api/testcase/attachment/774436/content']"
    locator_name_picture = "//span[@data-testid='element__attachment_name']"
    locator_name_attachment = "//div[@class='AttachmentRow__name' and contains(text(),'.png')]"
    locator_go_to_attachments = "//*[contains(text(),'Вложения')]"
    locator_go_to_review = "//*[contains(text(),'Обзор')]"
    locator_criteria_for_filter_by_test_cases = "//ul[@class='list  ListViewItems']"
    locator_only_criterion_test_case_regress = "//small[@data-testid='element__tag']/span[contains(text(),'regress')]"
    locator_name_feature_filter = "//div[@class='ListViewItems__content']//span[contains(text(),'Ермолов Эд')]"
    locator_name_story_filter = "//div[@class='ListViewItems__content']//span[contains(text(),'Рассчитанные цены')]"

    # Создание и удаление тест-кейса
    locator_create_test_case = "//span[@class='_text_1mh1e_790' and contains(text(),'Тест-кейс')]"
    locator_input_name_test_case = "//input[@class='_input_ux7g5_1']"
    locator_new_test_case = "//span[@data-testid='text__test-case-name' and contains(text(),'Новый тест-кейс')]"
    locator_test_case_menu = "//button[@aria-label='Меню тест-кейса']"
    locator_delete_test_case = "//span[@class='_label_1xwuz_25' and contains(text(),'Переместить в Корзину')]"

    # Поиск тест-кейса
    locator_test_case_search_field = "//div[@class='_comboBox_1wc1o_16']"

    # Локаторы для редактирования тест-кейса
    locator_search_and_filter_bar = "//div[@class='_comboBox_1wc1o_16']"
    locator_new_test_case_found = "//div[@class='_tree_14p85_8']//div[@class='test-tree-row'][last()]"
    locator_test_case_step_for_edit = "//div[@class='AllureTree-NodeContent__content']//div[@class='tiptap ProseMirror']"
    locator_edited_step = "//ul[@class='AllureTreeNodeList__list']//li[1]"
    locator_edit_test_case_description = "//*[contains(text(),'Описание')]/ancestor::*[1]//button[@data-testid='button__edit_section']"
    locator_test_case_description_edit = "//textarea[@placeholder='Введите описание']"
    locator_saved_button_description = "//button[@data-testid='markdown-editor-save-button']//span[@class='_text_1mh1e_790' and contains(text(),'Сохранить')]"


class LocatorCaseListPage:

    # Локаторы списка тест-кейсов
    locator_open_display_view = "//button[@aria-label='Все тест-кейсы']"
    locator_features = "//span[contains(text(),'Features')]"
    locator_test_cases_in_folder = "//*[@data-icon='line-files-folder']"
    locator_all_test_cases = "//span[contains(text(),'Все тест-кейсы')]"
    locator_options = "//*[contains(text(),'Опции')]"
    locator_select_sort_by = "div[aria-label='Сортировать по']"
    locator_sort_by_id = "div[aria-label='ID теста']"
    locator_sort_by_id_enable = "//div[@aria-label='ID теста' and @aria-checked='true']"
    locator_first_test_case = "//*[contains(text(),'01')]"
    locator_filter_button = "div._comboBox_1wc1o_16"
    locator_filter_status = "//*[contains(text(),'Статус')]"
    locator_filter_test_cases_by_review_status = "//span[@class='_label_1xwuz_25' and text()='Ревью']"
    locator_close_filter_by_test_cases = "div[data-testid='elements__empty_view']"
    locator_test_cases_for_review = "svg[style='color: var(--bg-dashboard-betelgeuse);']"
    locator_clear_filter = "//*[contains(text(),'Очистить')]"
    locator_all_types_of_test_cases = "div._out_hanhb_101"
    locator_filter_tag = "//*[contains(text(),'Тег')]"
    locator_filter_regress = "//*[contains(text(),'regress')]"
    locator_all_types_of_test_cases_regress = "div._out_hanhb_101"
    locator_filter_layer = "//*[contains(text(),'Слой')]"
    locator_filter_test_cases_by_review_layer = "//span[@class='_label_1xwuz_25' and text()='UI Tests']"
    locator_filter_test_cases_by_review_status_active = "//span[@class='_label_1xwuz_25' and text()='Активный']"
    locator_all_types_of_test_cases_ui_and_active = "div._out_hanhb_101"





class NavigationHelper:

    # Страница Allure
    @staticmethod
    def page_allure(browser):
        browser.get("https://allure.x5.ru")

        pass

    # Главная страница
    @staticmethod
    def page_main(browser):
        browser.get("https://allure.x5.ru/project/123/dashboards")

        pass

    # Страница создания suite и тест-кейсов
    @staticmethod
    def page_create_suite_and_test_cases(browser):
        browser.get("https://allure.x5.ru/project/45/test-cases/?treeId=0")

        pass

    # Страницу запусков
    @staticmethod
    def page_launch(browser):
        browser.get("https://allure.x5.ru/project/45/launches")

        pass

    # Обновить страницу
    @staticmethod
    def page_refresh(browser):
        browser.refresh()

        pass

    # Проверить текущий url
    @staticmethod
    def url_check(browser, url):
        return url.get_url == browser.current_url

    # Вернуться на главную страницу
    @staticmethod
    def page_return_main(browser):
        browser.back()

        pass

    # Закрыть браузер
    @staticmethod
    def browser_close(browser):
        browser.quit()

        pass


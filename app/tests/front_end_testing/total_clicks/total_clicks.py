from app.tests.utilities import selenium_utility


class TotalClicks(selenium_utility.SeleniumUtility):
    _url_input_locator = '//p[@id="total-p"]'

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def get_total_paragraph_text(self):
        return self.get_element(self._url_input_locator).text

from app.tests.utilities import selenium_utility
import pyperclip as pc


class Result(selenium_utility.SeleniumUtility):
    _url_input_locator = '//input[@id="copy-able"]'
    _copy_button_locator = '//button[@id="copy-btn"]'
    _total_clicks_url = '//a[@id="total-clicks-link"]'

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

        self.url_input = self.get_element(self._url_input_locator)
        self.copy_button = self.get_element(self._copy_button_locator)

    def get_input_text(self):
        return self.get_element(self._url_input_locator).get_attribute('value')

    def click_copy_button(self):
        self.copy_button.click()

    def go_to_total_clicks(self):
        self.get_element(self._total_clicks_url).click()

    @staticmethod
    def get_clipboard_content():
        text = pc.paste()
        return text

from app.tests.utilities import selenium_utility


class Index(selenium_utility.SeleniumUtility):
    _heading_locator = '//p[@id="heading-p"]'
    _url_input_locator = '//input[@id="url-input"]'
    _shorten_button_locator = '//button[@type="submit"]'
    _enter_url_warning = '//div[@class="alert-box alert-warning"]'
    _try_again_button = '//button[@id="try-again-btn"]'

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.url_input = self.get_element(self._url_input_locator)
        self.shorten_button = self.get_element(self._shorten_button_locator)

    def get_heading_text(self):
        return self.get_element(self._heading_locator).text

    def enter_valid_url(self):
        self.url_input = self.get_element(self._url_input_locator)
        self.url_input.click()
        self.url_input.send_keys('youtube.com')

    def enter_invalid_url(self):
        self.url_input.click()
        self.url_input.send_keys('https://www.youtube.com/what?a=b&c=d')

    def click_shorten_button(self):
        self.shorten_button = self.get_element(self._shorten_button_locator)
        self.shorten_button.click()

    def check_warning_present(self):
        return self.get_element(self._enter_url_warning).is_displayed()

    def get_current_url(self):
        return self.driver.current_url.split('/')[-1]

    def click_try_again(self):
        self.wait_for_element(self._try_again_button).click()

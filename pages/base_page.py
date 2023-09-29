class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def get_element_text(self, how, what):
        return self.browser.find_element(how, what).text

    def fill_input(self, how, what, input_value):
        input_field = self.browser.find_element(how, what)
        input_field.send_keys(input_value)

    def should_be_visible(self, how, what):
        element = self.browser.find_element(how, what)
        assert element.is_displayed(), f"Element {what} is not displayed"

    def should_not_be_visible(self, how, what):
        element = self.browser.find_element(how, what)
        assert not element.is_displayed(), f"Element {what} is displayed"

    def text_should_be_equal_to(self, how, what, expected_text):
        actual_text = self.get_element_text(how, what)
        assert actual_text == expected_text, f"Actual text'{actual_text}' is not equal to expected text {expected_text}"

    def press_button(self, how, what):
        button = self.browser.find_element(how, what)
        button.click()

    def url_should_be_equal_to(self, what):
        assert self.browser.current_url == what, f"Actual URL'{self.browser.current_url}' is not equal to expected URL {what}"

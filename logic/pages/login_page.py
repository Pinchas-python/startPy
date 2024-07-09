from infra.page_base import PageBase


class LogInPage(PageBase):

    button_text = "Login"
    error_message_selector = "Enter a valid email address"
    error_message_selector_pass = "Password cannot be empty"
    text_input = "//input[@id=':r1:']"
    text_input_pass = "//input[@id=':r2:']"

    def __init__(self, page):
        super().__init__(page)

    def click_log_in(self):
        self.pw_page.locator(f"text={self.button_text}").click()

    def get_text(self):
        error_message = self.pw_page.locator(f"text={self.error_message_selector}").text_content()
        return error_message

    def get_text_pass(self):
        error_message = self.pw_page.locator(f"text={self.error_message_selector_pass}").text_content()
        return error_message

    def inser_email(self):
        self.pw_page.locator(self.text_input).fill("pinimari1@gmail.com")

    def inser_pass(self):
        self.pw_page.locator(self.text_input_pass).fill("pass")
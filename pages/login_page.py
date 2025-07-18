# pages/login_page.py

from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('#username')
        self.password_input = page.locator('#password')
        self.login_button = page.locator('button[type="submit"]')
        self.flash_message = page.locator('#flash')

    def navigate(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_flash_text(self):
        return self.flash_message.text_content()

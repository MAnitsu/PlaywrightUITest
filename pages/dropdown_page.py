# pages/dropdown_page.py

from playwright.sync_api import Page

class DropdownPage:
    def __init__(self, page: Page):
        self.page = page
        self.dropdown = page.locator("#dropdown")

    def navigate(self):
        self.page.goto("https://the-internet.herokuapp.com/dropdown")

    def select_option(self, option: str):
        self.dropdown.select_option(option)

    def check_option(self, option: str) -> bool:
        return self.dropdown.input_value() == option
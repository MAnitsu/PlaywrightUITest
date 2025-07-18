# pages/checkbox_page.py

from playwright.sync_api import Page

class CheckboxPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkboxes = page.locator("form#checkboxes input[type='checkbox']")

    def navigate(self):
        self.page.goto("https://the-internet.herokuapp.com/checkboxes")

    def check(self, index: int):
        box = self.checkboxes.nth(index)
        if not box.is_checked():
            box.check()
    
    def uncheck(self, index: int):
        box = self.checkboxes.nth(index)
        if box.is_checked():
            box.uncheck()

    def is_checked(self, index: int) -> bool:
        return self.checkboxes.nth(index).is_checked()
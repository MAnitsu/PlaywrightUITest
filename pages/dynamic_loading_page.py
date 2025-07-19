# page/dynamic_loading_page.py

from playwright.sync_api import Page

class DynamicLoadingPage:
    def __init__(self, page: Page):
        self.page = page
        self.start_button = page.locator("#start button")
        self.finish_locator = page.locator("#finish")
        
    def navigate(self):
        self.page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

    def click_start(self):
        self.start_button.click()

    def wait_loading(self, miliseconds):
        self.finish_locator.wait_for(timeout = miliseconds)

    def check_message(self, expected_message: str) -> bool:
        return self.finish_locator.inner_text() == expected_message

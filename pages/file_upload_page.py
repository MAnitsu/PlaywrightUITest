# pages/file_upload_page.py

from playwright.sync_api import Page

class FileUploadPage:
    def __init__(self, page: Page):
        self.page = page
        self.dropdown = page.locator("#dropdown")
        self.choose_file_button = page.locator("#file-upload")
        self.upload_button = page.locator("#file-submit")
        self.uploaded_text = page.locator("#uploaded-files")

    def navigate(self):
        self.page.goto("https://the-internet.herokuapp.com/upload")

    def upload_file(self, filename: str):
        self.choose_file_button.set_input_files(filename)
        self.upload_button.click()

    def check_file_name(self, filename: str) -> bool:
        return self.uploaded_text.inner_text() == filename

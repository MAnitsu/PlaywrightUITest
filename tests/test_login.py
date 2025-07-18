# tests/test_login.py

from pages.login_page import LoginPage

def test_login_valid(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login_page.get_flash_text()

def test_login_invalid(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("wronguser", "wrongpass")
    assert "Your username is invalid!" in login_page.get_flash_text()

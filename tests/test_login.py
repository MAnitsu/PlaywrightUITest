# tests/test_login.py

def test_login_success(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    assert page.locator("div.flash.success").is_visible()
    assert "You logged into a secure area!" in page.locator("div.flash.success").inner_text()

def test_login_failure(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "wronguser")
    page.fill("#password", "wrongpass")
    page.click("button[type='submit']")

    assert page.locator("div.flash.error").is_visible()
    assert "Your username is invalid!" in page.locator("div.flash.error").inner_text()

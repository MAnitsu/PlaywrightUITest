# tests/test_dynamic_loading.py

def test_dynamic_loading(page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    page.click("button")
    page.wait_for_selector("#finish", timeout=5000)
    assert page.locator("#finish").inner_text() == "Hello World!"

# tests/test_dropdown.py

def test_dropdown(page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    dropdown = page.locator("#dropdown")
    dropdown.select_option("2")
    selected = dropdown.input_value()
    assert selected == "2"

# tests/test_checkboxes.py

def test_checkboxes(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = page.locator("input[type='checkbox']")
    
    # Check first checkbox if not checked
    if not checkboxes.nth(0).is_checked():
        checkboxes.nth(0).check()
    assert checkboxes.nth(0).is_checked()
    
    # Uncheck second checkbox
    if checkboxes.nth(1).is_checked():
        checkboxes.nth(1).uncheck()
    assert not checkboxes.nth(1).is_checked()

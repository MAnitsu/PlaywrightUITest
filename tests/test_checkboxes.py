# tests/test_checkboxes.py

from pages.checkbox_page import CheckboxPage


def test_checkboxes(page):
    checkbox_page = CheckboxPage(page)
    checkbox_page.navigate()
    
    # Ensure checkbox 0 is checked
    checkbox_page.check(0)
    assert checkbox_page.is_checked(0) is True

    # Ensure checkbox 2 is not checked
    checkbox_page.uncheck(1)
    assert checkbox_page.is_checked(1) is False

# tests/test_dropdown.py

from pages.dropdown_page import DropdownPage


def test_dropdown(page):
    dropdown_page = DropdownPage(page)
    dropdown_page.navigate()

    # Select option from dropdown
    dropdown_page.select_option("2")

    # Ensure option is correct
    assert dropdown_page.check_option("2") is True
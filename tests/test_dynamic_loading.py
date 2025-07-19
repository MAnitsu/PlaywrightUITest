# tests/test_dynamic_loading.py

from pages.dynamic_loading_page import DynamicLoadingPage


def test_dynamic_loading(page):
    dynamic_loading_page = DynamicLoadingPage(page)
    dynamic_loading_page.navigate()

    # Click the start button
    dynamic_loading_page.click_start()

    # Wait 6 seconds for selector
    dynamic_loading_page.wait_loading(6000)

    # Ensure final message is correct
    assert dynamic_loading_page.check_message("Hello World!") is True
# tests/test_file_upload.py

def test_file_upload(page):
    page.goto("https://the-internet.herokuapp.com/upload")
    page.set_input_files("#file-upload", "textfile.txt")
    page.click("#file-submit")
    
    uploaded_text = page.locator("#uploaded-files").inner_text()
    assert uploaded_text == "textfile.txt"

# tests/test_file_upload.py

from pages.file_upload_page import FileUploadPage


def test_file_upload(page):
    file_upload_page = FileUploadPage(page)
    file_upload_page.navigate()

    # upload the file named "textfile.txt"
    file_upload_page.upload_file("textfile.txt")

    # check if the correct file was updated
    assert file_upload_page.check_file_name("textfile.txt") is True
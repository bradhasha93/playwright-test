from playwright.sync_api import *


class BookPage:

    BACK_TO_BOOKSTORE_BUTTON = "//button[@id='addNewRecordButton']"
    BOOK_TITLE_TEXT = "//*[@id='title-wrapper']//*[@id='userName-value']"

    def __init__(self, page: Page):
        self.page = page

    def verify_book_data(self, book):
        expect(self.page.locator(selector=self.BOOK_TITLE_TEXT)).to_have_text(expected=book)

    def click_back_to_bookstore_button(self):
        self.page.locator(selector=self.BACK_TO_BOOKSTORE_BUTTON).click()
        self.page.wait_for_selector(selector=self.BACK_TO_BOOKSTORE_BUTTON, state="detached")


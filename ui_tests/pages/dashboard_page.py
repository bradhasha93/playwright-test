from playwright.sync_api import *


class DashboardPage:

    SEARCH_INPUT = "input#searchBox"
    BOOK_LINK = "//a[contains(., '%s')]"

    def __init__(self, page: Page):
        self.page = page

    def open_book_link(self, book):
        self.page.locator(selector=self.SEARCH_INPUT).type(text=book)
        self.page.locator(selector=self.BOOK_LINK % book).click()

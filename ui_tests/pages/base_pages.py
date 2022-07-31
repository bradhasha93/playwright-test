from playwright.sync_api import Page
from ui_tests.pages.book_page import BookPage
from ui_tests.pages.dashboard_page import DashboardPage


class BasePages:

    def __init__(self, page: Page):
        self.page = page
        self.DashboardPage = DashboardPage(page)
        self.BookPage = BookPage(page)


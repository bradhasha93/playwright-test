import pytest
from playwright.sync_api import expect


class TestBookStore:

    @pytest.mark.parametrize("book", [
        "Git Pocket Guide",
        "Learning JavaScript Design Patterns",
        "Designing Evolvable Web APIs with ASP.NET",
        "Speaking JavaScript"
    ])
    def test_open_book_link(self, bp, book):
        bp.DashboardPage.open_book_link(book)
        bp.BookPage.verify_book_data(book)
        bp.BookPage.click_back_to_bookstore_button()

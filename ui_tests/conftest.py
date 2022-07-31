import pytest

from ui_tests.pages.base_pages import BasePages


@pytest.fixture(scope="function")
def bp(page):
    page.goto("https://demoqa.com/books")
    yield BasePages(page)

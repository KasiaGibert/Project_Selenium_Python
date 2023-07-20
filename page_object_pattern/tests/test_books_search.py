import pytest
from page_object_pattern.pages.search_books import SearchBooksPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestBooksSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    def test_hotels_search(self, setup):
        self.driver.get("https://www.taniaksiazka.pl/")
        search_books_page = SearchBooksPage(self.driver)
        search_books_page.set_books("sapiens")
        search_books_page.perform_search()
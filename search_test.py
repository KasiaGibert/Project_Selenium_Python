import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.relative_locator import locate_with

# DANE TESTOWE
book = "sapiens"


class SearchTest(unittest.TestCase):
    """ Testy wyszukiwania"""

    def setUp(self):
        """Przygotowanie testu"""
        # 1. Otwarta strona główna
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.taniaksiazka.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)


    def testValidPassword(self):
        """ Prawidłowe wyszukiwanie ksiazki """
        # 1. Kliknij pole wyszukiwania i wyczysc je, jezeli nie jestr puste
        search_field = self.driver.find_element(By.ID, 'inputSearch')
        # 2. Sprawdzani, czy pole wyszukiwarki jest puste
        if search_field == "":
            print("Pole jest puste")
        else:
            print("Pole nie jest puste, wyczyszcze je")
        search_field.clear()

        # 3. Wpisz nazwe ksiazki
        search_field.send_keys('sapiens')
        sleep(3)
        # 4.  Kliknij przycisk wyszukiwania
        search_button = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        search_button.submit()
        # 5. Sprawdzam poprawność adresu URL
        URL = self.driver.current_url
        self.assertEqual("https://www.taniaksiazka.pl/Szukaj/q-sapiens", URL,"Incorrect URL")
        # 6. Pobranie nazw ksiazek z wynikow wyszukiwania
        books = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'product-main-top-info')]//h2/a")
        books_name = [book.get_attribute("textContent") for book in books]
        for name in books_name:
            print("Book name:" + name)

    def tearDown(self):
        self.driver.quit()
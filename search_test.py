import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# DANE TESTOWE
book = "sapiens"

class SearchTest(unittest.TestCase):
# Sprawdzenie funkcjonalności wyszukiwarki

    def setUp(self):
        """Przygotowanie testu"""
        # 1. Otwarta strona główna
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.taniaksiazka.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def testSearchFunction(self):
        """ Wyszukiwanie ksiazek zawierajacych okreslona fraze"""
        # 1. Kliknij w pole wyszukiwania
        search_field = self.driver.find_element(By.ID, 'inputSearch')
        # 2. Sprawdz, czy pole wyszukiwania jest puste. Jezeli nie wyczysc je
        if search_field == "":
            print("Pole jest puste")
        else:
            print("Pole nie jest puste, wyczyszcze je")
        search_field.clear()
        # 3. Wpisz w pole wyszukiwania fraze "sapiens"
        search_field.send_keys(book)
        # 4.  Kliknij przycisk wyszukiwania
        search_button = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        search_button.submit()
        # Sprawdzam poprawność adresu URL
        URL = self.driver.current_url
        self.assertEqual("https://www.taniaksiazka.pl/Szukaj/q-sapiens", URL,"Incorrect URL")
        # Pobranie nazw ksiazek z wynikow wyszukiwania
        #books = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'product-main-top-info')]//h2/a")
        books = self.driver.find_elements(By.XPATH, "//a[contains(@class, 'ecommerce-datalayer product-title ')]")
        books_name = [book.get_attribute("textContent") for book in books]
        for name in books_name:
            print("Book name:" + name)
        # Pobieranie cen ksiazek z wynikow wyszukiwania
        prices = self.driver.find_elements(By.XPATH, "//span[contains(@class, 'product-price')]")
        price_values = [price.get_attribute("textContent") for price in prices]
        for price in price_values:
            print("Price:" + price)
        # Sprawdzanie pierwszych 3 cen hoteli
        assert price_values[0] == "28,07 zł"
        assert price_values[1] == "38,93 zł"
        assert price_values[2] == "27,95 zł"

    def tearDown(self):
        self.driver.quit()
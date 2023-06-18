import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.relative_locator import locate_with

# DANE TESTOWE
email = "kasia.gibert@gmail.com"
password = "kasiagibert"
invalid_password = "kas"

class LoginTest(unittest.TestCase):
    """ Testy logowania"""

    def setUp(self):
        """Przygotowanie testu"""
        # 1. Otwarta strona główna
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.taniaksiazka.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)



        # 2. Użytkownik niezalogowany

    def testValidPassword(self):
        """ Prawidłowe hasło """
        # 1. Kliknij „Zaloguj sie”
        log_in = self.driver.find_element(By.XPATH, '//*[@id="user-box"]/div[1]/p/a/strong')
        log_in.click()
        # 2. Wpisz email
        email_input = self.driver.find_element(By.ID, 'loginEmail')
        email_input.send_keys(email)
        # 2.  Wpisz hasło
        password_input = self.driver.find_element(By.ID, 'loginPassword')
        password_input.send_keys(password)
        # 9. Kliknij zaloguj sie
        log_in_button = self.driver.find_element(By.XPATH, '//*[@id="LoginPage"]/form[1]/p/button')
        log_in_button.submit()

        # 10. Sprawdzam poprawność adresu URL
        URL = self.driver.current_url
        self.assertEqual("https://www.taniaksiazka.pl/Konto", URL,"Incorrect URL")

        sleep(2)

    def testInvalidPassword(self):
        """ Nieprawidłowe hasło """
        # 1. Kliknij „Zaloguj sie”
        log_in = self.driver.find_element(By.XPATH, '//*[@id="user-box"]/div[1]/p/a/strong')
        log_in.click()
        # 2. Wpisz email
        email_input = self.driver.find_element(By.ID, 'loginEmail')
        email_input.send_keys(email)
        # 2.  Wpisz bledne hasło
        password_input = self.driver.find_element(By.ID, 'loginPassword')
        password_input.send_keys(invalid_password)
        # 9. Kliknij zaloguj sie
        log_in_button = self.driver.find_element(By.XPATH, '//*[@id="LoginPage"]/form[1]/p/button')
        log_in_button.submit()

        # 10. Sprawdzam poprawność adresu URL
        URL = self.driver.current_url
        self.assertEqual("https://www.taniaksiazka.pl/Konto", URL, "Incorrect URL")

        sleep(2)

    def tearDown(self):
        self.driver.quit()
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# DANE TESTOWE
email = "kasia.gibert@gmail.com"
password = "kasiagibert"
invalid_password = "kas"

class LoginTest(unittest.TestCase):
#Logowanie uzytkownika

    def setUp(self):
        """ Przygotowanie testu """
        # 1. Otwarta strona główna
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.taniaksiazka.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # 2. Użytkownik niezalogowany

    def testCorrectLogin(self):
        """ Logowanie z prawidlowymi danymi """
        # 1. Kliknij przycisk „Zaloguj sie”
        log_in = self.driver.find_element(By.XPATH, '//*[@id="user-box"]/div[1]/p/a/strong')
        log_in.click()
        # 2. Wpisz prawidlowy e-mail
        email_input = self.driver.find_element(By.ID, 'loginEmail')
        email_input.send_keys(email)
        # 3.  Wpisz haslo
        password_input = self.driver.find_element(By.ID, 'loginPassword')
        password_input.send_keys(password)
        # 4. Kliknij przycisk "Zaloguj sie"
        log_in_button = self.driver.find_element(By.XPATH, '//*[@id="LoginPage"]/form[1]/p/button')
        log_in_button.submit()

        # Testy sprawdzajace poprawność adresu URL
        URL = self.driver.current_url
        self.assertEqual("https://www.taniaksiazka.pl/Konto", URL,"Incorrect URL")

    def testInvalidPassword(self):
        """ Logowaanie z nieprawidłowym hasłem """
        # 1. Kliknij przycisk „Zaloguj sie”
        log_in = self.driver.find_element(By.XPATH, '//*[@id="user-box"]/div[1]/p/a/strong')
        log_in.click()
        # 2. Wpisz email
        email_input = self.driver.find_element(By.ID, 'loginEmail')
        email_input.send_keys(email)
        # 3.  Wpisz nieprawidlowe hasło
        password_input = self.driver.find_element(By.ID, 'loginPassword')
        password_input.send_keys(invalid_password)
        # 4. Kliknij przycisk "Zaloguj sie"
        log_in_button = self.driver.find_element(By.XPATH, '//*[@id="LoginPage"]/form[1]/p/button')
        log_in_button.submit()

        # Testy sprawdzajace poprawność adresu URL
        URL = self.driver.current_url
        self.assertEqual("https://www.taniaksiazka.pl/Logowanie", URL, "Incorrect URL")

    def tearDown(self):
        self.driver.quit()

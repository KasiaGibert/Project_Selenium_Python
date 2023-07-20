import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.relative_locator import locate_with

# DANE TESTOWE
name = "Katarzyna"
last_name = "Owerko"
phone_number = "723922682"
email = "kasia.g@gmail.com"
password = "kasiagibert"
invalid_password = "kas"

class NewUserRegistration(unittest.TestCase):
# Rejestracja nowego uzytkownika

    def setUp(self):
        """Przygotowanie testu"""
        # 1. Otwarta strona główna
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.taniaksiazka.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # 2. Użytkownik niezalogowany

    def testInvalidPassword(self):
        """ Rejestracja nowego uzytkownika uzywajac niepoprawnego hasla """

        # 1. Kliknij przycisk „Zaloguj sie”
        log_in = self.driver.find_element(By.XPATH, '//*[@id="user-box"]/div[1]/p/a/strong')
        log_in.click()
        # 2. Wpisz imię
        name_input = self.driver.find_element(By.ID, 'registerFirstName')
        name_input.send_keys(name)
        # 3. Wpisz nazwisko
        last_name_input = self.driver.find_element(By.ID, 'registerLastName')
        last_name_input.send_keys(last_name)
        # 4. Wpisz numer telefonu
        phone_number_input = self.driver.find_element(By.ID, 'registerPhone')
        phone_number_input.send_keys(phone_number)
        # 5. Wpisz e-mail
        email_input = self.driver.find_element(By.ID, 'registerEmail')
        email_input.send_keys(email)
        # 6. Wpisz bledne hasło
        password_input = self.driver.find_element(By.ID, 'registerPassword')
        password_input.send_keys(invalid_password)
        # 7. Wpisz bledne hasło
        password1_input = self.driver.find_element(By.ID, 'registerPassword1')
        password1_input.send_keys(invalid_password)
        # 8. Zaznacz checkboxa
        checkbox = self.driver.find_element(By.ID, 'registerAgree')
        checkbox.click()
        # 9. Kliknij zaloz konto
        create_account_button = self.driver.find_element(By.ID, 'CreateAccountSubmit')
        create_account_button.submit()
        # Screenshot
        screenshot = self.driver.get_screenshot_as_file('screen.png')


        #Testy sprawdzajace
        # 1. Szukam wszystkich komunikatów o błędzie
        password_error = self.driver.find_elements(By.CLASS_NAME, 'error')
        # 2. Sprawdzam, czy jest jeden taki komunikat
        self.assertEqual(1, len(password_error))
        # 3. Sprawdzam poprawność treści komunikatu i jego widoczność
        self.assertEqual("Wpisz min. 4 znaki", password_error[0].text, "Komunikat o błędzie ma niepoprawną treść")

        # 4. Sprawdzam położenie tego napisu
        # a) Ponownie szukam tego elementu względem pola haslo
        password_error_locator = locate_with(By.CLASS_NAME, 'error').near({By.ID: 'registerPassword'})
        password_error_location = self.driver.find_element(password_error_locator)
        # b) Sprawdzam, czy element wyszukany na oba sposoby to w istocie ten sam element
        self.assertEqual(password_error[0].id, password_error_location.id)

    def testNoCheckbox(self):
        """ Rejestracja nowego uzytkownika w przypadku nie zaznaczenia checkboxa """

        # 1. Kliknij przycisk „Zaloguj sie”
        log_in = self.driver.find_element(By.XPATH, '//*[@id="user-box"]/div[1]/p/a/strong')
        log_in.click()
        # 2. Wpisz imię
        name_input = self.driver.find_element(By.ID, 'registerFirstName')
        name_input.send_keys(name)
        # 3. Wpisz nazwisko
        last_name_input = self.driver.find_element(By.ID, 'registerLastName')
        last_name_input.send_keys(last_name)
        # 4. Wpisz numer telefonu
        phone_number_input = self.driver.find_element(By.ID, 'registerPhone')
        phone_number_input.send_keys(phone_number)
        # 5. Wpisz e-mail
        email_input = self.driver.find_element(By.ID, 'registerEmail')
        email_input.send_keys(email)
        # 6. Wpisz hasło
        password_input = self.driver.find_element(By.ID, 'registerPassword')
        password_input.send_keys(password)
        # 7. Wpisz hasło
        password1_input = self.driver.find_element(By.ID, 'registerPassword1')
        password1_input.send_keys(password)
        # 9. Kliknij przycisk "zaloz konto"
        create_account_button = self.driver.find_element(By.ID, 'CreateAccountSubmit')
        create_account_button.submit()
        # Screenshot
        screenshot = self.driver.get_screenshot_as_file('screen1.png')

    def tearDown(self):
        self.driver.quit()

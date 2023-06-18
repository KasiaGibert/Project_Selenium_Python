import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.relative_locator import locate_with

# DANE TESTOWE
name = "Katarzyna"
last_name = "Owerko"
phone_number = "723922682"
email = "kasia.gibert@gmail.com"
password = "kasiagibert"
invalid_password = "kas"

class NewUserRegistration(unittest.TestCase):
    """ Testy rejestracji"""

    def setUp(self):
        """Przygotowanie testu"""
        # 1. Otwarta strona główna
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.taniaksiazka.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)



        # 2. Użytkownik niezalogowany

    def testInvalidPassword(self):
        """ Nieprawidłowe hasło """
        # 1. Kliknij „Załóż konto”
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
        password_input.send_keys(invalid_password)
        # 7. Wpisz błędne hasło
        password1_input = self.driver.find_element(By.ID, 'registerPassword1')
        password1_input.send_keys(invalid_password)
        # 8. Zaznacz checkboxa
        checkbox = self.driver.find_element(By.ID, 'registerAgree')
        checkbox.click()
        # 9. Kliknij zaloz konto
        create_account_button = self.driver.find_element(By.ID, 'CreateAccountSubmit')
        create_account_button.submit()
        # 10. Zrob screenshota
        screenshot = self.driver.get_screenshot_as_file('screen.png')


        ### UWAGA! SPRAWDZENIE REZULTATU! ###
        # Użytkownik otrzymuje informację „Wymagania: DUŻA litera, cyfra lub znak specjalny, minimum 8 znaków” pod haslem
        # a) Szukam wszystkich komunikatów o błędzie
        password_error = self.driver.find_elements(By.CLASS_NAME, 'error')
        # b) Sprawdzam, czy jest jeden taki komunikat
        self.assertEqual(1, len(password_error))
        # c) Sprawdzam poprawność treści komunikatu i jego widoczność
        self.assertEqual("Wpisz min. 4 znaki",
                         password_error[0].text,
                         "Komunikat o błędzie ma niepoprawną treść")

        # - Sprawdzam położenie tego napisu
        # d) Ponownie szukam tego elementu względem pola e-mail (OBOK pola imię)
        password_error_locator = locate_with(By.CLASS_NAME, 'error').near({By.ID: 'registerPassword'})
        password_error_location = self.driver.find_element(password_error_locator)
        # e) Sprawdzam, czy element wyszkukany na oba sposoby to w istocie ten sam element
        # assert email_blad.id == komunikaty_o_bledzie[0].id
        self.assertEqual(password_error[0].id, password_error_location.id)

        # Poczekaj chwilę, żebym zdążył zobaczyć co się dzieje
        sleep(3)
    def tearDown(self):
        self.driver.quit()
'''
        def testInvalidEmail(self): 

        """ Nieprawidłowy e-mail - brak znaku @ """
        # 1. Kliknij „Załóż konto”
        zaloz_konto_btn = self.driver.find_element(By.XPATH, '//li[@class="top-bar-item link-item"][6]/button')
        zaloz_konto_btn.click()
        # 2. Wpisz imię
        imie_input = self.driver.find_element(By.ID, 'firstname-register')
        imie_input.click()
        imie_input.send_keys(self.fake.first_name())
        # 3. Wpisz błędny e-mail (brak znaku @)
        email_input = self.driver.find_element(By.NAME, 'email')
        email_input.click()
        email_input.send_keys(zly_email)
        # 4. Wpisz hasło
        haslo_input = self.driver.find_element(By.ID, 'password-register')
        haslo_input.click()
        haslo_input.send_keys(haslo)

    def tearDown(self):
        self.driver.quit()

        
    

        ### UWAGA! SPRAWDZENIE REZULTATU! ###
        # Użytkownik otrzymuje informację „To nie jest adres email. Sprawdź pisownię.” pod emailem
        # a) Szukam wszystkich komunikatów o błędzie
        komunikaty_o_bledzie = self.driver.find_elements(By.XPATH, '//span[@class="error-msg"]')
        # b) Sprawdzam, czy jest jeden taki komunikat
        self.assertEqual(1, len(komunikaty_o_bledzie))
        # c) Sprawdzam poprawność treści komunikatu i jego widoczność
        self.assertEqual("To nie jest adres email. Sprawdź pisownię.", komunikaty_o_bledzie[0].text,
                         "Komunikat o błędzie ma niepoprawną treść")
        # - Sprawdzam położenie tego napisu
        # d) Ponownie szukam tego elementu względem pola e-mail (OBOK pola imię)
        email_blad_locator = locate_with(By.XPATH, '//span[@class="error-msg"]').near({By.ID: 'email-register'})
        email_blad = self.driver.find_element(email_blad_locator)
        # e) Sprawdzam, czy element wyszkukany na oba sposoby to w istocie ten sam element
        # assert email_blad.id == komunikaty_o_bledzie[0].id
        self.assertEqual(komunikaty_o_bledzie[0].id, email_blad.id)
        # Poczekaj chwilę, żebym zdążył zobaczyć co się dzieje
        # sleep(3)

'''

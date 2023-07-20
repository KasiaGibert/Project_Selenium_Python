from selenium.webdriver.common.by import By


class SearchBooksPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_field_id = 'inputSearch'
        self.search_button_xpath = '//*[@id="search-form"]/fieldset/button'

    def set_books(self, books):
        self.driver.find_element(By.ID, self.search_field_id)
        self.driver.find_element(By.ID, self.search_field_id).clear()
        self.driver.find_element(By.ID, self.search_field_id).send_keys(books)


    def perform_search(self:
        self.driver.find_element(By.XPATH, self.search_button_xpath)
        self.driver.find_element(By.XPATH, self.search_button_xpath).submit()

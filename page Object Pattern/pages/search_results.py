class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.books_name_xpath = "//a[contains(@class, 'ecommerce-datalayer product-title ')]"
        self.books_prices_xpath = "//span[contains(@class, 'product-price')]"


    def get_books_name(self):
        books = self.driver.find_elements(By.XPATH, self.books_name_xpath)
        return [book.get_attribute("textContent") for book in books]

    def get_books_prices(self):
        prices = self.driver.find_elements(By.XPATH, self.books_prices_xpath)
        return [price.get_attribute("textContent") for price in prices]

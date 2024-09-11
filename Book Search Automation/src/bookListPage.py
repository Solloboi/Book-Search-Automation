from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BookPage:
    def __init__(self, driver):
        self.driver = driver
        self.book_elements_locator = (By.XPATH, "//div[@data-component-type='s-search-result']")
        self.next_page_locator = (By.XPATH, "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")

    def get_book_elements(self):
        return self.driver.find_elements(*self.book_elements_locator)

    def open_specific_book(self, book_element):
        specific_book_locator = (By.XPATH, ".//a[@class='a-link-normal s-no-outline']")
        WebDriverWait(book_element, 10).until(EC.element_to_be_clickable(specific_book_locator)).click()
    def get_next_page(self):
        try:
            next_page = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.next_page_locator))
            return next_page
        except:
            return None
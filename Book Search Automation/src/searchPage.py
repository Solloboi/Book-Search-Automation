from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.books_section_link = (By.ID, "nav-search-dropdown-card")
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.book_option = (By.XPATH, '//option[text()="Books"]')

    def go_to_books_section(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.books_section_link)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.book_option)).click()

    def search_for_books(self, keyword):
        search_box_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.search_box))
        search_box_element.send_keys(keyword)
        search_box_element.submit()

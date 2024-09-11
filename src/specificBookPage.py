from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class SpecificBookPage:
    def __init__(self, driver):
        self.driver = driver

    def get_book_data(self, book_element):
        try:
            title = self.driver.find_element(By.ID, "productTitle").text
        except:
            title = "Unknown"
        try:
            author = self.driver.find_element(By.XPATH, "//*[@id='bylineInfo']/span/a").text
        except:
            author = "Unknown"
        try:
            price = self.extract_price()
        except:
            price = "0.00"
        try:
            rating = self.driver.find_element(By.XPATH, "//*[@id='acrPopover']/span[1]/a/span").text
        except:
            rating = "0.0"
        try:
            link = self.driver.current_url
        except:
            link = "Unknown"
        return {"title": title, "author": author, "price": price, "rating": rating, "link": link}

    def extract_price(self):
        price_classes = [
            "a-size-base a-color-price a-color-price",
            "a-size-base a-color-secondary"
        ]

        price = 0.00
        for class_name in price_classes:
            try:
                price_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f".//span[contains(@class, '{class_name}')]"))
                )
                price_text = price_element.text
                if '$' in price_text:
                    price_text = price_text.replace('$', '').strip()
                    if ' - ' in price_text:
                        low_price, high_price = map(float, price_text.split(' - '))
                        price = round((low_price + high_price) / 2, 2)
                    else:
                        price = round(float(price_text), 2)
                    break
            except:
                continue
        return price
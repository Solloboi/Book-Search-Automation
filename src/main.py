from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException

from searchPage import SearchPage
from bookListPage import BookPage
from specificBookPage import SpecificBookPage
from сsvDataCleaner import CSVDataCleaner

import csv
import time
def get_source_html(url, max_pages=None):
    service = Service('D:\\GitHub Repositories\\Book-Search-Automation\\chromedriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    search_page = SearchPage(driver)
    book_page = BookPage(driver)
    specific_book_page = SpecificBookPage(driver)
    cleaner = CSVDataCleaner()

    try:
        driver.get(url=url)
        time.sleep(3)
        search_page.go_to_books_section()
        time.sleep(2)
        search_page.search_for_books("Java")
        time.sleep(2)

        books = []
        current_page = 0

        while True:
            book_elements = book_page.get_book_elements()

            for i in range(len(book_elements)):
                try:
                    book_elements = book_page.get_book_elements()
                    book_element = book_elements[i]
                    book_page.open_specific_book(book_element)
                    book_data = specific_book_page.get_book_data(book_element)
                    books.append(book_data)

                    driver.back()
                    time.sleep(2)
                except StaleElementReferenceException:
                    print("Stale element reference, re-locating the book element.")
                    continue

            current_page += 1
            if max_pages is not None and current_page >= max_pages:
                break

            next_page = book_page.get_next_page()
            if next_page:
                next_page.click()
                time.sleep(2)
            else:
                break

        books.sort(key=lambda x: x["price"])

        with open("Archive/books.csv", mode="w", newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["title", "author", "price", "rating", "link"])
            writer.writeheader()
            writer.writerows(books)

        cleaner.clean_csv()

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()


def main():
    url = "https://www.amazon.com/"
    user_input = input("Enter the number of pages to parse (or 'all' to parse all pages): ")

    if user_input.lower() == 'all':
        max_pages = None
    else:
        try:
            max_pages = int(user_input)
            if max_pages <= 0:
                raise ValueError("The number of pages must be greater than zero.")
        except ValueError:
            print("Invalid input. Please try again.")
            return

    get_source_html(url=url, max_pages=max_pages)


if __name__ == "__main__":
    main()

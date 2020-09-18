from bs4 import BeautifulSoup

from locators.all_books_page import AllBooksPageLocator
from parsers.bookparser import BookParser


class AllBooksPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        locator = AllBooksPageLocator.BOOKS
        books = self.soup.select(locator)
        return [BookParser(each) for each in books]

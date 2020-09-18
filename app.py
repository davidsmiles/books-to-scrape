import requests

from pages.all_books_page import AllBooksPage

page_content = requests.get('http://books.toscrape.com').content
books = AllBooksPage(page_content).books

import requests

from pages.all_books_page import AllBooksPage

page_content = requests.get('http://books.toscrape.com').content
all = AllBooksPage(page_content)

for book in all.books:
    print(book)

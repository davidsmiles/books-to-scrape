from app import books


def print_five_star_books():
    best_books = filter(lambda x: x.rating == 5, books)
    for each in best_books:
        print(each)


def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for each in best_books:
        print(each)


def print_cheapest_books():
    best_books = sorted(books, key=lambda x: x.price)[:10]
    for each in best_books:
        print(each)


books_generator = (g for g in books)


def get_next_book():
    print(next(books_generator))


print('----FIVE-STAR-----')
print_five_star_books()
print()
print('--------BEST-------')
print_best_books()
print()
print('------CHEAPEST------')
print_cheapest_books()
print()


get_next_book()
get_next_book()
get_next_book()
from locators.book_locators import BookLocators


class Book:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<{self.name} with price worth of {self.price} and rated {self.rating} of 5>'

    @property
    def name(self):
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        name = item_link.attrs['title']
        return name

    @property
    def link(self):
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator)
        link = item_link.attrs['href']
        return link

    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        price = self.parent.select_one(locator)
        return price.string

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        star_rating_tags = self.parent.select_one(locator)
        classes = star_rating_tags.attrs['class']
        rating = [x for x in classes if 'star-rating' != x][0]
        return Book.RATINGS[rating]


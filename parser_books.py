import re
import logging

from Book_parser_scraping.locators_books import BookLocators


logger = logging.getLogger('scraping.parser_books')


class ParserBooks:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created...')
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name} with prise {self.price} - {self.rating} stars.'

    @property
    def name(self):
        logger.debug('Finding book name...')
        name_link = self.parent.select_one(BookLocators.NAME_LOCATOR)
        book_name = name_link.attrs['title']
        logger.debug(f'Found book name, {book_name}.')
        return book_name

    @property
    def link(self):
        logger.debug('Finding book link...')
        link = self.parent.select_one(BookLocators.LINK_LOCATOR)
        book_link = link.attrs['href']
        logger.debug(f'Found book link, {book_link}.')
        return book_link

    @property
    def price(self):
        logger.debug('Finding book price...')
        price_link = self.parent.select_one(BookLocators.PRICE_LOCATOR).string
        pattern = '£([0-9]+\.[0-9]+)'
        book_price = re.search(pattern, price_link)
        price = book_price.group(1)
        logger.debug(f'Found book price, {price}.')
        return price

    @property
    def rating(self):
        logger.debug('Finding book rate...')
        rating_link = self.parent.select_one(BookLocators.RATING_LOCATOR)
        classes = rating_link.attrs['class']
        book_rating = [rate for rate in classes if rate != 'star-rating']
        rating_number = ParserBooks.RATINGS.get(book_rating[0])
        logger.debug(f'Found book rating, {rating_number}.')
        return rating_number


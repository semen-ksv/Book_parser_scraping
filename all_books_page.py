import re
import logging
from bs4 import BeautifulSoup
from Book_parser_scraping.locators_books import BookLocators
from Book_parser_scraping.parser_books import ParserBooks


logger = logging.getLogger('scraping.all_books_page')

class AllBooksPage:
    def __init__(self, page_content):
        logger.debug('Parsing page content with Beautiful soup HTML parser.')
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using {BookLocators.BOOKS}')
        books = self.soup.select(BookLocators.BOOKS)
        return [ParserBooks(elem) for elem in books]

    @property
    def pages_counter(self):
        logger.debug('Finding all number of catalogue pages available...')
        content = self.soup.select_one(BookLocators.PAGE_COUNTER).string
        logger.info(f'Found number of catalogue pages available: ...')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages as integer" `{pages}`')
        return pages


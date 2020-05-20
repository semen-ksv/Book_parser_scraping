import requests
import logging

from Book_parser_scraping.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs_books.txt')

logger = logging.getLogger('scraping')

logger.info('Loading books list...')
# logger.warning('This will.')
# logger.debug('This is a debug message.')
# logger.critical('A critical error.')


page_content = requests.get('http://books.toscrape.com').content
page = AllBooksPage(page_content)

books = page.books


for page_num in range(1, page.pages_counter):
    url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = requests.get(url).content
    logger.debug('Creating AllBooksPage from page content.')
    page = AllBooksPage(page_content)
    books.extend(page.books)

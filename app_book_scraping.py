import requests
import logging
import asyncio
import aiohttp
import async_timeout
import time

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

loop = asyncio.get_event_loop()

books = page.books

async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(response.status)
            print(f'Func work {time.time() - page_start}')
            return await response.text()

async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_task = asyncio.gather(*tasks)
        return await grouped_task


urls = [f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
        for page_num in range(1, page.pages_counter)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'All took {time.time() - start}')

for page_content in pages:
    logger.debug('Creating AllBooksPage from page content.')
    page = AllBooksPage(page_content)
    books.extend(page.books)

import logging

from Book_parser_scraping.app_book_scraping import books

logger = logging.getLogger('scraping.menu')

USER_CHOICE = """  Enter one of the following
- 'a' to look at all books by name
- 'b' to look at best 10 books
- 'c' to look at cheapest 10 books
- 'n' to get the next available book
- 'q' to exit

Enter your choice: 
"""


def print_all_book():
    for book in books:
        print(book)


def print_best_books():
    logger.info('Printing best books...')
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in best_books:
        print(book)


def best_price_books():
    logger.info('Printing best price books...')
    best_price = sorted(books, key=lambda x: x.price)[:10]
    for book in best_price:
        print(book)


def alfabet_name_books():
    logger.info('Printing books by name...')
    best_books = sorted(books, key=lambda x: x.name)
    for book in best_books:
        print(book)


books_generator = (book for book in books)


def print_next_book():
    logger.info('Printing next books...')
    print(next(books_generator))

USER_CHOICES = {
    'a': alfabet_name_books,
    'b': print_best_books,
    'c': best_price_books,
    'n': print_next_book
}


def menu():
    logger.info('Start menu...')
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('a', 'b', 'c', 'n'):
            USER_CHOICES[user_input]()
        else:
            print('Please choose a valid command.')
        user_input = input(USER_CHOICE)
    logger.debug('Terminating program')


if __name__ == '__main__':
    menu()

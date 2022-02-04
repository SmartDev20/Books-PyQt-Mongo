# This Python file uses the following encoding: utf-8
import json
from book import Book


def load_books():
    try:
        file = open('books.dat', 'r')
        books_dict = json.loads(file.read())
        books = []
        for book in books_dict:
            book_obj = Book(book['id'], book['name'], book['desc'], book['isbn'],
                            book['page_count'], book['issued'], book['author'], book['year'])
            books.append(book_obj)
        return books
    except Exception as e:
        print(e.__dict__)
        return []


def save_books(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
    with open('books.dat', 'w') as file:
        file.write(json.dumps(json_books, indent=4))


def update_book(book):
    book = Book(book['id'], book['name'], book['desc'], book['isbn'],
                book['page_count'], book['issued'], book['author'], book['year'])
    books = load_books()
    if book is not None:
        books = list(filter(lambda bk: int(bk.id) != int(book.id), books))
        books.append(book)
        save_books(books)


def add_book(book):
    books = load_books()
    new_book = Book(book['id'], book['name'], book['desc'], book['isbn'],
                    book['page_count'], book['issued'], book['author'], book['year'])
    save_books([*books, valid_id(books, new_book)])


def valid_id(books, new_book):
    books_ids = []
    for book in books:
        books_ids.append(int(book.id))
    if not list(filter(lambda id: id == int(new_book.id), books_ids)):
        return new_book
    else:
        new_book.id = int(max(books_ids) + 1)
        return new_book


def get_issued():
    books = load_books()
    return list(filter(lambda book: book.issued == True, books))


def get_unissued():
    books = load_books()
    return list(filter(lambda book: book.issued == False, books))


def get_all():
    books = load_books()
    return list(books)


def find_book(book_id):
    books = load_books()
    for book in books:
        if int(book.id) == int(book_id):
            return book
    return None


def delete_book(book_id):
    books = load_books()
    books = list(filter(lambda bk: int(bk.id) != int(book_id), books))
    save_books(books)

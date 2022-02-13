# This Python file uses the following encoding: utf-8

from database import DataBase


class Book:
    conn = DataBase("mongodb://127.0.0.1:27017", "Library")

    def __init__(self, id, name, desc, isbn, page_count, issued, author, year):
        self.id = id
        self.name = name
        self.desc = desc
        self.isbn = isbn
        self.page_count = page_count
        self.issued = issued
        self.author = author
        self.year = year
        self.conn = DataBase("mongodb://127.0.0.1:27017", "Library")

    def to_dict(self):
        dictionary = {
            "id": self.id,
            "name": self.name,
            "desc": self.desc,
            "isbn": self.isbn,
            "page_count": self.page_count,
            "issued": self.issued,
            "author": self.author,
            "year": self.year}
        return dictionary

    def save_one_book(self):
        self.conn.insert_one('books', self.to_dict())

    @classmethod
    def get_one_book(cls, book_id):
        book = cls.conn.find_one('books', {"id": book_id})
        return cls(**book)

    @classmethod
    def get_books(cls):
        data = cls.conn.find_many('books', {})
        if data is not None:
            return [book for book in data]

    @classmethod
    def get_issued_book(cls):
        data = cls.conn.find_many('books', {"issued": True})
        if data is not None:
            return [book for book in data]

    @classmethod
    def get_unissued_book(cls):
        data = cls.conn.find_many('books', {"issued": False})
        if data is not None:
            return [book for book in data]

    def update_book(self, book_id):
        self.conn.update('books', {"id": book_id}, self.to_dict())

    @classmethod
    def delete_book(cls, book_id):
        cls.conn.delete('books', {"id": book_id})


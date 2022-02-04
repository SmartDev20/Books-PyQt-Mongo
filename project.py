# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# import UIs
from main_window import Ui_MainWindow
from add_dialog import Ui_add_dialog as add
from delete_dialog import Ui_delete_dialog as dele
from edit_dialog import Ui_edit_dialog as edit

from books import Book
import my_functions as lib

from stylesheets import main_style_sheet, dialog_style_sheet


class AddDialog(QDialog):
    def __init__(self, parent=None):
        super(AddDialog, self).__init__(parent)
        self.ui = add()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.setStyleSheet(dialog_style_sheet)


class EditDialog(QDialog):
    def __init__(self, parent=None):
        super(EditDialog, self).__init__(parent)
        self.ui = edit()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.setStyleSheet(dialog_style_sheet)


class DeleteDialog(QDialog):
    def __init__(self, parent=None):
        super(DeleteDialog, self).__init__(parent)
        self.ui = dele()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.setStyleSheet(dialog_style_sheet)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.btn_new_bok.pressed.connect(self.show_add)
        self.load_issued_table()
        self.load_all_table()
        self.load_unissued_table()
        self.btn_edit_iss.clicked.connect(lambda: self.edit_book(self.issued_table))
        self.btn_edit_uni.clicked.connect(lambda: self.edit_book(self.unissued_table))
        self.btn_ref_iss.clicked.connect(self.load_issued_table)
        self.btn_ref_uni.clicked.connect(self.load_unissued_table)
        self.btn_ref.clicked.connect(self.load_all_table)
        self.btn_delete_iss.clicked.connect(lambda: self.delete_book(self.issued_table))
        self.btn_delete_uni.clicked.connect(lambda: self.delete_book(self.unissued_table))
        self.btn_serch.clicked.connect(self.search_book)
        self.setStyleSheet(main_style_sheet)

    def save_new_book(self, ui):

        new_book = {
            "id": int(ui.id_input.text()),
            "name": ui.name_input.text(),
            "desc": ui.desc_input.text(),
            "isbn": ui.isbn_input.text(),
            "page_count": int(ui.pgs_input.text()),
            "issued": ui.yes_rdb.isChecked(),
            "author": ui.auth_input.text(),
            "year": int(ui.year_input.text())}
        for attr in new_book:
            if new_book[attr] is None or str(new_book[attr]) == '':
                return False
        lib.add_book(new_book)

    def save_to_db(self, ui):
        new_book = Book(
            # book_id,
            int(ui.id_input.text()),
            ui.name_input.text(),
            ui.desc_input.text(),
            ui.isbn_input.text(),
            int(ui.pgs_input.text()),
            ui.yes_rdb.isChecked(),
            ui.auth_input.text(),
            int(ui.year_input.text())
        )
        dict_book = new_book.to_dict()
        for attr in dict_book:
            if dict_book[attr] is None or str(dict_book[attr]) == '':
                return False
        new_book.save_one_book()

    def update_to_db(self, ui):
        new_book = Book(
            int(ui.id_input.text()),
            ui.name_input.text(),
            ui.desc_input.text(),
            ui.isbn_input.text(),
            int(ui.pgs_input.text()),
            ui.yes_rdb.isChecked(),
            ui.auth_input.text(),
            int(ui.year_input.text())
        )
        dict_book = new_book.to_dict()
        for attr in dict_book:
            if dict_book[attr] is None or str(dict_book[str(attr)]) == '':
                return False
        new_book.update_book(int(ui.id_input.text()))

    def show_add(self):
        add_flg = AddDialog()
        add_flg.ui.buttonBox.accepted.connect(
            lambda: self.save_new_book(add_flg.ui))
        add_flg.ui.buttonBox.accepted.connect(
            lambda: self.save_to_db(add_flg.ui))
        add_flg.exec()

    def load_issued_table(self):
        # books = lib.get_issued()   # from local file
        books = Book.get_issued_book()
        self.issued_table.setRowCount(len(books))
        for index, book in enumerate(books):
            # book = book.to_dict() for books from local file to be dict
            for book_index, attr in enumerate(book):
                self.issued_table.setItem(
                    index, book_index, QTableWidgetItem(str(book[str(attr)]))
                )
                self.issued_table.item(index, book_index).setFlags(
                    Qt.ItemIsSelectable | Qt.ItemIsEnabled
                )

    def load_all_table(self):
        # books = lib.get_all()     # from local file
        books = Book.get_books()  # from MongoDB
        self.all_table.setRowCount(len(books))
        for index, book in enumerate(books):
            # book = book.to_dict()   # from local file to conv. Obj to dict
            for book_index, attr in enumerate(book):
                self.all_table.setItem(
                    index, book_index, QTableWidgetItem(str(book[str(attr)]))
                )
                self.all_table.item(index, book_index).setFlags(
                    Qt.ItemIsSelectable | Qt.ItemIsEnabled
                )

    def load_unissued_table(self):
        # books = lib.get_unissued() from local file
        books = Book.get_unissued_book()
        self.unissued_table.setRowCount(len(books))
        for index, book in enumerate(books):
            # book = book.to_dict() #for books from local file to be converted to dict
            for book_index, attr in enumerate(book):
                self.unissued_table.setItem(
                    index, book_index, QTableWidgetItem(str(book[str(attr)]))
                )
                self.unissued_table.item(index, book_index).setFlags(
                    Qt.ItemIsSelectable | Qt.ItemIsEnabled
                )

    def save_exiting_book(self, ui):
        book = {
            "id": int(ui.id_input.text()),
            "name": ui.name_input.text(),
            "desc": ui.desc_input.text(),
            "isbn": ui.isbn_input.text(),
            "page_count": int(ui.pgs_input.text()),
            "issued": ui.yes_rdb.isChecked(),
            "author": ui.auth_input.text(),
            "year": int(ui.year_input.text())
        }
        lib.update_book(book)

    def edit_book(self, table):
        selected_row = table.currentRow()
        if selected_row != -1:
            book_id = int(table.item(selected_row, 0).text())
            # book = lib.find_book(book_id) #from local file
            book = Book.get_one_book(book_id)  # from MongoB
            dlg = EditDialog()
            dlg.ui.id_input.setValue(int(book.id))
            dlg.ui.name_input.setText(book.name)
            dlg.ui.desc_input.setText(book.desc)
            dlg.ui.pgs_input.setValue(book.page_count)
            dlg.ui.auth_input.setText(book.author)
            dlg.ui.year_input.setValue(book.year)
            dlg.ui.yes_rdb.setChecked(book.issued)
            dlg.ui.isbn_input.setText(book.isbn)
            dlg.ui.no_rdb.setChecked(not book.issued)

            dlg.ui.buttonBox.accepted.connect(
                lambda: self.save_exiting_book(dlg.ui))
            dlg.ui.buttonBox.accepted.connect(
                lambda: self.update_to_db(dlg.ui))
            dlg.exec()

    def delete_book(self, table):
        selected_row = table.currentRow()
        if selected_row != -1:
            book_id = int(table.item(selected_row, 0).text())
        dlg = DeleteDialog()
        dlg.ui.buttonBox.accepted.connect(lambda: lib.delete_book(book_id))
        dlg.ui.buttonBox.accepted.connect(lambda: Book.delete_book(book_id))
        dlg.exec()

    def search_book(self):
        if self.id_input.text() != "":
            if self.id_input.text().isnumeric():
                book_id = int(self.id_input.text())
                # book = lib.find_book(book_id)  # from local file
                book = Book.get_one_book(book_id)
                if book is not None:
                    self.search_table.setRowCount(1)
                    book = book.to_dict()  # from local file to conv object to dictionary
                    for book_index, attr in enumerate(book):
                        self.search_table.setItem(
                            0, book_index, QTableWidgetItem(str(book[str(attr)]))
                        )
                        self.search_table.item(0, book_index).setFlags(
                            Qt.ItemIsSelectable | Qt.ItemIsEnabled)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()

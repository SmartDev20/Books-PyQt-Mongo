# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete-dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_delete_dialog(object):
    def setupUi(self, delete_dialog):
        delete_dialog.setObjectName("delete_dialog")
        delete_dialog.resize(489, 153)
        self.buttonBox = QtWidgets.QDialogButtonBox(delete_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 100, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textBrowser = QtWidgets.QTextBrowser(delete_dialog)
        self.textBrowser.setGeometry(QtCore.QRect(30, 20, 421, 51))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(delete_dialog)
        self.buttonBox.accepted.connect(delete_dialog.accept)
        self.buttonBox.rejected.connect(delete_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(delete_dialog)

    def retranslateUi(self, delete_dialog):
        _translate = QtCore.QCoreApplication.translate
        delete_dialog.setWindowTitle(_translate("delete_dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("delete_dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#ef2929;\">Are you sure want to delete this book ?</span></p></body></html>"))

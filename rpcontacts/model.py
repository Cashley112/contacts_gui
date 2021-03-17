#This module provides a model to manage the contacts table

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class ContactsModel:
    def __init__(self):
        #create instance attribute to hold the model
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        #Create and set up model
        tableModel = QSqlTableModel()
        tableModel.setTable("contacts")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID","Name","Job","Email")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

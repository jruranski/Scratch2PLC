from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QDialog, QTextEdit
from PyQt5.QtCore import Qt, QDateTime
import json
import os
import datetime

# The new EditorDialog class
class EditorDialog(QDialog):
    def __init__(self, parent=None):
        super(EditorDialog, self).__init__(parent)
        self.setWindowTitle('SCL Code Editor')
        self.text_editor = QTextEdit(self)

        self.save_button = QPushButton('Save', self)
        self.cancel_button = QPushButton('Cancel', self)
        self.run_button = QPushButton('Run', self)
        self.run_button.setStyleSheet("background-color: yellow")

        self.save_button.clicked.connect(self.save)
        self.cancel_button.clicked.connect(self.close)
        self.run_button.clicked.connect(self.run)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_editor)
        self.layout.addWidget(self.save_button)
        self.layout.addWidget(self.cancel_button)
        self.layout.addWidget(self.run_button)
        self.setLayout(self.layout)

    def save(self):
        # Here you can implement the saving of the text.
        with open('mainCode.scl', 'w') as f:
            f.write(self.text_editor.toPlainText())
        self.close()
    def run(self):
        # Here you can implement the running of the code.
        self.save()
        

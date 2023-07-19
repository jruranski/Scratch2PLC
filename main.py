import pickle
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QPushButton, QVBoxLayout, QWidget, QDialog, QLabel, QLineEdit, QFormLayout, QHBoxLayout, QDateTimeEdit, QDialogButtonBox, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt, QDateTime
from process import ScratchConverter
from code_editor import EditorDialog

class Student:
    def __init__(self, name, link, project_name, last_run_date):
        self.name = name
        self.link = link
        self.project_name = project_name
        self.last_run_date = last_run_date

class StudentTable(QTableWidget):
    def __init__(self, *args, **kwargs):
        super(StudentTable, self).__init__(*args, **kwargs)
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(['Name', 'Link', 'Project Name', 'Last Run'])
        header = self.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

class StudentDialog(QDialog):
    def __init__(self, parent=None):
        super(StudentDialog, self).__init__(parent)

        self.name_edit = QLineEdit(self)
        self.link_edit = QLineEdit(self)
        self.project_name_edit = QLineEdit(self)
        self.last_run_edit = QDateTimeEdit(self)
        self.last_run_edit.setDateTime(QDateTime.currentDateTime())

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        layout = QFormLayout(self)
        layout.addRow('Name', self.name_edit)
        layout.addRow('Link', self.link_edit)
        layout.addRow('Project Name', self.project_name_edit)
        layout.addRow('Last Run', self.last_run_edit)
        layout.addWidget(self.button_box)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('Scratch Project Manager')
        self.resize(1000, 800)
        self.students = self.load_students()  # This will be our data source
        
        self.table = StudentTable(self)

        self.table.setStyleSheet("""
            QTableView {
                alternate-background-color: #f0f0f0;
            }
            QHeaderView::section {
                background-color: #396285;
                color: #ffffff;
                padding: 4px;
                border: 1px solid #396285;
                margin: 1px;
            }
        """)

        self.add_button = QPushButton('Add student')
        self.add_button.clicked.connect(self.add_student)

        self.edit_button = QPushButton('Edit student')
        self.edit_button.clicked.connect(self.edit_student)

        self.delete_button = QPushButton('Delete student')
        self.delete_button.clicked.connect(self.delete_student)

        self.run_button = QPushButton('Run selected')
        self.run_button.clicked.connect(self.run_selected)
        mainLayout = QVBoxLayout()
        layout = QHBoxLayout()
        mainLayout.addWidget(self.table)
        layout.addWidget(self.add_button)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.run_button)
        mainLayout.addLayout(layout)
        widget = QWidget()
        widget.setLayout(mainLayout)
        # self.window.resize(800, 600)
        self.setCentralWidget(widget)
        self.update_table()

    def save_students(self):
        with open('students.pkl', 'wb') as f:
            pickle.dump(self.students, f)

    def load_students(self):
        try:
            with open('students.pkl', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    def update_table(self):
      
        self.table.setRowCount(len(self.students))
        for i, student in enumerate(self.students):
            self.table.setItem(i, 0, QTableWidgetItem(student.name))
            self.table.setItem(i, 1, QTableWidgetItem(student.link))
            self.table.setItem(i, 2, QTableWidgetItem(student.project_name))
            self.table.setItem(i, 3, QTableWidgetItem(student.last_run_date))
        self.table.sortItems(3, Qt.AscendingOrder)

    
    def add_student(self):
        dialog = StudentDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            student = Student(
            dialog.name_edit.text(),
            dialog.link_edit.text(),
            dialog.project_name_edit.text(),
            dialog.last_run_edit.dateTime().toString(Qt.ISODate)
        )
        self.students.append(student)
        self.update_table()
        self.save_students()

    def edit_student(self):
        indexes = self.table.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            student = self.students[row]
            dialog = StudentDialog(self)
            dialog.name_edit.setText(student.name)
            dialog.link_edit.setText(student.link)
            dialog.project_name_edit.setText(student.project_name)
            dialog.last_run_edit.setDateTime(QDateTime.fromString(student.last_run_date, Qt.ISODate))
            if dialog.exec_() == QDialog.Accepted:
                student.name = dialog.name_edit.text()
                student.link = dialog.link_edit.text()
                student.project_name = dialog.project_name_edit.text()
                student.last_run_date = dialog.last_run_edit.dateTime().toString(Qt.ISODate)
                self.update_table()
                self.save_students()

    def delete_student(self):
        indexes = self.table.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            del self.students[row]
            self.update_table()
            self.save_students()

    def run_selected(self):
        indexes = self.table.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            student = self.students[row]
            student.last_run_date = QDateTime.currentDateTime().toString(Qt.ISODate)
            # Implement running the selected student's project here
            converter = ScratchConverter(student.link)
            stl_code = converter.convertFromScratch()
            self.update_table()
            dialog = EditorDialog(self)
            dialog.text_editor.setPlainText(stl_code)
            dialog.exec_()



            

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
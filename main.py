import os
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from interface import Ui_MainWindow



class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.number_photo = 0
        self.files = []
        self.dir = ''
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.but_con.clicked.connect(self.next_photo)
        self.ui.but_ret.clicked.connect(self.prev_photo)
        self.ui.but_ok.clicked.connect(self.rename_photo)
        self.ui.but_choose.clicked.connect(self.choose_directory)


    def choose_directory(self):
        self.dir = QtWidgets.QFileDialog.getExistingDirectory(self)
        if self.dir != '':
            supported_type = ['.jpg', '.png', '.jpeg']
            self.files = [file for file in os.listdir(self.dir) if os.path.splitext(file)[1].lower() in supported_type]
            self.number_photo = 0
            self.show_photo()


    def show_photo(self):
        height, width = self.ui.output_pic.height(), self.ui.output_pic.width()
        if len(self.files) > abs(self.number_photo):
            pixmap = QtGui.QPixmap(rf'{self.dir}//{self.files[self.number_photo]}')
            pixmap = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
            self.ui.output_pic.setPixmap(pixmap)
            self.ui.old_name.setText(self.files[self.number_photo])
        else:
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(25)
            self.ui.output_pic.setFont(font)
            self.ui.output_pic.setText('В папке отсутствуют фото для переименования')

    def check_number(self, count):
        if abs(self.number_photo) < len(self.files)-1:
            self.number_photo += count
        else:
            self.number_photo = 0

    def next_photo(self):
        self.ui.new_name.clear()
        self.check_number(count=1)
        self.show_photo()

    def prev_photo(self):
        self.ui.new_name.clear()
        self.check_number(count=-1)
        self.show_photo()

    def rename_photo(self):
        type_photo = '.' + self.files[self.number_photo].split('.')[1]
        new = self.ui.new_name.toPlainText() + type_photo
        if os.path.isfile(fr'{self.dir}//{new}'):
            i = 1
            while (os.path.isfile(fr'{self.dir}//{new}')):
                new = self.ui.new_name.toPlainText() + str(i) + type_photo
                i += 1
            os.rename(fr'{self.dir}//{self.files[self.number_photo]}', fr'{self.dir}//{new}')
        else:
            os.rename(fr'{self.dir}//{self.files[self.number_photo]}', fr'{self.dir}//{new}')
        self.ui.new_name.clear()
        self.files[self.number_photo] = new
        self.check_number(count=1)
        self.show_photo()

app = QtWidgets.QApplication([])
application = window()
application.show()

sys.exit(app.exec())
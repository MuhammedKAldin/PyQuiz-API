#--------------------- APP-1 ---------------------#

from ast import If
from pickle import GLOBAL
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import sys
from QuestionPage import QuestionPage
import UserData

# Created a class object

class Main(QMainWindow):
    
    def __init__(self):
        super(Main, self).__init__()
        loadUi('Login.ui', self)
        
        # ~~---------- Ui Logic -------------~~
        
        # set the page base settings
        self.setWindowTitle("Exium - Login")
        self.setFixedSize(430, 721)
        
        # Adding difficulties to the combo box
        self.comboBox.addItems('easy medium hard'.split())
        self.comboBox.setStyleSheet('background-color: white')
        
        # OnClick Get Started button -> start the game
        self.pushButton.clicked.connect(lambda:self.Login())
        
    # Get Started button behavior
    def Login(self):
        
        # Pass Name & Difficulty to the next window
        UserData.student_name = self.textEdit.toPlainText()
        UserData.student_score = 0
        UserData.question_index = 0
        UserData.difficulty = self.comboBox.currentText()
        print(UserData.student_name, UserData.difficulty)
        
        # Transport to the next window
        self.anotherwindow = QuestionPage()
        self.anotherwindow.show()
        self.hide()
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    app.exec_() 

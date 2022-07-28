#--------------------- APP-1 ---------------------#

from ast import If
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import sys
import UserData
import asyncio

# Created a class object

class QuestionPage(QMainWindow):
    
    def __init__(self):
        super(QuestionPage, self).__init__()
        loadUi('Question.ui', self)

        # ~~---------- Ui Logic -------------~~
        
        # set the page base settings
        self.setWindowTitle("Exium - Quiz")
        self.setFixedSize(810, 571)
        
        # Reading User Data
        currentIndex = UserData.question_index
        currentScore = UserData.student_score
        currentUsername = UserData.student_name
        currentDifficulty = UserData.difficulty
        
        self.label_username.setText(f"User: {currentUsername}")
        self.label_difficulty.setText(f"Group Difficulty: {currentDifficulty}")
        self.label_score.setText(f"Correct anwers: {currentScore}")
        
        
        # Provide Question to the user
        self.questionText.setText(UserData.get_question(currentIndex))
        self.questionIndex.setText(f"Question {currentIndex + 1}")
        
        # Answers provided -> Await the user's answer to be received
        # Answers collecting loop
        answers = asyncio.run(UserData.get_answers(currentIndex)) 
            
        # Check if all answers are loaded to the list or not before going further 
        if(len(answers) >= 3): # if the list is not empty
            self.answer1.setText(answers[0])
            self.answer2.setText(answers[1])
            self.answer3.setText(answers[2])
            self.answer4.setText(answers[3])     
        
        # # OnClick check if the answer is correct
        first_buttonText = self.answer1.text()
        second_buttonText = self.answer2.text()
        third_buttonText = self.answer3.text()
        fourth_buttonText = self.answer4.text()
        self.answer1.clicked.connect(lambda:self.check_answer(first_buttonText, currentIndex))
        self.answer2.clicked.connect(lambda:self.check_answer(second_buttonText, currentIndex))
        self.answer3.clicked.connect(lambda:self.check_answer(third_buttonText, currentIndex))
        self.answer4.clicked.connect(lambda:self.check_answer(fourth_buttonText, currentIndex))
        
        # # OnClick Previous button -> go to the previous question
        # self.pushButton_previous.clicked.connect(lambda:self.previous_question())
        
        # # OnClick Finish button -> go to the finish page
        # self.pushButton_finish.clicked.connect(lambda:self.finish_game())
        
        # # OnClick Home button -> go to the home page
        # self.pushButton_home.clicked.connect(lambda:self.home_page())
        
    # async def animation_CorrectAnswer(self):
    #     self.questionText.setStyleSheet('color: rgb(0, 255, 64)')
    #     await asyncio.sleep(3)
    
    # async def animation_InCorrectAnswer(self):
    #     self.questionText.setStyleSheet('color: red')
    #     await asyncio.sleep(3)
    
    def check_answer(self, answer, index):
        
        # Writing in User Data
        if UserData.question_index <= UserData.max_index - 2:
            UserData.question_index += 1
            
            # OnCondition: if the answer is correct && the Game is not finished
            if UserData.evaluateAnswer(answer, index):
                UserData.student_score += 1
                print("Correct")
            else:
                print("InCorrect ")

            # Empty the list of answers
            UserData.current_answers = []
            print(f"Question index: {UserData.question_index}")
            
            # import time
            # time.sleep(3)
            self.anotherwindow = QuestionPage()
            self.anotherwindow.show()
            self.hide()
            
        else:
            print ("Game Over")
            self.questionText.setText("Exam is Over")
            self.questionIndex.setText(f" Your score is: {UserData.student_score}/10")
            self.answer1.hide()
            self.answer2.hide()
            self.answer3.hide()
            self.answer4.hide()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = QuestionPage()
    ui.show()
    app.exec_() 

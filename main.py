import json
import os
import requests

response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=hard")

def requestJson(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

# Parse JSON into an object with attributes corresponding to dict keys.
data = json.loads(requestJson(response.json()["results"]))
#print(x[0]["category"])

#--------------------- Design ---------------------#
from ast import If
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('Login.ui', self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    app.exec_() 

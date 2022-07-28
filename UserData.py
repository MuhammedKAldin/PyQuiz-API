from mimetypes import init
import requests
import json
import os
import random
import asyncio

#--------------------- USER ---------------------#

student_name = "None"
student_score = 0
difficulty = "easy"
question_index = 0
max_index = 10
response = requests.get(f"https://opentdb.com/api.php?amount={max_index}&difficulty={difficulty}")
m_json = response.json()
current_answers = []

def get_question(index):
    data = m_json["results"][index]["question"]
    return data

async def get_answers(index):
    correct = m_json["results"][index]["correct_answer"]
    wrong = m_json["results"][index]["incorrect_answers"]
    current_answers.extend(wrong)
    current_answers.append(correct)
    
    return current_answers
    
    
# async def async_get_answers(index):
#     task1 = asyncio.create_task(get_answers(index))  # returns immediately, the task is created
#     await asyncio.sleep(3)
#     await task1
    
    # Filled the List with answers then returning it
    # print(current_answers)
    return current_answers
    
def evaluateAnswer(answer, index):
    # print(answer)
    if str(answer) == str(m_json["results"][index]["correct_answer"]):
        return True
    else:
        return False

# def __init__(self, question, answer):
#     self.question = question
#     self.answer = answer
# def ask_and_evaluate(self):
#     print(self.question)
#     return self.answer == input()

# This script recreates a simple quiz using Object Oriented Programming (OOP)
#
# Created by: Lohit Deva
# 30/12/2022

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = list()

for question in question_data:
    question_bank.append(
        Question(question['question'], question['correct_answer']))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.input()

print(
    f"\nYou completed the quiz! Your final score is: {quiz_brain.score}/{quiz_brain.question_number}")

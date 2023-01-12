"""OOP - Kvíz"""

from question_model import Question
from data import question_data
from brain import Brain

question_list = []

for one_que in question_data:
    question_t = one_que["text"]
    question_a = one_que["answer"]
    new_question = Question(question_t, question_a)
    question_list.append(new_question)

# print(question_list)
quiz = Brain(question_list)

while quiz.has_question():
    quiz.next_question()
print("Dokončili jste kvíz")
print(f"Vaše celkové skóre je {quiz.score}/{quiz.que_num}")
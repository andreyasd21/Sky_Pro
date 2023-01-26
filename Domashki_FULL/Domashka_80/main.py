import requests
import random

from utils import load_question, statistics

response = requests.get('https://www.jsonkeeper.com/b/FU3K')
filename = response.json()
questions = load_question(filename)

random.shuffle(questions)

for question in questions:
    print(question.build_question())
    user_input = input('Введите свой ответ: ')
    question.user_answer = user_input
    print(question.build_feedback())
    print('')

print('')
print(statistics(questions))

import requests

response = requests.get('https://www.jsonkeeper.com/b/FU3K')
data = response.json()
print(data)


def load_question(file_name):
    '''
    Функция получает данные о вопросах из файла JSON и возвращает список вопросов.
    '''
    with open(file_name, 'r', encoding='utf=8') as f:
        data = json.load(f)
    questions = []
    for i in data:
        text = i['q']
        difficulty = int(i['d'])
        right_answer = i['a']
        question = Question(text, difficulty, right_answer)
        questions.append(question)

    return questions
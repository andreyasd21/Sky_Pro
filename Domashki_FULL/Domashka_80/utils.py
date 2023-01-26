from Domashki_FULL.Domashka_80.question import Question


def load_question(file_name):
    """
    Функция получает данные о вопросах из списка словарей и возвращает список вопросов.
    """
    data = file_name
    questions = []
    for i in data:
        text = i['q']
        difficulty = int(i['d'])
        right_answer = i['a']
        question = Question(text, difficulty, right_answer)
        questions.append(question)

    return questions


def statistics(questions):
    """
    Функция выводит статистику игрока (очки
    :param questions:
    :return:
    """
    score = 0
    count = 0

    for question in questions:
        if question.is_correct():
            score += question.score
            count += 1
    return f'Вот и все!\n' \
           f'Отвечено {count} вопроса из {len(questions)}\n' \
           f'Набрано баллов: {score}'

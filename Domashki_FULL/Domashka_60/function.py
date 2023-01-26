import random


def get_word(words_txt):
    """
    Функция считывает файл со словами и возвращает список слов.
    """
    word_list = []
    with open(words_txt, 'r', encoding='utf-8') as w:
        for word in w.readlines():
            word_list.append(word.rstrip('\n'))
    return word_list


def random_word(word):
    """
    Функция получает слово и возвращает его рандомную версию.
    """
    word = list(word)
    random.shuffle(word)
    return ''.join(word)


def record_score(history_txt, name, score):
    """
    Функция записывает в файл имя и счет игрока.
    """
    with open(history_txt, 'a', encoding='utf-8') as r:
        r.write(f'{name} {score}\n')


def read_history(history_txt):
    """
    Функция считывает файл с именем и счетом ВСЕХ игроков
    и возвращает максимальный счет и количество игр.
    """
    max_score = 0
    count = 0
    with open(history_txt, 'r', encoding='utf-8') as his:
        for line in his.readlines():
            count += 1
            score = int(line.split(' ')[1])
            if score > max_score:
                max_score = score
    return f'Всего сыграно игр: {count}.\nМаксимальный рекорд: {max_score}.'

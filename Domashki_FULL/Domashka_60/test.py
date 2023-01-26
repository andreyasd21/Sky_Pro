import random


def random_word(i):
    """
    Функция получает слово и возвращет его рандомную версию.
    """
    word_ = ''.join([k.rstrip('\n') for k in i])
    random_ = ''.join(random.sample(word_, len(word_)))
    return word_, random_


user_name = input('Введите ваше имя: ')
user_score = 0

with open('words.txt', 'r') as words:
    for word in words:
        word_, random_ = random_word(word)
        print(f'Угадайте слово - {random_}')
        user_answer = input('Ваш ответ: ').lower()
        if user_answer == word_:
            user_score += 10
            print('Верно! Вы получаете 10 очков.')
        else:
            print(f'Неверно! Верный ответ – {word_}.')

with open('history.txt', 'a') as score:
    score.write(user_name + ':' + str(user_score) + '\n')

with open('history.txt', 'r') as s:
    score = 0
    games = 0
    for data in s:
        games += 1
        name, nums = data.rstrip('\n').split(':')
        if int(nums) >= score:
            score = int(nums)
    print(f'Всего сыграно игр: {games}.\nМаксимальный рекорд: {score}.')

#######################

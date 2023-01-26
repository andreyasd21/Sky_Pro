from function import random_word, get_word, record_score, read_history

if __name__ == '__main__':
    WORDS_TXT = 'words.txt'
    HISTORY_TXT = 'history.txt'
    USER_NAME = input("Введите ваше имя: ")
    words = get_word(WORDS_TXT)
    user_score = 0
    for word in words:
        print(f'Угадайте слово - {random_word(word)}')
        user_answer = input('Ваш ответ: ')
        if user_answer.lower().rstrip(' ') == word:
            user_score += 10
            print('Верно! Вы получаете 10 очков.')
        else:
            print(f'Неверно! Верный ответ – {word}.')
    record_score(HISTORY_TXT, USER_NAME, user_score)
    print(read_history(HISTORY_TXT))

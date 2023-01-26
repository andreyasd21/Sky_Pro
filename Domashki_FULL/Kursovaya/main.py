from functions import load_random_word
from basic_word import BasicWord
from player import Player

JSON = 'https://www.jsonkeeper.com/b/0ZIA'
basic_word = load_random_word(JSON)

print('Привет, введи свое имя.')
user_input = input('Имя: ').capitalize()
player = Player(name=user_input)
print(f'Привет, {player.get_name()}!')
print(f'''Составь 8 слов из слова {basic_word.get_word().title()}\n\
Слова должны быть не короче 3 букв.\n\
Чтобы закончить игру, угадай все слова или напиши "стоп/stop".\n\
Поехали, твоё первое слово?''')

while player.count_input_word() < basic_word.count_subwords():
    user_input = input()
    if len(user_input) <= 2:
        print('Слишком короткое слово.')
    elif player.count_input_word() == 8:
        print(f'Игра завершена, вы отгадали слов: {player.count_input_word()}.')
    elif user_input in ['стоп', 'stop']:
        break
    elif player.has_input_word(user_input):
        print('Слово уже использовано.')
    elif not basic_word.has_subwords(user_input):
        print('Неверно.')
    else:
        print('Верно.')
        player.add_word(user_input)

print(f'Игра завершена, вы отгадали слов: {player.count_input_word()}.')

user = input('Вы готовы ввести свой вес? (1-да/0-нет): ')
if user == '1':
    with open('weight.txt', 'a', encoding='utf-8') as data:
        data.write(input('Введите вес: '))
        data.write('\n')
    print('Данные записаны!')
else:
    print('До новых встреч!')
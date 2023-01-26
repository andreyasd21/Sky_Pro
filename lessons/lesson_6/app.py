from validators.validate_pin import validate_pin
from validators.validate_card import validate_card

print(f'Введите ваш номер карты\n')
card_number = input()
print(f'Введите ваш ПИН-код\n')
card_pin = input()

if validate_card(card_number):
    print('Номер карты допустимый')
else:
    print('Номер карты недопустимый')
if validate_pin(card_pin):
    print('ПИН-код допустимый')
else:
    print('ПИН-код недопустимый')

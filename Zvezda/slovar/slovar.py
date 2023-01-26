with open('slovar1.csv', 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()
lines = [s.strip('"') for s in lines]
print(lines)

slovo = {}

for line in lines:
    key, value = line.split(',"')
    slovo.update({key: value})

user = input('Введите значение: ')

if user in slovo.keys():
    print(user + ' - ' + slovo[user])
else:
    print('По вашему запросу ничего не найдено, могу предложить:', *slovo.keys(), sep='\n')

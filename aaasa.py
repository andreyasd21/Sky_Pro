users_list = '''Киселёв / Всеволод / Эдуардович / 342 020 / 14 ноября 2001 года / +7 (908) 161-64-28 / главный инженер
Довлатова / Эмилия /  Ефимовна / 342 000 / 18 мая 2001 года / +7 (924) 588-50-15 / технолог
Аверин / Мартын / Егорович / 217 340 / 12 февраля 1981 года / +7 (933) 768-22-15 / технолог
Князева / Августа / Егоровна / 320 021 / 2 июля 1984 года / +7 (965) 886-27-01 / расфасовщик
Шанская / Аграфена / Семёновна / 116 404 / 7 июля 1982 года / +7 (954) 940-47-96 / психолог для рыб'''
employees = {}

new_users_list = users_list.split('\n')
users_list = [i.split(' / ') for i in new_users_list]

for i in users_list:
    employees[i[0]] = {'f': i[0], 'i': i[1], 'o': i[2], 'pass': i[3], 'birthday': i[4], 'phone': i[5], 'position': i[6]}
print(employees)

for employee in employees.values():
    for key, value in employee.items():
        print(key, value)
    print("-")

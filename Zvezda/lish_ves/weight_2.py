with open('weight.txt', 'r', encoding='utf-8') as data:
    list = [int(i.rstrip('\n')) for i in data.readlines()]
    print(list)
prev_ves = 0
ves = 0
for k in list:
    ves = k
    if prev_ves >= ves:
        prev_ves = ves
        print('ves uhodit')
    else:
        prev_ves = ves
        print('cheto net')
with open('password.txt', 'r', encoding='utf-8') as file:
    ent = file.readlines()
    list_2 = [i.rstrip('\n') for i in ent]
    print(*list_2, sep='\n')

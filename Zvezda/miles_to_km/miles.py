with open('miles.txt', 'r', encoding='utf-8') as miles:
    for mile in miles.readlines():
        mtok = round(float(mile) * 1.6, 2)
        with open('kilometers.txt', 'a', encoding='utf-8') as kilo:
            kilo.write(f'{str(mtok)}\n')




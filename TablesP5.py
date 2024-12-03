print('--Program start')
cont = 'y'
while (cont == 'y') or (cont == 'Y'):
    print('Table codes: A= add, S = subtract, M = Multiply, D = divide')
    Table = input('Select a table code: ')
    Num = float(input('Enter number for table: '))
    if Table == 'A':
        for add in range(1, 11, 1):
            totalA = Num + add
            print(Num, '+', add, '=', totalA)
    else:
        if Table == 'S':
            for sub in range(10, 0, -1):
                totalS = Num - sub
                print(Num, '-', sub, '=', totalS)
        else:
            if Table == 'M':
                for mult in range(1, 11):
                    totalM = Num * mult
                    print(Num, 'X', mult, '=', totalM)
            else:
                if Table == 'D':
                    for div in range(1, 11):
                        totalD = Num / div
                        print(Num, '/', div, '=', totalD)
    cont = input('\nRun again? y/n -> ')
print('--Done--')

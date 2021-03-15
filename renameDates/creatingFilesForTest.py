#!python3
import random


for i in range(20):
    ano = random.randint(1990, 2020)
    mes = random.randint(1, 12)
    anobissexto = (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0))
    if anobissexto and mes == 2:
        print(f'{ano} é bissexto')
        dia = random.randint(1, 29)
    elif mes == 2:
        dia = random.randint(1, 28)
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dia = random.randint(1, 31)
    else:
        dia = random.randint(1, 31)
    data = f'{dia}-{mes}-{ano}'
    print(data)
    filename = f'arquivo-{data}.txt'
    print(filename)
    newFile = open(filename, 'w')
    newFile.write('teste')
    newFile.close()

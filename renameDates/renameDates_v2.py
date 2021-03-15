#!python3
'''
    renameDates.py: renomeia os nomes de arquivos 
    com formato DD-MM-AAAA em estilo brasileiro 
    para MM-DD-AAAA em estilo americano
'''
import  shutil, os, re

# Cria o regex que corresponde aos arquivos com formato de data em estilo brasileiro
datePattern = re.compile(r'''
    ^(.*?)-             # todo texto antes da data
    ((0|1|2|3)?\d)-     # um ou dois dígitos para o dia
    ((0|1)?\d)-         # um ou dois dígitos para o mês
    ((19|20)\d\d)       # quatro dígitos para o ano
    (.*?)$              #todo texto após a data
''', re.VERBOSE)

# Percorre os arquivos do diretório de trabalho com um loop
for brazFilename in os.listdir('.'):
    mo = datePattern.search(brazFilename)
    # Ignora os arquivos que não tenham data
    if mo == None:
        continue
    # Obtém as diferentes partes do nome do arquivo
    beforePart = mo.group(1)
    dayPart = mo.group(2)
    monthPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    # print(f'{brazFilename}, {beforePart}, {dayPart}, {monthPart}, {yearPart}, {afterPart}') 
    # print(f'{mo.group(3)}, {mo.group(5)}, {mo.group(7)}\n')
# TODO: Compões o nome do arquivo em estilo americano
# TODO: Obtém os paths absolutos completos dos arquivos
# TODO: Renomeia os arquivos


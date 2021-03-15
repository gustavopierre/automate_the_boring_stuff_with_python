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

# TODO: Percorre os arquivos do diretório de trabalho com um loop
# TODO: Ignora os arquivos que não tenham data
# TODO: Obtém as diferentes partes do nome do arquivo
# TODO: Compões o nome do arquivo em estilo americano
# TODO: Obtém os paths absolutos completos dos arquivos
# TODO: Renomeia os arquivos


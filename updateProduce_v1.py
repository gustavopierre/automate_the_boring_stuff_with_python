#!python3
'''
    updateProduce.py - corrige os preços em uma planilha de venda de produtos
'''
import openpyxl

wb = openpyxl.Workbook('procuceSales.xlsx')
sheet = wb['Sheet']
PRICE_UPDATES = {'Garlic': 3.07, 'Celery': 1.19, 'Lemon': 1.27}
# TODO: Percorre todas as linhas em um loop e atualiza os preços
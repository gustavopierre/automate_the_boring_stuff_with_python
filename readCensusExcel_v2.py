#!python3
'''
    readCensusExcel.py - Cria uma tabela com a população e o 
    número de setores censitários de cada condado.
'''
import openpyxl, pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

# TODO: Preencher countyData com a população e os setores de cada condado.

print('Reading rows...')
for row in range(2, len(sheet['A']) + 1):
    state = sheet['B'+str(row)].value
    county = sheet['C'+str(row)].value
    pop = sheet['D'+str(row)].value

    countyData.setdefault(state, {})
    countyData[state].setdefault(county,{'tracts': 0, 'pop': 0})
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

    # TODO: Abre um novo arquivo-texto e grava o conteúdo de countyData nesse arquivo.

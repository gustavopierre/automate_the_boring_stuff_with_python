#!python3
'''
    #quickWeather.py - Exibe a previsão do tempo para uma localidade na linha de comando
'''
import json, requests, sys

if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()

location = ''.join(sys.argv[1:])

# TODO: Faz download dos dados JSON a partir da API de openweathermap.org
# TODO: Carrega dados JSON em uma variável Python
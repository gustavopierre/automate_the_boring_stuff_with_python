#!python3
'''
    #quickWeather.py - Exibe a previsão do tempo para uma localidade na linha de comando
'''
import json, requests, sys

if len(sys.argv) < 2:
    print('Usage: quickWeather.py <cidade, estado, país>')
    sys.exit()

location = ''.join(sys.argv[1:])

# Faz download dos dados JSON a partir da API de openweathermap.org
url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&APPID=91b5c5fd4b8f50dbd7541c50a0f3ecf8'

response = requests.get(url)
response.raise_for_status()

# Carrega dados JSON em uma variável Python
weatherData = json.loads(response.text)
# Exibe as descrições da previsão do tempo
w = weatherData['list']
print(f'Current weather in {location}')
print(f'{w[0]["weather"][0]["main"]} - {w[0]["weather"][0]["description"]}\n')
print('Tomorrow:')
print(f'{w[1]["weather"][0]["main"]} - {w[1]["weather"][0]["description"]}\n')
print('Day after tomorrow:')
print(f'{w[2]["weather"][0]["main"]} - {w[2]["weather"][0]["description"]}\n')
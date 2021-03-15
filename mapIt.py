#!python3
'''
    mapIt.py - Inicia um mapa no navegador usando um endereço
    da linha de comando ou do clipboard
'''
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open(f'https://www.google.com.br/maps/place/{address}')

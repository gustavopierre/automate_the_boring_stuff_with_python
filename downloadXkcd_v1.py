#!python3
'''
    downloadXkcd.py - Faz o download de todas as tirinhas de XKCD
'''
import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exit_ok=True)
while not url.endswith('#'):
    # TODO: Faz download da página
    # TODO: Encontra o URL da imagem da tirinha
    # TODO: Faz o download da imagem
    # TODO: Salva a imagem em ./xkcd
    # TODO: Obtém o url do botão Prev
    pass

print('Done!')

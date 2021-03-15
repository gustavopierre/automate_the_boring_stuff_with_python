#!python3
'''
    resizeAndAddLogo.py - redimensiona todas as imagens do diretório 
    de trabalho atual para que caibam em um quadrado de 300x300 e 
    acrescenta catlogo.png no canto inferior direito.
'''

import  os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.SQUARE_FIT_SIZE

# TODO:  Percorre todos arquivos do diretório de trabalho em um loop.
# TODO: Verifica se a imagem deve ser redimensionada.
# TODO: Calcula a nova largura e a nova altura para o redimensionamento.
# TODO: Redimensiona a imagem.
# TODO: Adiciona o logo.
# TODO: Salva as alterações.
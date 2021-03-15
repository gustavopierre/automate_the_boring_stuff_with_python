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
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)

# Percorre todos arquivos do diretório de trabalho em um loop.
for filename in os.listdir('.'):
    if not (filename.endswith('.pnj') or filename.endswith('.jpg'))\
        or filename == LOGO_FILENAME:
        continue
    im = Image.open(filename)
    width, height = im.size

# TODO: Verifica se a imagem deve ser redimensionada.
# TODO: Calcula a nova largura e a nova altura para o redimensionamento.
# TODO: Redimensiona a imagem.
# TODO: Adiciona o logo.
# TODO: Salva as alterações.
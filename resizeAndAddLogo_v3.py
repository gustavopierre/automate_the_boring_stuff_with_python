#!python3
'''
    resizeAndAddLogo.py - redimensiona todas as imagens do diretório 
    de trabalho atual para que caibam em um quadrado de 300x300 e 
    acrescenta catlogo.png no canto inferior direito.
'''

import  os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo2.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)

# Percorre todos arquivos do diretório de trabalho em um loop.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg'))  or filename == LOGO_FILENAME:
        continue
    im = Image.open(filename)
    width, height = im.size

    # Verifica se a imagem deve ser redimensionada.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calcula a nova largura e a nova altura para o redimensionamento.
        if width > height:
            height = int((SQUARE_FIT_SIZE/width)*height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE/height)*width)
            height = SQUARE_FIT_SIZE
        
        # Redimensiona a imagem.
        print(f'Resizing {filename}...')
        im = im.resize((width, height))

    # Adiciona o logo.
    print(f'Adding logo to {filename}')
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Salva as alterações.
    im.save(os.path.join('withLogo', filename))

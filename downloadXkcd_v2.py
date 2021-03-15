#!python3
'''
    downloadXkcd.py - Faz o download de todas as tirinhas de XKCD
'''
import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    # Faz download da página
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    # Encontra o URL da imagem da tirinha
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = f'http:{comicElem[0].get("src")}'
        # Faz o download da imagem
        print(f'Downloading image {comicUrl}')
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Salva a imagem em ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

        # Obtém o url do botão Prev
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
    
print('Done!')

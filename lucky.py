#!python3
'''
    lucky.py - abre vários resultados de pesquisa no Google
'''
import requests, sys, webbrowser, bs4

print('Googling...')
url = 'http://google.com/search?q=mascara'
res = requests.get(url)
# res = requests.get(f'http://google.com/search?q={"".join(sys.argv[1:])}')

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select(".r a")
#print(linkElems)
print(len(linkElems))
numOpen = min(5, len(linkElems))
#for i in range(numOpen):
    #webbrowser.open(f'http://google.com{linkElems[i].get("href")}')

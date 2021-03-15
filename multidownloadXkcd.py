#!python3
import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True)


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print(f'Downloading page http://xkcd.com/{urlNumber}...')
        res = requests.get(f'https://xkcd.com/{urlNumber}')
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            print(f'Downloading image {comicUrl}...')
            res = requests.get(comicUrl)
            res.raise_for_status()
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


downloadThreads = []
for i in range(1, 1401, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')

import requests
from bs4 import BeautifulSoup

songsPk = 'http://www.songspk.link'
#baseUrl = songsPk + movieName.lower() + '.html'

def GetUrlFromFirstLetter(url):
    return songsPk + '/' + url[0].lower() + '_list.html'

def getName(movieName):
    link = GetUrlFromFirstLetter(movieName)
    html = requests.get(link)
    soup = BeautifulSoup(html.text)
    anchorList = []
    for anchor in soup.find_all('a'):
        if movieName.lower() in anchor.text.lower():
            anchorList.append(anchor['href'])
    return anchorList

def PrepareUrl(movieName):
    anchor = getName(movieName)
    for i in range(len(anchor)):
        if not 'http' in anchor[i]:
            newUrl = songsPk + '/' + anchor[i]
            anchor[i] = newUrl
    return anchor

def ListImages(listOfUrl):
    link = listOfUrl[0]
    html = requests.get(link)
    soup = BeautifulSoup(html.text)
    imgLink = soup.find_all(attrs={"align":"left"})
    imgSrc = imgLink[0]['src']
    return imgSrc

def GetSongsList(movieName):
    listOfUrl = PrepareUrl(movieName)
    imgSrc = ListImages(listOfUrl)
    songsList = []
    for url in listOfUrl:
        if not 'albums' in url:
            html = requests.get(url)
            soup = BeautifulSoup(html.text)
            for anchor in soup.find_all('a'):
                try:
                    if '/song.php?songid=' in anchor['href'].lower():
                        name_link_dict = {'Name':anchor.text,'link':anchor['href'],'imgSrc': imgSrc}
                        songsList.append(name_link_dict)
                except Exception as error:
                    continue
        else:
            html = requests.get(url)
            soup = BeautifulSoup(html.text)
            for anchor in soup.find_all('a'):
                try:
                    if '.mp3slash.net' in anchor['href']:
                        name_link_dict = {'Name':anchor.text,'link':anchor['href'],'imgSrc':imgSrc}
                        songsList.append(name_link_dict)
                except Exception as e:
                    continue
    return songsList


#print PrepareUrl('bajirao mastani')

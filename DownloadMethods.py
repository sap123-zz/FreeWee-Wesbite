# this file is to write functions to download from various sites
import requests
import datetime
from bs4 import BeautifulSoup

def GetFileExtension(URL):
  formats = ['.jpg','.jpeg','.png']
  for i in formats:
    if (i in URL):
      return i

def CreateFileName(picUrl):
  timenowInMilli = str(datetime.datetime.now().strftime("%s"))
  extension = GetFileExtension(picUrl)
  nameOfImage = 'static/images/'+timenowInMilli + extension
  return str(nameOfImage)


def DownloadPic(url):
    imgDict = {}
    htmlText = requests.get(url)
    soup = BeautifulSoup(htmlText.text)
    for meta in soup.find_all('meta'):
        _property = str(meta.get('property'))
        if _property == 'og:image':
            picUrl = str(meta.get('content'))
            nameOfImage = CreateFileName(picUrl)
            fileName = open(nameOfImage,'wb')
            fileName.write(requests.get(picUrl).content)
            imgDict = {'picURL': picUrl,'filelocation':nameOfImage}
            return imgDict


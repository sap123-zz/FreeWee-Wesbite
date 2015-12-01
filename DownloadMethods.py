# this file is to write functions to download from various sites
import urllib2
import datetime as time
from bs4 import BeautifulSoup

def GetFileExtension(URL):
  formats = ['.jpg','.jpeg','.png','.mp3']
  for i in formats:
    if (i in URL):
      return i

def GetFileName(url):
    extension = GetFileExtension(url)
    return 'Download_' + str(time.datetime.now().hour) + str(time.datetime.now().second) + extension

def DownloadPic(url):
    imgDict = {}
    htmlText = ""
    try:
        htmlText = urllib2.urlopen(url)
    except Exception as e:
        #print e #error handled
        return
    soup = BeautifulSoup(htmlText.read())
    for meta in soup.find_all('meta'):
        _property = str(meta.get('property'))
        if _property == 'og:image':
            picUrl = str(meta.get('content'))
            imgDict = {'picURL': picUrl}
            return imgDict

def CreateDownload(url):
    try:
        resp = urllib2.urlopen(url)
        return resp.read()
    except Exception as e:
        #print e #error handled
        return 


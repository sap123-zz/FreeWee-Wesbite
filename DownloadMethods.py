# this file is to write functions to download from various sites
import urllib2
import datetime as time
from bs4 import BeautifulSoup
import json

def GetFileExtension(URL):
  formats = ['.jpg','.jpeg','.png','.mp3','.mp4']
  for i in formats:
    if (i in URL):
      return i

def GetFileName(url):
    extension = GetFileExtension(url)
    return 'Download_' + str(time.datetime.now().hour) + str(time.datetime.now().second) + extension

def DownloadPic(url):
#this method checks if the given url has gif, if so return the video/gif url 
    try:
        htmlText = urllib2.urlopen(url)
    except Exception as e:
        return
    soup = BeautifulSoup(htmlText.read())
    imgDict = {'picURL':''}
    for meta in soup.find_all('meta'):
        # then get the video link only
        _property = str(meta.get('property'))
        if _property == 'og:video':
            videoDict = {'picURL': meta.get('content')}
            return videoDict
        else:
            # then get the image content
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

def GetMimeType(url):
# accept the filename and detect what is mimetype and send accordingly
    formats = GetFileExtension(url)
    return {
            '.jpg'  :'image/jpeg',
            '.jpeg' :'image/jpeg',
            '.png'  :'image/jpeg',
            '.mp3'  :'audio/mpeg3',
            '.mp4'  :'video/mp4'
            }[formats]
    

#url_video = 'https://www.instagram.com/p/_6QQJujJ9Z/?taken-by=9gag'
#url_image = 'https://www.instagram.com/p/_6CzIljJ7e/?taken-by=9gag'


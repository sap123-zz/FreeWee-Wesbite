# this file is to write functions to download from various sites
import requests
from bs4 import BeautifulSoup

def DownloadPic(url):
    htmlText = requests.get(url)
    soup = BeautifulSoup(htmlText.text)
    for meta in soup.find_all('meta'):
        _property = str(meta.get('property'))
        if _property == 'og:image':
            picUrl = str(meta.get('content'))
            return picUrl


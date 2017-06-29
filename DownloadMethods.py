# this file is to write functions to download from various sites
import urllib2
import datetime as time
from bs4 import BeautifulSoup
import json
from Constants import *

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
    soup = soupResponse(url)
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
 
def soupResponse(url):
	response = urllib2.urlopen(url)
	return BeautifulSoup(response.read(),'html.parser')

def urlList(url):
	url_list = []
	soup = soupResponse(url)
	for link in soup.find_all('a',href=True):
		url_list.append(link['href'])
	return url_list

def getUrl(word):
	return start_url + word[0] + end_url

def getMatchedResults(word):
	url_to_search = getUrl(word)
	url_list = urlList(url_to_search)
	url_matched_result_list = []
	for link in url_list:
		if word in str(link):
			url_matched_result_list.append(str(domain_url) + str(link))
	return url_matched_result_list

def getFilteredUrlList(word):
	url_matched_result_list = getMatchedResults(word)
	download_list = []
	for url in url_matched_result_list:
		new_soup = soupResponse(url)
		for param in new_soup.find_all('param'):
			download_list.append(str(param['value']))
	return filterDownloadLinks(download_list)
	
def filterDownloadLinks(list):
	download_links = []
	for value in list:
		if '.mp3' in str(value):
			download_links.append(value)	
	return downloadList(download_links)

def downloadList(list):
	final_download_list = []
	for string in list:
		final_download_list.append(domain_url + string[string.index('/files/'):string.index('.mp3')] + '.mp3')
	return final_download_list
		#final_download_list.append(string[string.index('/files/'):string.index('.mp3')] + '.mp3')

#print getFilteredUrlList('gangster')

#url_video = 'https://www.instagram.com/p/_6QQJujJ9Z/?taken-by=9gag'
#url_image = 'https://www.instagram.com/p/_6CzIljJ7e/?taken-by=9gag'


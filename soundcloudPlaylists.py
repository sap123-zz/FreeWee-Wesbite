#this file holds soundcloud api

import soundcloud
client_id = 'eef823eb72081eccc8684bc619021062'
client = soundcloud.Client(client_id=client_id)

#this def return the list of playlists
# {[{'title','artwork_url','id','stream_url'}],}
def Playlists(name):
    lists = client.get('/playlists',q={str(name)})
    reqDict = dict()
    reqPlaylist = []
    for objects in lists:
        innerLists = []
        nameOfPlaylist = {'name':objects.permalink}
        for lists in objects.tracks:
            innerDict = dict()
            innerDict = {'stream_url':lists['stream_url'],'id':lists['id'],'title':lists['title'],'artwork_url':lists['artwork_url']}
            innerLists.append(innerDict)
        reqPlaylist.append(innerDict)
    print len(reqPlaylist)
    return reqPlaylist


#print Playlists('arigit singh')

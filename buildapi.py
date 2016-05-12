# file to get the query string and return the api
import soundcloud

client_id = 'eef823eb72081eccc8684bc619021062'

def MillisecondsToDate(milliseconds):
    seconds = (milliseconds/1000)%60
    minutes = (milliseconds/(1000*60))%60
    return str(minutes) + ":" + str(seconds)
def BuildJsonApi(tracks,error):
#the json given by soundcloud is decoded into required format
    json_array  = []
    if error != "":
        return error
    else:
        for i in range(len(tracks)):
            items = tracks[i]
            artworkUrl = ""
            if items.artwork_url:
                artworkUrl = items.artwork_url
            else:
                artworkUrl = ""
            json_array.append({
                    "id"         : items.id,
                    "title"      : items.title,
                    "stream_url" : items.stream_url,
                    "artwork_url": artworkUrl,
                    "duration"   : MillisecondsToDate(items.duration)
                })
        return json_array


def BuildApi(query):
#gets the name of song searched and builds the tracks json
    client = soundcloud.Client(client_id = client_id)
    try :
        tracks = client.get('/tracks', q=str(query))
    except Exception, e:
        return BuildJsonAPi("",e.message)
    return BuildJsonApi(tracks,"")



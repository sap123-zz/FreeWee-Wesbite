# file to get the query string and return the api
import soundcloud

client_id = 'eef823eb72081eccc8684bc619021062'

def BuildJsonApi(tracks,error):
    json_array  = []
    if error != "":
        return error
    else:
        for i in range(len(tracks)):
            items = tracks[i]
            json_array.append({
                    "id"         : items.id,
                    "title"      : items.title,
                    "stream_url" : items.stream_url,
                })
        return json_array


def BuildApi(query):
    client = soundcloud.Client(client_id = client_id)
    try :
        tracks = client.get('/tracks', q=str(query))
    except Exception, e:
        return BuildJsonAPi("",e.message)
    return BuildJsonApi(tracks,"")



from io import BytesIO
import json
import os

from flask import Flask,render_template,request,redirect,send_file,jsonify,send_from_directory
app = Flask(__name__)

from DownloadMethods import DownloadPic, CreateDownload, GetFileName,GetMimeType
from Platform import IS_OPENSHIFT
from buildapi import BuildApi
from TestProto import songData
from Songspk import *
from soundcloudPlaylists import *

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        url = str(request.form['url'])
        downloadUrl = DownloadPic(url)
        return render_template('index.html', downloadUrl = downloadUrl['picURL'])
        
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/about_us',methods=['GET'])
def aboutUs():
    return render_template('about_us.html')

@app.route('/download/pics/v1', methods=['GET'])
def DownloadImage():
    url = request.args.get('urlvalue','')
    resp = CreateDownload(url)
    filename = GetFileName(url)
    mimeType = GetMimeType(url)
    return send_file(BytesIO(resp), mimetype=mimeType, attachment_filename=filename, as_attachment=True)

@app.route('/songs',methods=['GET'])
def songs():
    return render_template('downloadsongs.html')

@app.route('/download/songs/v1',methods=['GET'])
def DownloadSongs():
    data  = request.args.get('urlvalue','')
    jsonValue = json.loads(data)
    title = jsonValue['title'].encode('utf-8')[:30] + '.mp3'
    url = str(jsonValue['url'])
    resp = CreateDownload(url)
    return send_file(BytesIO(resp), mimetype="audio/mpeg", attachment_filename=title, as_attachment=True)

#api to get json of songs with query
#http://imgdownload-searchall.rhcloud.com/api/v1/songs/tum%20sath%20ho
@app.route('/api/v1/songs',methods=['GET'])
def version():
    songName = request.args.get('urlvalue','')
    return jsonify({"result":BuildApi(songName)})

@app.route('/api/v1/bolly_songs',methods=['GET'])
def bolly_api():
    movieName = request.args.get('urlvalue','')
    return jsonify({"result":GetSongsList(movieName)})

@app.route('/api/v1/sc_playlists',methods=['GET'])
def playlists():
    nameOfPlaylist = request.args.get('urlvalue','')
    #return str(Playlists(nameOfPlaylist))
    return jsonify({"result":Playlists(nameOfPlaylist)})

#api to get json of insta pic url with query as shareurl of instagram pic
@app.route('/api/v1/pic')
def instaApi():
    url = request.args.get('urlvalue','')
    return jsonify(DownloadPic(str(url)))

#this route contains default data of songs api
@app.route('/api/default/songs')
def default():
    return str(songData)

@app.route('/download/apk')
def android_apk():
    return send_file(BytesIO('/static/android_apk/app-release.apk'),attachment_filename="freewee.apk",as_attachment=True)

if __name__ == '__main__':
    if IS_OPENSHIFT:
        app.run()
    else:
        app.run(debug = True)


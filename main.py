from io import BytesIO
import json

from flask import Flask,render_template,request,redirect,send_file,jsonify
app = Flask(__name__)

from DownloadMethods import DownloadPic, CreateDownload, GetFileName,GetMimeType
from Platform import IS_OPENSHIFT
from buildapi import BuildApi
from TestProto import songData

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        url = str(request.form['url'])
        downloadUrl = DownloadPic(url)
        return render_template('index.html', downloadUrl = downloadUrl['picURL'])
        
    if request.method == 'GET':
        return render_template('index.html')

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

#api to get json of insta pic url with query as shareurl of instagram pic
@app.route('/api/v1/pic')
def instaApi():
    url = request.args.get('urlvalue','')
    return jsonify(DownloadPic(str(url)))

#this route contains default data of songs api
@app.route('/api/default/songs')
def default():
    return str(songData)
if __name__ == '__main__':
    if IS_OPENSHIFT:
        app.run()
    else:
        app.run(debug = True)


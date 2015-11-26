from io import BytesIO
import urllib2

from flask import Flask,render_template,request,redirect,send_file
app = Flask(__name__)

from DownloadMethods import DownloadPic, CreateDownload, GetFileName
from Platform import IS_OPENSHIFT

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        url = str(request.form['url'])
        downloadUrl = DownloadPic(url)
        return render_template('index.html', downloadUrl = downloadUrl['picURL'])
        
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/download/v1', methods=['GET'])
def DownloadImage():
    url = request.args.get('urlvalue','')
    resp = CreateDownload(url)
    filename = GetFileName(url)
    return send_file(BytesIO(resp), mimetype="image/jpeg", attachment_filename=filename, as_attachment=True)

@app.route('/songs',methods=['GET'])
def songs():
    resp = urllib2.urlopen(url) 
    return render_template('downloadsongs.html')

if __name__ == '__main__':
    if IS_OPENSHIFT:
        app.run()
    else:
        app.run(debug = True)


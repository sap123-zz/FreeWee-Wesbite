from flask import Flask,render_template,request,redirect
app = Flask(__name__)

from DownloadMethods import DownloadPic
from Platform import IS_OPENSHIFT

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        url = str(request.form['url'])
        downloadUrl = DownloadPic(url)
        return render_template('index.html', downloadUrl = downloadUrl['picURL'])
        
    if request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    if IS_OPENSHIFT:
        app.run()
    else:
        app.run(debug = True)


from flask import Flask,render_template,request,redirect
app = Flask(__name__)

from DownloadMethods import DownloadPic
from Platform import IS_OPENSHIFT

<<<<<<< HEAD
#url_extensions = ['.jpg','.png']
=======
url_extensions = ['.jpg','.png']
>>>>>>> 8f2768c1396fe95ad4c674ca699d2deca9b54f3f

@app.route('/',methods=['GET','POST'])
def index():
    notication = ""
    if request.method=='POST':
        url = str(request.form['url'])
        downloadUrl = DownloadPic(url)
        return render_template('index.html', downloadUrl = downloadUrl)
        
    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    if IS_OPENSHIFT:
        app.run()
    else:
        app.run(debug = True)


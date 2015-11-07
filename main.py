from flask import Flask,render_template,request,redirect
app = Flask(__name__)

from DownloadMethods import DownloadPic

url_extensions = ['.jpg','.png']

@app.route('/',methods=['GET','POST'])
def index():
    notication = ""
    if request.method=='POST':
        url = str(request.form['url'])
        downloadUrl = DownloadPic(url)
        notification = 'Download Complete'
        
    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

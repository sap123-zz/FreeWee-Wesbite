from flask import Flask,render_template,request
app = Flask(__name__)

import requests
import wget
from bs4 import BeautifulSoup

url_extensions = ['.jpg','.png']

def downloadFile(url):
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text)
    for meta in soup.find_all('meta'):
        proper = str(meta.get('property'))
        if proper == 'og:image':
            picUrl = str(meta.get('content'))
            #print picUrl
            filename = wget.download(picUrl)
            #print 'download done'

@app.route('/',methods=['GET','POST'])
def index():
    notication = ""
    if request.method=='POST':
        url = str(request.form['url'])
        downloadFile(url)
        notification = 'Download Complete'
        return render_template('thanks.html',notification=notification)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

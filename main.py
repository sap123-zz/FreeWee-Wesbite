from flask import Flask,render_template,request,redirect
app = Flask(__name__)

#from DownloadMethods import DownloadPic
#from Platform import IS_OPENSHIFT

#url_extensions = ['.jpg','.png']

@app.route('/',methods=['GET','POST'])
def index():
    return 'hello'
if __name__ == '__main__':
  if IS_OPENSHIFT:
    app.run()
  else:
    app.run(debug = True)


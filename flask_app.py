from flask import Flask, render_template, \
    request, redirect, url_for, send_from_directory
import base64
import random, string, os, datetime

app = Flask(__name__)
local_mode=os.getenv('USER')=='pydev'
app.config['UPLOAD_FOLDER'] =\
    '/home/shopeiro/fmedia/static/uploads' #default for pythonanywhere
if local_mode:
    print('start in local mode')
    app.config['UPLOAD_FOLDER'] = 'static/uploads/'


def randomword(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def log(msg):
    f = open("log.txt", "a")
    f.write(str(datetime.datetime.now().isoformat())+":"+msg + "\n")
    f.close()


@app.route('/')
def hello_world():
    log('we start /')
    return render_template('index.template.html')


@app.route('/looks')
def looks():
    log('we are in  '+os.getcwd())
    log('search for files in '+ app.config['UPLOAD_FOLDER'])
    return render_template("looks.template.html",files=os.listdir(app.config['UPLOAD_FOLDER']))


@app.route('/upload', methods=['GET'])
def upload_start():
    print("upload page")
    return render_template("upload.template.html")


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    img = request.form['img'][22:]
    fname=app.config['UPLOAD_FOLDER'] + "/"+randomword(20) + '.png'
    log('we try to save in '+fname)
    f = open(fname, 'wb')
    f.write(base64.b64decode(img))
    f.close()
    log(fname+" Uploaded")

# make comment for pythonanywhere
if local_mode and __name__ == "__main__":
    app.run(debug=True)

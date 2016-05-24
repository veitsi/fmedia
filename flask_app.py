# A very simple Flask Hello World app for you to get started with...
import os
from flask import Flask, render_template, \
    request, redirect, url_for, send_from_directory
import base64
import random, string, os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'fmedia/static/uploads/'


def randomword(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def log(msg):
    f = open('log.txt', 'a')
    f.write(msg + "\n")
    f.close()


@app.route('/')
def hello_world():
    log('we start /' + randomword(20))
    return render_template('index.template.html')


@app.route('/looks')
def looks():
    return render_template("looks.template.html"
                           , files=(os.listdir(app.config['UPLOAD_FOLDER'])))


@app.route('/upload', methods=['GET'])
def upload_start():
    print("upload page")
    return render_template("upload.template.html")


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    log('we try to save')
    img = request.form['img'][22:]
    f = open(app.config['UPLOAD_FOLDER'] + randomword(20) + '.png', 'wb')
    f.write(base64.b64decode(img))
    f.close()
    log("Uploaded")


# make comment for pythonanywhere
# if __name__ == "__main__":
#     app.run(debug=True)

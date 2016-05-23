# A very simple Flask Hello World app for you to get started with...
import os
from flask import Flask, render_template,\
    request, redirect, url_for, send_from_directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def hello_world():
    return render_template('uploader.template.html')


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if True: #file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = file.filename #secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return "Hello"
            # redirect(url_for('uploaded_file',
            #                     filename=filename))


# make comment for pythonanywhere
if __name__ == "__main__":
    app.run(debug=True)

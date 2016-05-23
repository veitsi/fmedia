# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.template.html')

# make comment for pythonanywhere
# if __name__ == "__main__":
#     app.run(debug=True)
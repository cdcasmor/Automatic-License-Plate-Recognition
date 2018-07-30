import os
from flask import Flask, jsonify, render_template, request
import Main

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/members")
def members():
    return render_template("members.html")

@app.route("/technologies")
def technologies():
    return render_template("technologies.html")

@app.route("/references")
def references():
    return render_template("references.html")

@app.route("/demo")
def demo():
    return render_template("demo.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], "plate.jpg")
    ff = os.path.join(app.config['UPLOAD_FOLDER'], "removeimgOriginalScene.png")
    if os.path.exists(f):
        os.remove(f)
    if os.path.exists(ff):
        os.remove(ff)
    file.save(f)
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)

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
#my_file = os.path.join(THIS_FOLDER, 'myfile.txt')
#UPLOAD_FOLDER = os.path.join('..','uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'gif'])

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
    f = os.path.join(app.config['UPLOAD_FOLDER'], "in.jpg")
    ff = os.path.join(app.config['UPLOAD_FOLDER'], "removeimgOriginalScene.png")
    if os.path.exists(f):
        os.remove(f)
    if os.path.exists(ff):
        os.remove(ff)
    file.save(f)
#Main.main(f)
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/team.html', methods=['GET'])
def team():
    # Team page
    return render_template('team.html')
@app.route('/events.html', methods=['GET'])
def events():
    # Events page
    return render_template('events.html')

@app.route('/gallery.html', methods=['GET'])
def gallery():
    # Gallery page
    return render_template('gallery.html')
@app.route('/ml.html', methods=['GET'])
def exploreml():
    # Explore page
    return render_template('ml.html')
@app.route('/reg.html', methods=['GET'])
def registration():
    # Registration page
    return render_template('reg.html')
@app.route('/git.html', methods=['GET'])
def git():
    # Git page
    return render_template('git.html')
@app.route('/git-reg.html', methods=['GET'])
def git_reg():
    # Git Registration page
    return render_template('git-reg.html')

@app.route('/coding.html', methods=['GET'])
def coding():
    #  Geeks page
    return render_template('coding.html')
@app.route('/crio.html', methods=['GET'])
def crio():
    # Crio page
    return render_template('crio.html')
@app.route('/mli.html', methods=['GET'])
def ExploreML():
    # Explore ML intermediate page
    return render_template('mli.html')

if __name__ == '__main__':
    app.run(debug=True)


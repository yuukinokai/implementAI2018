from flask import Flask, render_template, request, url_for, jsonify, send_file
from processImage import getDescription


app = Flask(__name__)


@app.route('/desc', methods=['POST'])
def test():
    img = request.form['img']
    print(img)
    result = getDescription(img)
    return render_template("index.html", description=result)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
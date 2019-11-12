from flask import Flask, render_template, send_from_directory
app = Flask("See")

@app.route('/public/<path:path>')
def send_public(path):
    return send_from_directory('public', path)

@app.route("/")
def hello():
    return render_template('main.html')


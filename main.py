from flask import Flask, render_template, send_from_directory, request, jsonify
app = Flask("See")

@app.route('/public/<path:path>')
def send_public(path):
    return send_from_directory('public', path)

@app.route("/")
def hello():
    return render_template('main.html')

@app.route("/start", methods = ["POST"])
def startCodeExecution():
    print(request.json)
    return {"msg": "Data submitted successfuly"}

@app.route("/pause", methods = ["GET"])
def pauseCodeExecution():
    return {"msg": "Execution paused"}

@app.route("/stop", methods = ["GET"])
def stopCodeExecution():
    return {"msg": "Execution stopped"}

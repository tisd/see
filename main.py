from flask import Flask, render_template, send_from_directory, request, jsonify
app = Flask("See")

from worker import create_source_file, compile, get_program_output

@app.route('/public/<path:path>')
def send_public(path):
    return send_from_directory('public', path)

@app.route("/")
def hello():
    return render_template('main.html')

@app.route("/start", methods = ["POST"])
def startCodeExecution():
    create_source_file(request.json['source'])
    err, output = compile()
    if err:
        return {'err': True, 'msg': err}
    err, output = get_program_output()
    if err:
        return {'err': True, 'msg': err}
    print(output.decode("utf-8") )
    return jsonify({"output": output.decode("utf-8") })

@app.route("/pause", methods = ["GET"])
def pauseCodeExecution():
    return {"msg": "Execution paused"}

@app.route("/stop", methods = ["GET"])
def stopCodeExecution():
    return {"msg": "Execution stopped"}

from flask import Flask,request
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/post',methods=["POST"])
def processcontent():
    team_id = request.json["team_id"]
    lang = request.json["lang"]
    problem_id = request.json["prb_id"]
    code = request.json["code"]
    filename = os.path.join('submission',lang)
    filename = os.path.join(filename,problem_id)
    if lang=="python":
        extens = '.py'
    elif lang=="java":
        extens='.java'
    else:
        extens=".cpp"

    filename = os.path.join(filename,str(team_id)+extens)
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(filename,"w") as f:
        f.write(code)
    return "OK"



app.run(host='0.0.0.0')
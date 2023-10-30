from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask import make_response
import config
import all
import json

app = Flask(__name__)
config = config.Config()
api_config = config.readApi()
host = api_config[0]
port = api_config[1]
upload_folder = app.config["UPLOAD_FOLDER"] = api_config[2]

@app.post("/scan")
def scan():
    if request.method == 'POST':
        f = request.files['sample']
        f.save(upload_folder + secure_filename(f.filename))
        file = secure_filename(f.filename)
        all_plugins = all.All()
        result = all_plugins.scan(file)
        ### small parser for clamav result ###
        result = result[0][0]
        result = {
                "filename": result[1],
                "status": result[2]
        }
        json_out = json.dumps(result)
        return json_out
            
@app.get("/check")
def check():
    return 'in progress'

def run():
    app.run(host=host, port=port)


    
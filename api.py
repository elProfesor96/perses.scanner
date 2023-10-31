from flask import Flask, request
from werkzeug.utils import secure_filename
from flask import make_response
import config
import engine

app = Flask(__name__)
config = config.Config()
api_config = config.readApi()
host = api_config[0]
port = api_config[1]
upload_folder = app.config["UPLOAD_FOLDER"] = api_config[2]
engine = engine.Engine()

@app.post("/scan")
def scan():
    if request.method == 'POST':
        f = request.files['sample']
        f.save(upload_folder + secure_filename(f.filename))
        file = secure_filename(f.filename)
        result = engine.scan(file)
        return result
            
@app.get("/check")
def check():
    return 'in progress'

def run():
    app.run(host=host, port=port)


    
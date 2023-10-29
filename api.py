from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask import make_response
import subprocess
import config

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
        try:
            clamav_run = subprocess.Popen(['docker', 'run', '-v', '/Users/elprofesor/dev/github/perses.scanner/samples:/samples:ro', '--rm', 'registry.elprofesor.io/perses/clamav:23.10.1', 'clamscan', '/samples/'+secure_filename(f.filename)], stdout=subprocess.PIPE)
            out, err = clamav_run.communicate()
            #scan_status = clamav_run.split(":")
            print(out.decode())
            scan_filename_parsed = out.decode().split(":")[0]
            scan_status_parsed = out.decode().split(":")[1].split("\n")[0]
            response = jsonify({'filename': scan_filename_parsed,
                            'status': scan_status_parsed
                            })

            return response
        except subprocess.CalledProcessError:
            pass
            
@app.get("/check")
def check():
    return 'in progress'

def run():
    app.run(host=host, port=port)


    
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask import make_response
import subprocess



class Api:
    pass

### change this to your own upload path
app = Flask(__name__)
upload_folder = app.config["UPLOAD_FOLDER"] = "/Users/elprofesor/dev/github/perses.scanner/samples/"



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
            return ""
            pass

    

#if __name__ == "__main__":
    
app.run(host="127.0.0.1", port=1337)
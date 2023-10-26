from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask import make_response
from subprocess import check_output



### change this to your own upload path
app = Flask(__name__)
upload_folder = app.config["UPLOAD_FOLDER"] = "/Users/elprofesor/dev/github/perses.scanner/samples/"



@app.post("/scan")
def scan():
    if request.method == 'POST':
        f = request.files['sample']
        f.save(upload_folder + secure_filename(f.filename))

        #resp = make_response("file uploaded successfully")
        #resp.headers['Server'] = 'perses'
      ## execute the scan and return the results
        cmd_out = check_output(['time', 'sleep', '300'])
        print(cmd_out)
        response = jsonify({'message': 'file uploaded successfully'
                            })
        return response
    

#if __name__ == "__main__":
    
app.run(host="127.0.0.1", port=1337)
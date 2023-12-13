

import subprocess
import config
import json

class Avg:
    def __init__(self):
        self.name = "avg"
        self.api_upload_folder = config.Config().readApi()[2]
        self.file = " "
        self.filehash = ''

    
    def scan(self, file, filehash):
        self.filehash = filehash
        self.file = file
        try:
            plugin_run = subprocess.Popen(['docker', 'run','--rm' , '-v', self.api_upload_folder+':/malware:ro',  'registry.elprofesor.io/perses/'+self.name+':23.10.1', '/malware/'+file], stdout=subprocess.PIPE)
            out, err = plugin_run.communicate()
            return out.decode()
        except (subprocess.CalledProcessError, TypeError):
            result = {
                "filename": file,
                "filehash": filehash,
                "status": "ERROR",
                "plugin": "avg"
            } 
            return result
        

    def pprint(self, result, filehash, filename):
        try:
            json_out = json.loads(result)
            json_avg = json_out['avg']
            result = {
                "filename": filename,
                "filehash": filehash,
                "status": str(json_avg["infected"])  + json_avg["result"],
                "plugin": "avg"
            }
            if result["status"] == "False":
                result["status"] = "OK"
            return result
        except json.decoder.JSONDecodeError:
            pass


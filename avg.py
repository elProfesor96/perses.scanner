

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
        except subprocess.CalledProcessError as e:
            return e
        

    def pprint(self, result):
        try:
            json_out = json.loads(result)
            json_avg = json_out['avg']
            result = {
                "filename": self.file,
                "filehash": self.filehash,
                "status": str(json_avg["infected"])  + json_avg["result"],
                "plugin": "avg"
            }
            if result["status"] == "False":
                result["status"] = "OK"
            return result
        except json.decoder.JSONDecodeError:
            pass


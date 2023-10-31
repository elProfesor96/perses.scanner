

import json
import subprocess
import config

class Comodo:
    def __init__(self):
        self.name = 'comodo'
        self.api_upload_folder = config.Config().readApi()[2]
        self.file = " "
    
    def scan(self, file):
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
            json_avg = json_out['comodo']
            result = {
                "filename": self.file,
                "status": str(json_avg["infected"])  + json_avg["result"],
                "plugin": "comodo"
            }
            if result["status"] == "False":
                result["status"] = "OK"
            return result
        except json.decoder.JSONDecodeError:
            pass




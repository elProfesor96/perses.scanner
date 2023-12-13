

import subprocess
import config
import json
import time

class Symantec:
    def __init__(self):
        self.name = "symantec"
        self.api_upload_folder = config.Config().readApi()[2]
        self.file = " "
        self.filehash = ''

    
    def scan(self, file, filehash):
        self.filehash = filehash
        self.file = file
        try:
            plugin_run = subprocess.Popen(['docker', 'exec' ,  'perses_symantec', 'sav', 'manualscan', '-s' ,'/malware/'+file], stdout=subprocess.PIPE)
            out, err = plugin_run.communicate()
            plugin_run.wait()
            time.sleep(3)
            plugin_logs = subprocess.Popen(['docker', 'logs', '--tail', '2',  'perses_symantec'],stdout=subprocess.PIPE)
            out2, err2 = plugin_logs.communicate()
            #print(out2.decode())
            return out2.decode()
        except (subprocess.CalledProcessError, TypeError):
            result = {
                "filename": file,
                "filehash": filehash,
                "status": "ERROR",
                "plugin": "symantec"
            } 
            return result
        

    def pprint(self, result, filehash, filename):
        try:
            if 'Threat Found' in result:
                result = {
                    "filename": filename,
                    "filehash": filehash,
                    "status": result.split(":")[2],
                    "plugin": "symantec"
                }
                return json.dumps(result)
            else:
                result = {
                    "filename": filename,
                    "filehash": filehash,
                    "status": "OK",
                    "plugin": "symantec"
                }
                return json.dumps(result)
        except json.decoder.JSONDecodeError:
            pass

#symantec = Symantec()
#result = symantec.scan("test.txt", "eicar.com")
#print(symantec.pprint(result, "test.txt", "eicar.com"))
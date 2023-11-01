import subprocess
import config

class Defender:
    def __init__(self):
        self.name = 'defender'
        self.api_upload_folder = config.Config().readApi()[2]
        self.file = " "
        self.filehash = ""
    
    def scan(self, file, filehash):
        self.filehash = filehash
        self.file = file
        try:
            plugin_run = subprocess.Popen(['docker', 'exec',  'perses_defender', 'mdatp', 'scan', 'custom', '--path' ,'/malware/'+file], stdout=subprocess.PIPE)
            out, err = plugin_run.communicate()
            return out.decode()
        except subprocess.CalledProcessError as e:
            return e
        

    def pprint(self, result):
        if 'found' in result:
            result = {
                "filename": self.file,
                "filehash": self.filehash,
                "status": result.split(":")[3].split("\n")[0],
                "plugin": "defender"
            }
            return result
        else:
            result = {
                    "filename": self.file,
                    "filehash": self.filehash,
                    "status": "OK",
                    "plugin": "defender"
                }
            return result




import subprocess
import config

class Plugin:
    def __init__(self, name):
        self.name = name
        self.api_upload_folder = config.Config().readApi()[2]
    
    def scan(self, file, cmd):
        try:
            clamav_run = subprocess.Popen(['docker', 'run', '-v', self.api_upload_folder+':/samples:ro', '--rm', 'registry.elprofesor.io/perses/'+self.name+':23.10.1', cmd, '/samples/'+file], stdout=subprocess.PIPE)
            out, err = clamav_run.communicate()
            return out.decode()
        except subprocess.CalledProcessError as e:
            return e
        
import configparser

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()                                                                                                                                        
        self.config.read("/Users/elprofesor/dev/github/perses.scanner/perses-cli/perses-cli.conf")
        self.default_perses_server = ""
        self.perses_license = ""

    def readDefaultPersesServer(self):             
        self.default_perses_server = self.config['PERSES-CLI']['DEFAULT_PERSES_SERVER']                  
        return self.default_perses_server
    
    def readPersesLicente(self):
        self.perses_license = self.config['PERSES-CLI']['PERSES_LICENSE']
        return self.perses_license
        
   
        


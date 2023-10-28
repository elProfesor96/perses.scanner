import configparser

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()                                                                                                                                        
        self.config.read("/Users/elprofesor/dev/github/perses.scanner/perses.conf")
        self.api_config = []

    def readApi(self):             
        root_url = self.config['API']['ROOT_URL']                   
        root_port = self.config['API']['ROOT_PORT']
        upload_folder = self.config['API']['UPLOAD_FOLDER']
        self.api_config.append([root_url, root_port, upload_folder])                                 
        return self.api_config[0]
        

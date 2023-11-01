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
        if upload_folder[-1] == "/":
            upload_folder = upload_folder
        else:
            upload_folder = upload_folder + "/"
        self.api_config.append([root_url, root_port, upload_folder])                                 
        return self.api_config[0]
        
    def readSlack(self):
        slack_webhook = self.config['SLACK']['SLACK_WEBHOOK']
        return slack_webhook
        




import plugin

class Clamav:
    def __init__(self):
        self.clamav = plugin.Plugin("clamav")
        self.filehash = ''
    
    def scan(self, file, filehash):
        self.filehash = filehash
        result = self.clamav.scan(file, "clamscan")
        #pprint_result = self.pprint(result)
        return result

    def pprint(self, result):
        try:
            filename = result.split(":")[0].split("/")[-1]
            #print(filename)
            status = result.split(":")[1].split("\n")[0]
            #print(status)
            result = {
                "filename": filename,
                "filehash": self.filehash,
                "status": status,
                "plugin": "clamav"
            }
            
            return result
        except Exception as e:
            pass
            



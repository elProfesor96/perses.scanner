

import plugin

class Clamav:
    def __init__(self):
        self.clamav = plugin.Plugin("clamav")
    
    def scan(self, file):
        result = self.clamav.scan(file, "clamscan")
        return result

    def pprint(self, result):
        filename = result.split(":")[0].split("/")[-1]
        #print(filename)
        status = result.split(":")[1].split("\n")[0]
        #print(status)
        result = ['clamav', filename, status]
        return result


clam = Clamav()
result = clam.scan("test.txt")
pprint = clam.pprint(result)
print(pprint)
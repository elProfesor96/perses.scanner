#### ---------------------------- 
# code for development, for git clone perses.scanner (DEV) #
#### ---------------------------- 


#currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#parentdir = os.path.dirname(currentdir)
#sys.path.insert(0, parentdir)
#### ---------------------------- 
# the above code is only for dev project and will let us import modules from the parent directory #
# like plugin module
#### ---------------------------- 

import json
import plugin

class Comodo:
    def __init__(self):
        self.comodo = plugin.Plugin("comodo")
    
    def scan(self, file):
        result = self.comodo.scan(file, "")
        return result

    def pprint(self, result):
        json_out = json.loads(result)
        print(json_out['comodo'])
        return result


#comodo = Comodo()
#result = comodo.scan("not.txt")
#comodo.pprint(result)

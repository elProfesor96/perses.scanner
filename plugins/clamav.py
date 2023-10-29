#### ---------------------------- 
# code for development, for git clone perses.scanner (DEV) #
#### ---------------------------- 
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
#### ---------------------------- 
# the above code is only for dev project and will let us import modules from the parent directory #
# like plugin module
#### ---------------------------- 

import plugin

class Clamav:
    def __init__(self):
        self.clamav = plugin.Plugin("clamav")
    
    def scan(self, file):
        result = self.clamav.scan(file, "clamscan")
        return result

    def pprint(self, result):
        return result


clamav = Clamav()
result = clamav.scan("test.txt")
print(result)
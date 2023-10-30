import all

class Engine:

    def scan(self, file):
        all_plugins = all.All()
        all_plugins_result = all_plugins.scan(file)
        return all_plugins_result

    def updatedb(self):
        pass

    def api(self):
        pass
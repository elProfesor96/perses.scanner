import all
import comodo
import avg
import clamav


class Engine:
    def __init__():
        self.clamav = clamav.Clamav()
        self.avg = avg.Avg()
        self.comodo = comodo.Comodo()

    def scan(self, file):
        all_plugins = all.All()
        all_plugins_result = all_plugins.scan(file)
        return all_plugins_result

    def updatedb(self):
        pass

    def api(self):
        pass
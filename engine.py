import comodo
import avg
import clamav


class Engine:
    def __init__(self):
        self.clamav = clamav.Clamav()
        self.avg = avg.Avg()
        self.comodo = comodo.Comodo()

    def scan(self, file):
        avg_out = self.avg.scan(file)
        comodo_out = self.comodo.scan(file)
        clamav_out = self.clamav.scan(file)

        raw_result = [clamav_out, avg_out, comodo_out]
        self.log( raw_result)

        result = [self.clamav.pprint(clamav_out), self.avg.pprint(avg_out), self.comodo.pprint(comodo_out)]
        self.log(result)
        return result

    def plugins(self):
        pass

    def api(self):
        pass

    def filehash(self, file):
        pass

    def log(self, result):
        print(result)

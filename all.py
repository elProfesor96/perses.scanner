import clamav
import comodo
import avg

class All:
    def __init__(self):
        self.all_results = []
        self.clamav = clamav.Clamav()
      #  self.avg = avg.Avg()
      #  self.comodo = comodo.Comodo()

    def scan(self, file):
        clamav_result = self.clamav.scan(file)
        pprint_clamav = self.clamav.pprint(clamav_result)
       # avg_result = self.avg.scan(file)
      #  comodo_result = self.comodo.scan(file)
        self.all_results.append([pprint_clamav])
        print(self.all_results)
        return self.all_results
    

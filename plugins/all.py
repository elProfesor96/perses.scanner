import clamav
import comodo
import avg

class All:
    def __init__(self):
        self.all_results = []
        self.clamav = clamav.Clamav()
        self.avg = avg.Avg()
        self.comodo = comodo.Comodo()

    def scan(self, file):
        clamav_result = self.clamav.scan(file)
        avg_result = self.avg.scan(file)
        comodo_result = self.comodo.scan(file)
        self.all_results.append([file, clamav_result, avg_result, comodo_result])
        return self.all_results
    
all = All()
result = all.scan("test.txt")    
print(result)
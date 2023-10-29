import clamav

class All:
    def __init__(self):
        self.all_results = []
        self.clamav = clamav.Clamav()

    def scan(self, file):
        clamav_result = self.clamav.scan(file)

        self.all_results.append([file, clamav_result])
        return self.all_results
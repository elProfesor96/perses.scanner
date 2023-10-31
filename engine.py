import comodo
import avg
import clamav
import hashlib
import config



class Engine:
    def __init__(self):
        self.clamav = clamav.Clamav()
        self.avg = avg.Avg()
        self.comodo = comodo.Comodo()
        self.file_hash = ''

        self.config = config.Config()
        self.api_config = self.config.readApi()
        self.upload_folder = self.api_config[2]


    def scan(self, file):
        self.file_hash = self.filehash(self.upload_folder + file)

        avg_out = self.avg.scan(file, self.file_hash)
        comodo_out = self.comodo.scan(file, self.file_hash)
        clamav_out = self.clamav.scan(file, self.file_hash)

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
        sha256_hash = hashlib.sha256()
        with open(file,"rb") as f:
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def log(self, result):
        print(result)

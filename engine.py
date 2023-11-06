import comodo
import avg
import clamav
import hashlib
import config
import database
import defender
from datetime import datetime



class Engine:
    def __init__(self):
        self.clamav = clamav.Clamav()
        self.avg = avg.Avg()
        self.comodo = comodo.Comodo()
        self.defender = defender.Defender()
        self.file_hash = ''

        self.config = config.Config()
        self.api_config = self.config.readApi()
        self.upload_folder = self.api_config[2]

        self.db = database.Database()


    def scan(self, file):
        self.file_hash = self.filehash(self.upload_folder + file)
        search_hash = self.db.search(self.file_hash)

        timestamp = self.timestamp()

        if search_hash:
            result_search = search_hash
            result = self.toJson(result_search)
            return result
        else:
            avg_out = self.avg.scan(file, self.file_hash)
            comodo_out = self.comodo.scan(file, self.file_hash)
            clamav_out = self.clamav.scan(file, self.file_hash)
            defender_out = self.defender.scan(file, self.file_hash)

            analyzed = self.analyzed(False, timestamp)

            raw_result = [clamav_out, comodo_out, avg_out, defender_out, analyzed]
            self.log(raw_result)

            result = [self.clamav.pprint(clamav_out), self.comodo.pprint(comodo_out), self.avg.pprint(avg_out), self.defender.pprint(defender_out), analyzed]
            self.log(result)
         
            if self.file_hash == '275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f':
                return result
            else:
                self.db.insert(self.file_hash, file, result[0]["status"], result[1]["status"], result[2]["status"], result[3]["status"], timestamp)
                return result

    def analyzed(self, flag, timestamp):
        if flag is True:
            result = {
                "analyzed": timestamp
            }
            return result
        elif flag is False:
            result = {
                "analyzed": "NEVER"
            }
            return result

    def timestamp(self):
        now = datetime.now()
        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
        return timestamp
    
    def toJson(self, db_search_result):
        filehash = db_search_result[0][1]
        filename = db_search_result[0][2]
        clamav = db_search_result[0][3]
        comodo = db_search_result[0][4]
        avg = db_search_result[0][5]
        defender = db_search_result[0][6]
        analyzed = db_search_result[0][7]
        clamav_json = {
            "filename": filename,
            "filehash": filehash,
            "status": clamav,
            "plugin": "clamav"
        }
        comodo_json = {
            "filename": filename,
            "filehash": filehash,
            "status": comodo,
            "plugin": "comodo"
        }
        avg_json = {
            "filename": filename,
            "filehash": filehash,
            "status": avg,
            "plugin": "avg"
        }
        defender_json = {
            "filename": filename,
            "filehash": filehash,
            "status": defender,
            "plugin": "defender"
        }
        analyzed_json = {
            "analyzed": analyzed
        }
        result = [clamav_json, comodo_json, avg_json, defender_json, analyzed_json]
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



import comodo
import avg
import clamav
import hashlib
import config
import database
import defender
from datetime import datetime
import multiprocessing



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
        self.plugins = ['clamav', 'comodo', 'avg', 'defender']
        db = database.Database()

        

    def scanForMultiprocess(self, file, filehash, plugin):
        if plugin == 'clamav':
            result = self.clamav.scan(file, filehash)
            return result
        elif plugin == 'comodo':
            result = self.comodo.scan(file, filehash)
            return result
        elif plugin == 'avg':
            result = self.avg.scan(file, filehash)
            return result
        elif plugin == 'defender':
            result = self.defender.scan(file, filehash)
            return result

    def scan(self, file):
        file_hash = self.filehash(self.upload_folder + file)
        db = database.Database()
        search_hash = db.search(file_hash)
        self.log(file_hash)
        #self.log(search_hash)
        timestamp = self.timestamp()

        if search_hash:
            result_search = search_hash
            result = self.toJson(result_search)
            return result
        else:
           # avg_out = self.avg.scan(file, self.file_hash)
           # comodo_out = self.comodo.scan(file, self.file_hash)
           # clamav_out = self.clamav.scan(file, self.file_hash)
           # defender_out = self.defender.scan(file, self.file_hash)
            ## multi
            #raw_result = []
       
            
            pool = multiprocessing.Pool(processes=4)
            raw_result = pool.starmap(self.scanForMultiprocess, 
                                    [(file, file_hash, 'clamav'), 
                                    (file, file_hash, 'comodo'), 
                                    (file, file_hash, 'avg'), 
                                    (file, file_hash, 'defender')])
                
            pool.close()
            pool.join()
            

            analyzed = self.analyzed(False, timestamp)

            #raw_result = [clamav_out, comodo_out, avg_out, defender_out, analyzed]
            self.log(raw_result)

            result = [self.clamav.pprint(raw_result[0], file_hash), 
                        self.comodo.pprint(raw_result[1], file_hash, file), 
                        self.avg.pprint(raw_result[2], file_hash, file), 
                        self.defender.pprint(raw_result[3], file_hash, file), 
                        analyzed]
            self.log(result)
            
            if file_hash == '275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f':
                return result
            else:
                try:
                    db.insert(file_hash, file, result[0]["status"], result[1]["status"], result[2]["status"], result[3]["status"], timestamp)
                    return result
                except TypeError:
                    self.log('Defender plugin error')
                    db.insert(file_hash, file, result[0]["status"], result[1]["status"], result[2]["status"], "NULL", timestamp)
                    pass
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

    def filehashRequest(self, contents):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(contents)
        return sha256_hash.hexdigest()

    def log(self, result):
        print(result)



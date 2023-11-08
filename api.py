from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask import make_response
import config
from engine import Engine
from redis import Redis
from rq import Queue
import database


app = Flask(__name__)
config = config.Config()
api_config = config.readApi()
host = api_config[0]
port = api_config[1]
upload_folder = app.config["UPLOAD_FOLDER"] = api_config[2]
#engine = engine.Engine()
redis_conn = Redis()
que = Queue(connection=redis_conn)
#db = database.Database()


def task(file):
    engine = Engine()
    result = engine.scan(file)
    return result

@app.post("/scan")
def scan():
    if request.method == 'POST':
        engine = Engine()
        f = request.files['sample']
        
       # contents = f.read()
       # file_hash = engine.filehashRequest(contents)
       # print("Hash from filehashRequest " + file_hash)
       # if len(file_hash) == 64:
       #     db = database.Database()
       #     search_hash = db.search(file_hash)
       #     print(search_hash)
        #    if search_hash:
        #        print('DA')
        #        result = engine.toJson(search_hash)
        #        f.close()
        #        return result

        #print("API Search db by hash function result")
       # print("Result", search_hash)
       # if search_hash:
       #     result_search = search_hash
       #     result = engine.toJson(result_search)
       #     f.close()
       #     return result
       # else:
        f.save(upload_folder + secure_filename(f.filename))
        
        file = secure_filename(f.filename)
        scan_job = que.enqueue(engine.scan, file)
        scan_job_id = scan_job.id
        scan_job_result = scan_job.result
        print(scan_job_result)
        print(len(que))
        f.close()
        return jsonify({"scanid":scan_job_id})
       
        #print(engine.filehash(f.filename))
        #f.save(upload_folder + secure_filename(f.filename))
        #file = secure_filename(f.filename)
        #result = engine.scan(file)

       # scan_job = que.enqueue(engine.scan, file)
       # scan_job_id = scan_job.id
      # scan_job_result = scan_job.result
       # print(scan_job_result)
       # print(len(que))
        #file_hash = engine.filehash(engine.upload_folder + secure_filename(f.filename))
        #search_hash = engine.db.search(file_hash)
        #if not search_hash:
        #    result_search = search_hash
        #    result = engine.toJson(result_search)
        #    return result
        #else:
        #    f.save(upload_folder + secure_filename(f.filename))
        #    file = secure_filename(f.filename)
        #    result = engine.scan(file)
      #  return jsonify({"scanid":scan_job_id})
            
@app.get("/check")
def check():
    if request.method == 'GET':
        try:
            scan_id = request.args.get('scanid')
            scan_job = que.fetch_job(scan_id)
            if scan_job.result:
                return jsonify(scan_job.result)
            else:
                return jsonify({"status":"PENDING"})
        except TypeError:
            return 'not found'
            
@app.get("/reset")
def reset():
    pass

def run():
    app.run(host=host, port=port)


    
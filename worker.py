from rq import Worker, Queue, Connection



if __name__ == '__main__':
    with Connection():
        worker = Worker(Queue('default'))
        worker.work()
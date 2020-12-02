from multiprocessing import Queue
from multiprocessing import Process
from multiprocessing import Pool
from time import sleep

def write_log(q):
    try:
        for value in ['第一条消息', '第二条消息', '第三条信息']:
            q.put_nowait(value)
            print('---写入log---value=%s'%value)
    except Exception as ret:
        print('---写入error-%s-'%ret)
            
def read_log(q):
    while True:
        if not q.empty():
           sleep(1)
           vals = q.get()
           print('---读取log---val=%s'%vals)
        else:
            break

if __name__=='__main__':
    q = Queue(2)
    pw = Process(target=write_log, args=(q, ))
    pr = Process(target=read_log, args=(q, ))
    #po = Pool(2)
    #po.apply_async(write_log, (q, ))
    #po.apply_async(read_log, (q, ))
    pw.start()
    pw.join()

    #po.close()
    #po.join()
    pr.start()
    pr.join()

    print('写入与读取log完成')

from multiprocessing import Manager
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
    q = Manager().Queue(2) # 如果在进程池之间建立通信队列，需要使用Manager().Queue()
    po = Pool(2) # 开辟进程池，最多两个进程
    po.apply_async(write_log, (q, ))
    po.apply_async(read_log, (q, ))
    

    po.close()
    po.join()

    print('写入与读取log完成')

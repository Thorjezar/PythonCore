import gevent

def info(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # 如果要让gevent切换协程去执行，需要进行耗时操作,需要调用gevent.sleep去完成耗时
        # 模拟进行IO操作
        gevent.sleep(1)

if __name__=="__main__":
    g1 = gevent.spawn(info, 5)
    g2 = gevent.spawn(info, 5)
    g3 = gevent.spawn(info, 5)
    g1.join()
    g2.join()
    g3.join()

import gevent

def info(n):
    for i in range(n):
        print(gevent.getcurrent(), i)

if __name__=="__main__":
    g1 = gevent.spawn(info, 5)
    g2 = gevent.spawn(info, 5)
    g3 = gevent.spawn(info, 5)
    g1.join()
    g2.join()
    g3.join()

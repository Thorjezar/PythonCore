"""

gevent网页数据抓取器，抓取网页的回访字节流量
在协程抓取数据时，会产生IO操作，导致占用协程

"""
from gevent import monkey
import gevent
# import urllib2 python2中可以导入
import urllib.request

# 有IO操作时需要
monkey.patch_all()

def catchData(url):
    print("GET:%s"%url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    print("%d bytes 数据已收到 从%s"%(len(data), url))

def main():
    g1 = gevent.spawn(catchData, "http://www.baidu.com/")
    g2 = gevent.spawn(catchData, "http://www.bilibili.com/")
    g3 = gevent.spawn(catchData, "http://ygw.jnkinfo.com/")
    g1.join()
    g2.join()
    g3.join()

if __name__=="__main__":
    main()

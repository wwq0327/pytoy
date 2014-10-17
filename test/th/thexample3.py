import urllib2
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'http://www.baidu.com',
    'http://www.yahoo.com',
    'http://weibo.com'
    ]

pool = ThreadPool(4)
results = pool.map(urllib2.urlopen, urls)
pool.close()
pool.join()


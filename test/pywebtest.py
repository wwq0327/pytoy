import threading, time, httplib, random

urls = [
    '/projects/1/',
    '/projects/13/',
    ]

MAX_PAGE = 10000
SERVER_NAME = '192.168.1.100'
TEST_COUNT = 10000

class RequestThread(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.test_count = 0

    def run(self):
        i = 0
        while i < TEST_COUNT:
            self.test_performace()
            i += 1

    def test_performace(elf):
        conn = httplib.HTTPConnection(SERVER_NAME)
        for i in range(0, random.randint(0, 100)):
            url = urls[random.randint(0, len(urls)-1)]
            url += str(random.randint(0, MAX_PAGE))
            try:
                conn.request("GET", url)
                rsps = conn.getresponse()
                if rsps.status == 200:
                    data = rsps.read()
                self.test_count += 1
            except:
                continue
        conn.close()

def main():
    start_time = time.time()
    threads = []
    thread_count = 100
    i = 0
    while i < thread_count:
        t = RequestThread('thread'+str(i))
        threads.append(t)
        t.start()
        i += 1
    word = ''
    while True:
        word = raw_input("cmd: ")
        if word == 's':
            time_span = time.time() - start_time
            all_count = 0
            for t in threads:
                all_count += t.test_count
            print "%s Request/Second" % str(all_count/time_span)
        elif word == 'e':
            TEST_COUNT = 0
            for t in threads:
                t.join(0)

            break

if __name__ == '__main__':
    main()


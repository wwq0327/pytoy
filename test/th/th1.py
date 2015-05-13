import threading

vars = 0

class MyThread(threading.Thread):
    def run(self):
        global vars
        read_vars = vars
        print "vars in %s is %d" % (self.name, read_vars)
        vars = read_vars
        print "vars in %s after is %d" % (self.name, vars)

def use_thread():
    threads = []
    for i in range(50):
        t = MyThread()
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print "After 50 modifications, some_var should have become 50"
    print "After 50 modifications, some_var is %d" % (vars,)

if __name__ == '__main__':
    use_thread()

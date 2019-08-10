from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.lfoo = Lock()
        self.lbar = Lock()
        self.lbar.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.lfoo.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lbar.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.lbar.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lfoo.release()
from threading import Lock

class Foo:
    def __init__(self):
        self.done1 = Lock()
        self.done2 = Lock()
        self.done1.acquire()
        self.done2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.done1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        with self.done1:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.done2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        
        with self.done2:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()


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


class TrafficLight:
    def __init__(self):
        self.openRoad = 1
        self.lock = Lock() # 1 for A, 2 for B
        self.direction2road = {1:1,2:1,3:2,4:2}

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:
        
        if direction:
            roadId = self.direction2road[direction]
        
        if roadId != self.openRoad: 
            with self.lock:
                self.openRoad = roadId
                turnGreen()
        
        crossCar()

                
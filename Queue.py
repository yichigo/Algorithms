class MyCircularQueue:
    
    def __init__(self, k: int):
        self.n = k+1
        self.queue = [0]*self.n
        self.head = 0
        self.tail = 0
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.n
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.n
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.tail - 1) % self.n]

    def isEmpty(self) -> bool:
        if self.tail == self.head:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if (self.tail + 1) % self.n == self.head:
            return True
        else:
            return False

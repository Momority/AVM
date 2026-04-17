class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [0] * k
        self.capacity = k
        self.head = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.q[(self.head + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.q[(self.head + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity

if __name__ == "__main__":
    obj = MyCircularQueue(3)
    print(f"enQueue 1: {obj.enQueue(1)}") # True
    print(f"enQueue 2: {obj.enQueue(2)}") # True
    print(f"enQueue 3: {obj.enQueue(3)}") # True
    print(f"enQueue 4: {obj.enQueue(4)}") # False
    print(f"Rear: {obj.Rear()}")          # 3
    print(f"IsFull: {obj.isFull()}")      # True
    print(f"deQueue: {obj.deQueue()}")    # True
    print(f"enQueue 4: {obj.enQueue(4)}") # True
    print(f"Rear: {obj.Rear()}")          # 4
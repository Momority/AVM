class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    def push(self, x: int) -> None:
        self.in_stack.append(x)
        print(f"Pushed {x}")
    def pop(self) -> int:
        self.move()
        val = self.out_stack.pop()
        print(f"Popped {val}")
        return val
    def peek(self) -> int:
        self.move()
        return self.out_stack[-1]
    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
if __name__ == "__main__":
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    print(f"Элемент на вершине: {myQueue.peek()}")
    
    myQueue.pop()
    
    print(f"Проверка на  пустоту {myQueue.empty()}")
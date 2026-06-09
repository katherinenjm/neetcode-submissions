
class MyStack:

    def __init__(self):
        self.lifo_struct = deque()
        self.lifo_size = 0


    def push(self, x: int) -> None:
        self.lifo_struct.append(x)
        self.lifo_size += 1
        
        

    def pop(self) -> int:
        for _ in range(self.lifo_size -1):
            self.lifo_struct.append(self.lifo_struct.popleft())
        self.lifo_size -= 1
        return self.lifo_struct.popleft()

        

    def top(self) -> int:
        return self.lifo_struct[-1]


        

    def empty(self) -> bool:
        return self.lifo_size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
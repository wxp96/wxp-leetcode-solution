from collections import deque
class MinStack:

    def __init__(self):
        self.stack=deque()
        self.minnum=deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.getMin() or val<self.getMin():
            self.minnum.append(val)
        else:
            self.minnum.append(self.getMin())

    def pop(self) -> None:
        self.stack.pop()
        self.minnum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minnum[-1]
    
m=MinStack()
m.push(-2)
m.push(0)
m.push(-3)
m.pop()
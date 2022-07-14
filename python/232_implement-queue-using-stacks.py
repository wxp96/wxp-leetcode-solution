from collections import deque
class MyQueue:

    def __init__(self):
        self.dq1=deque()
        self.dq2=deque()

    def push(self, x: int) -> None:
        self.dq1.append(x)

    def pop(self) -> int:
        if self.dq2:
            return self.dq2.pop()
        else:
            while self.dq1:
                self.dq2.append(self.dq1.pop())
            return self.dq2.pop()

    def peek(self) -> int:
        return self.dq2[-1] if self.dq2 else self.dq1[0]

    def empty(self) -> bool:
        return False if self.dq1 or self.dq2 else True
from collections import deque
class MyStack:

    def __init__(self):
        self.dq1=deque()
        self.dq2=deque()

    def push(self, x: int) -> None:
        self.dq1.append(x)
        while self.dq2:
            self.dq1.append(self.dq2.popleft())
        self.dq1,self.dq2=self.dq2,self.dq1

    def pop(self) -> int:
        return self.dq2.popleft()

    def top(self) -> int:
        return self.dq2[0]

    def empty(self) -> bool:
        return False if self.dq2 else True


# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
s=MyStack()
s.push(1)
s.push(2)
s.pop()
print(s.empty())
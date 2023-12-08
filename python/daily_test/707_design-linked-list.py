from collections import deque
class MyLinkedList:

    def __init__(self):
        self.dq=deque()

    def get(self, index: int) -> int:
        return self.dq[index]

    def addAtHead(self, val: int) -> None:
        self.dq.appendleft(val)

    def addAtTail(self, val: int) -> None:
        self.dq.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        self.dq.insert(index,val)

    def deleteAtIndex(self, index: int) -> None:
        del self.dq[index]

obj = MyLinkedList()

obj.addAtHead(2)
obj.deleteAtIndex(1)
obj.addAtHead(2)
obj.addAtHead(7)
obj.addAtHead(3)
obj.addAtHead(2)
obj.addAtHead(5)
obj.addAtTail(5)
param_1 = obj.get(5)
obj.deleteAtIndex(6)
obj.deleteAtIndex(4)
# ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
# [[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]
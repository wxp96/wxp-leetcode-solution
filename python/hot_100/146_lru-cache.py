from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.size=0
        self.capacity=capacity
        self.od=OrderedDict()

    def get(self, key: int) -> int:
        if key in self.od.keys():
            self.od.move_to_end(key)
            return self.od[key]
        else:return -1

    def put(self, key: int, value: int) -> None:
        if key in self.od.keys:
            self.od[key]=value
            self.od.move_to_end(key)
        elif self.size<self.capacity:
            self.size+=1
            self.od[key]=value
        elif self.size==self.capacity:
            self.od.popitem(last=False)
            self.od[key]=value
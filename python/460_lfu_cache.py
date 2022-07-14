from collections import defaultdict,OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.k2f=defaultdict(int)
        self.f2kv=defaultdict(OrderedDict)
        self.min_f=0
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key not in self.k2f:
            return -1
        res=self.f2kv[self.k2f[key]][key]
        del self.f2kv[self.k2f[key]][key]
        if not self.f2kv[self.min_f] and self.min_f==self.k2f[key]:
            self.min_f+=1
        self.k2f[key]+=1
        self.f2kv[self.k2f[key]][key]=res
        return res

    def put(self, key: int, value: int) -> None:
        if self.capacity==0:
            return 
        if key not in self.k2f and len(self.k2f)==self.capacity:
            k,v=self.f2kv[self.min_f].popitem(last=False)
            del self.k2f[k]
            self.min_f=1
        elif key not in self.k2f:
            self.min_f=1
        elif key in self.k2f:
            del self.f2kv[self.k2f[key]][key]
            if not self.f2kv[self.min_f] and self.min_f==self.k2f[key]:
                self.min_f+=1
        self.k2f[key]+=1
        self.f2kv[self.k2f[key]][key]=value


# ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]

lfu=LFUCache(2)
lfu.put(3,1)
lfu.put(2,1)
lfu.put(2,2)
lfu.put(4,4)
print(lfu.get(2))
# lfu.put(3,3)
# print(lfu.get(2))
# lfu.put(4,4)
# print(lfu.get(1))
# print(lfu.get(3))
# print(lfu.get(4))
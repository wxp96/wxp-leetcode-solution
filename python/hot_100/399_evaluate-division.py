from typing import List
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def union(p,q,w):
            root_p,wp=find(p)
            root_q,wq=find(q)
            if root_p==root_q:
                return
            parent[root_q]=root_p
            weight[root_q]=wp*w/wq

        def find(x):
            if x not in parent.keys():
                parent[x]=x
                weight[x]=1
            if x!=parent[x]:
                parent[x],w=find(parent[x])
                weight[x]*=w
            else:
                return x,1
            return parent[x],weight[x]
        
        def connected(x,y):
            root_x,wx=find(x)
            root_y,wy=find(y)
            if root_x!=root_y:
                return -1
            else:
                return wy/wx
        
        parent=dict()
        weight=dict()
        for i,(p,q) in enumerate(equations):
            union(p,q,values[i])

        res=[]
        for x,y in queries:
            if x not in parent.keys() or y not in parent.keys():
                res.append(-1)
                continue
            res.append(connected(x,y))
        return res
    
s=Solution()
print(s.calcEquation(equations = [["a","e"],["b","e"]], values = [4.0,3.0], queries = [["a","b"],["e","e"],["x","x"]]))
            
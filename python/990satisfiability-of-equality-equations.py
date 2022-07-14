from typing import List
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        def union(p,q):
            root_p=find(p)
            root_q=find(q)
            if root_p==root_q:
                return 
            parent[root_p]=root_q

        def find(x):
            if x not in parent.keys():
                parent[x]=x
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]

        parent=dict()
        for equation in equations:
            if equation[1]=='=':
                union(equation[0],equation[-1])
        for equation in equations:
            if equation[1]=='!' and find(equation[0])==find(equation[-1]):
                return False
        return True

s=Solution()
print(s.equationsPossible(["f==a","a==b","f!=e","a==c","b==e","c==f"]))
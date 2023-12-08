from typing import List
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        def union(p,q):
            root_p=find(p)
            root_q=find(q)
            if root_p==root_q:
                return 
            parent[root_p]=root_q

        def find(root):
            if root!=parent[root]:
                parent[root]=find(parent[root])
            return parent[root]

        def connected(p,q):
            return find[p]==find[q]

        g=[[] for i in range(n)]
        parent=list(range(n+1))
        for x,y in dislikes:
            g[x-1].append(y-1)
            g[y-1].append(x-1)
        for x,nodes in enumerate(g):
            for y in nodes:
                union(y,nodes[0])
                if connected(x,y):
                    return False
        return True



s=Solution()
print(s.possibleBipartition(4,[[1,2],[1,3],[2,4]]))
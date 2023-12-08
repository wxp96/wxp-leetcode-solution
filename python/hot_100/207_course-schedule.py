from typing import List
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=[0]*numCourses
        edges=defaultdict(list)
        for i,j in prerequisites:
            edges[i].append(j)

        def dfs(k):
            nonlocal valid
            visited[k]=1
            edlist=edges[k]
            for j in edlist:
                if visited[j]==1:
                    valid=False
                elif visited[j]==0:
                    dfs(j)
            visited[k]=2

        valid=True
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        return valid

s=Solution()
print(s.canFinish(2,[[0,1]]))
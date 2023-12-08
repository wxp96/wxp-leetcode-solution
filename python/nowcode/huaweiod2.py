import sys
from collections import deque

def dfs(node):
    if node in memo.keys():
        return memo[node]
    max_length=0
    for i in range(n):
        if i==node:
            continue
        if matrix[node][i]==1:
            max_length=max(max_length,dfs(i))
    memo[node]=max_length+matrix[node][node]
    return memo[node]

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    ans = 0
    matrix=[]
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        matrix.append(values)
    k=int(sys.stdin.readline().strip())-1
    # n=5
    # matrix=[[1 ,0 ,0 ,0 ,0]
    # ,[0 ,2 ,0 ,0 ,0]
    # ,[1 ,1 ,3 ,0 ,0]
    # ,[1 ,1 ,0 ,4 ,0]
    # ,[0 ,0 ,1 ,1 ,5]]
    # k=4
    memo=dict()
    print(dfs(k))

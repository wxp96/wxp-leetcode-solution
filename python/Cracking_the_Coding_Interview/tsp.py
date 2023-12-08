from functools import lru_cache

def tsp(n,array):
    """
    利用动态规划 find_minimum_distance_from12i(s,i)为从0出发经过s中的节点到达i节点的最小距离，
    采用递归并用lru_cache记录状态，时间复杂度是O(n^2 * 2^n) 
    """
    @lru_cache()
    def find_minimum_distance_from12i(s,i):
        if not s:
            return array[0][i]
        ret=float('inf')
        for j in range(1,n):
            if j not in s or j==i or array[j][i]==-1:
                continue
            else:
                ret_tmp=find_minimum_distance_from12i(frozenset(s-{j}),j)
                if ret_tmp!=-1:
                    ret=min(ret_tmp+array[j][i],ret)
        return ret if ret!=float('inf') else -1

    ans=float('inf')
    s=frozenset(range(1,n))
    for i in range(1,n):
        temp=find_minimum_distance_from12i(frozenset(s-{i}),i)
        if temp!=-1:
            ans=min(ans,temp)
        return ans if ans!=float('inf') else -1

print(tsp(5,[[0 ,3 ,6 ,-1 ,1],
[3 ,0 ,2 ,-1 ,4],
[6 ,2 ,0 ,2 ,3],
[-1 ,-1 ,2 ,0 ,1],
[1 ,4 ,3 ,1 ,0]]))
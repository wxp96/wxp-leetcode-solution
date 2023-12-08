from functools import lru_cache
class Solution:
    def numTrees(self, n: int) -> int:

        @lru_cache()
        def numTree_inner(n):
            if n==0 or n==1:
                return 1
            res=0
            for i in range(n):
                ans=1
                ans*=numTree_inner(i)
                ans*=numTree_inner(n-i-1)
                res+=ans
            return res

        return numTree_inner(n)
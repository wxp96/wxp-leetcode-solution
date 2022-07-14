class Solution:
    def numTrees(self, n: int) -> int:
        res=[1,1]
        for i in range(2,n+1):
            num=0
            for j in range((i+1)//2):
                if j==i//2 and i&1:
                    num+=res[j]*res[i-j-1]
                else:
                    num+=(res[j]*res[i-j-1])*2
            res.append(num)
        return res[-1]

s=Solution()
print(s.numTrees(3))
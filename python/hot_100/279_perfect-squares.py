class Solution:
    def numSquares(self, n: int) -> int:
        i=1
        squares=[]
        while i**2<=n:
            squares.append(i**2)
            i+=1
        memo=[0]*n
        for j in range(n):
            for k in squares:
                if j+1-k==0:
                    memo[j]=1
                    break
                elif j+1-k>0 and memo[j-k]!=0:
                    if memo[j]==0:
                        memo[j]=memo[j-k]+1
                    else:
                        memo[j]=min(memo[j-k]+1,memo[j])
        return memo[-1]
    
s=Solution()
print(s.numSquares(1))
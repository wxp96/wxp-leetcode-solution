class Solution:
    def getKthMagicNumber(self, k: int) -> int:

        res=[1]
        candidate=[3,5,7]
        i=j=p=0
        last_3=res[i]*3
        last_5=res[j]*5
        last_7=res[p]*7
        idx=0
        while idx<k-1:
            last=min(last_3,last_5,last_7)
            if last<=res[-1]:
                idx-=1
            else:
                res.append(last)
            if last==last_3:
                i+=1
                last_3=3*res[i]
            elif last==last_5:
                j+=1
                last_5=5*res[j]
            else:
                p+=1
                last_7=7*res[p]
            idx+=1
            
        return res[-1]

s=Solution()
print(s.getKthMagicNumber(11))
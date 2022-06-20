class Solution:
    def addDigits(self, num: int) -> int:
        num_l=list(map(int,str(num)))
        while len(num_l)!=1:
            num=sum(num_l)
            num_l=list(map(int,str(num)))
        return num

s=Solution()
print(s.addDigits(38))
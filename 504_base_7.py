class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return '0'
        l=[]
        sign='-' if num<0 else ''
        num=abs(num)
        while num != 0:
            l.append(num%7)
            num=num//7
        return sign+"".join(map(str,l[::-1]))

s=Solution()
print(s.convertToBase7(100))
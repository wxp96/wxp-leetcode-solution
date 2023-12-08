from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        dq=deque()
        i=0
        while i<len(s):
            if s[i]!=']':
                dq.append(s[i])
            else:
                tmp=[]
                while dq[-1]!='[':
                    tmp.append(dq.pop())
                tmp=''.join(tmp[::-1])
                num=''
                dq.pop()
                while dq and dq[-1].isdigit():
                    num+=dq.pop()
                num=int(num[::-1])
                dq.append(tmp*num)
            i+=1         
        
        return ''.join(dq)
    
s=Solution()
print(s.decodeString('2[2[y]pq4[2[jk]e1[f]]]ef'))

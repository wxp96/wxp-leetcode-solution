from collections import Counter,deque
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ct=Counter(s)
        dq=deque()
        s_set=set()
        for cha in s:
            ct[cha]-=1
            if cha in s_set:
                continue
            while dq and dq[-1]>cha and ct[dq[-1]]>0:
                s_set.remove(dq.pop())
            dq.append(cha)
            s_set.add(cha)
            
        return ''.join(dq)

s=Solution()
print(s.removeDuplicateLetters("abacb"))

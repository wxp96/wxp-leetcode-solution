from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        d={']':'[',')':'(','}':'{'}
        dq=deque()
        for ch in s:
            if ch in d.keys():
                if d[ch]!=dq[-1]:
                    return False
                dq.pop()
            else:
                dq.append(ch)
        return not dq

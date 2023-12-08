from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        # [] {} ()
        dq=deque()
        for cha in s:
            if cha in ('[','{','('):
                dq.append(cha)
            else:
                if not dq:
                    return False
                pre=dq.pop()
                if cha==']' and pre!='[':
                    return False
                if cha=='}' and pre!='{':
                    return False
                if cha==')' and pre!='(':
                    return False
        return True if not dq else False
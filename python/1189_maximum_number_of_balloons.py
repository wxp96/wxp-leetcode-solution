from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c=Counter(text)
        minimum=float("inf")
        for k in ("balon"):
            if k == "l" or k=="o":
                minimum=min(minimum,c.get(k,0)//2)
            else:
                minimum=min(minimum,c.get(k,0))
        return minimum

s=Solution()
print(s.maxNumberOfBalloons("nlaebolko"))
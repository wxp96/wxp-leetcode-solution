class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_l=list(s)
        left=0
        right=len(s)-1
        while left<right:
            while left<right and not s_l[left].isalpha():
                left+=1
            while left<right and not s_l[right].isalpha():
                right-=1
            s_l[left],s_l[right]=s_l[right],s_l[left]
            left+=1
            right-=1
        return "".join(s_l)

s=Solution()
print(s.reverseOnlyLetters("ab-cd"))
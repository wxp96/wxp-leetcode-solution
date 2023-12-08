class Solution:
    def maxScore(self, s: str) -> int:
        left=1 if s[0]=="0" else 0
        right=0
        for c in s[1:]:
            if c=="1":
                right+=1
        max_sum=sum_tmp=left+right
        for c in s[1:]:
            if c=="0":
                sum_tmp+=1
                max_sum=max(max_sum,sum_tmp)
            else:
                sum_tmp-=1
        return max_sum

s=Solution()
print(s.maxScore("011101"))
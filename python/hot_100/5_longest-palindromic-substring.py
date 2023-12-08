# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def inner(i,j):
#             while i>=0 and j<len(s) and s[i]==s[j]:
#                 i-=1
#                 j+=1
#             return i+1,j-1
#         if len(s)==1:
#             return s
#         max_len=0
#         for i in range(len(s)-1):
#             m,n=inner(i,i)
#             single=n-m+1
#             if single>max_len:
#                 max_len=single
#                 res=s[m:n+1]
#             m,n=inner(i,i+1)
#             double=n-m+1
#             if double>max_len:
#                 max_len=double
#                 res=s[m:n+1]
#         return res
class Solution(object):
    def longestPalindrome(self, s):
        res = ''
        for i in range(len(s)):
            start = max(i - len(res) -1, 0)
            temp = s[start: i+1]
            if temp == temp[::-1]:
                res = temp
            else:
                temp = temp[1:]
                if temp == temp[::-1]:
                    res = temp
        return res

s=Solution()
s.longestPalindrome('cccdecbabced')
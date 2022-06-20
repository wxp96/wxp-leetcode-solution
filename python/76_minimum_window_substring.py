from collections import Counter,defaultdict
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         c = Counter(t)
#         d = defaultdict(int)
#         l=r=0
#         min_len=len(s)
#         lost=''
#         def all_char_containted():
#             for key in c.keys():
#                 if d[key] < c[key]:
#                     return False
#             return True

#         while r<len(s) and not all_char_containted():
#                 if s[r] in c.keys():
#                     d[s[r]]+=1
#                 r+=1
#         if not all_char_containted():
#             return ""

#         r-=1
#         res=s[l:r+1]

#         while r < len(s):
#             while l<=r:
#                 if s[l] in c.keys():
#                     d[s[l]]-=1
#                     if d[s[l]]<c[s[l]]:
#                         lost=s[l]
#                         if min_len>r-l+1:
#                             min_len=r-l+1
#                             res=s[l:r+1]
#                         l+=1
#                         break
#                 l+=1
#             while r<len(s):
#                 r+=1
#                 if r<len(s) and s[r] in c.keys():
#                     d[s[r]]+=1
#                     if s[r]==lost:
#                         break
#         return res

class Solution:
       def minWindow(self, s: str, t: str) -> str:
        need=defaultdict(int)
        for c in t:
            need[c]+=1
        needCnt=len(t)
        i=0
        res=(0,float('inf'))
        for j,c in enumerate(s):
            if need[c]>0:
                needCnt-=1
            need[c]-=1
            if needCnt==0:       #步骤一：滑动窗口包含了所有T元素
                while True:      #步骤二：增加i，排除多余元素
                    c=s[i] 
                    if need[c]==0:
                        break
                    need[c]+=1
                    i+=1
                if j-i<res[1]-res[0]:   #记录结果
                    res=(i,j)
                need[s[i]]+=1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt+=1
                i+=1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]

s=Solution()
print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))
                     
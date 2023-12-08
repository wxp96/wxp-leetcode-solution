from collections import Counter,defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c=Counter(t)
        my_c=defaultdict(int)
        i,j=0,0
        valid=0
        min_len=len(s)+1
        res=""
        while j!=len(s):
            while j!=len(s) and valid!=len(c.keys()):
                j+=1
                if s[j-1] in c.keys():
                    my_c[s[j-1]]+=1
                    if my_c[s[j-1]]==c[s[j-1]]:
                        valid+=1
            while i<j and valid==len(c.keys()):
                i+=1
                if s[i-1] in c.keys():
                    my_c[s[i-1]]-=1
                    if my_c[s[i-1]]<c[s[i-1]]:
                        if j-i+1<min_len:
                            min_len=j-i+1
                            res=s[i-1:j]
                        valid-=1
        return res
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        def find_next(needle):
            
            j=0
            for i in range(1,len(needle)):
                while j>0 and needle[i]!=needle[j]:
                    j=next[j-1]
                if needle[i]==needle[j]:
                    j+=1
                next.append(j)
            
        next=[0]
        find_next(needle)
        j=0
        for i in range(len(haystack)):
            while j>0 and haystack[i]!=needle[j]:
                j=next[j-1]
            if haystack[i]==needle[j]:
                j+=1
            if j==len(needle):
                return i-j+1
        return -1

s=Solution()
print(s.strStr("mississippi","issip"))
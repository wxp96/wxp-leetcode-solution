class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d={}
        res=-1
        for i,char in enumerate(s):
            if char not in d.keys():
                d[char]=i
            else:
                res=max(res,i-d[char]-1)
        return res
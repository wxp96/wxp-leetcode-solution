from typing import List
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d={}
        for k,piece in enumerate(pieces):
            d[piece[0]]=k
        i=j=0
        while i<len(arr):
            if arr[i] not in d.keys():
                return False
            else:
                d[pieces[j][0]]=d[arr[i]]
                pieces[j],pieces[d[arr[i]]]=pieces[d[arr[i]]],pieces[j]
            k=0
            while k<len(pieces[j]):
                if arr[i]!=pieces[j][k]:
                    return False
                k+=1
                i+=1
            j+=1
        return True

s=Solution()
print(s.canFormArray([15,85],[[85],[15]]))
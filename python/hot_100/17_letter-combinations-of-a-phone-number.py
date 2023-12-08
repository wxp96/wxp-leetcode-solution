from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def dfs(digits):
            res=[]
            if not digits:
                return []
            first=digits[0]
            next=dfs(digits[1:])
            for ch in phoneMap[first]:
                if not next:
                    res.append(ch)
                else:
                    for st in next:
                        res.append(ch+st)
            return res

        return dfs(digits)


s=Solution()
print(s.letterCombinations("23"))
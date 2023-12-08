from typing import List
from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set=set(wordDict)
        @lru_cache()
        def inner(s):
            if not s:
                return True
            for i in range(len(s)):
                if s[:i+1] in word_set:
                    ret=inner(s[i+1:])
                    if ret:
                        return ret
            return False
        return inner(s)
from typing import List
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=Counter(tasks)
        cnt=c.most_common(1)[0][1]
        return max(cnt*(n-1)+1,len(tasks))
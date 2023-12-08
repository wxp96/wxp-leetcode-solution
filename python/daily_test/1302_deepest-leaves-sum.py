from collections import deque
class Solution:
    def deepestLeavesSum(self, root) -> int:
        d1=deque()
        d2=deque()
        d1.append(root)
        while d1:
            res=0
            while d1:
                cur=d1.pop()
                res+=cur.val
                if cur.left:
                    d2.append(cur.left)
                if cur.right:
                    d2.append(cur.right)
            if not d2:
                return res
            d1,d2=d2,d1
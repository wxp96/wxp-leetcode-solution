from python.lc_utils import TreeNode
from typing import Optional,List
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret=[]
        d1=deque()
        d2=deque()
        if root:
            d1.append(root)
        while d1:
            tmp=[]
            while d1:
                v=d1.popleft()
                tmp.append(v.val)
                if v.left:
                    d2.append(v.left)
                if v.right:
                    d2.append(v.right)
            ret.append(tmp)
            d1,d2=d2,d1
        return ret

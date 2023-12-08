from typing import Optional
from lc_utils import TreeNode
from collections import deque
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        dq=deque()
        dq.append(root)
        pre=None
        while dq:
            cur=dq.pop()
            if cur.right:
                dq.append(cur.right)
                cur.right=None
            if cur.left:
                dq.append(cur.left)
                cur.left=None
            if not pre:
                continue
            pre.right=cur
            pre=cur
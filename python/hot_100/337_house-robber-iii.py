from typing import Optional
from python.lc_utils import TreeNode
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def backtrack(root):
            if not root:
                return 0,0
            lnxt,lnxt2=backtrack(root.left)
            rnxt,rnxt2=backtrack(root.right)
            nxt2=lnxt+rnxt
            nxt=lnxt2+rnxt2+root.val
            return max(nxt,nxt2),nxt2
        
        res=backtrack(root)
        return res[0]
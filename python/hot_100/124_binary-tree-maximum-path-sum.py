from typing import Optional
import sys
sys.path.append(f'D:\code\leetcode\python')
from lc_utils import TreeNode,BinaryTree
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:        
        def inner(root):
            nonlocal res
            if not root:
                return 0
            left=inner(root.left)
            right=inner(root.right)
            cur=root.val
            if left>0:
                cur+=left
            if right>0:
                cur+=right
            res=max(cur,res)
            return max(left,right,0)+root.val
        res=-float('inf')
        inner(root)
        return res
    
s=Solution()
tree=BinaryTree()
root=tree.deserialize_levelorder_lc("[9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]")
s.maxPathSum(root)
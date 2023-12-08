from typing import Optional
import sys
sys.path.append(r'D:\code\leetcode')
from python.lc_utils import TreeNode,BinaryTree
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        res=0
        def inner(root):
            nonlocal res
            if not root:
                return 0
            left=inner(root.left)
            right=inner(root.right)
            tmp=0
            if root.left and root.val==root.left.val:
                left+=1
                tmp+=left
            if root.right and root.val==root.right.val:
                right+=1
                tmp+=right
            res=max(res,tmp)
            return max(left,right)
        
        inner(root)
        return res

tree=BinaryTree()
root=tree.deserialize_levelorder('1 4 5 4 4 5')
s=Solution()
print(s.longestUnivaluePath(root))
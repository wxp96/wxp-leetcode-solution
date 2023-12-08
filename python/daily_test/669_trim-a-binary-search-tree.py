from typing import Optional
import sys
sys.path.append(r'D:\code\leetcode')
from python.lc_utils import TreeNode,BinaryTree
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        parent=TreeNode(0)
        parent.left=root
        ori=parent
        while root:
            if root.val<low:
                root=root.right
                parent.left=root
            else:
                parent=root
                root=root.left
        parent=ori
        root=parent.left
        parent.right=root
        parent.left=None
        while root:
            if root.val>high:
                root=root.left
                parent.right=root
            else:
                parent=root
                root=root.right
        return ori.right 

tree=BinaryTree()
root=tree.deserialize_levelorder_lc('[1,null,2]')
s=Solution()
s.trimBST(root,2,4)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from matplotlib.cbook import flatten
from lc_utils import TreeNode
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root,root
        left,l_bottom=self.flatten(root.left)
        l_bottom=root if not l_bottom else l_bottom
        right,r_bottom=self.flatten(root.right)
        r_bottom=root if not r_bottom else r_bottom
        if left:
            root.left=None
            root.right=left
            if right:
                l_bottom.right=right
            else:
                r_bottom=l_bottom
        return root,r_bottom
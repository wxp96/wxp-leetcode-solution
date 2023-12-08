from typing import Optional
from python.lc_utils import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inner(root,l,r):
            if root.val<=l or root.val>=r:
                return False
            left=right=True
            if root.left:
                left=inner(root.left,l,root.val)
            if root.right:
                right=inner(root.right,root.val,r)
            return left and right
        
        return inner(root,-float('inf'),float('inf'))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from threading import local
from matplotlib.pyplot import get
from python.lc_utils import TreeNode
from typing import Optional
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def get_max_diameter(root):
            nonlocal diameter
            if not root:
                return 0
            l_len=get_max_diameter(root.left)
            r_len=get_max_diameter(root.right)
            diameter=max(diameter,l_len+r_len)
            return max(l_len,r_len)+1

        diameter=0
        get_max_diameter(root)
        return diameter
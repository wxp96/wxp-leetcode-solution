# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

from sklearn import tree
sys.path.append(r'd:\code\leetcode')
from lc_utils import BinaryTree
from collections import deque
class Solution:
    def kthSmallest(self, root, k: int) -> int:

        def search(root):
            nonlocal k
            if not root or k==0:
                return 0
            left=search(root.left)
            k-=1
            if k==0:
                return root.val
            right=search(root.right)
            return left or right

        return search(root)


tree=BinaryTree()
root=tree.deserialize_levelorder('3 1 4 # 2')
s=Solution()
print(s.kthSmallest(root,3))
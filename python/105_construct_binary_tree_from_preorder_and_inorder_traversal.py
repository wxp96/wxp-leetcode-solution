import sys
sys.path.append(r"D:\code\leetcode")
from python.lc_utils import TreeNode
from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def inner(preorder,inorder):
            if not inorder:
                return None
            root=TreeNode(preorder[0])
            i=index[preorder[0]]-index[inorder[0]]
            root.left=self.buildTree(preorder[1:i+1],inorder[:i])
            root.right=self.buildTree(preorder[i+1:len(preorder)],inorder[i+1:])
            return root
        
        index={num:i for i,num in enumerate(inorder)}
        return inner(preorder,inorder)

s=Solution()
s.buildTree([1],[1])
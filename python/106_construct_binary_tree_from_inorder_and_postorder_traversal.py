from lc_utils import TreeNode
from typing import List
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        index={num:i for i,num in enumerate(inorder)}
        def inner(inorder,postorder):
            if not inorder:
                return None
            root=TreeNode(postorder[-1])
            i=index[postorder[-1]]-index[inorder[0]]
            root.left=inner(inorder[:i],postorder[:i])
            root.right=inner(inorder[i+1:-1],postorder[i:-1])
            return root

        return inner(inorder,postorder)

s=Solution()
s.buildTree([1,2],[2,1])

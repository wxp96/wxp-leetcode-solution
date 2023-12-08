import sys
sys.path.append(f'D:\code\leetcode\python')
from lc_utils import TreeNode
from typing import List,Optional
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root=TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i]==preorder[0]:
                left=self.buildTree(preorder[1:i+1],inorder[:i])
                right=self.buildTree(preorder[i+1:],inorder[i+1:])
                root.left=left
                root.right=right
                break
        return root


s=Solution()
s.buildTree([3,9,20,15,7],[9,3,15,20,7])
from python.lc_utils import TreeNode
from typing import Optional,List
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inorder(root):
            if not root:
                return root
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)

        ans=[]
        inorder(root)
        return ans
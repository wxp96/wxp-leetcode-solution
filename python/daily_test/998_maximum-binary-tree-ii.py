from typing import Optional
from python.lc_utils import TreeNode
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        head=TreeNode(101,right=root)
        parent=head
        while root:
            if root.val<val:
                tmp=TreeNode(val)
                tmp.left=root
                parent.right=tmp
                break
            else:#root.val>=val
                if not root.right:
                    tmp=TreeNode(val)
                    root.right=tmp
                    break
                else:
                    parent=root
                    root=root.right
        return head.right
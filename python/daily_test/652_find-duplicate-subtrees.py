from typing import Optional,List
from python.lc_utils import TreeNode
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        memo=set()
        memo1=set()
        res=[]
        def dfs(root):
            if not root:
                return '#'
            left=dfs(root.left)
            right=dfs(root.right)
            tmp=' '.join([str(root.val),left,right])
            if tmp in memo and tmp not in memo1:
                res.append(root)
                memo1.add(tmp)
            else:
                memo.add(tmp)
            return tmp
        dfs(root)
        return res
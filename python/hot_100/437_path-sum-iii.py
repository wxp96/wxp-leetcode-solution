from typing import Optional
import sys
sys.path.append(f'D:\code\leetcode\python')
from lc_utils import TreeNode
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        dd=defaultdict(int)
        dd[0]=1
        res=0
        def recursion(root,curr):
            if not root:
                return
            nonlocal res
            curr+=root.val
            res+=dd[curr-targetSum]
            dd[curr]+=1
            recursion(root.left,curr)
            recursion(root.right,curr)
            dd[curr]-=1
            return 
        
        recursion(root,0)
        return res
    
s=Solution()
s.pathSum(TreeNode(1),0)


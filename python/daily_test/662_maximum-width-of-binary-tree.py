import sys
sys.path.append('D:\\code\\leetcode')
from python.lc_utils import TreeNode,BinaryTree
from typing import Optional
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d1=deque()
        d2=deque()
        d1.append((root,1))
        res=1
        while d1:
            res=max(res,d1[-1][1]-d1[0][1]+1)
            while d1:
                cur,idx=d1.popleft()
                if cur.left:
                    d2.append((cur.left,2*idx))
                if cur.right:
                    d2.append((cur.right,2*idx+1))
            d1,d2=d2,d1
            
        return res

tree=BinaryTree()
root=tree.deserialize_levelorder('1 1 1 1 # 1 # 1 # 1 # 1 # 1 # 1 #')
s=Solution()
print(s.widthOfBinaryTree(root))
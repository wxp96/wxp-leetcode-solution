import sys
sys.path.append(r'd:\code\leetcode')
from lc_utils import BinaryTree
class Solution:
    def isValidBST(self, root) -> bool:

        def inner(root,left_range,right_range):
            res=left=right=True
            if root.val<left_range or root.val>right_range:
                res=False
            if root.left:
                left=inner(root.left,left_range,root.val)
            if root.right:
                right=inner(root.right,root.val,right_range)
            return res and left and right

        return inner(root,-float('inf'),float('inf'))

# [32,26,47,19,null,null,56,null,27]
tree=BinaryTree()
root=tree.deserialize_levelorder('32 26 47 19 # # 56 # 27')
s=Solution()
print(s.isValidBST(root))
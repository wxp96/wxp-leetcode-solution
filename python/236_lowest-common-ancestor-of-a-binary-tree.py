from collections import deque
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        #'''recursion p and q both in tree'''
        # if not root:
        #     return None
        # if root.val==p.val or root.val==q.val:
        #     return root
        # left=self.lowestCommonAncestor(root.left,p,q)
        # right=self.lowestCommonAncestor(root.right,p,q)
        # if left and right:
        #     return root
        # else:
        #     return left or right

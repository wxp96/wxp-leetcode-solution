from lc_utils import TreeNode
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val==p.val or root.val==q.val:
            return root
        left=self.lowestCommonAncestor(root,p,q)
        right=self.lowestCommonAncestor(root,p,q)
        if left and right:
            return root
        elif left or right:
            return left or right
        else:
            return None
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if p.val>q.val:
            p,q=q,p
        while True:
            if root.val>=p.val and root.val<=q.val:
                return root
            elif root.val>p.val and root.val>q.val:
                root=root.left
            elif root.val<p.val and root.val<q.val:
                root=root.right
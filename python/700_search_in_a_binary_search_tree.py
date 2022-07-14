from jmespath import search


class Solution:
    def searchBST(self, root, val: int):
        if not root:
            return None
        if root.val>val:
            return self.searchBST(root.left)
        elif root.val<val:
            return self.searchBST(root.right)
        else:
            return root
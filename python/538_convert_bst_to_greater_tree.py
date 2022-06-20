class Solution:
    def convertBST(self, root):
        val=0

        def inner(root):
            nonlocal val
            if not root:
                return
            inner(root.right)
            val+=root.val
            root.val=val
            inner(root.left)

        inner(root)
        return root
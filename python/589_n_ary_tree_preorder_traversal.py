from typing import List
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def inner(root):
            if not root:
                return None
            ans.append(root.val)
            for child in root.children:
                inner(child)

        ans=[]
        inner(root)
        return ans

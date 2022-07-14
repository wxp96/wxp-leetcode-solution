

class Solution:
    def insertIntoBST(self, root, val: int):
        if not root:
            return TreeNode(val)
        cur=root
        while True:
            if cur.val<val:
                if cur.right:
                    cur=cur.right
                else:
                    cur.right=TreeNode(val)
                    break
            elif cur.val>val:
                if cur.left:
                    cur=cur.left
                else:
                    cur.left=TreeNode(val)
                    break
        return root


# class Solution:
#     def insertIntoBST(self, root, val: int):

#         def insert(root,val):
            
#             if root.val>val:
#                 if not root.left:
#                     node=TreeNode(val)
#                     root.left=node
#                 else:
#                     self.insertIntoBST(root.left,val)
#             elif root.val<val:
#                 if not root.right:
#                     node=TreeNode(val)
#                     root.right=node
#                 else:
#                     self.insertIntoBST(root.right,val)
                    
#         if not root:
#                 return TreeNode(val)
#         insert(root,val)
#         return root
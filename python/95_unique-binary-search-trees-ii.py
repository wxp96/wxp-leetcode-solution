from itertools import permutations
from collections import defaultdict
class Solution:
    def generateTrees(self, n: int):

        def inner(root,val):
            cur=root
            while True:
                if val<cur.val:
                    if not cur.left:
                        cur.left=TreeNode(val)
                        break
                    else:
                        cur=cur.left
                elif val>cur.val:
                    if not cur.right:
                        cur.right=TreeNode(val)
                        break
                    else:
                        cur=cur.right

        def unique_tree(root):
            if not root:
                return '#'
            return ' '.join((str(root.val),unique_tree(root.left),unique_tree(root.right)))

        perms=permutations([i+1 for i in range(n)])
        d=defaultdict(int)
        res=[]
        for perm in perms:
            root=TreeNode(perm[0])
            for num in perm[1:]:
                inner(root,num)
            if d[unique_tree(root)]==0:
                d[unique_tree(root)]+=1
                res.append(root)

        return res
from typing import Optional,List
import sys
sys.path.append(r'd:\code\leetcode')
from python.lc_utils import TreeNode,BinaryTree
from collections import defaultdict,Counter
# class Solution:
#     def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
#         memo=defaultdict(int)
#         res=[]
#         def inner(root):
#             if not root:
#                 return '#'
#             left=inner(root.left)
#             right=inner(root.right)
#             subtree=' '.join((str(root.val),left,right))
#             if memo[subtree]==1:
#                 res.append(root)
#             memo[subtree]+=1
#             return subtree
#         inner(root)
#         return res
class Solution(object):
    def findDuplicateSubtrees(self, root):
        trees = defaultdict()
        trees.default_factory = trees.__len__
        count = Counter()
        ans = []
        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        lookup(root)
        return ans

s=Solution()
tree=BinaryTree()
root=tree.deserialize_levelorder("2 1 1 11 # 11")
s.findDuplicateSubtrees(root)
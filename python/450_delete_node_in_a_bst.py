# Definition for a binary tree node.
import sys
sys.path.append(r'd:\code\leetcode')
from lc_utils import TreeNode,BinaryTree

class Solution:
    def deleteNode(self, root, key: int):
        cur,cur_parent=root,None
        while cur:
            if cur.val<key:
                cur,cur_parent=cur.right,cur
            elif cur.val>key:
                cur,cur_parent=cur.left,cur
            else:
                break
        if not cur:
            return root
        if not cur.left and not cur.right:
            cur=None
        elif not cur.left:
            cur=cur.right
        elif not cur.right:
            cur=cur.left
        else:
            successor,successor_parent=cur.right,cur
            while successor.left:
                successor,successor_parent=successor.left,successor
            if cur==successor_parent:
                successor_parent.right=successor.right
            else:
                successor_parent.left=successor.right
            successor.left=cur.left
            successor.right=cur.right
            cur=successor
        if not cur_parent:
            return cur
        if cur_parent.left and cur_parent.left.val==key:
            cur_parent.left=cur
        else:
            cur_parent.right=cur
        return root




# [5,3,6,2,4,null,7]
# 3
tree=BinaryTree()
root=tree.deserialize_levelorder('5 3 6 2 4 # 7')
s=Solution()
s.deleteNode(root,3)
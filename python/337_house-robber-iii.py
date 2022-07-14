from lc_utils import TreeNode,BinaryTree
class Solution:
    def rob(self, root: TreeNode) -> int:

        def dfs(root):
            if not root:
                return 0,0
            l_nxt,l_nxt_nxt=dfs(root.left)
            r_nxt,r_nxt_nxt=dfs(root.right)
            nxt_nxt=l_nxt+r_nxt
            nxt=max(nxt_nxt,l_nxt_nxt+r_nxt_nxt+root.val)
            
            return nxt,nxt_nxt

        res,_=dfs(root)
        return res           

tree=BinaryTree()
root=tree.deserialize_levelorder("3 4 5 1 3 # 1")
s=Solution()
print(s.rob(root))
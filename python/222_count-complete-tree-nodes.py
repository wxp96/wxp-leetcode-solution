from python.lc_utils import BinaryTree
class Solution:
    def countNodes(self, root) -> int:
        height=0
        cur=root
        while cur:
            cur=cur.left
            height+=1
        
        def count(root,h):
            if not root:
                return 0
            elif h==1:
                return 1
            right=count(root.right,h-1)
            if right<=2**(h-1)-1 and right>2**(h-2)-1:
                return 2**(h-1)+right
            left=count(root.left,h-1)
            return left+right+1

        return count(root,height)

tree=BinaryTree()
root=tree.deserialize_levelorder('1 2 3 4 5 6')
s=Solution()
print(s.countNodes(root))
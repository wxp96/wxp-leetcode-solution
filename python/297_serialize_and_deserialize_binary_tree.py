import sys
sys.path.append(r"d:\code\leetcode")
from lc_utils import TreeNode,BinaryTree
from collections import deque

# class Codec:

    # def serialize(self, root):
    #     """Encodes a tree to a single string.
        
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     if not root:
    #         return '#'
    #     return ' '.join([str(root.val),self.serialize(root.left),self.serialize(root.right)])

    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
        
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     if len(data)==1:
    #         return None
    #     l=data.split(' ')
    #     root_s=deque()
    #     root=TreeNode(int(l[0]))
    #     root_s.append(root)
    #     i=1
    #     while i<len(l):
    #         while l[i]!="#":
    #             left=TreeNode(int(l[i]))
    #             root_s[-1].left=left
    #             root_s.append(left)
    #             i+=1
    #         i+=1
    #         while l[i]=="#":
    #             # if root_s[-1].val==6:
    #             #     print('here')
    #             if i==len(l)-1:
    #                 return root
    #             i+=1
    #             root_s.pop()
    #             while root_s[-1].right:
    #                 root_s.pop()
    #         right=TreeNode(l[i])
    #         root_s[-1].right=right
    #         root_s.append(right)
    #         i+=1
    #     return root
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        d1=deque()
        d2=deque()
        d1.append(root)
        res=[]
        while d1:
            while d1:
                cur=d1.popleft()
                if not cur:
                    res.append('#')
                    continue
                d2.append(cur.left)
                d2.append(cur.right)
                res.append(str(cur.val))
            d1,d2=d2,d1
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=='#':
            return None
        data=data.split(' ')
        d1=deque()
        d2=deque(data)
        root=TreeNode(int(d2.popleft()))
        d1.append(root)
        while d1 and d2:
            cur=d1.popleft()
            if d2[0] != '#':
                left=TreeNode(int(d2.popleft()))
                cur.left=left
                d1.append(left)
            else:
                d2.popleft()
            if d2[0]!='#':
                right=TreeNode(int(d2.popleft()))
                cur.right=right
                d1.append(right)
            else:
                d2.popleft()
        return root

c1=BinaryTree()
c2=Codec()
root=c1.deserialize_preorder('1 2 # # 3 4 # # 5 # #')
data=c2.serialize(root)
print(data)
print(c2.serialize(c2.deserialize("1 2 3 # # 4 5")))
#[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
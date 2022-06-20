from typing import Optional,List
from collections import deque
class LinkedlistNode():
    def __init__(self,x) -> None:
        self.val=x
        self.next=None

class LinkedList():
    def __init__(self,nums) -> None:
        assert isinstance(nums,list),"the input should be list"
        self.nums=nums
        self.length=len(nums)
        self.head=self.list2linkedlist()
        self.print_linkedlist(self.head)

    def list2linkedlist(self):
        if not self.nums:
            return None
        head=pre=LinkedlistNode(self.nums[0])
        for i in range(1,len(self.nums)):
            cur = LinkedlistNode(self.nums[i])
            pre.next=cur
            pre=cur
        return head

    def print_linkedlist(self,head):
        if not head:
            print("null linkedlist")
        else:
            while head:
                print(head.val,end="->")
                head=head.next
            print()
            print(f'length:{self.length}')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left=self.maxDepth(root.left)+1
        right=self.maxDepth(root.right)+1
        return max(left,right)

    def serialize_preorder(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        return ' '.join([str(root.val),self.serialize(root.left),self.serialize(root.right)])

    def deserialize_preorder(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data)==1:
            return None
        l=data.split(' ')
        root_s=deque()
        root=TreeNode(int(l[0]))
        root_s.append(root)
        i=1
        while i<len(l):
            while l[i]!="#":
                left=TreeNode(int(l[i]))
                root_s[-1].left=left
                root_s.append(left)
                i+=1
            i+=1
            while l[i]=="#":
                # if root_s[-1].val==6:
                #     print('here')
                if i==len(l)-1:
                    return root
                i+=1
                root_s.pop()
                while root_s[-1].right:
                    root_s.pop()
            right=TreeNode(l[i])
            root_s[-1].right=right
            root_s.append(right)
            i+=1
        return root

    def serialize_levelorder(self, root):
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

    def deserialize_levelorder(self, data):
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
            if not d2:
                break
            if d2[0]!='#':
                right=TreeNode(int(d2.popleft()))
                cur.right=right
                d1.append(right)
            else:
                d2.popleft()
        return root

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)

    def construct_binary_tree_from_preorder_and_inorder_traversal(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root=TreeNode(preorder[0])
        i=inorder.index(preorder[0])
        root.left=self.construct_binary_tree_from_preorder_and_inorder_traversal(preorder[1:i+1],inorder[:i])
        root.right=self.construct_binary_tree_from_preorder_and_inorder_traversal(preorder[i+1:],inorder[i+1:])
        return root

if __name__=="__main__":
    tree=BinaryTree()
    root=tree.deserialize_levelorder("1 2 3 4 # 2 4 # # 4")
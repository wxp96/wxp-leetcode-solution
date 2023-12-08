import sys
sys.path.append(f'D:\code\leetcode\python')
from lc_utils import TreeNode
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        dq_node=deque()
        dq_val=deque()
        dq_node.append(root)
        dq_val.append(root.val)
        while dq_node:
            node=dq_node.popleft()
            if node.left:
                dq_node.append(node.left)
                dq_val.append(node.left.val)
            else:
                dq_val.append('#')
            if node.right:
                dq_node.append(node.right)
                dq_val.append(node.right.val)
            else:
                dq_val.append('#')
        return ' '.join(map(lambda x:str(x),dq_val))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        dq_val=deque(data.split(' '))
        dq_node=deque()
        val=dq_val.popleft()
        if val=="#":
            return None
        root=TreeNode(val)
        dq_node.append(root)
        while dq_node:
            node=dq_node.popleft()
            left=dq_val.popleft()
            right=dq_val.popleft()
            if left!='#':
                left_node=TreeNode(left)
                node.left=left_node
                dq_node.append(left_node)
            if right!='#':
                right_node=TreeNode(right)
                node.right=right_node
                dq_node.append(right_node)
        return root
    
c=Codec()
root=c.deserialize('1 2 3 # # 4 5 # # # #')
data=c.serialize(root=root)

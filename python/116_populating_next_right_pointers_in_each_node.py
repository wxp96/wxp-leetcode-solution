from collections import deque
class Solution:
    def connect(self, root):
        if not root:
            return root
        d1=deque()
        d2=deque()
        d1.append(root)
        while d1:
            pre=None
            while d1:
                cur=d1.popleft()
                if cur.left:
                    d2.append(cur.left)
                    d2.append(cur.right)
                if not pre:
                    pre=cur
                else:
                    pre.next=cur
                    pre=cur
            d1,d2=d2,d1
        return root
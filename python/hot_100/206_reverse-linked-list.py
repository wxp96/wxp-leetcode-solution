from typing import Optional
import sys
sys.path.append(f'D:\code\leetcode\python')
from lc_utils import LinkedlistNode as ListNode,LinkedList
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        newhead=self.reverseList(head.next)
        head.next.next=head
        # head.next=None
        return newhead

ll=LinkedList([1,2,3,4,5])
s=Solution()
print(s.reverseList(ll.head))
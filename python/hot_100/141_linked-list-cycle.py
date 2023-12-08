from typing import Optional
import sys
sys.path.append(f'D:\code\leetcode\python')
from lc_utils import LinkedList
from lc_utils import LinkedlistNode as ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow=head.next
        if not slow:
            return False
        fast=head.next.next    
        while fast:
            if fast==slow:
                return True
            fast=fast.next
            if not fast:
                return False
            fast=fast.next
            slow=slow.next
        return False

ll=LinkedList([1,2])
ll.head.next.next=ll.head
s=Solution()
s.hasCycle(ll.head)

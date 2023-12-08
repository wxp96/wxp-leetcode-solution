from typing import Optional
from lc_utils import LinkedlistNode as ListNode
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow=head.next
        if not slow:
            return None
        fast=slow.next
        while fast:
            slow=slow.next
            fast=fast.next
            if not fast:
                return None
            fast=fast.next
            if slow==fast:
                slow_2=head
                while slow!=slow_2:
                    slow=slow.next
                    slow_2=slow_2.next
                return slow
        return None 
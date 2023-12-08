from typing import Optional
from lc_utils import LinkedlistNode as ListNode
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast:            
            fast=fast.next
            if fast:
                slow=slow.next
                fast=fast.next
        pre=None
        while slow:
            next=slow.next
            slow.next=pre
            pre=slow
            slow=next
        while pre and head:
            if pre.val!=head.val:
                return False
        return True
        
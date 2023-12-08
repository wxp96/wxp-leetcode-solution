from typing import Optional
from python.lc_utils import LinkedlistNode as ListNode
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        head=ListNode(0)
        head.next=l1
        pre=head
        while l1 and l2:
            s=l1.val+l2.val+carry
            val=s%10
            l1.val=val
            carry=s//10
            pre=l1
            l1=l1.next
            l2=l2.next
        if not l1 and l2:
            l1=l2
            pre.next=l1
        while l1:
            s=l1.val+carry
            val=s%10
            l1.val=val
            carry=s//10
            pre=l1
            l1=l1.next
        if carry:
            node=ListNode(carry)
            pre.next=node
        return head.next

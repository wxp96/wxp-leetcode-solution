from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pre=h1=ListNode(0,list1)
        while list1 and list2:
            if list1.val<=list2.val:
                pre=list1
                list1=list1.next
            else:
                pre.next=list2
                list2=list2.next
                pre=pre.next
                pre.next=list1
        if list2:
            pre.next=list2
        return h1.next

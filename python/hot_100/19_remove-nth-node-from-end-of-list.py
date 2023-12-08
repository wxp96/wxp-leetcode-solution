# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
sys.path.append(r'D:\code\leetcode')
from typing import Optional
from python.lc_utils import LinkedlistNode as ListNode
from python.lc_utils import LinkedList
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pre_node=head
        step_ahead=0
        while step_ahead!=n:
            pre_node=pre_node.next
            step_ahead+=1
        node=head
        if not pre_node:
            return head.next
        while pre_node.next:
            pre_node=pre_node.next
            node=node.next
        node.next=node.next.next
        return head
l=LinkedList([1])
s=Solution()
l.print_linkedlist(s.removeNthFromEnd(l.head,1))
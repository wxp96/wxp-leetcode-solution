import sys
sys.path.append(f'D:\code\leetcode\python')
from typing import Optional
from lc_utils import LinkedlistNode as ListNode,LinkedList
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge_sort(l1,l2):
            if l1 and l2:
                head=l1 if l1.val<l2.val else l2
            else:
                head=l1 or l2
            pre=None
            while l1 and l2:
                if l1.val<l2.val:
                    if not pre:
                        pre=l1
                    else:
                        cur=l1
                        pre.next=cur
                        pre=cur
                    l1=l1.next
                else:
                    if not pre:
                        pre=l2
                    else:
                        cur=l2
                        pre.next=cur
                        pre=cur
                    l2=l2.next
            pre.next=l1 if l1 else l2
            return head


        def divide_sort(head):
            if not head:
                return None
            if not head.next:
                return head
            pre=slow=head
            fast=head
            while fast:
                fast=fast.next
                if fast:
                    fast=fast.next
                    if pre!=slow:
                        pre=pre.next
                    slow=slow.next                    
            pre.next=None
            l1=divide_sort(head)
            l2=divide_sort(slow)
            return merge_sort(l1,l2)


        return divide_sort(head)
    
ll=LinkedList([-1,5,3,4,0])
s=Solution()
head=s.sortList(ll.head)
ll.print_linkedlist(head)

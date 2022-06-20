class Solution:
    def isPalindrome(self, head) -> bool:

        def get_mid_node(head):
            fast=slow=head
            while fast!=None and fast.next!=None:
                fast=fast.next.next
                slow=slow.next
            if fast!=None:
                slow=slow.next
            return slow

        def reverse_linkedlist(head):
            pre=None
            cur=head
            while cur:
                cur.next,pre,cur=pre,cur,cur.next
            return pre

        mid=get_mid_node(head)
        head2=reverse_linkedlist(mid)
        while head and head2:
            if head.val==head2.val:
                head=head.next
                head2=head2.next
            else:
                return False
        return True

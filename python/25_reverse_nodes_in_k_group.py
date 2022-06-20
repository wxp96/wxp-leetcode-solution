from lc_utils import LinkedList
class Solution:
    def reverseKGroup(self, head, k: int):

        def reverse_linkedlist(head,k):
            pre=None
            cur=head
            nxt=cur.next
            i=0
            while i<k:
                cur.next=pre
                if nxt:  
                    pre,cur,nxt=cur,nxt,nxt.next
                else:
                    pre,cur=cur,nxt
                    i+=1
                    break
                i+=1
            head.next=cur
            return pre,head,i

        h,t,i=reverse_linkedlist(head,k)
        if i != k:
            h,t,i=reverse_linkedlist(head,k)
        head=h
        tail=t
        while t.next:
            h,t,i=reverse_linkedlist(t.next,k)
            if i != k:
                h,t,i=reverse_linkedlist(h,k)
                break
            tail.next=h
            tail=t
        return head

ll=LinkedList([1,2,3,4,5,6])
s=Solution()
ll.head=s.reverseKGroup(ll.head,3)
ll.print_linkedlist(ll.head)
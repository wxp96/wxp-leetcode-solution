import sys 
sys.path.append("d:\\code\\leetcode") 
from lc_utils import LinkedList

def reverse_kth_node(head,k):
    pre=None
    cur=head
    nxt=head.next
    i=0
    while i<k:
        cur.next=pre
        if nxt != None:
            pre,cur,nxt=cur,nxt,nxt.next
        else:
            pre,cur=cur,nxt
        i+=1
    head.next=cur
    return pre

ll=LinkedList([1,2,3,4,5])
ll.head=reverse_kth_node(ll.head,5)
ll.print_linkedlist(ll.head)
from typing import List,Optional
from python.lc_utils import LinkedlistNode as ListNode
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tmp=[]
        for node in lists:
            while node:
                heapq.heappush(tmp,node.val)
                node=node.next
        head=cur=ListNode(0)
        while tmp:
            val=heapq.heappop(tmp)
            nxt=ListNode(val)
            cur.next=nxt
            cur=nxt
        return head.next
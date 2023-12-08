import math
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        countA=countB=0
        nodea=headA
        nodeb=headB
        while nodea:
            countA+=1
            nodea=nodea.next
        while nodeb:
            countB+=1
            nodeb=nodeb.next
        if countA>countB:
            ahead=countA-countB
            nodea=headA
            nodeb=headB
        else:
            ahead=countB-countA
            nodea=headB
            nodeb=headA
        while ahead:
            nodea=nodea.next
            ahead-=1
        while nodea:
            if nodea is nodeb:
                return nodea
            nodea=nodea.next
            nodeb=nodeb.next
        return None
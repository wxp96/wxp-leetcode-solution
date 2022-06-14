class LinkedlistNode():
    def __init__(self,x) -> None:
        self.val=x
        self.next=None

class LinkedList():
    def __init__(self,nums) -> None:
        assert isinstance(nums,list),"the input should be list"
        self.nums=nums
        self.length=len(nums)
        self.head=self.list2linkedlist()
        self.print_linkedlist(self.head)

    def list2linkedlist(self):
        if not self.nums:
            return None
        head=pre=LinkedlistNode(self.nums[0])
        for i in range(1,len(self.nums)):
            cur = LinkedlistNode(self.nums[i])
            pre.next=cur
            pre=cur
        return head

    def print_linkedlist(self,head):
        if not head:
            print("null linkedlist")
        else:
            while head:
                print(head.val,end="->")
                head=head.next
            print()
            print(f'length:{self.length}')


if __name__=="__main__":
    l=LinkedList([1,2,3,4,5])
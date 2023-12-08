package main

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	node := head
	node1 := &ListNode{0, head}
	node2 := node1
	for n > 0 {
		node = node.Next
		n -= 1
	}
	for node != nil {
		node = node.Next
		node1 = node1.Next
	}
	node1.Next = node1.Next.Next
	return node2.Next
}

func main() {
	head := createLinkedList([]int{1})
	removeNthFromEnd(head, 1)
	head.printLinkedList()
}

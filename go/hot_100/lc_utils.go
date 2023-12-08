package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func createLinkedList(arr []int) *ListNode {
	pre := &ListNode{0, nil}
	head := pre
	for _, num := range arr {
		node := &ListNode{num, nil}
		pre.Next = node
		pre = node
	}
	return head.Next
}

func (head *ListNode) printLinkedList() {
	length := 0
	for head != nil {
		fmt.Printf("%v->", head.Val)
		head = head.Next
		length += 1
	}
	fmt.Println()
	fmt.Printf("length: %v\n", length)
}

// func main() {
// 	head := createLinkedList([]int{1, 2, 3, 4})
// 	head.printLinkedList()
// }

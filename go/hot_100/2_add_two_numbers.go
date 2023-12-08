package main

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	head := l1
	remain := 0
	jinwei := 0
	var pre *ListNode
	for l1 != nil && l2 != nil {
		remain = (l1.Val + l2.Val + jinwei) % 10
		jinwei = (l1.Val + l2.Val + jinwei) / 10
		l1.Val = remain
		pre = l1
		l1 = l1.Next
		l2 = l2.Next
	}
	if l1 == nil && l2 != nil {
		pre.Next = l2
		l1 = l2
	} else if l1 == nil && l2 == nil {
		if jinwei != 0 {
			pre.Next = &ListNode{jinwei, nil}
		} else {
			return head
		}
	}
	for jinwei != 0 {
		if l1 != nil {
			remain = (l1.Val + jinwei) % 10
			jinwei = (l1.Val + jinwei) / 10
			pre = l1
			l1.Val = remain
			l1 = l1.Next
		} else {
			pre.Next = &ListNode{jinwei, nil}
			jinwei = 0
		}
	}
	return head
}

// func main() {
// 	l1 := ListNode{3, nil}
// 	l3 := ListNode{7, nil}
// 	// l5 := ListNode{4, nil}
// 	// l7 := ListNode{9, nil}
// 	l1.Next = &l3
// 	// l3.Next = &l5
// 	// l5.Next = &l7
// 	l2 := ListNode{9, nil}
// 	l4 := ListNode{2, nil}
// 	// l6 := ListNode{9, nil}
// 	l2.Next = &l4
// 	// l4.Next = &l6
// 	addTwoNumbers(&l2, &l1)
// }

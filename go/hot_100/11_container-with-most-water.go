package main

func maxArea(height []int) int {
	l, r := 0, len(height)-1
	maxA := 0
	for l != r {
		if height[l] <= height[r] {
			maxA = Max(maxA, height[l]*(r-l))
			l += 1
		} else {
			maxA = Max(maxA, height[r]*(r-l))
			r -= 1
		}
	}
	return maxA
}

// func main() {
// 	maxArea([]int{1, 8, 6, 2, 5, 4, 8, 3, 7})
// }

package main

import "math"

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	m := len(nums1)
	n := len(nums2)
	if m > n {
		return findMedianSortedArrays(nums2, nums1)
	}
	left, right := 0, m
	for left <= right {
		i := (left + right) / 2
		j := (m+n+1)/2 - i
		if i != 0 && nums1[i-1] > nums2[j] {
			right = i - 1
		} else if i != m && nums2[j-1] > nums1[i] {
			left = i + 1
		} else {
			var max_left, min_right int
			if i == 0 {
				max_left = nums2[j-1]
			} else if j == 0 {
				max_left = nums1[i-1]
			} else {
				max_left = int(math.Max(float64(nums1[i-1]), float64(nums2[j-1])))
			}
			if (m+n)%2 == 1 {
				return float64(max_left)
			}
			if i == m {
				min_right = nums2[j]
			} else if j == n {
				min_right = nums1[i]
			} else {
				min_right = int(math.Min(float64(nums1[i]), float64(nums2[j])))
			}
			return float64(max_left+min_right) / 2
		}
	}
	return 0.0
}

// func main() {
// 	findMedianSortedArrays([]int{1, 3}, []int{2, 7})
// }

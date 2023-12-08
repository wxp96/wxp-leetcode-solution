package main

import "sort"

func threeSum(nums []int) [][]int {
	hashmap := make(map[int][]int)
	var res [][]int
	sort.Ints(nums)
	for i, v := range nums {
		if _, ok := hashmap[v]; ok {
			hashmap[v] = append(hashmap[v], i)
		} else {
			hashmap[v] = []int{i}
		}
	}
	for i := 0; i < len(nums); {
		for j := i + 1; j < len(nums); {
			if arr, ok := hashmap[-nums[i]-nums[j]]; ok {
				for _, k := range arr {
					if k > i && k > j {
						res = append(res, []int{nums[i], nums[j], nums[k]})
						break
					}
				}
			}
			j++
			for j < len(nums) && nums[j] == nums[j-1] {
				j++
			}
		}
		i++
		for i < len(nums) && nums[i] == nums[i-1] {
			i++
		}
	}
	return res
}

// func main() {
// 	threeSum([]int{0, 0, 0, 0})
// }

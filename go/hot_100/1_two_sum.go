package main

func twoSum(nums []int, target int) []int {
	dict := map[int]int{}
	for i, v := range nums {
		if j, ok := dict[target-v]; ok {
			return []int{i, j}
		}
		dict[v] = i
	}
	return nil
}

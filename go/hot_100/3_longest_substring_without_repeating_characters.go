package main

func Max(a int, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}

func lengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	}
	a, b, res := 0, 0, 1
	count := make(map[byte]int)
	count[s[b]] = 0
	for b < len(s)-1 {
		b++
		v, ok := count[s[b]]
		if ok {
			for a <= v {
				delete(count, s[a])
				a++
			}
		}
		count[s[b]] = b
		res = Max(res, b-a+1)
	}
	return res
}

// func main() {
// 	lengthOfLongestSubstring("abcabcbb")
// }

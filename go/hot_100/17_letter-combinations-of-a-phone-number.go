package main

// func main() {
// 	letterCombinations("23")
// }
func letterCombinations(digits string) []string {
	dict := map[string]string{
		"2": "abc",
		"3": "def",
		"4": "ghi",
		"5": "jkl",
		"6": "mno",
		"7": "pqrs",
		"8": "tuv",
		"9": "wxyz",
	}
	var res []string
	for _, v := range digits {
		tmp := make([]string, 0)
		for _, char := range dict[string(v)] {
			for _, item := range res {
				tmp = append(tmp, item+string(char))
			}
			if res == nil {
				tmp = append(tmp, string(char))
			}
		}
		res = tmp
	}
	return res
}

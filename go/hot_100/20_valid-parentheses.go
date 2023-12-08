package main

func isValid(s string) bool {
	slice := []string{}
	for _, v := range s {
		if string(v) == "{" || string(v) == "[" || string(v) == "(" {
			slice = append(slice, string(v))
		} else {
			if len(slice) == 0 {
				return false
			}
			pre := slice[len(slice)-1]
			if string(v) == ")" && pre != "(" || string(v) == "]" && pre != "[" || string(v) == "}" && pre != "{" {
				return false
			}
			slice = slice[:len(slice)-1]
		}
	}
	return len(slice) == 0
}

package main

type keys struct {
	slen int
	plen int
}

// func match(s string,p string) bool{
// 	if s==nil && p==nil{
// 		return true
// 	}else if p==nil{
// 		return false
// 	}
// 	res:=false
// 	if s[0]==p[0] || p[0]=="."{
// 		if len(p)>1 && p[1]=="*"{
// 			res=match(s[1:],p[:])||match(s[1:],p[2:])||match(s[:],p[2:])
// 		}else{
// 			res=match(s[1:],p[1:])
// 		}
// 	}
// 	return res
// }

func isMatch(s string, p string) bool {
	memo := make(map[keys]bool)
	var match func(i int, j int) bool
	match = func(i int, j int) bool {
		v, ok := memo[keys{i, j}]
		if ok {
			return v
		}
		if i == len(s) && j == len(p) {
			return true
		} else if j == len(p) {
			return false
		}
		res := false
		if i < len(s) && (s[i] == p[j] || string(p[j]) == ".") {
			if j < len(p)-1 && string(p[j+1]) == "*" {
				res = match(i+1, j) || match(i+1, j+2) || match(i, j+2)
			} else {
				res = match(i+1, j+1)
			}
		} else if j < len(p)-1 && string(p[j+1]) == "*" {
			res = match(i, j+2)
		}
		memo[keys{i, j}] = res
		return res
	}
	return match(0, 0)
}

// func main() {
// 	isMatch("a", "ab*")
// }

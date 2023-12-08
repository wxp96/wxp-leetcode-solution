package main

func MaxLength(i int,s string) (int,int,int){
	single,double:=1,0
	m,n:=i,i+1
	for j:=1;i+j<len(s)&&i-j>=0&&s[i+j]==s[i-j];j++{
		single+=2
		m-=1
		n+=1
	}
	if i!=len(s)-1 && s[i]==s[i+1]{
		double=2
		l,r:=i,i+2
		for j:=1;i+j+1<len(s)&&i-j>=0&&s[i+j+1]==s[i-j];j++{
			double+=2
			l-=1
			r+=1
		}
		if double>single{
			return double,l,r
		}
	}
	
	return single,m,n
}

func longestPalindrome(s string) string {
	length:=0
	var res string
	for i, _ := range s {
		nowLen,x,y:=MaxLength(i,s)
		if nowLen>length{
			res=s[x:y]
			length=nowLen
		}
	}
	return res
}

// func main(){
// 	longestPalindrome("babad")
// }
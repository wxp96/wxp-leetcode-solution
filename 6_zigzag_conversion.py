class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        i=1
        s_list=["" for j in range(numRows)]
        s_list[0]+=s[0]
        while i<len(s):
            if not ((i-1)//(numRows-1))%2:
                s_list[(i-1)%(numRows-1)+1]+=s[i]
            else:
                s_list[(numRows-2)-(i-1)%(numRows-1)]+=s[i]
            i+=1
        return "".join(s_list)


s=Solution()
print(s.convert("PAYPALISHIRING",3))
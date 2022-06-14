class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes=list(dominoes)
        if len(dominoes)==1:
            return dominoes
        left=0
        right=1
        while left < len(dominoes):
            while right<len(dominoes) and dominoes[right]==".":
                right+=1
            if right>=len(dominoes):
                if dominoes[left] =="R":
                    while left<len(dominoes):
                        dominoes[left]="R"
                        left+=1
                break
            if dominoes[left]==dominoes[right] or dominoes[left]=="." and dominoes[right]=="L":
                while left<right:
                    dominoes[left]=dominoes[right]
                    left+=1
                if dominoes[right]!="R":
                    left+=1
                right=left+1
            elif dominoes[right]=="R":
                left=right
                right+=1
            elif dominoes[left]=="R" and dominoes[right]=="L":
                mid=(right+left)//2
                if (right-left)%2:
                    dominoes[mid]="R"
                while left<mid:
                    dominoes[left]="R"
                    left+=1
                left=mid+1
                while left<right:
                    dominoes[left]="L"
                    left+=1
                right+=2
                left+=1
        return "".join(dominoes)

s=Solution()
print(s.pushDominoes(".L.R...LR..L.."))
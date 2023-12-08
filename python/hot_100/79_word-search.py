from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i,j,cur_len):
            if cur_len==len(word)-1:
                if board[i][j]==word[-1]:
                    return True
                else:
                    return False
            res=False
            tmp=board[i][j]
            board[i][j]='-1'
            for x,y in movement:
                new_i,new_j=i+x,j+y
                if 0<=new_i<len(board) and 0<=new_j<len(board[0]) and board[new_i][new_j]==word[cur_len+1]:  
                    res=backtrack(new_i,new_j,cur_len+1)
                    if res:
                        return res
            board[i][j]=tmp
            return res


        movement=[(-1,0),(0,-1),(1,0),(0,1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    res=backtrack(i,j,0)
                    if res:
                        return res
        return False


s=Solution()
print(s.exist([["a","a"]],'aaa'))
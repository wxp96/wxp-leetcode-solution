from typing import List
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_len=max(trips,key=lambda x:x[2])[2]
        trip_line=[0]*(max_len+1)
        for num,i,j in trips:
            trip_line[i]+=num
            trip_line[j]-=num
        if trip_line[0]>capacity:
            return False
        for i,item in enumerate(trip_line[1:],1):
            trip_line[i]+=trip_line[i-1]
            if trip_line[i]>capacity:
                return False
        return True

s=Solution()
print(s.carPooling([[2,1,5],[3,5,7]],3))
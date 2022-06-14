from typing import List
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        b_list=[0]*(n+1)
        for i,j,k in bookings:
            b_list[i-1]+=k
            b_list[j]-=k
        res=[b_list[0]]
        for i,num in enumerate(b_list[1:-1],1):
            res.append(res[-1]+num)
        return res
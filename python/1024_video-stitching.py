from typing import List
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # clips=sorted(clips,key=lambda x:(x[0],-x[1]))
        # if clips[0][0]!=0: return -1
        # pre_e=clips[0][1]
        # next=pre_e
        # if next>=time:
        #     return 1
        # res=1
        # i=1
        # while i<len(clips) and clips[i][0]<=pre_e:
        #     while i<len(clips) and clips[i][0]<=pre_e:
        #         next=max(next,clips[i][1])
        #         i+=1
        #     res+=1
        #     pre_e=next
        #     if next>=time:
        #         return res

        # return -1
        memo=[0]*time
        for start,end in clips:
            memo[start]=max(memo[start],end)
        res=pre=last=0
        for t in range(time):
            last=max(last,memo[t])
            if last==t:
                return -1
            if t==pre:
                res+=1
                pre=last
        return res


s=Solution()
# print(s.videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],9))
# print(s.videoStitching([[0,2],[1,6],[3,10]],10))
# print(s.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]],10))
# print(s.videoStitching([[5,7],[1,8],[0,0],[2,3],[4,5],[0,6],[5,10],[7,10]],5))
# print(s.videoStitching([[17,18],[25,26],[16,21],[3,3],[19,23],[1,5],[0,2],[9,20],[5,17],[8,10]],15))
# print(s.videoStitching([[0,0],[9,9],[2,10],[0,3],[0,5],[3,4],[6,10],[1,2],[4,7],[5,6]],5))
print(s.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]],10))


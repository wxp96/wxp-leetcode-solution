import sys
import bisect
from collections import defaultdict,deque
# metrix=[]
# for line in sys.stdin:
#     metrix.append(list(map(int,line.split())))
metrix=[[1 ,3 ,5 ,1]
,[2 ,1 ,5 ,10]
,[3 ,2 ,7 ,12]
,[4 ,3 ,2 ,20]
,[5 ,4 ,9 ,21]
,[6 ,4 ,2 ,22]]
id2inf={}
sortedw=[]
w2id=defaultdict(deque)
pre_d=0
for i,(id,w,s,a) in enumerate(metrix):
    if i!=0 and (pre_d<=a or pre_d>a and w<=pre_w):
        print(pre_id,pre_d)
        del id2inf[pre_id]
        if not w2id[pre_w]:
            sortedw=sortedw[:-1]
    elif i!=0 and (pre_d>a and w>pre_w):
        id2inf[pre_id]=[pre_d-a,a]
        if pre_w not in sortedw:
            bisect.insort_left(sortedw,pre_w)
        w2id[pre_w].appendleft(pre_id)
    if pre_d>a and w<=pre_w:
        a=pre_d

    id2inf[id]=[s,a]
    if w not in sortedw:
        bisect.insort_left(sortedw,w)
    w2id[w].append(id)
    pre_w=sortedw[-1]
    pre_id=w2id[pre_w].popleft()
    pre_s,pre_a=id2inf[pre_id]
    pre_d=a+pre_s
print(pre_id,pre_d)
if not w2id[w]:
    sortedw=sortedw[:-1]

while sortedw:
    w=sortedw[-1]
    id=w2id[w].popleft()
    s,a=id2inf[id]
    pre_d=pre_d+s
    print(id,pre_d)
    if not w2id[w]:
        sortedw=sortedw[:-1]

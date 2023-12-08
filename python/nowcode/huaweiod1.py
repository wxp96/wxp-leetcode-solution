import sys
from collections import Counter
for i,line in enumerate(['1','1 2 2 4 2 1 1 1']):
    if i==0:
        continue
    line=list(map(int,line.split()))
    c=Counter(line)
    longest=[]
    max_length=0
    for num in c.keys():
        if c[num]>max_length:
            max_length=c[num]
            longest=[num]
        elif c[num]==max_length:
            longest.append(num)
    line=''.join(map(str,line))
    result=len(line)
    for num in longest:
        l=line.find(str(num))
        r=line.rfind(str(num))
        if r-l+1<result:
            result=r-l+1
print(result)


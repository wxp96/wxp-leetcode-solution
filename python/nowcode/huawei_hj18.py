import sys

result_l=[0]*7
right_yanma=[255]
i=0
while i!=8:
    right_yanma.append(right_yanma[-1]-2**i)
    i+=1
for line in ["42.53.252.112~255.0.0.0","166.237.7.68~255.0.0.0","136.3.73.64~255.255.0.0","204.29.136.133~255.255.0.245","195.30.208.94~255.255.0.213","154.253.86.183~255.200.255.0","94.164.187.131~255.255.0.0","167.79.164.186~255.0.0.0","194.172.2.64~255.255.0.0","210.212.79.137~255.255.255.42","143.151.137.40~255.255.255.255","184.145.79.157~255.0.0.0","100.214.131.51~255.255.255.255","233.10.182.98~255.0.0.125","99.184.165.228~255.0.0.82","92.20.159.86~255.0.0.0","198.198.174.83~255.0.0.0","17.158.122.89~255.255.75.255","149.253.103.237~255.0.26.0","91.243.182.7~255.0.0.0","36.76.55.4~255.255.255.255","126.54.86.143~255.0.0.0"]:
'    mark=-1
    a = line.split('~')
    try:
        ip=list(map(int,a[0].split('.')))
        ziwangyanma=list(map(int,a[1].split('.')))
    except ValueError:
        result_l[5]+=1
        continue
    if ip[0] in (0,127):
        continue
    start_0=False
    for yanma_num in ziwangyanma:
        if yanma_num not in right_yanma:
            mark=0
            break
        if start_0==True and yanma_num !=0:
            mark=0
            break
        if yanma_num!=255:
            start_0=True
    if mark==0 or ziwangyanma[-1]==255:
        result_l[5]+=1
        continue
    for i,ip_num in enumerate(ip[::-1]):
        if ip_num>255 or ip_num<0:
            result_l[5]+=1
            break
        if i==3:
            if 1<=ip_num<=126:
                result_l[0]+=1
            elif 128<=ip_num<=191:
                result_l[1]+=1
            elif 192<=ip_num<=223:
                result_l[2]+=1
            elif 224<=ip_num<=239:
                result_l[3]+=1
            elif 240<=ip_num<=255:
                result_l[4]+=1
            if ip[0]==10 or ip[0]==172 and 16<=ip[1]<=31 or ip[0]==192 and ip[1]==168:
                result_l[6]+=1
print(' '.join(map(str,result_l)))'
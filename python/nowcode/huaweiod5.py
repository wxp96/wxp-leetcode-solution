import sys
import bisect
if __name__ == "__main__":
    # 读取第一行的n
    m,n = list(map(int,sys.stdin.readline().strip().split()))
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = sorted(list(map(int, line.split())))
    left=n-1
    result=0
    for i,value in enumerate(values):
        if i>=left:
            break
        left=bisect.bisect_right(values,m-value)-1
        if left<=i:
            break
        result+=1
    result=n-result
    print(result)


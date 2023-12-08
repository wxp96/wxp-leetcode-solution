def func(s):
    def inner(i,j):
        length=0
        while i>=0 and j<len(s) and s[i]==s[j]:
            length+=2
            i-=1
            j+=1

        return length

    res=1
    for i in range(len(s)-1):
        res=max(res,inner(i,i)-1)
        res=max(res,inner(i,i+1))
    return res

print(func('abcbd'))
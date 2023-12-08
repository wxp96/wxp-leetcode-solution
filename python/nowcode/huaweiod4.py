import sys
if __name__ == "__main__":
    # 读取第一行的n
    sentence = sys.stdin.readline().strip().split()
    for i,word in enumerate(sentence):
        j=0
        while j<len(word) and word[-j-1] in (',','.','?'):
            j+=1
        if j!=0:
            word=word[-j:]+word[:-j]
            sentence[i]=word[::-1]
        else:
            sentence[i]=word[::-1]
    print(' '.join(sentence))

from collections import Counter
if __name__=='__main__':
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(input())
    cnt=Counter(arr)
    print(len(cnt))
    for i in cnt.values():
        print(i, end=' ')

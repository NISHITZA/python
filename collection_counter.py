from collections import Counter

if __name__=='__main__':
    n=int(input())
    arr=[]
    arr=list(map(int,input().split(' ')))
    cnt=Counter(arr)
    m=int(input())
    amt=0
    for i in range(m):
        size,price=input().split(' ')
        size=int(size)
        price=int(price)
        if(cnt[size]!=0):
            amt=amt+price
            cnt.subtract({size:1})
        else:
            amt=amt+0

    print(amt)
    


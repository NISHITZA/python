from collections import deque
if(__name__=='__main__'):
    n=int(input())
    d=deque()
    for _ in range(n):
        res=input().split(' ')
        rem=res[0]
        if(rem=='append'):
            val=res[-1]
            val=int(val)
            d.append(val)
        if(rem=='appendleft'):
            val=res[-1]
            val=int(val)
            d.appendleft(val)
        if(rem=='pop'):
            d.pop()
        if(rem=='popleft'):
            d.popleft()

    for i in d:
        print(i,end=' ')

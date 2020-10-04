if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    n=list(arr)
    n.sort()
    val=0
    m=n[len(n)-1]
    for i in n:
        if(i!=m):
            val=i
    
    print(val)       
    

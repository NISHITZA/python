if __name__=='__main__':
    n=int(input())
    s=set()
    for _ in range(n):
        val=input()
        s.add(val)
    print(len(s))

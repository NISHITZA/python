from itertools import permutations
if __name__=='__main__':
    val,n=input().split(' ')
    n=int(n)
    per=list(permutations(val,n))
    per.sort()
    for i in per:
        print(''.join(i))


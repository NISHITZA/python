def average(array):
    # your code goes here
    n=set(array)
    avg=sum(n)/len(n)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

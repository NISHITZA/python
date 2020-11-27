import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    mins=0
    maxs=0
    arr.sort()
    for i,j in enumerate(arr):
        if(i!=0):
            maxs=maxs+j
        if(i!=4):
            mins=mins+j
    print(mins,maxs)
    
    
    
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

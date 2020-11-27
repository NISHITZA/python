#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(cal):
    total=0
    cal.sort(reverse=True)
    for i in range(0,len(cal)):
        print(i,cal[i])
        total = total + cal[i]*(math.pow(2,i))
    
    return int(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()

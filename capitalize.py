#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    n=s.split(' ')
    m=''
    for i in n:
        m=m+i.capitalize()+' '
    return m

if __name__ == '__main__':

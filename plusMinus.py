#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import Decimal

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    p,n,z = 0, 0, 0
    
    for i in arr:
        if i > 0: 
            p += 1
        elif i < 0:
            n += 1
        else:
            z += 1
            
    print ( round(Decimal(p)/ Decimal(p+n+z), 6))
    print ( round(Decimal(n)/ Decimal(p+n+z), 6))
    print ( round(Decimal(z)/ Decimal(p+n+z), 6))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

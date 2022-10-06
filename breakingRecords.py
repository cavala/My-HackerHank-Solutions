#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    qtMin, qtMax = 0 , 0
    nmin, nmax = scores[0], scores[0]
    for score in scores:
        if score > nmax:
            nmax = score
            qtMax += 1
        
        if score < nmin:
            nmin = score
            qtMin += 1
            
    return [qtMax, qtMin]
            
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

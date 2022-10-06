#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, la, lo, apples, oranges):
    #  s: integer, starting point of Sam's house location.
    #  t: integer, ending location of Sam's house location.
    #  la: integer, location of the Apple tree.
    #  lo: integer, location of the Orange tree.
    #  apples: integer array, distances at which each apple falls from the tree.
    #  oranges: integer array, distances at which each orange falls from the tree.
    a, o = 0 , 0
    for apple in apples:
        if (apple + la) >= s and (apple + la) <= t:
            a += 1
    
    for orange in oranges:
        if (orange + lo) >= s and (orange +lo) <= t:
            o += 1
    print(a)
    print(o)
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

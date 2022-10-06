#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#

from collections import defaultdict

def processLogs(logs, threshold):
    #user_map = {}
    #for log in logs:
    #    log_arr = log[0].split(" ")        
    #    user_map[log_arr[0]] = user_map.get(log_arr[0],0) + 1
    #    if len(log_arr) > 1:
    #        user_map[log_arr[1]] = user_map.get(log_arr[1],0) + 1
        
    #target_users = []    
    #for k, v in user_map.items():
    #    if v >= threshold:
    #        target_users.append(str(k))
   
    #for i in sorted(target_users):
    #    print(str(i))
    res = []
    dict = defaultdict(int)
    for each_rows in logs:
        row = ''.join(each_rows)
        temp = row.split()
        if temp[0] != temp[1]:
            dict[temp[1]] += 1
        dict[temp[0]] += 1

    for key, val in dict.items():
        if val >= threshold:
            #res.append(key)
            print(key)
    #return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    logs_count = int(raw_input().strip())

    logs = []

    for _ in xrange(logs_count):
        logs_item = raw_input()
        logs.append(logs_item)

    threshold = int(raw_input().strip())

    result = processLogs(logs, threshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

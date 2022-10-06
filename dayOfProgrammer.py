#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):    
    if year >= 1700 and year <= 2700:
        isleapYear = False
        if year >= 1918:
            isleapYear = (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))        
        else:
            isleapYear = (year % 4 == 0)
        
        if year == 1918:
            return ('26.09.'+str(year))
        else:
            if isleapYear:
                return ('12.09.'+str(year))
            # is not a leap year    
            else:
                return ('13.09.'+str(year))
    else:
        raise Exception ('Year must be in 1700 and 2700')
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

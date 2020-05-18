#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    num_valleys = 0        # number of valleys
    level = 0              # starts at sea level
    for d in s:
        if d == 'U':       # going upslope
            level += 1
        else:              # going downslope
            if level == 0:
                num_valleys += 1
            level -= 1
    return num_valleys
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
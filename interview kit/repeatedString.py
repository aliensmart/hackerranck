#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    print(s.count("a"))
    input()
    print(s[:n % len(s)])
    input()
    print(n % len(s))
    input()
    print(s[:n % len(s)].count("a"))
    input()
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")

s = 'akna'
n = 10
print(repeatedString(s,n))


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     n = int(input())

#     result = repeatedString(s, n)

#     fptr.write(str(result) + '\n')

#     fptr.close()
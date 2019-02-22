import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    rev = list()
    for i in reversed(arr):
        rev.append(i)
    A = " ".join(str(x) for x in rev)
    print(A)

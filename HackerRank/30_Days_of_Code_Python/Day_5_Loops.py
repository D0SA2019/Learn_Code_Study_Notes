# Given an integer,`n` , print its first 10 multiples. Each multiple `n x i` (where 1 <= i <= 10 ) should be printed on a new line in the form: n x i = result.

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Enter a number: "))

    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(n, "x", i, "=", (n*i))

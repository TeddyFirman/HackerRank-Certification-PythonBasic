#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def missingCharacters(s):
    # Write your code here
    MAX_CHAR = 26
    
    x = [False for i in range(MAX_CHAR)]
    y = []
    

    for i in range(len(s)):
        if (s[i] >= 'a' and s[i] <= 'z'):
            x[ord(s[i]) - ord('a')] = True
        if (s[i].isdigit()):
            y.append(int(s[i]))
        
    
    result = "".join(str(x) for x in range(10) if x not in y)

    for i in range(MAX_CHAR):
        if (x[i] == False):
          result += chr(i + ord('a'))
        
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()

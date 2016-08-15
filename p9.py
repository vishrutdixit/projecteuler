# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if(a+b+c == 1000):
                list = [a,b,c]
                sorted_list = sorted(list)
                if(math.pow(sorted_list[0], 2) + math.pow(sorted_list[1], 2) == math.pow(sorted_list[2], 2)):
                    print a*b*c
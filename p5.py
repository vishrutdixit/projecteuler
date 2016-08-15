#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

divs = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in xrange(2520, 10000000000, 2520):
    b = True
    print i
    for j in divs:
        if i%j != 0:
            b = False
    if b:
        print i
        break

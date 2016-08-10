#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum = 0
for i in range(1, 101):
    sum += (i*i)

div = 100*101/2


print div*div - sum

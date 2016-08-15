# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from p7 import getNthPrime

sum = 0
i = 0

map = {}
map[0] = 2
prime = 2

while(prime < 2000000):
	sum += prime
	i+= 1
	prime = getNthPrime(i, map)

print sum

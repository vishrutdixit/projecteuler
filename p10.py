# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import sys

sys.setrecursionlimit(100000)

def getNthPrime(n, map):
	if(map.get(n)):
		return map[n]
	if(not map.get(n)):
		candidate = getNthPrime(n-1, map)+1
		while(not isPrime(candidate, map)):
			# print candidate
			candidate+=1
		map[n] = candidate
		return candidate

sum = 0

for i in range(0, 100000):
	map= {}
	prime = getNthPrime(i, map)
	if(prime < 2000000):
		sum += prime

print prime

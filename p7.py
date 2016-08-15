#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

import sys
sys.setrecursionlimit(100000)

def getNthPrime(n, map):
	if(map.get(n)):
		return map[n]
	if(not map.get(n)):
		candidate = getNthPrime(n-1, map)+1
		while(not isPrime(candidate)):
			# print candidate
			candidate+=1
		map[n] = candidate
		return candidate


def isPrime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True


def main():
  map = {}
  map[0] = 2;
  print(getNthPrime(10000, map))

if __name__ == "__main__":
	main();



    

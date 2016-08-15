#What is the largest prime factor of the number 600851475143 ?

def findBiggestPrime(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return n

print findBiggestPrime(13195)
print findBiggestPrime(600851475143)

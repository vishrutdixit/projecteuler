#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#find the sum of the even-valued terms.

#memoize!
map = {}

def fib(n):
    if(n==0):
        map[0] = 1
        return 1
    if(n==1):
        map[1] = 2
        return 2

    map[n] = map[n-2] + map[n-1]
    return map[n]

def main():
    sum = 0
    for i in range(1000000):
        if fib(i) >= 4000000:
            return sum
        else:
            if fib(i)%2 == 0:
                sum += fib(i)


print main()

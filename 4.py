def isPalindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    return False

def main():
    biggest = 0
    for i in range(100,1000):
        for j in range(100,1000):
                if isPalindrome(i*j) and i*j>=biggest:
                    biggest=i*j
    return biggest

print main()

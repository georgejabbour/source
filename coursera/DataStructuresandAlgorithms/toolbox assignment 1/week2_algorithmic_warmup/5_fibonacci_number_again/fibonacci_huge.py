# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge(n,m):
    if n <= 1:
        return n
    # find the pisano period (p) for m
    p=pisano(m)
    # find the remainder of n when divided by piano period (p)
    r=n%p
    # find fib(r,m)
    return fibonacci_mod_m(r,m)

def pisano(n):
    # start off the pisano sequence
    a=0
    b=1
    c=a+b
    val=0
    for i in range(10*n):
        c=(a+b)%n
        a=b
        b=c
        # check for '01' sequence, marks recurrence
        if a==0 and b==1:
            val = i+1
            return val
    return val


def fibonacci_mod_m(n,m):
    if n <= 1:
        return n
    a=0
    b=1
    c=a+b
    for i in range(2,n+1):
        c=(a+b)%m
        a=b
        b=c
    return c

if __name__ == '__main__':
    val = sys.stdin.readline();
    n, m = map(int, val.split())
    # print(get_fibonacci_huge_naive(n, m))
    # print("------")
    print(get_fibonacci_huge(n, m))

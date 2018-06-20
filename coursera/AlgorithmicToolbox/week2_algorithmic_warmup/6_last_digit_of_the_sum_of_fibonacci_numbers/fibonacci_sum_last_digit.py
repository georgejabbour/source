# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    previous = 0
    current  = 1
    sum      = 1
    # print (previous, current, sum)
    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current
        # print (previous, current, sum)
    return sum % 10

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


def fibonacci_sum(n):
    if n <= 1:
        return n
    n = (n+2)%pisano(10)
    a=0
    b=1
    c=a+b
    for i in range(2,n+1):
        c=(a+b)%10
        a=b
        b=c
    if c==0:
        return 9
    return c%10-1

if __name__ == '__main__':
    val = sys.stdin.readline()
    n = int(val)
    # print("----")
    # print(fibonacci_sum_naive(n))
    # print("----")
    print(fibonacci_sum(n))

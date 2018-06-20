# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

# def get_fibonacci_last_digit(n):
#     if n <= 1:
#         return n
#     f = list(range(n+1))
#     f[0]=0
#     f[1]=1
#     for i in range(2,n+1):
#         f[i]=f[i-1]+f[i-2]
#     return f[n]%10

def get_fibonacci_last_digit2(n):
    if n <= 1:
        return n
    a=0
    b=1
    c=a+b
    for i in range(2,n+1):
        c=(a+b)%10
        a=b
        b=c
    return c

if __name__ == '__main__':
    val = sys.stdin.readline()
    n = int(val)
    # print(get_fibonacci_last_digit_naive(n))
    # print("-----")
    print(get_fibonacci_last_digit2(n))

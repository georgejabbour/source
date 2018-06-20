# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

# def fibonacci_sum_squares(n):
#     f = list(range(n+2))
#     # f[0]=0
#     # f[1]=1
#     # print (1, 0, 0)
#     for i in range(2,n+2):
#         f[i]=f[i-1]+f[i-2]
#         # print (1, 0, 0)
#     #it's just the sum of the last two fib numbers
#     return (f[n]*f[n+1])%10


def fibonacci_sum_squares2(n):#using the partial fib sum method
    if n <= 1:
        return n
    f=list(range(61))
    # f[0]=0
    # f[1]=1
    for i in range(2,61):
        f[i]=f[i-2]+f[i-1]
    n=n%60
    #just need the last digit
    return (f[n]*f[n+1])%10

# def partial_fibonacci_sum(m,n):
#     if n <= 1:
#         return n
#     if m>n:
#         return
#     #pisano period of fib mod 10 is 60
#     #only need fib(60) here
#     f=list(range(60))
#     # f[0]=0
#     # f[1]=1
#     for i in range(2,60):
#         f[i]=f[i-2]+f[i-1]

#     #because of this pisano period, 
#     # the partial fib sum from m to n will be the same as the partial fib sum from m%60 to n%60
#     n=n%60
#     m=m%60
#     if n<m:
#         n+=60
#     tot=0
#     #add up the values
#     for j in range(m,n+1):
#         tot+=f[j%60]
#     #just need the last digit
#     return tot%10

if __name__ == '__main__':
    n = int(stdin.readline())
    # print("-----")
    # print(fibonacci_sum_squares_naive(n))
    # print("-----")
    print(fibonacci_sum_squares2(n))
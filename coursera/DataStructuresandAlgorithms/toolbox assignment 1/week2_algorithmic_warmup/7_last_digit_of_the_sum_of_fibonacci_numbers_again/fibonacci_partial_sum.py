# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0
    current = 0
    next  = 1
    for i in range(to + 1):
        # print (next, current, sum)
        if i >= from_:
            sum += current
        current, next = next, current + next
    return sum%10


def partial_fibonacci_sum(m,n):
    if n <= 1:
        return n
    if m>n:
        return
    #pisano period of fib mod 10 is 60
    #only need fib(60) here
    f=list(range(60))
    # f[0]=0
    # f[1]=1
    for i in range(2,60):
        f[i]=f[i-2]+f[i-1]

    #because of this pisano period, 
    # the partial fib sum from m to n will be the same as the partial fib sum from m%60 to n%60
    n=n%60
    m=m%60
    if n<m:
        n+=60
    tot=0
    #add up the values
    for j in range(m,n+1):
        tot+=f[j%60]
    #just need the last digit
    return tot%10

if __name__ == '__main__':
    val = sys.stdin.readline();
    from_, to = map(int, val.split())
    # print(fibonacci_partial_sum_naive(from_, to))
    # print("---")
    print(partial_fibonacci_sum(from_, to))
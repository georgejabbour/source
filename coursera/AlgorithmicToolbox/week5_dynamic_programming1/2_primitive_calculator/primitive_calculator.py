# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def dp_optimal_sequence(n):
    sequence = []

    memo = [0]*(n+1)
    for i in range(1, n+1):
        opt = memo[i-1] + 1;
        if i % 2 == 0:
            opt = min(memo[i//2]+1, opt)
        if i % 3 == 0:
            opt = min(memo[i//3]+1, opt)
        memo[i]=opt

    while n >= 1:
        sequence.append(n)
        if memo[n] == memo[n-1] + 1:
            n = n - 1
        elif n % 2 == 0 and memo[n//2] == memo[n] - 1:
            n = n // 2
        elif n % 3 == 0 and memo[n//3] == memo[n] - 1:
            n = n // 3

    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(dp_optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

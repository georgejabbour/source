# Uses python3
import random

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
b=list(a)
b.remove(max(b))
result = max(a)*max(b)

print(result)
# Uses python3
import sys
from decimal import Decimal

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b

def EuclidGCD(a, b):
    if b == 0:
        return a
    aa = a%b
    return EuclidGCD(b,aa)

def lcm(a,b):
	return int(Decimal(a)*Decimal(b)/Decimal(EuclidGCD(a,b)))

if __name__ == '__main__':
    val = sys.stdin.readline()
    a, b = map(int, val.split())
    print(lcm(a, b))
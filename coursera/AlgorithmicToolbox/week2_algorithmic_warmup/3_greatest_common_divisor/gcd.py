# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

# lemma
# gcd(a,b)=gcd(a'b)=gcd(b,a')

def EuclidGCD(a, b):
	if b == 0:
		return a
	aa = a%b
	return EuclidGCD(b,aa)

if __name__ == "__main__":
    val = sys.stdin.readline()
    a, b = map(int, val.split())
    print(EuclidGCD(a, b))

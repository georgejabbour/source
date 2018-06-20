# Uses python3
import random

def mpp1(a):
	# n = int(input())
	# a = [int(x) for x in input().split()]
	# assert(len(a) == n)

	result = 0
	n=len(a)
	for i in range(0, n):
	    for j in range(i+1, n):
	        if a[i]*a[j] > result:
	            result = a[i]*a[j]

	print(result)

def mpp(a):
	# n = int(input())
	# a = [int(x) for x in input().split()]
	# assert(len(a) == n)

	result = 0
	b=list(a)
	b.remove(max(b))
	result = max(a)*max(b)

	print(result)

def StressTest(N,M):
	while True:
		n=random.randint(2,N)
		A = [x for x in range(1,n+1)]
		for i in range(1,n):
			A[i]=random.randint(0,M)
		print(A)
		result1=mpp1(A)
		result2=mpp(A)
		if result1==result2:
			print("OK")
		else:
			print("Wrong answer: ", result1, result2)
			return

N=int(input())
M=int(input())

StressTest(N,M)
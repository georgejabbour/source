# python3
import random

def read_input():
	return (input().rstrip(), input().rstrip())

def print_occurrences(output):
	print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
	return [
		i 
		for i in range(len(text) - len(pattern) + 1) 
		if text[i:i + len(pattern)] == pattern
	]

def RabinKarp(P,T):
	p=1000000007
	x=random.randint(1,p)
	# x=1
	result=[]
	pHash = PolyHash(P,p,x)
	H=PrecomputeHashes(T,len(P),p,x)
	for i in range(len(T)-len(P)+1):
		if pHash!=H[i]:
			continue
		if T[i:i+len(P)]==P:
			result.append(i)
	return result
	# return [
 #        i 
 #        for i in range(len(T) - len(P) + 1) 
 #        if pHash == H[i] and T[i:i + len(P)] == P
 #    ]

def PrecomputeHashes(T,Plength,p,x):
	H=[0]*(len(T)-Plength+1)
	S=T[-Plength:]
	H[len(T)-Plength]=PolyHash(S,p,x)
	
	y=1
	
	for i in range(1,Plength+1):
		# y=((y*x) % p + p) % p
		y = (y * x) % p
	
	for i in reversed(range(len(T) - Plength)):
		prehash = x * H[i + 1] + ord(T[i]) - y * ord(T[i + Plength])
		while(prehash < 0):
			prehash += p
		H[i] = prehash % p
	return H

def PolyHash(S,p,x):
	hashh=0
	for i in reversed(S):
		hashh=(hashh*x+ord(i))%p
	return hashh%p


if __name__ == '__main__':
	
	print_occurrences(RabinKarp(*read_input()))


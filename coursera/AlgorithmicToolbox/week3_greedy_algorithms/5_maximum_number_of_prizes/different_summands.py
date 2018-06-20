# Uses python3
import sys

def optimal_summands(n):
	summands = []
	i=1
	while n>0:
		if n-i >= i+1:
			n-=i
			summands.append(i)
			i+=1
		else:
			summands.append(n)
			n-=n
	return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

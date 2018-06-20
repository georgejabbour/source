# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fibonacci(n):
	if n <= 1:
		return n
	f = list(range(n))
	f[0]=0
	f[1]=1
	for i in range(2,n):
		f[i]=f[i-1]+f[i-2]
	return f[n-1]

def fibonacci2(n):
    if n <= 1:
        return n
    a=0
    b=1
    c=a+b
    #don't need to make a list and store everything...just keep the last two
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    return c

if __name__ == '__main__':
	n = int(input())
	print(fibonacci2(n))

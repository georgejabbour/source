#Uses python3

import sys, math

def largest_number(digits):
    #write your code here
    a=[int(x) for x in digits]
    a.sort(key=cmp_to_key(compare), reverse=True)
    answer = int(''.join(str(x) for x in a))
    return answer

def compare(a,b):
	a=str(a)
	b=str(b)
	ab=a+b
	ba=b+a
	if ab==ba:
		return 0
	elif ab < ba:
		return -1
	else:
		return 1

#https://docs.python.org/3/howto/sorting.html
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    digits = data[1:]
    print(largest_number(digits))
    

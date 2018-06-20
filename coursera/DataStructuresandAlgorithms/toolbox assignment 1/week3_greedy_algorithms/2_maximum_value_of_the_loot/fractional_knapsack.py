# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
	value = 0.
	n=len(weights)
	#init list
	A=[0 for i in range(n)]
	w,v=sort_weights_values(weights,values)
	ww=list(w)
	vv=list(v)
	for i in range(n):
		if capacity==0:
			return value
		a=min(ww[i],capacity)
		value=value+(a*(vv[i]/ww[i]))
		ww[i]=ww[i]-a
		A[i]=A[i]+a
		capacity=capacity-a
	return value

def sort_weights_values(weights,values):
	pairs = zip(values, weights) 
	# [(60, 20), (100, 50), (120, 30)]
	sorted_pairs = sorted(pairs, key=lambda t: t[1]/t[0]) 
	# [(100, 50), (60, 20), (120, 30)]
	values, weights = zip(*sorted_pairs)
	# (100, 60, 120), (50, 20, 30)
	return (weights,values)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{0:.10f}".format(opt_value))

# Uses python3
import sys, math

def get_majority_element(a):
    if len(a)==1: 
        return a[left]

    mid = math.floor(len(a)/2)
    leftelem=get_majority_element(a[:mid+1])
    rightelem=get_majority_element(a[mid+1:])

    lcount=0
    for i in range(len(a)):
        if a[i] == leftelem:
            lcount+=1
    if lcount>math.floor(len(a)/2):
        return leftelem

    rcount=0
    for i in range(left,right):
        if a[i]==rightelem:
            rcount+=1
    if rcount>math.floor(len(a)/2):
        return rightelem

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)

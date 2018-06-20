# Uses python3
import sys, math

def find_majority(k):
    myMap = {}
    maximum = ( '', 0 ) # (occurring element, occurrences)
    for n in k:
        if n in myMap: myMap[n] += 1
        else: myMap[n] = 1
        # Keep track of maximum on the go
        if myMap[n] > maximum[1]: maximum = (n,myMap[n])

    if maximum[1]>len(k)/2:
        return 1
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    # print(input)
    n, *a = list(map(int, input.split()))
    if find_majority(a) != -1:
        print(1)
    else:
        print(0)

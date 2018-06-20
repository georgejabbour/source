# Uses python3
import sys, math

# def gme(a):
#     l=len(a)
#     if l==0:
#         return -1
#     if l==1:
#         return a[0]

#     mid = math.floor(l/2)
#     leftelem = gme(a[:mid])
#     rightelem = gme(a[mid:])

#     if leftelem==rightelem:
#         return leftelem

#     #count the number of leftelems in range left-right
#     leftcount=a.count(leftelem)
#     #count the number of rightelems in range left-right
#     rightcount=a.count(rightelem)

#     if leftcount>mid:
#         return leftcount
#     elif rightcount>mid:
#         return rightcount
#     else:
#         return -1

def find_majority(a):
    counts = {}
    maximum=0
    for num in a:
        if num in counts: counts[num] += 1
        else: counts[num] = 1
        if counts[num] > maximum: maximum = counts[num]

    if maximum>len(a)/2:
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

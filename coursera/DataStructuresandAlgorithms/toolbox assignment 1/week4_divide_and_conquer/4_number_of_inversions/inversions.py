# Uses python3
import sys,math

def merge_sort(a):
    lena = len(a)
    if lena <= 1:
        return a
    B = merge_sort(a[:(lena//2)])
    C = merge_sort(a[(lena//2):])
    return merge_and_count(B,C)

def merge_and_count(B,C):
    global count
    D = []
    
    while len(B) > 0 and len(C) > 0:
        if B[0] <= C[0]:
            D.append(B[0])
            B.remove(B[0])
        else:
            count += len(B)
            D.append(C[0])
            C.remove(C[0])
    while len(B)!=0:
        D.append(B[0])
        B.remove(B[0])
    while len(C)!=0:
        D.append(C[0])
        C.remove(C[0])
    return D

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    count=0
    merge_sort(a)
    print(count)

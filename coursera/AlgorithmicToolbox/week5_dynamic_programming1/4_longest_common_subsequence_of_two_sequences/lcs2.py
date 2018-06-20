#Uses python3

import sys

def lcs2(s, t):
    #lengths
    n=len(s)+1
    m=len(t)+1

    #initialize D
    D=[[0] * (m) for x in range(n)]
    optimum=0
    for i in range(1,n):
        for j in range(1,m):
            if s[i-1]==t[j-1]:
                D[i][j]=D[i-1][j-1]+1
            else:
                D[i][j]=max(D[i-1][j],D[i][j-1])
            if D[i][j]>optimum:
                optimum=D[i][j]
    return optimum


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

#Uses python3

import sys

def lcs3(s, t, u):
    #lengths
    n=len(s)+1
    m=len(t)+1
    o=len(u)+1

    #initialize D
    #D=[[0] * (m) for x in range(n)]
    D = [[[0 for k in range(o)] for j in range(m)] for i in range(n)]
    optimum=0
    for i in range(n):
        for j in range(m):
            for k in range(o):
                if(i==0 or j==0 or k==0):
                    D[i][j][k]=0
                elif s[i-1]==t[j-1]==u[k-1]:
                    D[i][j][k]=D[i-1][j-1][k-1]+1
                else:
                    D[i][j][k]=max(D[i-1][j][k],D[i][j-1][k], D[i][j][k-1])
                if D[i][j][k]>optimum:
                    optimum=D[i][j][k]
    return optimum

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))

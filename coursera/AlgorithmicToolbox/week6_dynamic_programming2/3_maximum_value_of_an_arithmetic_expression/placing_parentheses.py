# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(i, j, ops, mins,Maxs):
    minn=100000
    maxx=-100000
    for k in range(i,j):
        a = evalt(Maxs[i][k], Maxs[k+1][j], ops[k])
        b = evalt(Maxs[i][k], mins[k+1][j], ops[k])
        c = evalt(mins[i][k], Maxs[k+1][j], ops[k])
        d = evalt(mins[i][k], mins[k+1][j], ops[k])
        minn = min(minn, a, b, c, d)
        maxx = max(maxx, a, b, c, d)
    return(minn, maxx)

def get_maximum_value(dataset):
    ops = dataset[1:len(dataset):2]
    exprs = dataset[0:len(dataset)+1:2]
    n=len(exprs)
    mins = [[0 for i in range(n)] for j in range(n)]  #minimized values
    Maxs = [[0 for i in range(n)] for j in range(n)]  #maximized values
    for i in range(len(exprs)):
        mins[i][i],Maxs[i][i]=int(exprs[i]),int(exprs[i])
    for s in range(1,n):
        for i in range(n-s):
            j=i+s
            mins[i][j],Maxs[i][j]=MinAndMax(i,j,ops, mins,Maxs)
    return Maxs[0][n-1]





if __name__ == "__main__":
    print(get_maximum_value(input()))


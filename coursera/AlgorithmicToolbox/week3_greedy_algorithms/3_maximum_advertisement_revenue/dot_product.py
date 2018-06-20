#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    #sort by biggest profits
    a.sort()
    #sort by most clicks
    b.sort()
    #multiply each largest number and add to total
    for i in range(len(a)):
        res += a[i] * b[i]
    return res
    
# def sort_profit_clicks(profits,clicks):
#     #[(1,3,-5),(-2,4,1)]
#     pairs = zip(clicks, profits) 
#     # [(60, 20), (100, 50), (120, 30)]
#     sorted_pairs = sorted(pairs, key=lambda t: t[1]*t[0]) 
#     # [(100, 50), (60, 20), (120, 30)]
#     clicks, profits = zip(*sorted_pairs)
#     # (100, 60, 120), (50, 20, 30)
#     return (profits,clicks)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    

# python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTreeHard(j, min_int, max_int):
  if not j in tree: 
    return True
  if (tree[j][0] < min_int) or (tree[j][0] > max_int): 
    return False
  l = IsBinarySearchTreeHard(tree[j][1], min_int, tree[j][0] - 1)
  r = IsBinarySearchTreeHard(tree[j][2], tree[j][0], max_int)
  return (l and r)

def main():
  nodes = int(sys.stdin.readline().strip())
  global tree
  tree, min_int, max_int = {}, -2147483648, 2147483647
  for i in range(nodes):
    tree[i] = (list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTreeHard(0, min_int, max_int):
    print("CORRECT")
  else:
    print("INCORRECT")
threading.Thread(target = main).start()
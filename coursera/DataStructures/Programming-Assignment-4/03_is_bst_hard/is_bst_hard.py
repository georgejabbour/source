# python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def IsBinarySearchTreeHard(self, root, min_int, max_int):
    # print("self.key[root]: ",self.key[root], ", self.left: ", self.left, ", self.right: ", self.right)
    if (self.key[root] < min_int) or (self.key[root] > max_int): 
      return False
    
    l = True if self.left[root]<0 else self.IsBinarySearchTreeHard(self.left[root], min_int, self.key[root] - 1)
    r = True if self.right[root]<0 else self.IsBinarySearchTreeHard(self.right[root], self.key[root], max_int)
    return (l and r)

def main():
  # nodes = int(sys.stdin.readline().strip())
  tree = TreeOrders()
  tree.read()
  min_int, max_int = -2147483648, 2147483647
  if tree.n ==0:
      print("CORRECT")
  elif tree.IsBinarySearchTreeHard(0,min_int,max_int):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
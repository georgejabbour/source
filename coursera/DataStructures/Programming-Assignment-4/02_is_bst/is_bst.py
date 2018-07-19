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


  def inOrder(self):
    self.result = []#wipe the result anew
    self.InOrderRecurse(0)                
    return self.result

  def InOrderRecurse(self,root):
    # if self.n ==0:
    #   return True

    if self.left[root]!=-1: #go as left as you can
      self.InOrderRecurse(self.left[root])
    
    self.result.append(self.key[root]) #once you can go left and reach a left, get that value

    if self.right[root] != -1: #then get the right node value
      self.InOrderRecurse(self.right[root])

  def IsBinarySearchTree(self):
    if sorted(self.result) != self.result:
      return False
    return True

def main():
  # nodes = int(sys.stdin.readline().strip())
  tree = TreeOrders()
  tree.read()
  if tree.n ==0:
      print("CORRECT")
  else:
    tree.inOrder()
    if tree.IsBinarySearchTree():
      print("CORRECT")
    else:
      print("INCORRECT")

threading.Thread(target=main).start()

# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

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
    if self.left[root]!=-1: #go as left as you can
      self.InOrderRecurse(self.left[root])
    
    self.result.append(self.key[root]) #once you can go left and reach a left, get that value

    if self.right[root] != -1: #then get the right node value
      self.InOrderRecurse(self.right[root])

  def preOrder(self):
    self.result = []#wipe the result anew
    self.PreOrderRecurse(0)                
    return self.result

  def PreOrderRecurse(self,root):
    self.result.append(self.key[root]) #first get the value of the current node

    if self.left[root]!=-1: #then get the value of the left node
      self.PreOrderRecurse(self.left[root])
    
    if self.right[root] != -1: #then get the right node value
      self.PreOrderRecurse(self.right[root])

  def postOrder(self):
    self.result = []
    self.PostOrderRecurse(0)
    return self.result

  def PostOrderRecurse(self,root):
    if self.left[root]!=-1:
      self.PostOrderRecurse(self.left[root])
    
    if self.right[root] != -1:
      self.PostOrderRecurse(self.right[root])

    self.result.append(self.key[root])

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()

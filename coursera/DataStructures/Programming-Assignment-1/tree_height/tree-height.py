# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        #make a memo to store the node depths
        self.memo=[0]*self.n
    
    def compute_height(self):
        #find the max of the heights of all nodes
        return max([self.node_depth(node) for node in range(self.n)])

    def node_depth(self,node):
        # find the parent of this node
        parent=self.parent[node]
        # if it's already memo'd, retrieve it
        if self.memo[node]:
            return self.memo[node]
        # if it's the root node, return that
        elif parent == -1:
            return 1
        #memoize 1 (to count this node) plus the length from the root to this node's parent
        else:
            self.memo[node]=1+self.node_depth(self.parent[node])
        #return the memo of this node
        return self.memo[node]



def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()

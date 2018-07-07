# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = [] #H

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def InPlaceHeapSort(self):
    for i in range(int(len(self._data)/2),-1,-1):
      self.SiftDown(i)

  def Parent(i): #return the index of the Parent of i
    return int((i - 1) / 2)
  
  def LeftChild(i): #return the index of the LeftChild of i
    return 2*i+1

  def RightChild(i): #return the index of the RightChild of i
    return 2*i+2

  def SiftUp(i): #sifts up the element at index i
    while i>1 and self._data[Parent(i)]>self._data[i]:
      self._data[Parent(i)],self._data[i] = self._data[i], self._data[Parent(i)]
      i=Parent(i)

  def SiftDown(self, i): #sifts down the element at index i
    minIndex = i
    l = HeapBuilder.LeftChild(i)
    if l<len(self._data) and self._data[l]<self._data[minIndex]:
      minIndex=l
    r = HeapBuilder.RightChild(i)
    if r<len(self._data) and self._data[r]<self._data[minIndex]:
      minIndex=r
    if i != minIndex:
      self._swaps.append((i,minIndex))
      self._data[i],self._data[minIndex] = self._data[minIndex],self._data[i]
      self.SiftDown(minIndex)

  def Solve(self):
    self.ReadData()
    self.InPlaceHeapSort()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()

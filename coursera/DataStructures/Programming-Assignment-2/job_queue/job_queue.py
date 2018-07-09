# python3
#from queue import PriorityQueue
#from threading import Thread

# TODO: try to implement using built in PriorityQueue class

class JobQueue:
	def read_data(self):
		self.num_threads, m = map(int, input().split())
		self.jobs = list(map(int, input().split()))
		assert m == len(self.jobs)

	def write_response(self):
		for i in range(len(self.jobs)):
		  print(self.assigned_threads[i], self.start_times[i]) 

	# def assign_jobs(self): # super slow default function
	# 	self.assigned_threads = [None] * len(self.jobs)
	# 	self.start_times = [None] * len(self.jobs)
	# 	next_free_time = [0] * self.num_threads
	# 	for i in range(len(self.jobs)):
	# 		next_thread = 0
	# 		for j in range(self.num_threads):
	# 			if next_free_time[j] < next_free_time[next_thread]:
	# 				next_thread = j
	# 	  self.assigned_threads[i] = next_thread
	# 	  self.start_times[i] = next_free_time[next_thread]
	# 	  next_free_time[next_thread] += self.jobs[i]

	def assign_jobs(self): # new and improved using minheap pqueue
		# make a thread marker for each job to show which thread processed that job
		self.assigned_threads = [None] * len(self.jobs) 
		# make a start time marker for each job
		self.start_times = [None] * len(self.jobs) 
		
		# construct new binary min heap containing some threads
		# this will allow us to sift through the threads based on the priority of their next start time
		H = BinaryMinHeap(self.num_threads) 
		
		# for each job
		# make note that the thread that will process this particular job is the at top of the heap
		# make note that the time this job is started is the next time that this particular thread can start a job
		for i in range(len(self.jobs)): 
			self.assigned_threads[i] = H._data[0][0] 
			self.start_times[i] = H._data[0][1] 
			
			# Increment the next time this thread can start a job by this particular job's length. 
			# This sifts it down in priority.
			H.ChangePriority(0, H._data[0][1] + self.jobs[i]) 

	def solve(self):
		self.read_data()
		self.assign_jobs()
		self.write_response()

class BinaryMinHeap:
	def __init__(self, num_threads):
		self._data = []
		self.size = num_threads

		# threads contain (index of the thread for comparisons in case of a tie, next available start time)
		# constructing a set of 4 threads will yield (0,0),(1,0),(2,0),(3,0) since they can all start at time 0
		for i in range(num_threads):
			self._data.append((i, 0))

	# following functions adapted from lecture pseudocode into python: 
	# Parent(), LeftChild(), RightChild(), SiftUp(), SiftDown(), ChangePriority()

	def Parent(self, i):
		return self._data[floor(i/2)+1]

	def LeftChild(self, i):
		return 2*i + 1

	def RightChild(self, i):
		return 2*i + 2

	def SiftUp(self, i):
		while i > 0 and self.ThreadCompare(self._data[i], self._data[self.Parent(i)]):
			self._data[i], self._data[self.Parent(i)] = self._data[self.Parent(i)], self._data[i]
			i = self.Parent(i)

	def SiftDown(self, i):
		minIndex = i
		left = self.LeftChild(i)
		if left < self.size and self.ThreadCompare(self._data[left], self._data[minIndex]):
			minIndex = left

		right = self.RightChild(i)
		if right < self.size and self.ThreadCompare(self._data[right], self._data[minIndex]):
			minIndex = right
		if i != minIndex:
			self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
			self.SiftDown(minIndex)
	
	def ChangePriority(self, i, priority):
		old_p = self._data[i][1]
		self._data[i] = (self._data[i][0], priority)
		if priority < old_p:
			self.SiftUp(i)
		else:
			self.SiftDown(i)

	# compares two threads based on their next start time, but....
	# ... in case multiple threads are available at the same time, choose the one with the lowest index first 
	# (see __init__ around line 59)
	def ThreadCompare(self, a, b):
		if a[1] != b[1]:
			return a[1] < b[1]
		else: 
			return a[0] < b[0]

if __name__ == '__main__':
	job_queue = JobQueue()
	job_queue.solve()


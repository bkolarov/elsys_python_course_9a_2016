class InvalidIndexError(Exception):
	def __init__(self, index, size):
		super().__init__('Index must be <= len(queue) and > 0. Your queue is of size: {}.'.format(size))
		self.index = index
	
class Queue:
	def __init__(self, head=None):
		self.head = head
		self.tail = head
		self.size = 0 if head == None else 1
		
	class Node:
		def __init__(self, value):
			self.value = value
			self.prev = None
			
		def __str__(self):
			return 'obj:with value: {}'.format(self.value)
			
	def enqueue(self, node):
		if self.head == None:
			self.head = self.tail = node
		else:
			self.tail.prev = node
			self.tail = node
			
		self.size += 1
			
	def dequeue(self):
		dequeued = self.head
		
		if dequeued == None:
			self.tail = None
			dequeued = self.head
		else:
			self.head = self.head.prev

		self.size -= 1

		return dequeued

	def dequeue_to(self, index, inclusive=False):
		if index < 0 or index >= self.size:
			raise InvalidIndexError(index, len(self))
			
		if inclusive:
			q_range = range(0, index + 1)
		else:
			q_range = range(0, index)
			
		dequeued = None
		for i in q_range:
			dequeued = self.dequeue()
			
		return dequeued
		
	def clear(self):
		while not self.is_empty():
			self.dequeue()
		
	def peek(self):
		return self.head

	def is_empty(self):
		return len(self) == 0

	def __len__(self):
		return self.size
		
	def __iter__(self):
		return Queue.Iterator(self)
		
	class Iterator:
		def __init__(self, queue):
			self.queue = queue
			
		def __next__(self):
			next = self.queue.dequeue()
					
			if next == None:
				raise StopIteration

			return next.value
			
q = Queue()

for i in range(10):
	q.enqueue(Queue.Node(i))
	
print('tail: ' + str(q.peek()))
print('size: ' + str(len(q)))

q.dequeue_to(5)
print('size: ' + str(len(q)))

for node in q:
	print(node)
	

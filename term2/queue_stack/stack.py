class InvalidIndexError(Exception):
	def __init__(self, index, size):
		super().__init__('Index must be <= len(queue) and > 0. Your stack is of size: {}.'.format(size))
		self.index = index

class Stack:
	def __init__(self, top=None):
		self.top = top
		self.size = 0 if top == None else 1
		
	class Node:
		def __init__(self, value):
			self.value = value
			self.prev = None
		
	def push(self, value):
		node = Stack.Node(value)
		if self.top == None:
			self.top = node
		else:
			node.prev = self.top
			self.top = node	
			
		self.size += 1
		
	def pop(self):
		popped = self.top
		
		if popped != None:
			self.top = self.top.prev
		else:
			return None
		
		self.size -= 1
		
		return popped.value

	def pop_to(self, index, inclusive=False):
		if index < 0 or index >= len(self):
			raise InvalidIndexError(index, self.size)
			
		if inclusive:
			s_range = range(0, index + 1)
		else:
			s_range = range(0, index)
			
		popped = None
		for i in s_range:
			popped = self.pop()
			
		return popped
			
	def peek(self):
		return self.top
		
	def clear(self):
		while not self.is_empty():
			self.pop()
		
	def __iter__(self):
		return Stack.Iterator(self)
		
	class Iterator:
		def __init__(self, stack):
			self.stack = stack
			
		def __next__(self):
			next = self.stack.pop()
			
			if next == None:
				raise StopIteration
			
			return next
		
	def is_empty(self):
		return len(self) == 0
		
	def __len__(self):
		return self.size
		
		
stack = Stack()

for i in range(10):
	stack.push(i)

print(stack.is_empty())
stack.clear()
print(stack.is_empty())


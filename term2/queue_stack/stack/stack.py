class InvalidIndexError(Exception):
	def __init__(self, index, size):
		super().__init__('Index must be <= len(queue) and > 0. Your stack is of size: {}.'.format(size))
		self.index = index

class InvalidNodeError(Exception):
	def __init__(self):
		super().__init__("Pushed node's value must not be None.")

class Stack:
	def __init__(self):
		# init a new empty stack. Since it is empty,
		# there is nothing for top to point to and the 
		# size is 0.
		self.top = None
		self.size = 0
		
	class Node:
		def __init__(self, value):
			# Create a node that contains the given value.
			# Since it is a new node, it hasn't been added
			# to the stack yet. Therefore next points to 
			# None.
			self.value = value
			self.next = None
		
	'''
	Push new value to the top of the stack.
	Remember that the principle of adding and removing
	values from the stack is FIFO - First In First Out.
	'''
	def push(self, value):
		if value == None:
			raise InvalidNodeError
			
		new_node = Stack.Node(value)
		if self.top == None:
			# The stack is empty so we just tell the top
			# to point to the newly pushed node.
			self.top = new_node
		else:
			# The newly puhed node must be at the top
			# of the stack. This means that new_node's
			# next must point to the current top node.
			new_node.next = self.top
			# Then we move the top to point to the new
			# node, since it is the new one that is at 
			# the top of the stack.
			self.top = new_node	
			
		self.size += 1
		
	'''
	Pop the most top value from the stack.
	Remember that the principle of adding and removing
	values from the stack is FIFO - First In First Out.
	The last node, that has been pushed, must be poped now.
	'''
	def pop(self):
		if self.is_empty():
			# If the stack is empty, top will point to None.
			# In that case we do nothing, there is nothing
			# to return and we returne None.
			return None
			
		# We are going to move top to point to it's next
		# node, because we are popping the current one.
		# Since we will lose the connection to the popped
		# node, we have to store it's value so it can be
		# it can be returned.
		popped = self.top
		
		# Since we reached this line, this means that
		# the stack is not empty. We saved the current 
		# top node so now it is safe to move top to point
		# to its next. 
		self.top = self.top.next
		
		self.size -= 1
		
		# We saved the top before we poped it, so we can
		# return its value here. self.top no longer
		# points to popped (where it used to point)
		return popped.value
			
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

print('popped: {}'.format(stack.pop()))
stack.push('TOP')

print()
for i in stack:
	print(i)

print()
print('clear stack')
stack.clear()
print('is empty: {}'.format(stack.is_empty()))

print()
stack.push('Bottom')
stack.push('Mid')
stack.push('Top')

for i in stack:
	print(i)

print()
print('after iteration')
print('is empty: {}'.format(stack.is_empty()))

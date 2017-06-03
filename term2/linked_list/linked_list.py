class InvalidInsertionError(Exception):
	def __init__(self):
		super().__init__("Attempring to insert into an empty list or into one, that doesn't have a node with the given before_value")
		
class LinkedList:

	def __init__(self):
		self.head = None
		self.size = 0

	class Node:
		def __init__(self, value):
			self.value = value
			self.next = None

	def add(self, value):
		new_node = LinkedList.Node(value)
		current_node = self.head

		if self.is_empty():
			self.head = new_node
		else:
			while current_node.next != None:
				current_node = current_node.next
	
			current_node.next = new_node
			
		self.size += 1

	def delete(self, value):
		if self.is_empty():
			return
			
		current_node = self.head
	
		if self.head.value == value:
			self.head = self.head.next
		else:
			while current_node.next != None:
				if current_node.next.value == value:
					to_delete_node = current_node.next
					current_node.next = to_delete_node.next
					break
					
				current_node = current_node.next
				
		self.size -= 1

	def insert(self, before_value, new_value):
		new_node = LinkedList.Node(new_value)
		insert_succeeded = False
	
		if self.is_empty():
			insert_succeeded = False
		elif self.head.value == before_value:
			tmp = self.head
			new_node.next = tmp
			self.head = new_node
			insert_succeeded = True
		else:
			current_node = self.head
			while current_node.next != None:
				if current_node.next.value == before_value:
					new_node.next = current_node.next
					current_node.next = new_node
					insert_succeeded = True
					break
				
				current_node = current_node.next
		
		if insert_succeeded:
			self.size += 1
		else:
			raise InvalidInsertionError

	def __iter__(self):
		return LinkedList.Iterator(self.head)

	class Iterator:
		def __init__(self, head):
			self.current_node = head

		def __next__(self):
			if self.current_node == None:
				raise StopIteration
				
			current_value = self.current_node.value
			self.current_node = self.current_node.next
			
			return current_value

	def is_empty(self):
		return self.head == None

	
	def __len__(self):
		return self.size

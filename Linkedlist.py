class Node:
	def __init__(self):
		self.data = None
		self.next = None

	def setData(self,data):
		self.data = data

	def getData(self):
		return self.data

	def setNext(self,next):
		self.next = next

	def getNext(self):
		return self.next

	def hasNext(self):
		return self.next != None


class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, data):
		node = Node()
		node.setData(data)
		node.next = None
		if self.head == None:
			self.head = node
			self.head.data = node.data
			self.head.next = node.next
		else:
			current = self.head
			while current.next != None:
				current=current.next
			current.next = node

	def insert_at_middle(self,data):
		pass

	def insert_first(self, data):
		node = Node()
		node.data = data
		if self.head == None:
			self.head = node
		else:
			node.next = self.head

	def insert_position(self,data,pos):
		pass

	def delete():
		pass

	def delete_at_first():
		pass

	def delete_at_middle():
		pass

	def delete_postion(self, data):
		pass

	def display(self):
		current = self.head
		while current != None:
			print(current.data,"\t")
			current=current.next

	def getLength(self):
		count = 0
		current = self.head
		while current != None:
			count+=1
			current=current.next
		print(count)


l1 = LinkedList()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.insert_first(40)

l1.display()
l1.getLength()




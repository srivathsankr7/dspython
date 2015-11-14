class node(object):
	def __init__(self,data,next=None):
		self.data=data
		self.next=next

	def setNext(self,next):
		self.next=next

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

class linkedlist(object):

	def __init__(self,head=None):
		self.head=head

	def insertAtFront(self,data):
		newnode=node(data)
		newnode.setNext(self.head)
		self.head=newnode

	def insert(self,data):
		newnode=node(data)
		current=self.head
		while current is not None and current.getData()<data:
			current = current.getNext()
		if current is not None:
			newnode.setNext(current.getNext())
		current.setNext(newnode)

	def insertAtEnd(self,data):
		newnode=node(data)
		if self.head is None:
			self.head=newnode
		else:
			current=self.head
			while current.getNext() is not None:
				current = current.getNext()
			current.setNext(newnode)

	def display(self):
		current = self.head
		while current is not None:
			print current.getData()
			current = current.getNext()

def linkedlistmanip():
	 choice=0
	 list=linkedlist()
	 while choice !=3:
	 	choice=eval(raw_input("1. Insert At Front\t2.Insert in order\t3.Insert At End\t4. Print\t3. Exit\nEnter your choice:"))
	 	if choice==1:
	 		data=eval(raw_input("Enter the data:"))
	 		list.insertAtFront(data)
	 	elif choice==2:
	 		data=eval(raw_input("Enter the data:"))
	 		list.insert(data)
	 	elif choice==3:
	 		data=eval(raw_input("Enter the data:"))
	 		list.insertAtEnd(data)
	 	elif choice==4:
	 		list.display()
	 	else:
	 		exit()

linkedlistmanip()






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

	def insert(self,data):
		newnode=node(data)
		newnode.setNext(self.head)
		self.head=newnode

	def display(self):
		current = self.head
		while current is not None:
			print current.getData()
			current = current.getNext()

def linkedlistmanip():
	 choice=0
	 list=linkedlist()
	 while choice !=3:
	 	choice=eval(raw_input("1. Insert\t2. Print\t3. Exit\nEnter your choice:"))
	 	if choice==1:
	 		data=eval(raw_input("Enter the data:"))
	 		list.insert(data)
	 	elif choice==2:
	 		list.display()
	 	else:
	 		exit()

linkedlistmanip()






class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            temp = self.head
            while temp:
                print(temp.data ,'-->', end=' ')
                temp = temp.ref
    def add_new(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('The node is not empty')

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            else:
                n = n.ref
        if n is None:
            print('The Given Node is not Present')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self,data,x):
        if self.head is None:
            print('There is NO Linked List')
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            else:
                n = n.ref
        if n.ref is None:
            print("No NODE found !")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


linkedlist = LinkedList()

exit = False
while exit == False:
    process = input("\n Enter the place where you need to add an element in the linked list or EXIT ['new','begning','end','after','before','exit'] :")
    if process.lower() == 'new':
        data = int(input('Enter the number you need to add in the new list :'))
        linkedlist.add_new(data)
        linkedlist.display()
    elif process.lower() == 'begning':
        data = int(input('Enter the number you need to add in the begning :'))
        linkedlist.add_begin(data)
        linkedlist.display()
    elif process.lower() == 'end':
        data = int(input('Enter the number you need to add in the end :'))
        linkedlist.add_end(data)
        linkedlist.display()
    elif process.lower() == 'after':
        data = int(input('Enter the number you need to add after:'))
        x = int(input('Enter the node :'))
        linkedlist.add_after(data,x)
        linkedlist.display()
    elif process.lower() == 'before':
        data = int(input('Enter the number you need to add before:'))
        x = int(input('Enter the node :'))
        linkedlist.add_before(data,x)
        linkedlist.display()
    elif process.lower() == 'exit':
        exit = True

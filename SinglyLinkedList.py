# Creating a Node
from pickle import NONE


class Node:
    def __init__(self,data):
        self.data = data #The value of the node
        self.ref = None #The adress of the node

class LinkedList:
    def __init__(self):
        self.head = None #The adress of the current node

    #Function to Display the list
    def display(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            temp = self.head
            while temp:
                print(temp.data ,'-->', end=' ')
                temp = temp.ref

    #Adding the element to an empty list
    def add_new(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('The node is not empty')

    #Adding the element at the begning of the list
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    #Adding the element at the end of the list
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    #Adding the element after an element
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

    #Adding the element before an element
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

    #Removing a element in the begning of the linked list
    def remove_begin(self):
        if self.head is None:
            print('There is no Linked List')
        else:
            self.head = self.head.ref

    #removnig an element in the end of the Linked List
    def remove_end(self):
        if self.head is None:
            print('There is no Linked List')
        else:
            n = self.head
            f = n.ref
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    
    #Removing at the given position
    def remove_position(self,x):
        n = self.head
        if self.head is None:
            print('There is no Linked List')
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print('No NODE is found')
        else:
            n.ref = n.ref.ref

        


linkedlist = LinkedList()

exit = False
while exit == False:
    add_remove = input('\nAdd or Delete or Exit ?  :')

    if add_remove.lower() == 'add':
        process = input("\nWhere do you need to perforn the action ['new','begning','end','after','before','exit'] :")
        if process.lower() == 'new':
            data = input('Enter the number you need to add in the new list :')
            linkedlist.add_new(data)
            linkedlist.display()
        elif process.lower() == 'begning':
            data = input('Enter the number you need to add in the begning :')
            linkedlist.add_begin(data)
            linkedlist.display()
        elif process.lower() == 'end':
            data = input('Enter the number you need to add in the end :')
            linkedlist.add_end(data)
            linkedlist.display()
        elif process.lower() == 'after':
            data = input('Enter the number you need to add after:')
            x = input('Enter the node :')
            linkedlist.add_after(data,x)
            linkedlist.display()
        elif process.lower() == 'before':
            data = input('Enter the number you need to add before:')
            x = input('Enter the node :')
            linkedlist.add_before(data,x)
            linkedlist.display()
    
    elif add_remove.lower() == 'delete':
        process = input("\nWhere do you need to perforn the action ['begning','end','position','exit'] :")
        if process.lower() == 'begning':
            linkedlist.remove_begin()
            linkedlist.display()
        elif process.lower() == 'position':
            f = input('Enter the element you want to remove :')
            linkedlist.remove_position(f)
            linkedlist.display()
        elif process.lower() == 'end':
            linkedlist.remove_end()
            linkedlist.display()

    elif add_remove.lower() == 'exit':
        exit = True




class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display_forward(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            temp = self.head
            while temp:
                print(temp.data , '-->' , end = '  ')
                temp = temp.nref

    def display_backward(self):
        if self.head is None:
            print('There is no Linked List')
        else:
            temp = self.head
            while temp.nref:
                temp = temp.nref
            while temp:
                print(temp.data, '-->' , end = '  ')
                temp = temp.pref


    def add_new(self,x):
        if self.head is None:
            new_node = Node(x)
            self.head = new_node
        else:
            print('The Linked List is not Empty')
    
    def add_begning(self,x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self,x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref

            n.nref = new_node
            new_node.pref = n

    def add_after(self,data,x):
        n = self.head
        if self.head is None:
            print('The Linked List is Empty ')
        else:
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            
            if n is None:
                print('There is NO such Node')
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node


    def add_before(self,data,x):
        n = self.head
        if self.head is None:
            print('The Linked List is Empty ')
        else:
            new_node = Node(data)
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print('There is No such NODE')
            else:
                new_node.nref = n
                new_node.pref = n.pref
                if n is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node


    def remove_begning(self):
        if self.head is None:
            print('THe Linked List is Empty')
        else:
            n = self.head
            n.nref.pref = None
            self.head = n.nref

    def remove_end(self):
        if self.head is None:
            print('The Linked List is Empty')
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            if self.head == n:
                self.head = None
            else:
                n.pref.nref = None
    def remove_position(self,x):
        if self.head is None:
            print('The Linked List is Empty')
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print('The Given Node is not present')
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
        
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print('The Given Node is not Present')


linkedlist = DoublyLinkedList()



exit = False
while exit == False:
    add_remove = input('\nAdd or Delete or Exit ?  :')

    if add_remove.lower() == 'add':
        process = input("\nWhere do you need to perforn the action ['new','begning','end','after','before','exit'] :")
        if process.lower() == 'new':
            data = input('Enter the number you need to add in the new list :')
            linkedlist.add_new(data)
            linkedlist.display_forward()
        elif process.lower() == 'begning':
            data = input('Enter the number you need to add in the begning :')
            linkedlist.add_begning(data)
            linkedlist.display_forward()
        elif process.lower() == 'end':
            data = input('Enter the number you need to add in the end :')
            linkedlist.add_end(data)
            linkedlist.display_forward()
        elif process.lower() == 'after':
            data = input('Enter the number you need to add after:')
            x = input('Enter the node :')
            linkedlist.add_after(data,x)
            linkedlist.display_forward()
        elif process.lower() == 'before':
            data = input('Enter the number you need to add before:')
            x = input('Enter the node :')
            linkedlist.add_before(data,x)
            linkedlist.display_forward()
    
    elif add_remove.lower() == 'delete':
        process = input("\nWhere do you need to perforn the action ['begning','end','position','exit'] :")
        if process.lower() == 'begning':
            linkedlist.remove_begning()
            linkedlist.display_forward()
        elif process.lower() == 'position':
            f = input('Enter the element you want to remove :')
            linkedlist.remove_position(f)
            linkedlist.display_forward()
        elif process.lower() == 'end':
            linkedlist.remove_end()
            linkedlist.display_forward()

    elif add_remove.lower() == 'exit':
        exit = True





class StackOverflowError(Exception):
    pass

class StackUnderflowError(Exception):
    pass


class Stack():

    def __init__(self):
        self.stacks = []
        self.length = int(input('length of your Stack :'))
    
    def push(self,x):
        if len(self.stacks) >= self.length:
            raise StackOverflowError

        self.stacks.append(x)
        print(self.stacks)

    
    def pop(self):
        if len(self.stacks) <= 0:
            raise StackUnderflowError

        self.stacks.pop()
        print(self.stacks)


stack = Stack()

exit = False
while exit == False:
    q = input('Enter the operation you have to do [push,pop,exit] :')
    if q == 'push':
        f = input('enter the element to be pushed :')
        stack.push(f)
    elif q == 'pop':
        stack.pop()
    elif q == 'exit':
        exit = True

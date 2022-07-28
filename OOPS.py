'''Expirement 1'''



# class Circle:
#     def __init__(self,r):
#         self.r = r
#     def area(self):
#         a = round(3.14*self.r**2)
#         return f'The area is :{a} {u} sqr'
#     def circumfrence(self):
#         c = round(2*3.14*self.r)
#         return f'The circumfrence is :{c} {u}'

# r = int(input('Enter radious :'))
# u = input('Units :')
# obj = Circle(r)
# x = obj.area()
# y = obj.circumfrence()
# print(x)
# print(y)


# class CharDiv:
#     def __init__(self,strings,k):
#         self.strings = strings
#         self.k = k 
#     def multiple(self):
#         for i in range(1, len(self.strings)):
#             if 1 % self.k == 0:
#                 print(f'The character in index is divisible by k is {self.strings[i-1]}')

# k = int(input("Enter the number for which the index of multiples should be returned :"))
# strings = input('Enter a string :')
# obj = CharDiv(strings,k)
# obj.multiple()


'''Stack'''

from os import remove


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
        exti = True


'''Queue'''

class QueueOverflowError(Exception):
    pass

class QueueUnderflowError(Exception):
    pass


class Queue():

    def __init__(self):
        self.queues = []
        self.length = int(input('length of your Queue :'))
    
    def enqueue(self,x):
        if len(self.queues) >= self.length:
            raise QueueOverflowError

        self.queues.append(x)
        print(self.queues)

    
    def dequeue(self):
        if len(self.queues) <= 0:
            raise QueueUnderflowError

        self.queues.pop(0)
        print(self.queues)


queue = Queue()

exit = False
while exit == False:
    q = input('Enter the operation you have to do [enqueue,dequeue,exit] :')
    if q == 'enqueue':
        f = input('enter the element to be pushed :')
        queue.enqueue(f)
    elif q == 'dequeue':
        queue.dequeue()
    elif q == 'exit':
        exti = True


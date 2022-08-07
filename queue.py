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
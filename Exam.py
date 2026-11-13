'''Suppose you are building software for a hardware-handling technician. The software receives a list of hardware devices:

Mouse, Keyboard, CPU, Chromebook, Laptop

Create a Queue data structure to handle the technician's work in FIFO order.

Your task:
1. Select a suitable Queue implementation.
2. Write Python code to insert all five devices into the Queue.
3. Perform two dequeue operations.
4. Display the remaining devices.
5. Explain why Queue is suitable for this scenario.'''
#Create a Class
class queue:
    def __init__(self,size):
        self.data = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1
 #Write Python code to insert all five devices into the Queue. enque krnay kaliya
    def enqueue(self,value):# to add element in rear(tail)
        if self.rear == self.size - 1:
            print("queue overflow there is  no place for new variables bcz queue is full")
        else:
            self.rear += 1
            self.data[self.rear] = value
    def dequeue(self): # to remove element from front(head)
        if self.front == self.rear:
            print("queue underfow there is  no thing to remove")
        else:
            self.front += 1
            return self.data[self.front]
    def peek(self):# to show fist element in the queue
        if self.front == self.rear:
            print("queue underfow there is  no thing to remove")
        else:
           
            return self.data[self.front + 1]
    def display(self):
        if self.front == self.rear:
            print("queue underfow there is  no thing to show")
        else:
            for i in range(self.front + 1, self.rear + 1):
                print(self.data[i], end=" ")
            print()
q = queue(5)
q.enqueue("mouse")
q.enqueue("keyboard")
q.enqueue("CPU")
q.enqueue("CHROMEBBOK")
q.enqueue("Laptop")
q.dequeue()
q.dequeue()
print(q.peek())
q.display()











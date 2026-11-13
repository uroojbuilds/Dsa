'''A university computer lab has one shared printer. Students send their print jobs in the following order:
1. Assignment.pdf
2. Report.docx
3. Notes.pdf
4. Project.pptx
5. Research.pdf
The printer processes jobs in FIFO (First In, First Out) order.

The queue has a fixed capacity of 5 jobs. After printing two jobs, two new students submit their jobs: Thesis.pdf and Slides.pptx.

Requirements:
1. Select a suitable data structure and explain why.
2. Implement a Circular Queue using an array of size 5.
3. Perform enqueue and dequeue operations.
4. Show the final array, front, rear, and remaining queue.'''
class Circular_queue:
    def __init__ (self,size):
        self.data = [None]*size
        self.size = size
        self.front = -1
        self.rear = -1
    def enqueue(self,value):
        if (self.rear + 1 ) % self.size == self.front:
            print("stack overflow ha bcz self.front agr last may tha tu ab woh  front kay equal aajay gha jaha pr element pr pra hua ha due tu circular")
            return
        if self.front == -1:
            self.front = 0 # yh sirf issliya kiya kay set krday kay jb b deque kra gay yhi say kra gay 
       
        self.rear = (self.rear + 1) % self.size
        self.data[self.rear] = value
    def dequeue(self):
        if self.front == -1:
            return None
        value = self.data[self.front]
        if self.rear == self.front:
           self.rear = self.front = -1
        else:
           self.front = (self.front +1) % self.size
        return value
    def display(self):
        if self.front == -1:
            print("empty")
        else:
            i = self.front
            while True:
                print(self.data[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1 )%self.size# dobara zero pay aane kaliya


q = Circular_queue(5)
q.enqueue("Assignment.pdf")
q.enqueue("Report.docx")
q.enqueue("Notes.pdf")
q.enqueue("Project.pptx")
q.enqueue("Research.pdf")
q.dequeue()
q.dequeue()
q.enqueue("Thesis.pdf")
q.enqueue("Slides.pptx")
q.display()

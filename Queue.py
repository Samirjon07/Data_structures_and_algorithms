class Queue:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size must be a positive integer")
        self.capacity = size
        self.queue =[None] *size
        self.front=-1
        self.rear= -1
        self.current_size=0


    def enqueue(self, data):
        if self.isFull():
            return
        if self.current_size==0:
            self.front=0
            self.rear=0
        else:
            self.rear=(self.rear+1)%self.capacity
        self.queue[self.rear]=data
        self.current_size+=1    


    def dequeue(self):
        if self.isEmpty():
            return None

        value = self.queue[self.front]      
        self.queue[self.front] = None       

        self.front = (self.front + 1) % self.capacity
        self.current_size -= 1

        if self.current_size == 0:
            self.front = -1
            self.rear = -1

        return value                       

            
    def isEmpty(self):
        return self.current_size==0
    
    def isFull(self):
        return self.current_size==self.capacity

    def size(self):
        return self.current_size
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[self.front]
    
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        print("Queue content (front to rear): ", end="")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()
    

if __name__ == "__main__":
    print("Queue Testing\n")
    q=Queue(5)
    print("Empty?", q.isEmpty())
    print("Size", q.size())

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)


    q.display()

    print("Dequeue:", q.dequeue())
    print("Dequeue:", q.dequeue())
    q.display()

    print("Current Size:", q.size())

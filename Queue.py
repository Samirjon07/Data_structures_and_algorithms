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
        if self.is_full():
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
            return
        self.front=(self.front+1)%self.capacity
        self.current_size-=1
        if self.current_size==0:
            self.front=-1
            self.rear=-1
            
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

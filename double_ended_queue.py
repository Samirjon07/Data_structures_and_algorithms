from Queue import Queue  # Import base Queue class


class DoubleEndedQueue(Queue):  # Inherit from Queue

    def __init__(self, size):  # constructor
        super().__init__(size)  # calling parent constructor
        self.current_size = 0  # adding size tracking


    def enqueue(self, data, position):  # Add element to deque
        if self.isFull():  # Check if full
            print("Deque is full")
            return

        if self.current_size == 0:  # First element
            self.front = 0
            self.rear = 0
            self.queue[self.front] = data

        elif position:  # Insert at rear
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = data

        else:  # Insert at front
            self.front = (self.front - 1 + self.capacity) % self.capacity
            self.queue[self.front] = data

        self.current_size += 1  #increase size


    def dequeue(self, position):  # Remove element
        if self.isEmpty():  #check empty
            print("Deque is empty")
            return

        if position:  # remove from front
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.capacity

        else:  # Remove from rear
            self.queue[self.rear] = None
            self.rear = (self.rear - 1 + self.capacity) % self.capacity

        self.current_size -= 1  #decrease size

        if self.current_size == 0:  #Reset if empty
            self.front = -1
            self.rear = -1


    def isEmpty(self):  #check whether empty
        return self.current_size == 0


    def isFull(self):  # Check full
        return self.current_size == self.capacity


    def size(self):  # Return size
        return self.current_size

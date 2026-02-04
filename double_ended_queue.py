from Queue import Queue

class DoubleEndedQueue(Queue):
    def __init__(self, size):
        super().__init__(size)

    def enqueue(self, data, position):
        if self.isFull():
            return
        if self.current_size == 0:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data

        else:
            if position:
                self.rear = (self.rear + 1) % self.capacity
                self.queue[self.rear] = data
            else:
                self.front = (self.front - 1 + self.capacity) % self.capacity
                self.queue[self.front] = data
        self.current_size += 1


    def dequeue(self, position):
        if self.isEmpty():
            return
        if position:
            self.front = (self.front + 1) % self.capacity
        else:
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.current_size -= 1
        if self.current_size == 0:
            self.front = -1
            self.rear = -1

    def peek_front(self):
        if self.isEmpty():
            return None
        return self.queue[self.front]
    
    def peek_rear(self):
        if self.isEmpty():
            return None
        return self.queue[self.rear]
    
if __name__ == "__main__":
    deq = DoubleEndedQueue(6)

    deq.enqueue(100, False)   # front
    deq.enqueue(200, True)    # rear
    deq.enqueue(50, False)    # front again
    deq.enqueue(300, True)    # rear

    print("Content front - rear:", [deq.queue[(deq.front + i) % deq.capacity] for i in range(deq.current_size)])

    deq.dequeue(True)   # remove front
    deq.dequeue(False)  # remove rear

    print("After two removes:", [deq.queue[(deq.front + i) % deq.capacity] for i in range(deq.current_size)])
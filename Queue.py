class Queue: # Defined a class called Queue

    def __init__(self, size): # constructor to create a queue with given size
        if size <= 0: # checking whether size is invalid
            raise ValueError("Size must be a positive integer") # stop program is invalid
        
        self.capacity = size # Maximum number of elements the queue can hold
        self.queue =[None] *size  #creates list with None
        self.front=-1 # Front index -1 , queue is empty
        self.rear= -1 # rear also index -1, queue is empty

    def isEmpty(self):  # function to check if queue is empty 
        return self.front == -1  # Queue is empty when front is -1


    def isFull(self):  # Function to check if queue is full
        return self.rear == self.capacity - 1  # Full when rear reaches last index
        


    def enqueue(self, data): # enqueue - add element at the rear
        if self.isFull(): # check whther queue is full or not 
            print("Queue is full")  # if full, says that it is full
            return  # stops the function

        if self.front == -1:  # check whether the queue is empty or not
            self.front = 0  # make front 0

        self.rear += 1  # move rear one step forward
        self.queue[self.rear] = data  #insert data at the position of the rear


    def dequeue(self): # dequeue - remove elemtn from the front
        if self.isEmpty(): # checks if queue is empty
            print("Queue is empty")  # print that it is empty
            return  #stop the function

        self.queue[self.front] = None  # remove the front element, it is now equal to NOne 

        self.front += 1  # move front one step forward

        # If all elements are removed, reset queue to empty state
        if self.front > self.rear:
            self.front = -1  # Reset front
            self.rear = -1  # Reset rear


    def size(self):  # Function to return number of elements in queue
        if self.isEmpty():  # If queue is empty
            return 0  # Size is 0
        return self.rear - self.front + 1  # Calculate number of elements


    def display(self):  # Function to print queue elements
        if self.isEmpty():  # Check if queue is empty
            print("Queue is empty")  # Print message
            return  # Stop function

        print("Queue content:", end=" ")  # Print heading

        for i in range(self.front, self.rear + 1):  # Loop from front to rear
            print(self.queue[i], end=" ")  # Print each element

        print()  # Move to next line


# Main program to test the queue
if __name__ == "__main__":
    print("Simple Queue Testing\n")  # Print title

    q = Queue(5)  # Create a queue of size 5

    print("Empty?", q.isEmpty())  # Check if empty
    print("Size:", q.size())  # Print size

    q.enqueue(10)  # Add 10
    q.enqueue(20)  # Add 20
    q.enqueue(30)  # Add 30
    q.enqueue(40)  # Add 40
    q.enqueue(50)  # Add 50
    q.enqueue(60)  # expriment: trying to add the element( will fail)

    q.display()  # Show queue

    q.dequeue()  # Remove front element
    q.dequeue()  # Remove next element

    q.display()  # Show queue after removal

    print("Current Size:", q.size())  # Print final size
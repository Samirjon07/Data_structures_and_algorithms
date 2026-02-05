from Queue import Queue  # importing Queue class

def reverseKElementsInQueue(k, q): # function that reverse first k elements
    if k <= 0 or k > q.size() or q.isEmpty(): # check invalid cases, used or - since one of the conditions should be true
        return q  # return unchanged queue
    
    stack = [] # temporary stack - it is just Python list

    for _ in range(k): # removing first k elements and push into stack
        value = q.queue[q.front]  # read front value directly
        q.dequeue()  # remove it from queue
        stack.append(value)  # push into stack


    while stack: # adding back reversed elements
        q.enqueue(stack.pop()) # pop from stack and enqueue


    remaining = q.size() - k # count remaing elments

    for _ in range(remaining):
        value = q.queue[q.front]  # Read front value
        q.dequeue()  # Remove it
        q.enqueue(value)  # adding to rear

    return q # returning modified queue



def print_queue(q): # helper fucntion to print queue 
    if q.isEmpty(): # check whether empty
        print("[]")
        return
    
    content = [] #temporary list to store values

   
    for i in range(q.front, q.rear + 1):  # Loop from front to rear
        content.append(q.queue[i])  # Add each element

    print(content)  # Print list

# Testing program
if __name__ == "__main__":
    q = Queue(10)  # Create queue

    # Add initial elements
    for x in [1, 10, 11, 100, 101]:
        q.enqueue(x)

    print("Original:")
    print_queue(q)

    reverseKElementsInQueue(3, q)

    print("\nAfter reversing first 3:")
    print_queue(q)                   




   
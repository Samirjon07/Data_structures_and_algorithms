from Queue import Queue

def reverseKElementsInQueue(k, q):
    if k <= 0 or k > q.size() or q.isEmpty():
        return q
    
    stack = []

    for _ in range(k):
        val = q.dequeue()
        stack.append(val)


    while stack:
        q.enqueue(stack.pop())


    remaining = q.size() - k
    for _ in range(remaining):
        val = q.dequeue()
        q.enqueue(val)

    return q



def print_queue(q):
    if q.isEmpty():
        print("[]")
        return
    content = []
    i = q.front
    for _ in range(q.current_size):
        content.append(q.queue[i])
        i = (i + 1) % q.capacity
    print(content)

q = Queue(10)
for x in [1, 10, 11, 100, 101]:
    q.enqueue(x)

print("Original:")
print_queue(q)                      

reverseKElementsInQueue(3, q)
print("\nAfter reverse first 3:")
print_queue(q)                      

print("\nAfter reverse first 0 (no change):")
reverseKElementsInQueue(0, q)
print_queue(q)

print("\nAfter reverse first 7 (larger than size):")
reverseKElementsInQueue(7, q)
print_queue(q)                       




   
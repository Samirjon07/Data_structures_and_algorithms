from queue import Queue

def reverseKELementsInQueue(q, k):
    if k<=0 or k>q.size() or q.isEmpty():
        return q
    s=q.size()
    stack=[]
    for _ in range(k):
        temp=q.peek()
        if temp is None:
            break
        stack.append(temp)
    while stack:
        q.enqueue(stack.pop())
    for _ in range(s - k):
        temp=q.peek()
        if temp is None:
            break
        q.dequeue()
        q.enqueue(temp)
    return q
from queue import Queue

def generateBinaryQueue(n):
    if n< 1:
        return Queue(0)
    q=Queue(n)
    for i in range(1, n+1):
        q.enqueue(bin(i)[2:])
    return q    
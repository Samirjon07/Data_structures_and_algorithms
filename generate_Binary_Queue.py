from Queue import Queue

def generateBinaryQueue(n):
    if n< 1:
        return Queue(0)
    q=Queue(n)
    for i in range(1, n+1):
        q.enqueue(bin(i)[2:])
    return q    

if __name__ == "__main__":
    q = generateBinaryQueue(6)
    print("Binary numbers from 1 to 6:")
    q.display()
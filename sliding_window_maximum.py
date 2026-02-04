from double_ended_queue import DoubleEndedQueue


def slidingWindowMaximum(Nums , k):
    if not nums or k<=0:
        return []
    
    n=len(Nums)
    if k>n:
        k=n

    deq=DoubleEndedQueue(n)
    result=[]

    for i in range(n):

        if not deq.isEmpty() and deq.peek_front()<=i-k:
            deq.dequeue(True)
        
        while not deq.isEmpty() and Nums[deq.peek_rear()]< Nums[i]:
            deq.dequeue(False)

        deq.enqueue(i, True)
        if i>=k-1:
            result.append(Nums[deq.peek_front()])

    return result
from double_ended_queue import DoubleEndedQueue


def slidingWindowMaximum(Nums , k):
    if not Nums or k<=0: #checking if the input is empty or window size is invlid 
        return []
    
    n=len(Nums)

    if k>n: # If window size is larger than array size , adjust window size to array size
        k=n

    deq=DoubleEndedQueue(n) # initialize the deque to store indices of array elemnts
    result=[]

    for i in range(n):
        # 1. Remove indices that are out of the current window
        if not deq.isEmpty() and deq.queue[deq.front] <= i - k:
            deq.dequeue(True) # True = remove from front
        
        # 2. Remove elements from rear that are smaller than current
        # (they can never be maximum while current is in window)
        while not deq.isEmpty() and Nums[deq.queue[deq.rear]] < Nums[i]:
            deq.dequeue(False) # False = remove from rear
        
        # 3. Add current index to rear
        deq.enqueue(i, True)
        
        # 4. After first k-1 elements, start collecting answers
        if i >= k - 1:
            result.append(Nums[deq.queue[deq.front]])
    
    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

# Calling the function
output = slidingWindowMaximum(nums, k)

# Printing the output
print(f"Input Nums: {nums}")
print(f"Input k: {k}")
print(f"Output: {output}")
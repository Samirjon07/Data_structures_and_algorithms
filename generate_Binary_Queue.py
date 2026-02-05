from Queue import Queue # importing Queue Class 

def generateBinaryQueue(n):# function to create queue of binary numbers
    if n< 1: # check if n is invalid
        return ValueError("n must be >=1") # will say that n must be more or equal to 1
    q=Queue(n)  # create a queue with capeacity n

    for i in range(1, n+1): # loop from 1 to n
        q.enqueue(bin(i)[2:]) # convert number to binary string 
    return q    # return the added queue


# testing program 
if __name__ == "__main__":
    q = generateBinaryQueue(6) # create binary queue

    print("Binary numbers from 1 to 6:") # just printing
    q.display() # display queue , uses function what was created 
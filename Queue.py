class Queue:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size must be a positive integer")

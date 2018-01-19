def class SLNode:
    def __init__(self, data):
        self.data = data
        self.front = None # can't use "next" - used by python.

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        pass

def class SLList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def get(i):
        '''SL.get(int) -> value

        Returns the value stored at index, i. Returns None if i is an
        invalid index. Only non-negative indexes are allowed.

        Runs in O(i) time.
        '''
        pass

    def set(i, x):
        '''SL.set(int, value) -> bool

        Sets the element at index, i, to x and returns True. Does not
        set and returns False if i is invalid. Only non-negative
        indexes are allowed.

        Runs in O(i) time.
        '''
        pass

    def add(i, x):
        '''SL.add(int, value) -> bool

        Inserts x at index, i, and returns True. Does not insert x and
        returns False if i is invalid. Only non-negative indexes are
        allowed.

        Runs in O(i) time.
        '''
        pass

    def remove(i):
        '''SL.remove(int) -> value

        Removes the element at index, i, and returns it. Returs None
        if i is an invalid index. Only non-negative indexes are
        allowed.

        Runs in O(i) time.
        '''
        pass
    

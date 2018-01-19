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

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        pass

    def get(self, i):
        '''SL.get(int) -> value

        Returns the value stored at index, i.
        Returns None if i \notin {0, ..., n-1}.

        Runs in O(i) time.
        '''
        pass

    def set(self, i, x):
        '''SL.set(int, value) -> bool

        Sets the element at index, i, to x and returns True.
        Returns False if i \notin {0, ..., n-1}.

        Runs in O(i) time.
        '''
        pass

    def add(self, i, x):
        '''SL.add(int, value) -> bool

        Inserts x at index, i, and returns True.
        Returns False if i \notin {0, ..., n-1}.

        Runs in O(i) time.
        '''
        pass

    def remove(self, i):
        '''SL.remove(int) -> value

        Removes the element at index, i, and returns it.
        Returns None if i \notin {0, ..., n-1}.

        Runs in O(i) time.
        '''
        pass
    

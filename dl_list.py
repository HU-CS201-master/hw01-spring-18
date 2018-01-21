class DLNode:
    def __init__(self, data):
        self.data = data
        self.front = self.back = None

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        pass

class DLList:
    def __init__(self):
        '''Initializes the dummy node and size.'''
        pass

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        pass

    def get(self, i):
        '''DL.get(int) -> value

        Returns the value stored at index, i.
        Returns None if i \notin {-n, ... , n-1}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        pass

    def set(self, i, x):
        '''DL.set(int, value) -> bool

        Sets the element at index, i, to x and returns True.
        Returns False if i \notin {-n, ... , n-1}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        pass

    def add(self, i, x):
        '''DL.add(int, value) -> bool

        Inserts x at index, i, and returns True.
        Returns False if i \notin {0, ... , n}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        pass

    def remove(self, i):
        '''DL.remove(int) -> value

        Removes the element at index, i, and returns it.
        Returs None if i \notin {0, ... , n-1}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        pass

    '''The next few methods involve performing manipulations on
    DLLists. You should complete them without allocating any new nodes
    or temporary arrays. They can all be done only by changing the
    value of front and back in existing nodes.
    '''
    
    def is_palindrome(self):
        '''As described in Exercise 3.7.
        '''
        pass
    
    def truncate(self):
        '''As described in Exercise 3.9.
        '''
        pass
    
    def absorb(self):
        '''As described in Exercise 3.10.

        Your code should run in O(1) time.
        '''
        pass
    
    def reverse(self):
        '''As described in Exercise 3.12.

        Your code should run in O(n) time.
        '''
        pass

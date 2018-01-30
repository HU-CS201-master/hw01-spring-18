class SLNode:
    def __init__(self, data):
        self.data = data
        self.front = None # can't use "next" - used by python.

    def __str__(self):
        '''N.__str__() -> str

        Returns a string representation of N for print(). Called
        automatically.

        >>> N = SLNode(4)
        >>> print(N)
        4/
        '''
        s = '{}'.format(self.data)
        if self.front:
            s += '->'
        else:
            s += '/'
        return s
    
    def __repr__(self):
        '''N.__repr__() -> str

        Returns a string representation of N for interactive
        mode. Called automatically.

        >>> N = SLNode(4)
        >>> N
        4/
        '''
        return '{}'.format(self)

    def ahead(self, n):
        '''N.ahead(int) -> SLNode

        Returns the SLNode that is n SLNodes in front of N.

        >>> N = SLNode(4)
        >>> N.front = SLNode(5)
        >>> m = N.ahead(1)
        >>> m
        5/
        '''
        if n == 0:
            return self
        if n < 0:
            raise Exception("Cannot advance SLNode by a -ve number.")
        if not self.front:
            raise Exception("Cannot advance missing SLNode.")
        return self.front.ahead(n-1)
    
class SLList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        if not self.head:
            return '/'
        temp = self.head
        s = ''
        while temp:
            s += '{}'.format(temp)
            temp = temp.front
        return s

    def __repr__(self):
        '''Returns a representation of an object for interactive mode.
        '''
        return self.__str__()
    
    def get(self, i):
        '''SL.get(int) -> value

        Returns the value stored at index, i.
        Returns None if i \notin {0, ..., n-1}.

        Runs in O(i) time.
        '''
        if i < 0 or i >= self.size:
            return
        return self.head.ahead(i).data
    
    def set(self, i, x):
        '''SL.set(int, value) -> bool

        Sets the element at index, i, to x and returns True.
        Returns False if i \notin {0, ..., n-1}.

        Runs in O(i) time.
        '''
        if i < 0 or i >= self.size:
            return False
        self.head.ahead(i).data = x
        return True

    def add(self, i, x):
        '''SL.add(int, value) -> bool

        Inserts x at index, i, and returns True.
        Returns False if i \notin {0, ..., n}.

        Runs in O(i) time.
        '''
        if i < 0 or i > self.size:
            return False
        add_me = SLNode(x)
        if not self.size:  # Empty list.
            self.head = self.tail = add_me
        elif i == 0:  # Adding at head.
            add_me.front = self.head
            self.head = add_me
        elif i == self.size:  # Adding at the end.
            self.tail.front = add_me
            self.tail = add_me
        else:  # Adding in between.
            prev = self.head.ahead(i-1)
            add_me.front = prev.front
            prev.front = add_me
        self.size += 1
        return True

    def remove(self, i):
        '''SL.remove(int) -> value

        Removes the element at index, i, and returns it.
        Returns None if i \notin {0, ..., n-1}.

        Runs in O(i) time.
        '''
        if i < 0 or i >= self.size:
            return
        if self.size == 1:  # Removing the only element.
            data = self.head.data
            self.head = self.tail = None
        elif i == 0:  # Removing head.
            data = self.head.data
            self.head = self.head.front
        else:  # Removing from the rest of the list.
            # Get to previous node to the one to remove and update links.
            prev = self.head.ahead(i-1)
            remove_me = prev.front
            data = remove_me.data
            prev.front = remove_me.front
            if i == self.size-1:  # Tail is being removed.
                self.tail = prev
        self.size -= 1
        return data
    

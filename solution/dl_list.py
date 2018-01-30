class DLNode:
    def __init__(self, data):
        self.data = data
        self.front = self.back = None

    def __str__(self):
        '''N.__str__() -> str

        Returns a string representation of N for print(). Called
        automatically.

        >>> N = DLNode(4)
        >>> print(N)
        /4/
        '''
        d = {None: '/'}
        back_symbol = d.get(self.back, '<-')
        front_symbol = d.get(self.front, '->')
        s = '{}'.format(self.data)
        s = back_symbol + s + front_symbol
        return s
    
    def __repr__(self):
        '''N.__repr__() -> str

        Returns a string representation of N for interactive
        mode. Called automatically.

        >>> N = DLNode(4)
        >>> N
        /4/
        '''
        return '{}'.format(self)

    def ahead(self, n):
        '''N.ahead(int) -> DLNode

        Returns the DLNode, M, which is n DLNode's in front of N. If n
        is negative then M is n DLNode's to the back of N.

        >>> N = DLNode(4)
        >>> N.front = SLNode(5)
        >>> m = N.ahead(1)
        >>> m
        <-5/
        >>> m = m.ahead(-1)
        >>> m
        /4->
        '''
        if n == 0:
            return self
        if n < 0:
            if not self.back:
                raise Exception("Cannot regress missing DLNode.")
            return self.back.ahead(n+1)
        if not self.front:
            raise Exception("Cannot advance missing DLNode.")
        return self.front.ahead(n-1)
    
class DLList:
    def __init__(self):
        '''Initializes the dummy node and size.'''
        self.dummy = DLNode(None)
        self.dummy.front = self.dummy
        self.dummy.back = self.dummy
        self.size = 0
        
    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        temp = self.dummy.front
        s = ''
        while temp != self.dummy:
            s += '{}'.format(temp)
            temp = temp.ahead(1)
        return s

    def __repr__(self):
        '''Returns a representation of an object for interactive mode.
        '''
        return self.__str__()
    
    def get(self, i):
        '''DL.get(int) -> value

        Returns the value stored at index, i.
        Returns None if i \notin {-n, ... , n-1}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        if i < -self.size or i >= self.size:
            return
        if i >= 0:
            i += 1
        return self.dummy.ahead(i).data

    def set(self, i, x):
        '''DL.set(int, value) -> bool

        Sets the element at index, i, to x and returns True.
        Returns False if i \notin {-n, ... , n-1}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        if i < -self.size or i >= self.size:
            return False
        if i >= 0:
            i += 1
        self.dummy.ahead(i).data = x
        return True
    
    def add(self, i, x):
        '''DL.add(int, value) -> bool

        Inserts x at index, i, and returns True.
        Returns False if i \notin {-n, ... , n}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        if not -self.size <= i <= self.size:
            return False
        add_me = DLNode(x)
        prev = self.dummy.ahead(i)
        add_me.front = prev.front
        prev.front.back = add_me
        prev.front = add_me
        add_me.back = prev
        self.size += 1
        return True

    def remove(self, i):
        '''DL.remove(int) -> value

        Removes the element at index, i, and returns it.
        Returs None if i \notin {-n, ... , n-1}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        if not -self.size <= i < self.size:
            return
        prev = self.dummy.ahead(i)
        remove_me = prev.ahead(1)
        prev.front = remove_me.front
        remove_me.front.back = prev
        self.size -= 1
        return remove_me.data

    '''The next few methods involve performing manipulations on
    DLLists. You should complete them without allocating any new nodes
    or temporary arrays. They can all be done only by changing the
    value of front and back in existing nodes.
    '''
    
    def is_palindrome(self):
        '''As described in Exercise 3.7.
        '''
        n = self.size//2
        t1 = t2 = self.dummy
        for _ in range(n):
            t1 = t1.back
            t2 = t2.front
            if t1.data != t2.data:
                return False
        return True
    
    def truncate(self, i):
        '''As described in Exercise 3.9.
        '''
        # Assumes that i is a valid index.
        if i <= self.size-i:
            skip = i
        else:
            skip = i-self.size-1
        last = self.dummy.ahead(skip)
        last.front = self.dummy
        self.dummy.back = last
        self.size = i
        
    def absorb(self, l2):
        '''As described in Exercise 3.10.

        Your code should run in O(1) time.
        '''
        last = self.dummy.back
        l2_first = l2.dummy.front
        l2_last = l2.dummy.back
        last.front = l2_first
        l2_first.back = last
        l2_last.front = self.dummy
        self.dummy.back = l2_last
        self.size += l2.size
        
    def reverse(self):
        '''As described in Exercise 3.12.

        Your code should run in O(n) time.
        '''
        node = self.dummy
        for _ in range(self.size+1):
            node.front, node.back = node.back, node.front
            node = node.front
    

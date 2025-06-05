
""" linked_list.py

Student: Albin Svensson 
Mail: Albin.svensson.7131@student.uu.se
Reviewed by: Divya
Date reviewed:2024-10-09
"""

class ExceptionError(Exception):
    def __init__(self, msg):
        self.msg = msg

class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False
    
    ### A5 BEGIN ###
    def __getitem__(self, index): #method to get the element at a specific index
        ind = 0
        for x in self:
            if ind == index:
                return x
            ind += 1
        raise ExceptionError(f'Index out of range: {index}')
    
    def __setitem__(self, index, value):                 ##### A6
        """ Store value at position index.
            ExamException if index < 0 or index >= n where n
            is the length of the list."""
        if index < 0 or index >= self.length():
            raise ExceptionError(f'Index out of range: {index}')
        f = self.first
        ind = 0

        while f is not None:
            if ind == index:
                f.data = value
                return
            f = f.succ
            ind += 1
        raise ExceptionError(f'Index out of range: {index}')
        
    ### A5 END ###

    def insert(self, x):
        if self.first is None or x <= self.first.data: #Insert at the beginning of the list
            self.first = self.Node(x, self.first)
        else: #Insert somewhere else
            f = self.first #f is the current node
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self): 
        count = 0
        f = self.first
        while f:
            count += 1
            f = f.succ
        return count

    def mean(self):               
        if self.first is None:
            raise ValueError("The list is empty")
        
        total_sum = 0
        count = 0
        f = self.first

        while f is not None:
            total_sum += f.data
            count += 1
            f = f.succ
        
        return total_sum / count

    def remove_last(self):       
        if self.first is None: #Base case 0
            raise ValueError("The list is empty")
            
        if self.first.succ is None: #Base case 1
            value = self.first.data
            self.first = None
            return value

        f = self.first #General case
        while f.succ.succ:
            f = f.succ

        value = f.succ.data
        f.succ = None
        return value

    def remove(self, x):         
        
        if self.first is None: #empty list
            return False

        if self.first.data == x: #if first element is x 
            self.first = self.first.succ
            return True

        f = self.first
        while f.succ:
            if f.succ.data == x:
                f.succ = f.succ.succ
                return True
            f = f.succ

        return False
    
    def to_list(self): 
        def _to_list(node):
            if node is None: #base case
                return []
            return [node.data] + _to_list(node.succ) #recursive case
        
        return _to_list(self.first)

    def remove_all(self, x):      
        def _remove_all(node, count): #helper method
            if node is None: #base case
                return None, count
            if node.data == x: #recursive case
                next_node, count = _remove_all(node.succ, count + 1)
                return next_node, count
            else:
                node.succ, count = _remove_all(node.succ, count)
                return node, count
        
        self.first, count = _remove_all(self.first, 0)
        return count
        
    
    def __str__(self):            

        return f"({', '.join(map(str, self))})" #map applies str to all elements in the list

    #def copy(self):               # Compulsary
        #result = LinkedList()
        #for x in self:
            #result.insert(x)
        #return result
    ''' Complexity for this implementation:
        Iteration: Iterating through the list has a complexity of O(n), where n is the number of elements.
        Insertion: Each insertion has a complexity of O(n) because it may require scanning the entire list.
        Total Complexity: The total complexity is O(n^2) because you have to insert n elements, each taking O(n) time.
    '''
    def copy(self): # Using recursion, linear time and space complexity
        result = LinkedList() #new list

        def _copy_nodes(node): # Helper function 
            if node is None:  # Base case
                return None
            else:
                # Create a new node with the same data, recursively copy the next node
                return LinkedList.Node(node.data, _copy_nodes(node.succ)) # Recursive case

        result.first = _copy_nodes(self.first) 
        return result
    ''' Complexity for this implementation:
        Iteration: Iterating through the list has a complexity of O(n), where n is the number of elements.
        Node Creation: Creating new nodes has a constant complexity of O(1) for each node.
        Total Complexity: The total complexity is O(n) because you iterate through n elements, each taking O(1) time to create a new node.
    '''

    def append(self, x):
        self.first = self._append(self.first, x)
    
    def _append(self, f, x): #helper method
        if f is None:
            return self
        else:
            f.succ = self._append(f.succ, x)
            return f

def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()

    # Test code:
    #print(lst.to_list())

    

if __name__ == '__main__':
    main()

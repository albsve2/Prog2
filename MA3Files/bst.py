""" bst.py

Student: Albin Svensson 
Mail: Albin.svensson.7131@student.uu.se
Reviewed by: Divya
Date reviewed:2024-10-09
"""

import random
from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  
        return r
    
    
    def __getitem__(self, index):
        def _in_order(node):
            if node is None:
                return []
            return _in_order(node.left) + [node.key] + _in_order(node.right)

        sorted_keys = _in_order(self.root)
        if index < 0 or index >= len(sorted_keys):
            raise IndexError(f"Tree index out of range: {index}")
        return sorted_keys[index]

    def __setitem__(self, index, value):
        def _in_order(node):
            if node is None:
                return []
            return _in_order(node.left) + [node] + _in_order(node.right)

        nodes = _in_order(self.root)
        if index < 0 or index >= len(nodes):
            raise IndexError(f"Tree index out of range: {index}")
        
        nodes[index].key = value


    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k): 
        def _contains(node, k):
            if not node:
                return False
            if k == node.key:
                return True
            elif k < node.key:
                return _contains(node.left, k)
            else:
                return _contains(node.right, k)
        return _contains(self.root, k)


    def size(self):
        return self._size(self.root)

    def _size(self, r): #count of nodes in the tree
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):             
        return self._height(self.root)
    
    def _height(self, r): #helper method
        if r is None:
            return 0
        else:
            return 1 + max(self._height(r.left), self._height(r.right))             

    def remove(self, key): 
        self.root = self._remove(self.root, key)

    def _remove(self, r, k): #helper method r-node, k-key
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)# r.left = left subtree with k removed

        elif k > r.key:
            r.right = self._remove(r.right, k) # r.right =  right subtree with k removed

        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                succ = r.right
                while succ.left is not None: # while r.right.left is not None, move left
                    succ = succ.left

                r.key = succ.key

                r.right = self._remove(r.right, succ.key)
                
        return r  

    def __str__(self):                            
        elements = list(self)
        return f"<{', '.join(map(str, elements))}>" #Returns a string representation of the tree, with a separator between elements
        #map applies the str function to each element in the list

    def to_list(self):                      #      
        
        def _to_list(node): #Complexity is O(n) because we do a constant amout of work for each node two recursive calls per node

            if node == None:
                return []     
            
            left_node = _to_list(node.left) 

            right_node = _to_list(node.right)     #Goes all the way down left side and works like the height method

            return left_node + [node.key] + right_node

        return _to_list(self.root)



    def to_LinkedList(self): #Complexity is O(n) because we do a constant amout of work for each node two recursive calls per node               
        linked_list = LinkedList()  # New list to store the keys
         
        def _to_LinkedList(node, linked_list): # current node, list thats being built
            if node:  # If the current node is not None
                _to_LinkedList(node.left, linked_list)  # Traverse left subtree
                linked_list.insert(node.key)  # Insert the current node's key into the LinkedList
                _to_LinkedList(node.right, linked_list)  # Traverse right subtree               

        _to_LinkedList(self.root, linked_list)  #In-order traversal
        return linked_list # Return the linked list

    
    ### A6 BEGIN ###
    def sum_level(self, level): #sum of keys on each level of the tree
        def _sum_level(node, l):
            if node is None:
                return 0
            if l == level:
                return node.key
            else:
                return _sum_level(node.left, l+1) + _sum_level(node.right, l+1)
        return _sum_level(self.root, 0)
    # A6 END ###
    ### A7 BEGIN ###
    def nodes_on_level(level): #count of nodes on each level of the tree
        def _nodes_on_level(node, l):
            if node is None:
                return 0
            if l == level:
                return 1
            else:
                return _nodes_on_level(node.left, l+1) + _nodes_on_level(node.right, l+1)
        return _nodes_on_level(self.root, 0)
    # A7 END ###
    def count_leaves(self):
        """ Returns the number of leaves """
        return self._count_leaves(self.root)

    def _count_leaves(self, r): #number of leaves in the tree
        
        if not r:
            return 0
        else:
            if r.left or r.right:
                return self._count_leaves(r.left) + self._count_leaves(r.right)
            else:
                return 1


    def sum_nodes(self): #sum of all keys in the tree
        def _sum_nodes(node):
            if node is None:
                return 0
            return node.key + _sum_nodes(node.left) + _sum_nodes(node.right)
        return _sum_nodes(self.root)

    def __eq__(self, t): #if two trees contain the same key return True, otherwise False
        """ A8: Overloading =="""
        return str(self) == str(t)

def random_tree(n):                               # Useful
    bst = BST()
    while bst.size() < n:
        bst.insert(random.randint(0, 100))
    return bst


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")

    

if __name__ == "__main__":
    main()
    

"""
What is the generator good for?
==============================

1. computing size?
You can use the generator to iterate through the tree and count the number of elements in the tree.

2. computing height?
No. The height of the tree is typiclly computed recursively.

3. contains?
You can use the generator to iterate through the tree and check if the key is in the tree.

4. insert?
No. The generator is used to iterate through the tree, not modify it.

5. remove?
Similar to insert, the generator is used to iterate through the tree, not modify it.

"""

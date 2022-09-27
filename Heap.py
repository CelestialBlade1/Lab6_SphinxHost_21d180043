#---------------------------Heap-----------------------------------------------------------
class Heap:
    """| The Heap is a special kind of a binary tree which maintains a notion of priority. It follows two important rules.
    The children of a node in a Heap have lesser priority (higher prioirity value) than the node itself. Moreover, Heaps are left-filled.
    This is an array implementation of the Heap.
    | The heap is equipped with functions of parent, left, right, insert, min, heapify and deleteMin
    :param M: A limit on the total number of elements in the array
    :type M: int
    :param H: The array modelling the heap.
    :type H: list
    :param n: The current number of elements in the heap
    :type n: int
    """

    def __init__(self, cap):
        """Constructor Method.
        Generates a Heap with a maximum number of elements as given.
        :param cap: Upper limit on number of nodes
        :type cap: int
        :Example:
            >>> H = Heap(40)
            >>> H.H = [1, 2, 4]
            >>> H.n = 3
            >>> print(H.H, H.n)
            [1, 2, 4] 3
        """
        self.H = []
        self.n = 0
        self.M = cap
    
    def parent(self, i):
        """Function gives the index of the parent of the node at the current index

        :param i: Index of the node whose parent is required
        :type i: int 
        :return: Index of Parent
        :rtype: int
        :Example:
            >>> H = Heap(40)
            >>> H.H = [1, 2, 4, 7, 8, 5, 6]
            >>> H.n = 7
            >>> print(H.parent(3))
            1
        """
        return (i - 1) // 2
    
    def left(self, i):
        """| Function gives the index of the left-child of the node at the current index
        :param i: Index of the node whose left-child is required
        :type i: int 
        :return: Index of Left-Child
        :rtype: int
        :Example:
            >>> H = Heap(40)
            >>> H.H = [1, 2, 4, 7, 8, 5, 6]
            >>> H.n = 7
            >>> print(H.left(2))
            5
        """
        return (2 * i) + 1
    
    def right(self, i):
        """| Function gives the index of the Right-Child of the node at the current index
        :param i: Index of the node whose Right-Child is required
        :type i: int 
        :return: Index of Right-Child
        :rtype: int
        :Example:
            >>> H = Heap(40)
            >>> H.H = [1, 2, 4, 7, 8, 5, 6]
            >>> H.n = 7
            >>> print(H.right(1))
            4
        """
        return 2 * (i + 1)
    
    def insert(self, val):
        """| Inserts into heap a new node
        :param val: Value to be inserted
        :type val: int or float 
        :Example:
            >>> H = Heap(40)
            >>> H.insert(1)
            >>> H.insert(5)
            >>> H.insert(4)
            >>> H.insert(3)
            >>> print(H.H)
            [1, 3, 4, 5]
        """
        if self.n != self.M:
            self.H.append(val)
            i = self.n
            self.n += 1
            while i != 0 and self.H[self.parent(i)] > self.H[i]:
                self.H[i], self.H[self.parent(i)] = self.H[self.parent(i)], self.H[i]
                i = self.parent(i)
    
    def min(self):
        """ |Gives element with lowest priority value(most importance).
        :return: Minimum priority element (root)
        :rtype: int or float
        :Example:
            >>> H = Heap(40)
            >>> H.insert(1)
            >>> H.insert(5)
            >>> H.insert(4)
            >>> H.insert(3)
            >>> print(H.min())
            1
        """
        if (self.n != 0):
            return self.H[0]
        return -1
    
    def Heapify(self, root):
        """| Turns the array into an arrangement following heap properties
        :param root: Index of root of the sub-heap
        :type root: int
        :rtype: none
        :Example:
            >>> H = Heap(40)
            >>> H.H = [5, 3, 4, 6, 7]
            >>> H.n = 5
            >>> H.Heapify(0)
            >>> print(H.H)
            [3, 5, 4, 6, 7]
        """
        l = self.left(root)
        r = self.right(root)
        s = root
        if (l < self.n and self.H[l] < self.H[root]):
            s = l
        if (r < self.n and self.H[r] < self.H[s]):
            s = r
        if s != root:
            self.H[root], self.H[s] = self.H[s], self.H[root]
            self.Heapify(s)
    
    def deleteMin(self):
        """| Deletes the minimum element (i.e. root) and readjusts heap
        :rtype: none
        :Example:
            >>> H = Heap(40)
            >>> H.insert(1)
            >>> H.insert(5)
            >>> H.insert(4)
            >>> H.insert(3)
            >>> H.deleteMin()
            >>> print(H.H)
            [3, 5, 4]
        """
        if self.n > 0:
            if self.n == 1:
                self.H = []
                self.n = 0
            else:
                self.n -= 1
                self.H[0] = self.H[self.n]
                self.H.pop(self.n)
                self.Heapify(0)
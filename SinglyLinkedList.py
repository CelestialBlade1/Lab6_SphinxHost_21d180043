import SinglyLinkedListNode

class SinglyLinkedList:
    """| This implements a uni-directionally connected collection of objects called nodes.
    | The List comes with head and tail elements.
    | This class includes a Constructor and methods like insert, find, printer, deleteVal and reverse.
    :param head: Gives the head of the List, the leading element.
    :type head: SinglyLinkedListNode
    :param tail: The trailing element of the list, the point of addition of new elements.
    :type tail: SinglyLinkedListNode
    """
    
    def __init__(self):
        """| Constructor Method which builds Singly Linked List
        with empty head and tail. 
        :Example:
            >>> V = SinglyLinkedList()
            >>> V.insert(1)
            >>> V.printer(" ")
            [1]
        """
        self.head = None
        self.tail = None
   
    def insert(self, data):
        """| Inserts new node at tail
        :param data: The vale which would be contained in the new node
        :type data: int
        :Example:
            >>> V = SinglyLinkedList()
            >>> V.insert(1)
            >>> V.insert(10)
            >>> V.printer(" ")
            [1 10]
        """
        node = SinglyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node # add behind tail
        self.tail = node # move tail
    
    def find(self, data):
        """| Finds given data in the List.
        :param data: Content to be found in the
        :type data: int
        :return: The node BEFORE the node which contains the required value
        :rtype: SinglyLinkedListNode
        :Example:
            >>> V = SinglyLinkedList()
            >>> V.insert(1)
            >>> V.insert(2)
            >>> print(V.find(2).data)
            1
        """
        prev = None
        head = self.head
        while head != None and head.data != data:
            prev = head
            head = head.next
        return prev
    
    def deleteVal(self, data):
        """| Deletes a node
        :param data: Content of node to be deleted
        :type data: int
        :return: True, if deletion successful, False if node with content not found.
        :rtype: bool
        :Example:
            >>> V = SinglyLinkedList()
            >>> V.insert(1)
            >>> V.insert(2)
            >>> V.deleteVal(2)
            True
            >>> V.printer()
            [1]
        """
        prevPos = self.find(data)
        if prevPos.next == None:
            return False
        prevPos.next = prevPos.next.next
        if self.tail.data == data:
            self.tail = prevPos 
        return True
    
    def printer(self, sep = ', '):
        """| Prints the Linked List.
        :param sep: delimits the printed values, default value ", "
        :type sep: string, optional
        :Example:
            >>> V = SinglyLinkedList()
            >>> V.insert(1)
            >>> V.insert(2)
            >>> V.deleteVal(2)
            True
            >>> V.insert(3)
            >>> V.printer()
            [1, 3]
        """
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self):
        """| Reverses the Linked List, so that the tail becomes the hea dand vicce versa
        :rtype: None
        :Example:
            >>> V = SinglyLinkedList()
            >>> V.insert(1)
            >>> V.insert(2)
            >>> V.insert(3)
            >>> V.reverse()
            >>> V.printer()
            [3, 2, 1]
        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # while there is forward link left
            newHead = head.next # save extra pointer to next element
            head.next = prev # reverse the link of current element
            prev = head # move pointer to previous element
            head = newHead # use extra pointer to move to next element
        self.tail = self.head
        self.head = prev

def merge(list1, list2):
    """| Merges two Singly Linked Lists
    | Merged List is formed by taking the smaller of the lead elements of each list at every stage.
    :param list1: One of the lists to be merged
    :type list1: SinglyLinkedList
    :param list2: One of the lists to be merged
    :type list2: SinglyLinkedList
    :return: Merged List.
    :rtype: SinglyLinkedList
    :Example:
        >>> V = SinglyLinkedList()
        >>> V.insert(1)
        >>> V.insert(4)
        >>> V.insert(8)
        >>> U = SinglyLinkedList()
        >>> U.insert(3)
        >>> U.insert(10)
        >>> M = merge(U,V)
        >>> (M.printer())
        [1, 3, 4, 8, 10]
    """
    merged = SinglyLinkedList()
    head1 = list1.head
    head2 = list2.head
    while head1 != None and head2 != None: # both lists not empty
        if head1.data < head2.data: # link node with smaller data
            merged.insert(head1.data)
            head1 = head1.next
        else:
            merged.insert(head2.data)
            head2 = head2.next
    if head1 == None and head2 != None: # list 1 finished
        merged.tail.next = head2 # add remaining list 2 as is
    if head1 != None and head2 == None: # list 2 finished
        merged.tail.next = head1 # add remaining list 1 as is
    return merged
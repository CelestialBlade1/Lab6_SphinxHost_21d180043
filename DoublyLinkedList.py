import DoublyLinkedListNode

class DoublyLinkedList:
    """| A collection of nodes which is bi-directionally connected.
    | The class comes equipped with a Constructor and methods such as printer, reverse, insert
    :param head: Leading Node of the Doubly Linked List
    :type head: DoublyLinkedListNode
    :param tail: Leading Node of the Doubly Linked List
    :typed tail: DoublyLinkedListNode
    """
    
    def __init__(self):
        """| Constructs a Doubly Linked List with empty head and tail
        :Example:
            >>> D =  DoublyLinkedList()
            >>> D.head = DoublyLinkedListNode(90)
            >>> D.head.data
            90
        """ 
        self.head = None
        self.tail = None
        
    
    def insert(self, data):
        """| Inserts an element at the tail of the List
        :param data: Data to be contained in the node
        :type data: int
        :Example:
            >>> D = DoublyLinkedList()
            >>> D.insert(5)
            >>> D.head.data
            5
        """
        node = DoublyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
            node.prev = self.tail
        self.tail = node # move tail
    
    def printer(self, sep = ', '):
        """| Prints the Doubly Linked List in a visualizable format
        :param sep: Delimits adjacent element terms, default value = ', '
        :type sep: string, optional
        :Example:
            >>> S = DoublyLinkedList()
            >>> S.insert(60)
            >>> S.insert(50)
            >>> S.insert(70)
            >>> S.printer()
            [60, 50, 70]
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
        """|  Reverses the order of the elements of the Linked List
        | Swaps head and tail
        :Example:
            >>> S = DoublyLinkedList()
            >>> S.insert(60)
            >>> S.insert(50)
            >>> S.insert(70)
            >>> S.reverse()
            >>> S.printer()
            [70, 50, 60]
        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # new node left
            newHead = head.next # save pointer to next node (cut forward link)
            if newHead != None: # check if next node has a reverse link
                newHead.prev = head # save pointer to previous node (cut reverse link)
            head.next = prev # reverse the forward link
            head.prev = newHead # reverse the reverse link
            prev = head # move pointer to previous element
            head = newHead # use saved pointer to move head
        self.tail = self.head
        self.head = prev
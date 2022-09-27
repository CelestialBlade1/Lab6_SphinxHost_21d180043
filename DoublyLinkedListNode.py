# ------------------------------ Doubly Linked List ----------------------------

class DoublyLinkedListNode:
    """| A node in a Doubly Linked List
    | The Doubly Linked List Node comes with a Constructor and a String Converter 
    :param data: data to be contained inside the node.
    :type data: int 
    :param next: The next Doubly Linked List Node
    :type next: DoublyLinkedListNode
    :param prev: The previous Doubly Linked List Node
    :type next: DoublyLinkedListNode
    """
    
    def __init__(self, data):
        """| Constructs a Doubly Linked List Node
        :param: The data to be stored in the node
        :Example:
            >>> D = DoublyLinkedListNode(10)
            >>> D.data
            10
            >>> D.next = DoublyLinkedListNode(5)
            >>> D.next.data
            5
            """
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        """| Gives a method to convert the Doubly Linked List Node as a string by revealing its contents.
        :Example:
            >>> V = DoublyLinkedListNode(10)
            >>> print(V)
            10
        """
        return str(self.data) 
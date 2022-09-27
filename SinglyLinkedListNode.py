# ------------------------------- Singly Linked List -----------------------------


class SinglyLinkedListNode:
    """| This implements a node of a Singly Linked List.
    | The node consists of data and a next node element.
    | This implementation allows for the uni-directional nature of a singly linked list.
    | It comes with a constructor and a converter. 
    
    :param data: The data or contents carried by the node.
    :type data: int
    :param next: Leads to the next element in the Linked List.
    :type next: SinglyLinkedListNode
    """

    def __init__(self, data):
        """| Constructs a Node object with the given content/data
        :param data: Initializing content for node.
        :Example:
            >>> A = SinglyLinkedListNode(10)
            >>> print(A.data)
            10
        """
        self.data = data
        self.next = None
    
    def __str__(self):
        """| Convert Node to string format, ready to print
        :return: string with data in self
        :rtype: string
        :Example:
            >>> S = SinglyLinkedListNode(90)
            >>> print(str(S))
            90
        """
        return str(self.data)
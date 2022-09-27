# -------------------------- Binary Search Tree ------------------------------


class BSTNode:
    """| Node in a Binary Search Tree
    | The Node onject comes with a Constructor, string converter
    :param info: Data contained in the Node object
    :type info: any comparable object
    :param left: The left child of the Node
    :type left: BSTNode
    :param right: The right child of the Node
    :type right: BSTNode
    :param level: The level of the node from the root.
    :type level: int
    """
    
    def __init__(self, info):
        """| Constructs a BSTNode with data contained as given input
        | Functions available for the BSTNode include a string converter.
        :param info: info to be contained in node
        :type info: any comparable object
        :Exmaple:
            >>> B = BSTNode(60)
            >>> B.info
            60
        """
        self.info = info
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self):
        """| Converts a BSTNode input into a string based output using the info in the Node
        :Example:
            >>> K = BSTNode(50)
            >>> print(K)
            50
        """
        return str(self.info)
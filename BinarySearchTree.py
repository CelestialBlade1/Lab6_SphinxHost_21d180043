import BSTNode

class BinarySearchTree:
    """| A Tree in which each node in the tree has two children.
    | The left child of the the node has a value less than the value of its parent
    | The right child of the node has a value greater than or equal to its parent
    | Has a Constructor, and methods for insert, traverse and height.
    :param root: The only node with no parent. The  ancestor of all nodes.
    :type root: BSTNode
    """
    
    def __init__(self):
        """| Constructs a BInary Search Tree with empty root
        :Example:
            >>> BST = BinarySearchTree()
            >>> BST.root = BSTNode(56)
            >>> print(BST.root)
            56
        """
        self.root = None
    
    def insert(self, val):
        """| Inserts a new node in the Binary Search Tree
        :param val: Value to be contained in the node
        :type val: any comparable object
        :Example:
            >>> BST = BinarySearchTree()
            >>> BST.insert(28)
            >>> BST.insert(73)
            >>> print(BST.root)
            28
            >>> print(BST.root.right)
            73
            >>> print(BST.root.left)
            None
        """
        if self.root == None:
            self.root = BSTNode(val)
        else:
            current = self.root
            while True:
                if val < current.info: # move to left sub-tree
                    if current.left:
                        current = current.left # root moved
                    else:
                        current.left = BSTNode(val) # left init
                        break
                elif val > current.info: # move to right sub-tree
                    if current.right:
                        current = current.right # root moved
                    else:
                        current.right = BSTNode(val) # right init
                        break
                else:
                    break # value exists
    
    def traverse(self, order):
        """| Traverses the tree in a fashion chosen by the member function
        | Offers option of PRE-ORDER, IN-ORDER and POST-ORDER traversal
        :param order: specifies the traversing fashion
        :type order: string
        :Example:
                >>> Y = BinarySearchTree()
                >>> Y.insert(40)
                >>> Y.insert(30)
                >>> Y.insert(50)
                >>> Y.insert(35)
                >>> Y.insert(45)
                >>> Y.insert(25)
                >>> Y.insert(55)
                >>> Y.traverse('PRE')
                40 30 25 35 50 45 55 
        """
        def preOrder(root):
            """| Traverses the element in the following fashion:
                > Starts at the root and returns after a simple print at leaves.
                > First prints the current node contents.
                > Recursively traverses the left subtree, if any
                > Recursively traverses the right subtree, if any
            :Example:
                >>> Y = BinarySearchTree()
                >>> Y.insert(40)
                >>> Y.insert(30)
                >>> Y.insert(50)
                >>> Y.insert(35)
                >>> Y.insert(45)
                >>> Y.insert(25)
                >>> Y.insert(55)
                >>> Y.traverse('PRE')
                40 30 25 35 50 45 55
            """
            print(root.info, end = ' ')
            if root.left != None:
                preOrder(root.left)
            if root.right != None:
                preOrder(root.right)
        def inOrder(root):
            """| Traverses the element in the following fashion:
                > Starts at the root and returns after a simple print at leaves.
                > First Recursively traverses the left subtree, if any
                > Prints the current node contents.
                > Recursively traverses the right subtree, if any
            :Example:
                >>> Y = BinarySearchTree()
                >>> Y.insert(40)
                >>> Y.insert(30)
                >>> Y.insert(50)
                >>> Y.insert(35)
                >>> Y.insert(45)
                >>> Y.insert(25)
                >>> Y.insert(55)
                >>> Y.traverse('IN')
                25 30 35 40 45 50 55
            """
            if root.left != None:
                inOrder(root.left)
            print(root.info, end = ' ')
            if root.right != None:
                inOrder(root.right)
        def postOrder(root):
            """| Traverses the element in the following fashion:
                > Starts at the root and returns after a simple print at leaves.
                > First Recursively traverses the left subtree, if any
                > Recursively traverses the right subtree, if any
                > Prints the current node contents.
            :Example:
                >>> Y = BinarySearchTree()
                >>> Y.insert(40)
                >>> Y.insert(30)
                >>> Y.insert(50)
                >>> Y.insert(35)
                >>> Y.insert(45)
                >>> Y.insert(25)
                >>> Y.insert(55)
                >>> Y.traverse('POST')
                25 35 30 45 50 55 40    
            """
            if root.left != None:
                postOrder(root.left)
            if root.right != None:
                postOrder(root.right)
            print(root.info, end = ' ')
        if order == 'PRE':
            preOrder(self.root)
        elif order == 'IN':
            inOrder(self.root)
        elif order == 'POST':
            postOrder(self.root)
    
    def height(self, root):
        """| Gives the height off the tree
        | This is the distance between the root and the farthes descendant
        | The childless node has 0 height
        :param root: The root of the tree/sub-tree whose height is to be found
        :type root: BSTNode
        :return: height of tree, defined 0 for childless node
        :rtype: int
        :Example:
            >>> Y = BinarySearchTree()
            >>> Y.insert(40)
            >>> Y.insert(30)
            >>> Y.insert(50)
            >>> Y.insert(35)
            >>> Y.insert(45)
            >>> Y.insert(25)
            >>> Y.insert(55)
            >>> Y.height(Y.root)
            2
        """
        if root.left == None and root.right == None:
            return 0
        elif root.right == None:
            return 1 + self.height(root.left)
        elif root.left == None:
            return 1 + self.height(root.right)
        else:
            return 1 + max(self.height(root.left),self.height(root.right))
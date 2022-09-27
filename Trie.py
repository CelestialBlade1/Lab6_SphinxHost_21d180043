# --------------------------------- Suffix Trie --------------------------------

class Trie:
    """| Stores alphabetical sequences in an ADT implemented using Dictionaries.
    | Each dictionary acts as a node which may contain further dictionaries within.
    | The Trie has methods find, insert, checkPrefix, countPrefix and a constructor
    :param T: The root node of the Trie
    :type T: Dictionary
    """
    
    def __init__(self):
        """| Constructs a Trie with empty Dictionary as root
        | Offers functions for insert, find, checkPrefix, countPrefix.
        :Example:
            >>> trie = Trie()
            >>> trie.T['A'] = {}
            >>> trie.T['B'] = {}
            >>> print(trie.T)
            {'A': {}, 'B': {}}
        """
        self.T = {}
    
    def find(self, root, c):
        """| Find character in current root's children
        :param root: A trie node
        :type root: Dictionary
        :param c: Character to be searched for in the Children
        :type c: char
        :return: True if char is found in children, False otherwise
        :rtype: bool
        :Example:
            >>> trie = Trie()
            >>> trie.T['A'] = {}
            >>> trie.T['B'] = {}
            >>> trie.find(trie.T,'A')
            True
        """
        return (c in root)
    
    def insert(self, s):
        """| Inserts a new string in Trie
        :param s: string to insert
        :type s: string
        :Example:
            >>> trie = Trie()
            >>> trie.insert("foobar")
            >>> trie.insert("fbar")
            >>> print(trie.T)
            {'f': {'#': 2, 'o': {'#': 1, 'o': {'#': 1, 'b': {'#': 1, 'a': {'#': 1, 'r': {'#': 1}}}}}, 'b': {'#': 1, 'a': {'#': 1, 'r': {'#': 1}}}}}
        """
        root = self.T
        for c in s:
            if not self.find(root,c):
                root[c] = {}
            root = root[c]
            root.setdefault('#',0)
            root['#'] += 1
    
    def checkPrefix(self, s):
        """| Checks  for prescence of prefix in the Trie
        :param s: string to be checked for
        :type s: string
        :return: True if string found, False otherwise
        :rtype: bool
        :Example:
            >>> trie = Trie()
            >>> trie.insert("foobar")
            >>> trie.checkPrefix("foo")
            True
        """
        root = self.T
        for idx, char in enumerate(s):
            if char not in root:
                if idx == len(s) - 1:    
                    root[char] = '#'
                else:
                    root[char] = {}
            elif root[char] == '#' or idx == len(s) - 1:
                return True
            root = root[char]
        return False
    
    def countPrefix(self, s):
        """| counts number of prefix matches for given string
        :param s: string to be checked
        :type s: string
        :return: NUmber of unique matches of prefix with string
        :rtype: int
        :Example:
            >>> trie = Trie()
            >>> trie.insert("foobar")
            >>> trie.insert("foobur")
            >>> trie.countPrefix("foo")
            2
        """
        found = True
        root = self.T
        for c in s:
            if self.find(root,c):
                root = root[c]
            else:
                found = False
                break
        if found:
            return root['#']
        return 0
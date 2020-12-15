#zad 9.7
#Implementacja drzewa BST za pomocą klasy Node i klasy BinarySearchTree
class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, node):
        if node.data < self.data:   # mniejsze na lewo
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:   # większe lub równe na prawo
            if self.right:
                self.right.insert(node)
            else:
                self.right = node

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None

    def remove(self, data):  # self na pewno istnieje
        # Są lepsze sposoby na usuwanie.
        if data < self.data:
            if self.left:
                self.left = self.left.remove(data)
        elif self.data < data:
            if self.right:
                self.right = self.right.remove(data)
        else:                # self.data == data
            if self.left is None:   # przeskakuje self
                return self.right
            else:     # self.left na pewno niepuste
                # Szukamy największego w lewym poddrzewie.
                node = self.left
                while node.right:   # schodzimy w dół
                    node = node.right
                node.right = self.right   # przyczepiamy
                return self.left
        return self

#bst_min i bst_max napisane w wersji rekurencyjnej

    def bst_min(root):
        if root.left is not None:
            return root.left.bst_min()
        else:
            return root


    def bst_max(root):
        if root.right is not None:
            return root.right.bst_max()
        else:
            return root




class BinarySearchTree:
    """Klasa reprezentująca binarne drzewo poszukiwań."""

    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root:
            self.root.insert(node)
        else:
            self.root = node

    def count(self):
        if self.root:
            return self.root.count()
        else:
            return 0

    def search(self, data):   # zwraca node lub None
        if self.root:
            return self.root.search(data)
        else:
            return None

    def remove(self, data):
        if self.root:
            self.root = self.root.remove(data)

    def bst_min(self):
        if self.root:
            return self.root.bst_min()
        else:
            return None

    def bst_max(self):
        if self.root:
            return self.root.bst_max()
        else:
            return None


    
    
tree = BinarySearchTree()
tree.insert(Node(70))
tree.insert(Node(31))
tree.insert(Node(93))
tree.insert(Node(14))
tree.insert(Node(73))
tree.insert(Node(94))
tree.insert(Node(23))


print(tree.bst_min())
print(tree.bst_max())

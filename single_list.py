#zad. 9.2
#Żeby samemu zdefiniować klasy Node i Single_list trzeba nadpisać
#ich podstawowe metody, takie jak init, str, eq, lt, gt. W przeciwnym razie
#wystąpi bład (a przynajmniej w mojej wersji pythona, czyli 3.7) i nie będziemy 
#mogli wyświetlić listy za pomocą print(single_list)

class Node: 
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie
    

    def __eq__(self, other):
        return self.data == other.data

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def __str__(self):
        printedList = ''
        currentNode = self.head
        while currentNode is not None:
            printedList += (',' + str(currentNode))
            currentNode = currentNode.next
        printedList = '[' + printedList[1:] + ']'
        return printedList

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(n)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node


    def search(self, data):
        # Zwraca łącze do węzła o podanym kluczu lub None.
        currentNode = self.head
        foundNode = False
        while currentNode and foundNode is False:
            if currentNode.data == data:
                foundNode = True
            else:
                currentNode = currentNode.next
        if currentNode is None:
            raise ValueError("The node with this data is not in this list")
        return currentNode

    
    def find_min(self):
        # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy
        currentNode = self.head
        minNode = currentNode
        while currentNode.next is not None:
            currentNode = currentNode.next
            if currentNode < minNode:
                minNode = currentNode
        return minNode

    def find_max(self):
        # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.
        currentNode = self.head
        maxNode = currentNode
        while currentNode.next is not None:
            currentNode = currentNode.next
            if currentNode > maxNode:
                maxNode = currentNode
        return maxNode

    def reverse(self):    
        # Odwracanie kolejności węzłów na liście.
        prevNode = None
        currentNode = self.head 
        while(currentNode is not None): 
            next_saved = currentNode.next
            currentNode.next = prevNode 
            prevNode = currentNode 
            currentNode = next_saved
        self.head = prevNode
        return self


single_list = SingleList()
for i in range(15):
    single_list.insert_tail(Node(i))

print(single_list)

single_list.reverse()
print(single_list)
print(single_list.search(8))
print(single_list)
print(single_list.find_min())
print(single_list.find_max())

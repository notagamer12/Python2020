import random


class RandomQueue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def insert(self, item):
        if self.is_full():
            raise OverflowError("Kolejka jest już zapełniona.")
        self.items.append(item)

    
    def remove(self):    #zwraca losowy element
        if self.is_empty():
            raise ValueError("Kolejka jest pusta.")
        randomIndex = random.randint(0, len(self.items)-1)
        #w linijce poniżej zamieniamy elemnt spod wylosowanego indeksu z elementem z końca kolejki...
        self.items[randomIndex], self.items[len(self.items)-1] = self.items[len(self.items)-1], self.items[randomIndex]
        #...a następnie zwracamy ten losowy element z końca kolejki
        return self.items.pop()

    def is_empty(self):  # nigdy nie jest pusta
        return not self.items

   
    def is_full(self):
        return False

    
    def clear(self):    # czyszczenie listy
        self.items = []


#sprawdzenie, czy rzeczywiście elementy są pobierane z kolejki w losowej kolejności
randomQueue = RandomQueue()

for i in range(15):
    randomQueue.insert(i)
print(randomQueue)

for i in range(15):
    print(randomQueue.remove())

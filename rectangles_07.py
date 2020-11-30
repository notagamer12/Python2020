from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.

        if x1 >= x2 or y1 >= y2:
            raise ValueError("prawidłowe współrzędne powinny spełniać warunek x1 < x2, y1 < y2")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self): # "[(x1, y1), (x2, y2)]"
        
        return "[({0}, {1}), ({2}, {3})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self): # "[(x1, y1), (x2, y2)]"
        
        return "Rectangle({0}, {1}, {2}, {3})".format(self.pt1.x, self.pt1.y,self.pt2.x, self.pt2.y)

    def __eq__(self, other): # obsługa rect1 == rect2
        
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other): # obsługa rect1 != rect2
        
        return not self == other

    def center(self): # zwraca środek prostokąta
        
        x_cent = (self.pt1.x + self.pt2.x) / 2
        y_cent = (self.pt1.y + self.pt2.y) / 2
        return Point(x_cent, y_cent)

    def area(self): # pole powierzchni
       
        a = self.pt2.x - self.pt1.x
        b = self.pt2.y - self.pt1.y
        return a * b

    def move(self, x, y): # przesunięcie o (x, y)
        
        x1 = self.pt1.x + x
        y1 = self.pt1.y + y
        x2 = self.pt2.x + x
        y2 = self.pt2.y + y
        return Rectangle(x1, y1, x2, y2)

    def intersection(self, other): # część wspólna prostokątów

        p1 = self.pt1  #(x1,y1)
        p2 = self.pt2    #(x2,y2)
        p3 = other.pt1 #(x3, y3)
        p4 = other.pt2   #(x4,y4)

        x5 = max(p1.x, p3.x)
        y5 = max(p1.y, p3.y)
        x6 = min(p2.x, p4.x)
        y6 = min(p2.y, p4.y)

        if x5 > x6 or y5 > y6:
            return None
       
        return Rectangle(x5, y5, x6, y6)

    def cover(self, other): # prostąkąt nakrywający oba
        
        p1 = self.pt1
        p2 = self.pt2
        p3 = other.pt1
        p4 = other.pt2

        x5 = min(p1.x, p3.x)
        y5 = min(p1.y, p3.y)
        x6 = max(p2.x, p4.x)
        y6 = max(p2.y, p4.y)

        return Rectangle(x5, y5, x6, y6)

    def make4(self): # zwraca krotkę czterech mniejszych
        
        cent = self.center()
        rect1 = Rectangle(self.pt1.x, self.pt1.y, cent.x, cent.y)
        rect2 = Rectangle(self.pt1.x, cent.y, cent.x, self.pt2.y)
        rect3 = Rectangle(cent.x, self.pt1.y, self.pt2.x, cent.y)
        rect4 = Rectangle(cent.x, cent.y, self.pt2.x, self.pt2.y)
        return [rect1, rect2, rect3, rect4]

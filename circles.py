from points import Point
import math
from rectangles_07 import *
class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):       # "Circle(x, y, radius)"
        return "Circle({0}, {1}, {2})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):           # pole powierzchni
        area = math.pi*self.radius*self.radius
        return area

    def move(self, x, y):      # przesuniecie o (x, y)
        x_moved = self.pt.x + x
        y_moved = self.pt.y + y
        return Circle(x_moved, y_moved, self.radius)

    def coverr(self, other):    # najmniejszy okrąg pokrywający oba
        p1 = self.pt
        p2 = other.pt
        r1 = self.radius
        r2 = other.radius

        #każdy okrąg, który pojawi się w zadaniu, przybliżam kwadratem wpisanym w ten okrąg, ponieważ wtedy mogę
        #korzystać z tego, że:
        # 1) wierzchołki kwadratu wpisanego w okrąg leżą na tym okręgu
        # 2) odległości od środka kwadratu do każdego z  jego wierzchołków wynosi r, czyli tyle samo, co promień okręgu, w który ten kwadrat jest wpisany 


        #kwadrat pierwszy - przybliża pierwszy okrąg
        x1 = p1.x - r1
        y1 = p1.y - r1
        x2 = p1.x + r1
        y2 = p1.y + r1

        #kwadrat drugi - przybliża drugi okrąg
        x3 = p2.x - r2
        y3 = p2.y - r2
        x4 = p2.x + r2
        y4 = p2.y + r2


        overlaping_rectangle = Rectangle(x1, y1, x2, y2).cover(Rectangle(x3, y3, x4, y4))#prostokąt pokrywający oba okręgi, nazwijmy go PPok (funkcja cover z klasy Rectangle)
        center_of_overlaping_circle = overlaping_rectangle.center() #środek prostokąta pokrywającego oba okręgi (funkca center z klasy Rectangle)
        #okrąg pokrywający oba okręgi powstaje tak, że jego środkiem jest środek PPok, a jego promieniem jest odległość środka PPok...
        #...od wierzchołka PPok (odległość środka PPok od wszystkich wierzchołków PPok jest taka sama)
        radius_of_overlaping_circle = math.sqrt(((overlaping_rectangle.pt2.x - center_of_overlaping_circle.x )**2) + ((overlaping_rectangle.pt2.y - center_of_overlaping_circle.y )**2))
        return Circle(center_of_overlaping_circle.x, center_of_overlaping_circle.y, radius_of_overlaping_circle)

    def tearDown(self): pass








        
        

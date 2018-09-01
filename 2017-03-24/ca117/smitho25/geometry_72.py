class Point(object):
 
     def __init__(self, x=0, y=0):
         self.x = x
         self.y = y
 
     def distance(self, other):
         return ((other.x-self.x)**2 + (other.y-self.y)**2)**0.5
 
     def __str__(self):
         return '({:.1f}, {:.1f})'.format(self.x, self.y)
 
class Segment(object):
 
     def __init__(self, p1 =0, p2 = 0):
         self.p1 = p1
         self.p2 = p2
 
     def midpoint(self):
       return Point(((self.p1.x + self.p2.x) / 2), (self.p1.y + self.p2.y) / 2)
 
     def length(self):
         return self.p1.distance(self.p2)
 
     def __str__(self):
         return '{} to {} (length {:.1f})'.format(self.p1.__str__(),
                                                  self.p2.__str__(),
                                                  self.length())

class Circle(object):
    
     def __init__(self,centre=Point(0,0),radius=0):
         self.centre = centre
         self.radius = radius
     
     def overlaps(self,other):
         distance = self.centre.distance(other.centre)
         return True if (distance < self.radius + other.radius) else False
       
       

def main():
    p1 = Point()
    p2 = Point(5, 5)
    s1 = Segment(p1, p2)
    s2 = Segment(p2, p1)
    c1 = Circle(p1, 5)
    c2 = Circle(p2, 2)
    c3 = Circle(p1, 2)

    print(p1)
    print(p2)
    print(s1.midpoint())
    print(s2.midpoint())
    print(c1.overlaps(c2))
    print(c2.overlaps(c1))
    print(c1.overlaps(c3))
    print(c3.overlaps(c2))

if __name__ == '__main__':
    main()


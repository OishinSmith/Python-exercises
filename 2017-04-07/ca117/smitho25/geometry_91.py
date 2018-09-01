class Point(object):
  def __init__(self, x, y):
    self.x = float(x)
    self.y = float(y)
    

  def distance(point1, point2): #finds the distance automatically
    return((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5

class Shape(object):
  def __init__(self, list_points):
    self.points = list_points

  def sides(self):
    a = []
    for i in range(len(self.points)):
      n = self.points[i].distance(self.points[i-1])
      a.append(n)
    return(a[1:] + [a[0]])
    #return(a + [self.points[0].distance(self.points[-1])])

  def perimeter(self):
    total = 0
    for value in self.sides():
      total = total + value
    return(total)

class Triangle(Shape):
  def area(self):
    [side1, side2, side3] = self.sides()
    s = (side1 + side2 + side3)/2
    area = ((s*(s - side1)*(s - side2)*(s - side3))**0.5)
    return(area)


class Square(Shape):
  def area(self):
    area = self.sides()[0] * self.sides()[0]
    return(area)

def main():

    t1 = Triangle([Point(-10,-10), Point(103,34), Point(26, 10)])
    print(t1.sides())
    print(t1.perimeter())
    print((t1.area()))

    s1 = Square([Point(10,10), Point(1,1), Point(3,2), Point(1,5)])
    print(s1.sides())
    print(s1.perimeter())
    print(s1.area())

if __name__ == '__main__':
    main()


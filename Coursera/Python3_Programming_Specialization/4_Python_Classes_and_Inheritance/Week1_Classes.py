print("============================================")
print("Python 3 Programming Specialization")
print("Course 4 :Python Classes and Inheritance")
print("Week 1 : Classes")

print("")

print("============================================")
print("======== 1.1. User-Defined Classes =========")
print("--------------------------------------------")
class Point:
    """Point class for representing and manipulating x,y coordinates."""

    def __init__(self):
        self.x = 0
        self.y = 0

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print(p)
print(q)

print(p is q)


print("")

print("============================================")
print("= 1.2. Adding Parameters to the Constructor =")
print("--------------------------------------------")
class Point:
    """Point class for representing and manipulating x,y coordinates."""

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

p = Point(7,6)
print(p.x)
print(p.y)



print("")


class NumberSet():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

t = NumberSet(6, 10)
print(t)
print(t.num1)
print(t.num2)
print(t.num1, t.num2)


print("")

print("============================================")
print("=== 1.3. Adding Other Methods to a Class ===")
print("--------------------------------------------")
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5



p = Point(7,6)
print(p.getX())
print(p.getY())
print(p.distanceFromOrigin())


print("")


class Animal():
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs

    def limbs(self):
        return self.arms + self.legs

spider = Animal(4,4)
spidlimbs = spider.limbs()
print(spidlimbs)

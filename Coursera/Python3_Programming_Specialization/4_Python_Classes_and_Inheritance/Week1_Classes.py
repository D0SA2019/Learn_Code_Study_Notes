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


print("")

print("============================================")
print("= 1.4. Objects as Arguments and Parameters =")
print("--------------------------------------------")

import math

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

    def distance(self, point2):
        xdiff = point2.getX()-self.getX()
        ydiff = point2.getY()-self.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist

p = Point(4,3)
q = Point(0,0)
print(p.distance(q))

print("")

print("============================================")
print("== 1.5. Converting an Object to a String ===")
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

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

p = Point(7,6)
print(p)


print("")

class Cereal:
    def __init__(self, name, brand, fiber):
        self.name = name
        self.brand = brand
        self.fiber = fiber

    def __str__(self):
        return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name, self.brand, self.fiber)

c1 = Cereal("Corn Flakes", "Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)

print(c1)
print(c2)

print("")

print("============================================")
print("===== 1.6. Instances as Return Values ======")
print("--------------------------------------------")

class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx,my)

p = Point(3,4)
q = Point(5,12)
mid = p.halfway(q)

print(mid)
print(mid.getX())
print(mid.getY())

print("")

print("============================================")
print("===== 1.7. Sorting Lists of Instances ======")
print("--------------------------------------------")
L = ["Cherry", "Apple", "Blueberry"]

print(sorted(L, key=len))
print(sorted(L, key= lambda x: len(x)))


print("")

class Fruit():
	def __init__(self, name, price):
		self.name = name
		self.price = price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]

for f in sorted(L, key= lambda x: x.price):
	print(f.name)


print("")

class Fruit():
	def __init__(self, name, price):
		self.name = name
		self.price = price

	def sort_priority(self):
		return self.price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]

print("-----sorted by price, referencing a class method-----")
for f in sorted(L, key= Fruit.sort_priority):
	print(f.name)

print("---- one more way to do the same thing-----")
for f in sorted(L, key= lambda x: x.sort_priority()):
	print(f.name)


print("")

print("============================================")
print("=========== 1.8. Class Variables ===========")
print("========== and Instance Variables ==========")
print("--------------------------------------------")
class Point:
	printed_rep = "*"

	def __init__(self, initX, initY):
		self.x = initX
		self.y = initY

	def graph(self):
		rows = []
		size = max(int(self.x), int(self.y)) + 2

		for j in range(size-1):
			if (j+1) == int(self.y):
				special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
				rows.append(special_row)
			else:
				rows.append(str((j+1) % 10))

		rows.reverse()
		x_axis = ""
		for i in range(size):
			x_axis += str(i % 10)
		rows.append(x_axis)

		return "\n".join(rows)

p1 = Point(2,3)
p2 = Point(3,12)
print(p1.graph())
print("")
print(p2.graph())


print("")

print("============================================")
print("========= 1.10. A Tamagotchi Game ==========")
print("--------------------------------------------")
from random import randrange

class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ["Mrrp"]

    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]

    def clock_tick(self):
        self.boredom += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "    I'm " + self.name + "."
        state += " I feel " + self.mood() + "."
        #state += "Hunger {} Boredom {} Words {}".format(self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)


p1 = Pet("Fido")
print(p1)

for i in range(10):
    p1.clock_tick()
    print(p1)

p1.feed()
p1.hi()
p1.teach("Boo")

for i in range(10):
    p1.hi()
print(p1)


print("")

import sys
#sys.setExecutionLimit(60000)

def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None # no pet matched

def play():
    animals = []

    option = ""
    base_prompt = """
        Quit
        Adopt <petname_with_no_spaces_please>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: """
    feedback = ""
    while True:
        action = input(feedback + "\n" + base_prompt)
        feedback = ""
        words = action.split()
        if len(words) > 0:
            command = words[0]
        else:
            command = None
        if command == "Quit":
            print("Exiting...")
            return
        elif command == "Adopt" and len(words) > 1:
            if whichone(animals, words[1]):
                feedback += "You already have a pet with that name\n"
            else:
                animals.append(Pet(words[1]))
        elif command == "Greet" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again.\n"
                print()
            else:
                pet.hi()
        elif command == "Teach" and len(words) > 2:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.teach(words[2])
        elif command == "Feed" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.feed()
        else:
            feedback+= "I didn't understand that. Please try again."

        for pet in animals:
            pet.clock_tick()
            feedback += "\n" + pet.__str__()



play()

print("")
'''
print("============================================")
print("========== 1.11. Testing classes ===========")
print("--------------------------------------------")

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

import test

#testing instance variables x and y
p = Point(3, 4)
test.testEqual(p.y, 4)
test.testEqual(p.x, 3)

#testing the distance method
p = Point(3, 4)
test.testEqual(p.distanceFromOrigin(), 5.0)

#testing the move method
p = Point(3, 4)
p.move(-2, 3)
test.testEqual(p.x, 1)
test.testEqual(p.y, 7)
'''
print("")

print("============================================")
print("====== 1.12. Assessments & Exercises =======")
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

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        return (self.x, self.y)

    def __str__(self):
        return str(self.x)+","+str(self.y)

    def reflect_x(self):
        return (self.x, -self.y)

p = Point(3, 5)
print(p.reflect_x())
print(p.move(2,3))


print("")


class Bike():
    def __init__(self, color, price):
        self.color = color
        self.price = price

testOne = Bike("blue", 89.99)
testTwo = Bike("purple", 25.0)
print(testOne.color)
print(testTwo.color)
print(testOne.price)
print(testTwo.price)


print("")

class AppleBasket():
    def __init__(self, color, quantity):
        self.apple_color = color
        self.apple_quantity = quantity

    def increase(self):
        self.apple_quantity += 1
        return self.apple_quantity

    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)

app = AppleBasket("green", 12)
print(app)
app.increase()
app.increase()
app.increase()
print(app)


print("")

class Bank():
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt

    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name, str(self.amt))

t1 = Bank("Bob", 100.0)
print(t1)

print("")
print("------ 11. Introduction to Classes ------")

print("")
print("------ 11.1. Why Use Classes? ------")
class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))

  def is_edible(self):
    if not self.poisonous:
      print("Yep! I'm edible.")
    else:
      print("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()





print("")
print("------ 11.5. Instantiating Your First Object ------")
class Square(object):
  def __init__(self):
    self.sides = 4

my_shape = Square()
print(my_shape.sides)

class Animal(object):
  def __init__(self, name):
    self.name = name

zebra = Animal("Jeffrey")
print(zebra.name)





print("")
print("------ 11.6. More on __init__() and self ------")
# Class definition
class Animal(object):
  """Makes cute animals."""
  # For initializing our instance objects
  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print(zebra.name, zebra.age, zebra.is_hungry)
print(giraffe.name, giraffe.age, giraffe.is_hungry)
print(panda.name, panda.age, panda.is_hungry)





print("")
print("------ 11.7. Class Scope ------")
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print(zebra.name, zebra.age, zebra.is_alive)
print(giraffe.name, giraffe.age, giraffe.is_alive)
print(panda.name, panda.age, panda.is_alive)





print("")
print("------ 11.8. A Methodical Approach ------")
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print(self.name)
    print(self.age)

hippo = Animal("Mark", 4)
hippo.description()





print("")
print("------ 11.9. They're Multiplying! ------")
hippo = Animal("Jake", 12)
cat = Animal("Boots", 3)
print(hippo.is_alive)
hippo.is_alive = False
print(hippo.is_alive)
print(cat.is_alive)

print("")

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print(self.name)
    print(self.age)

hippo = Animal("Mark", 4)
sloth = Animal("Sia", 2)
ocelot = Animal("OJ", 5)
hippo.description()

print(hippo.health)
print(sloth.health)
print(ocelot.health)





print("")
print("------ 11.10. It's Not All Animals and Fruits ------")
class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""

  def __init__(self, customer_name):
    self.customer_name = customer_name
    self.items_in_cart = {}
  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print(product + " added.")
    else:
      print(product + " is already in the cart.")

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print(product + " removed.")
    else:
      print(product + " is not in the cart.")

my_cart = ShoppingCart("Heval")
my_cart.add_item("Coffee", 10)

print(my_cart.items_in_cart)





print("")
print("------ 11.11. Warning: Here Be Dragons ------")
class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()





print("")
print("------ 11.13. Override! ------")
class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print("Hello, %s" % other.name)

class CEO(Employee):
  def greet(self, other):
    print("Get back to work, %s!" % other.name)

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
ceo.greet(emp)





print("")
print("------ 11.14. This Looks Like a Job For... ------")
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00

  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee('Milton')
print(milton.full_time_wage(10))





print("")
print("------ 11.17. Instantiate an Object ------")
class Triangle(object):
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3

  number_of_sides = 3

  def check_angles(self):
    if self.angle1 + self.angle2 + self.angle3 == 180:
      return True
    else:
      return False


my_triangle = Triangle(90, 45, 45)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())





print("")
print("------ 11.18. Inheritance ------")
class Triangle(object):
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3

  number_of_sides = 3

  def check_angles(self):
    if self.angle1 + self.angle2 + self.angle3 == 180:
      return True
    else:
      return False

class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle

my_triangle = Triangle(90, 45, 45)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())

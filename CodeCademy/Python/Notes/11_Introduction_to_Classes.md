# 11. Introduction to Classes


### 11.1. Why Use Classes?
Python is an object-oriented programming language, which means it manipulates programming constructs called *objects*. You can think of an object as a single data structure that contains data as well as functions; the functions of an object are called its *methods*. For example, any time you call

```Python
len("Eric")
```
Python is checking to see whether the string object you passed it has a length, and if it does, it returns the value associated with that *attribute*. When you call

```Python
my_dict.items()
```

Python checks to see if `my_dict` has an `items()` method (which all dictionaries have) and executes that method if it finds it.

But what makes `"Eric"` a string and `my_dict` a dictionary? The fact that they're instances of the `str` and `dict` classes, respectively. A class is just a way of organizing and producing objects with similar attributes and methods.

##### Instructions
Check out the code in the editor to the right. We've defined our own class, `Fruit`, and created a `lemon` instance.When you're ready, click Run to get started creating classes and objects of your own.


```Python
# GIVEN
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



# OUTPUT
I'm a yellow lemon and I taste sour.
Yep! I'm edible.
```


### 11.2. Class Syntax
A basic class consists only of the `class` keyword, the name of the class, and the class from which the new class inherits in **parentheses**. (We'll get to inheritance soon.) For now, our classes will inherit from the `object` class, like so:

```Python
class NewClass(object):
  # Class magic here
```

This gives them the powers and abilities of a Python object. By convention, user-defined Python class names start with a capital letter.


##### Instructions
Create a class called `Animal` in the editor. For now, in the body of your class, use the `pass` keyword. (`pass` doesn't do anything, but it's useful as a placeholder in areas of your code where Python expects an expression.)


```Python
# SOLUTION
class Animal(object):
  pass
```

### 11.3. Classier Classes
We'd like our classes to do more than... well, *nothing*, so we'll have to replace our `pass` with something else.

You may have noticed in our example back in the first exercise that we started our class definition off with an odd-looking function: `__init__()`. This function is required for classes, and it's used to **initialize** the objects it creates. `__init__()` always takes at least one argument, `self`, that refers to the object being created. You can think of `__init__()` as the function that "boots up" each object the class creates.


##### Instructions
Remove the `pass` statement in your `class` definition, then go ahead and `def`ine an `__init__()` function for your `Animal` class. Pass it the argument `self` for now; we'll explain how this works in greater detail in the next section. Finally, put the `pass` into the body of the `__init__()` definition, since it will expect an indented block.


```Python
# GIVEN
class Animal(object):
  pass



# SOLUTION
class Animal(object):
  def __init__(self):
    pass

```

### 11.4. Let's Not Get Too Selfish
Excellent! Let's make one more tweak to our class definition, then go ahead and instantiate (create) our first object.

So far, `__init__()` only takes one parameter: `self`. This is a Python convention; there's nothing magic about the word `self`. However, it's overwhelmingly common to use `self` as the first parameter in `__init__()`, so you should do this so that other people will understand your code.

The part that *is* magic is the fact that `self` is the *first* parameter passed to `__init__()`. Python will use the first parameter that `__init__()` receives to refer to the object being created; this is why it's often called `self`, since this parameter gives the object being created its identity.



##### Instructions
Let's do two things in the editor:

* Pass `__init__()` a second parameter, `name`.
* In the body of `__init__()`, let the function know that `name` refers to the created object's name by typing `self.name = name`. (This will become crystal clear in the next section.)


```Python
# GIVEN
class Animal(object):
  def __init__(self):
    pass



# SOLUTION
class Animal(object):
  def __init__(self, name):
    self.name = name
```

### 11.5. Instantiating Your First Object
Perfect! Now we're ready to start creating objects.

We can access attributes of our objects using *dot notation*. Here's how it works:

```Python
class Square(object):
  def __init__(self):
    self.sides = 4

my_shape = Square()
print(my_shape.sides)


# OUTPUT
4
```

1. First we create a class named `Square` with an attribute `sides`.
2. Outside the class definition, we create a new instance of `Square` named `my_shape` and access that attribute using `my_shape.sides`.

##### Instructions

Outside the `Animal` class definition, create a variable named `zebra` and set it equal to `Animal("Jeffrey")`.

Then `print` out `zebra`'s name.


```Python
# GIVEN
class Animal(object):
  def __init__(self, name):
    self.name = name



# SOLUTION
class Animal(object):
  def __init__(self, name):
    self.name = name

zebra = Animal("Jeffrey")
print(zebra.name)



# OUTPUT
Jeffrey
```

### 11.6. More on `__init__()` and self
Now that you're starting to understand how classes and objects work, it's worth delving a bit more into` __init__()` and `self`. They can be confusing!

As mentioned, you can think of `__init__()` as the method that "boots up" a class' instance object: the `init` bit is short for "initialize."

The first argument `__init__()` gets is used to refer to the instance object, and by convention, that argument is called `self`. If you add additional arguments—for instance, a `name` and `age` for your animal—setting each of those equal to `self.name` and `self.age` in the body of `__init__()` will make it so that when you create an instance object of your `Animal` class, you need to give each instance a name and an age, and those will be associated with the particular instance you create.


##### Instructions
Check out the examples in the editor. See how `__init__()` "boots up" each object to expect a name and an age, then uses `self.name` and `self.age` to assign those names and ages to each object? Add a third attribute, `is_hungry` to `__init__()`, and click Run to see the results.


```Python
# GIVEN
# Class definition
class Animal(object):
  """Makes cute animals."""
  # For initializing our instance objects
  def __init__(self, name, age):
    self.name = name
    self.age = age

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print(zebra.name, zebra.age, zebra.is_hungry)
print(giraffe.name, giraffe.age, giraffe.is_hungry)
print(panda.name, panda.age, panda.is_hungry)



# SOLUTION by adding to the Animal class
  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry



# OUTPUT
Jeffrey 2 True
Bruce 1 False
Chad 7 True
```

### 11.7. Class Scope
Another important aspect of Python classes is *scope*. The scope of a variable is the context in which it's visible to the program.

It may surprise you to learn that not all variables are accessible to all parts of a Python program at all times. When dealing with classes, you can have variables that are available everywhere (*global variables*), variables that are only available to members of a certain class (*member variables*), and variables that are only available to particular instances of a class (*instance variables*).

The same goes for functions: some are available everywhere, some are only available to members of a certain class, and still others are only available to particular instance objects.


##### Instructions

Check out the code in the editor. Note that each individual animal gets its own `name` and `age` (since they're all initialized individually), but they all have access to the member variable `is_alive`, since they're all members of the `Animal` class. Click Run to see the output!

```Python
# GIVEN
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



# OUTPUT
Jeffrey 2 True
Bruce 1 True
Chad 7 True
```

### 11.8. A Methodical Approach
When a class has its own functions, those functions are called *methods*. You've already seen one such method: `__init__()`. But you can also define your own methods!



##### Instructions
Add a method, `description`, to your `Animal` class. Using two separate `print` statements, it should print out the `name` and `age` of the animal it's called on. Then, create an instance of `Animal`, `hippo` (with whatever name and age you like), and call its `description` method.


```Python
# GIVEN
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!



# SOLUTION
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



# OUTPUT
Mark
4
```

### 11.9. They're Multiplying!
A class can have any number of **member variables**. These are variables that are available to all members of a class.

```Python
hippo = Animal("Jake", 12)
cat = Animal("Boots", 3)
print(hippo.is_alive)
hippo.is_alive = False
print(hippo.is_alive)
print(cat.is_alive)

# OUTPUT
True
False
True
```

1. In the example above, we create two instances of an `Animal`.
2. Then we print out `True`, the default value stored in hippo's `is_alive` member variable.
3. Next, we set that to `False` and print it out to make sure.
4. Finally, we print out `True`, the value stored in cat's `is_alive` member variable. We only changed the variable in hippo, not in cat.

Let's add another member variable to Animal.



##### Instructions

After line 3, add a second member variable called `health` that contains the string `"good"`.

Then, create two new `Animals`: `sloth` and `ocelot`. (Give them whatever names and ages you like.)

Finally, on three separate lines, `print` out the `health` of your `hippo`, `sloth`, and `ocelot`.


```Python
# GIVEN
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



# SOLUTION
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



# OUTPUT
Mark
4
good
good
good
```

### 11.10. It's Not All Animals and Fruits
Classes like `Animal` and `Fruit` make it easy to understand the concepts of classes and instances, but you probably won't see many zebras or lemons in real-world programs.

However, classes and objects are often used to model real-world objects. The code in the editor is a more realistic demonstration of the kind of classes and objects you might find in commercial software. Here we have a basic `ShoppingCart` class for creating shopping cart objects for website customers; though basic, it's similar to what you'd see in a real program.


##### Instructions
Create an instance of `ShoppingCart` called `my_cart`. Initialize it with any values you like, then use the `add_item` method to add an item to your cart.


```Python
# GIVEN
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



# SOLUTION by adding at the end
my_cart = ShoppingCart("Heval")
my_cart.add_item("Coffee", 10)

# to test
print(my_cart.items_in_cart)


# OUTPUT
Coffee added.

{'Coffee': 10}
```

### 11.11. Warning: Here Be Dragons
*Inheritance* is a tricky concept, so let's go through it step by step.

Inheritance is the process by which one class takes on the attributes and methods of another, and it's used to express an `is`-a relationship. For example, a Panda is a bear, so a Panda class could inherit from a Bear class. However, a Toyota is not a Tractor, so it shouldn't inherit from the Tractor class (even if they have a lot of attributes and methods in common). Instead, both Toyota and Tractor could ultimately inherit from the same Vehicle class.


##### Instructions

Check out the code in the editor. We've defined a class, `Customer`, as well as a `ReturningCustomer` class that inherits from `Customer`. Note that we don't define the `display_cart` method in the body of `ReturningCustomer`, but it will still have access to that method via inheritance. Click Run to see for yourself!


```Python
# GIVEN
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



# OUTPUT
I'm a string that stands in for the contents of your shopping cart!
I'm a string that stands in for your order history!
```

### 11.12. Inheritance Syntax
In Python, inheritance works like this:

```Python
class DerivedClass(BaseClass):
  # code goes here
```

where `DerivedClass` is the new class you're making and `BaseClass` is the class from which that new class inherits.

##### Instructions
On lines 1-4, we've created a class named `Shape`.

* Create your own class, `Triangle`, that inherits from `Shape`, like this:
```python
class Triangle(Shape):
# code goes here
```
* Inside the `Triangle` class, write an `__init__()` function that takes four arguments: `self`, `side1`, `side2`, and `side3`.
* Inside the `__init__()` function, `set self.side1 = side1`, `self.side2 = side2`, and `self.side3 = side3`.



```Python
# GIVEN
class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

# Add your Triangle class below!


# SOLUTION by adding at the end
class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3
```

### 11.13. Override!
Sometimes you'll want one class that inherits from another to not only take on the methods and attributes of its parent, but to *override* one or more of them.

```Python
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


# OUTPUT
Hello, Emily
Get back to work, Steve!
```

Rather than have a separate `greet_underling` method for our CEO, we override (or re-create) the `greet` method on top of the base `Employee.greet` method. This way, we don't need to know what type of Employee we have before we greet another Employee.


##### Instructions
Create a new class, `PartTimeEmployee`, that inherits from `Employee`.

Give your derived class a `calculate_wage` method that overrides `Employee`'s. It should take `self` and `hours` as arguments.

Because `PartTimeEmployee.calculate_wage` overrides `Employee.calculate_wage`, it still needs to set `self.hours = hours`.

It should `return` the part-time employee's number of `hours` worked multiplied by `12.00 `(that is, they get $12.00 per hour instead of $20.00).


```Python
# GIVEN
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!



# SOLUTION by adding at the end
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
```


### 11.14. This Looks Like a Job For...
On the flip side, sometimes you'll be working with a derived class (or *subclass*) and realize that you've overwritten a method or attribute defined in that class' base class (also called a *parent* or *superclass*) that you actually need. Have no fear! You can directly access the attributes or methods of a superclass with Python's built-in `super` call.

The syntax looks like this:

```Python
class Derived(Base):
  def m(self):
    return super(Derived, self).m()
```
Where `m()` is a method from the base class.


##### Instructions
First, inside your `PartTimeEmployee` class:

  * Add a new method called `full_time_wage` with the arguments `self` and `hours`.
  * That method should `return` the result of a `super` call to the `calculate_wage` method of `PartTimeEmployee`'s parent class. Use the example above for help.

Then, after your class:

  * Create an instance of the `PartTimeEmployee` class called `milton`. Don't forget to give it a name.
  * Finally, `print` out the result of calling his `full_time_wage` method. You should see his wage printed out at $20.00 per hour! (That is, for `10` hours, the result should be `200.00`.)


```Python
# GIVEN
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



# SOLUTION
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00

  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee('Milton')
print(milton.full_time_wage(10))



# OUTPUT
200.0
```

### 11.15. Class Basics
First things first: let's create a class to work with.


##### Instructions

Create a class, `Triangle`. Its `__init__()` method should take `self`, `angle1`, `angle2`, and `angle3` as arguments. Make sure to set these appropriately in the body of the `__init__()` method (see the Hint for more).

```Python
# SOLUTION
class Triangle(object):
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
```

### 11.16. Class It Up
Great! Now let's add a member variable and a method to our class.


##### Instructions
Inside the `Triangle` class:

* Create a variable named `number_of_sides` and set it equal to `3`.
Create a method named `check_angles`. The sum of a triangle's three angles should return `True` if the sum of `self.angle1`, `self.angle2`, and `self.angle3` is equal `180`, and `False` otherwise.


```Python
# GIVEN
class Triangle(object):
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3



# SOLUTION
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
```

### 11.17. Instantiate an Object
Let's go ahead and create an instance of our `Triangle` class.


##### Instructions
Create a variable named `my_triangle` and set it equal to a new instance of your `Triangle` class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).

Print out `my_triangle.number_of_sides`

Print out `my_triangle.check_angles()`


```Python
# GIVEN
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



# SOLUTION by adding at the end
my_triangle = Triangle(90, 45, 45)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())



# OUTPUT
3
True
```

### 11.18. Inheritance
Finally, let's create an `Equilateral` class that inherits from our `Triangle` class. (An equilateral triangle is a triangle whose angles are all 60˚, which also means that its three sides are equal in length.)


##### Instructions
Create a class named `Equilateral` that inherits from `Triangle`.

Inside `Equilateral`, create a member variable named `angle` and set it equal to `60`.

Create an `__init__()` function with only the parameter `self`, and set `self.angle1`, `self.angle2`, and `self.angle3` equal to `self.angle` (since an equilateral triangle's angles will always be 60˚).


```Python
# GIVEN
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



# SOLUTION
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



# OUTPUT
3
True
```

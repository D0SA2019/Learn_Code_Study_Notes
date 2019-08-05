# Python Classes and Inheritance
*Coursera | Python 3 Programming Specialization | Course 4*

## Week 1 : Classes

### Constructing Classes


Python is an object-oriented programming language. That means it provides features that support object-oriented programming (OOP).

Object-oriented programming has its roots in the 1960s, but it wasn’t until the mid 1980s that it became the main programming paradigm used in the creation of new software. It was developed as a way to handle the rapidly increasing size and complexity of software systems and to make it easier to modify these large and complex systems over time.

Up to now, some of the programs we have been writing use a procedural programming paradigm. In procedural programming the focus is on writing functions or procedures which operate on data. In object-oriented programming the focus is on the creation of objects which contain both data and functionality together. Usually, each object definition corresponds to some object or concept in the real world and the functions that operate on that object correspond to the ways real-world objects interact.


In Python, every value is actually an object. Whether it be a dictionary, a list, or even an integer, they are all objects. Programs manipulate those objects either by performing computation with them or by asking them to perform methods. To be more specific, we say that an object has a **state** and a collection of **methods** that it can perform. (More about **methods** below.) The state of an object represents those things that the object knows about itself. The state is stored in **instance variables**. For example, as we have seen with turtle objects, each turtle has a state consisting of the turtle’s position, its color, its heading and so on. Each turtle also has the ability to go forward, backward, or turn right or left. Individual turtles are different in that even though they are all turtles, they differ in the specific values of the individual state attributes (maybe they are in a different location or have a different heading).

![](https://fopp.umsi.education/runestone/static/fopp/_images/objectpic1.png)



#### 1.1. User-Defined Classes

We’ve already seen classes like `str`, `int`, `float` and `list`. These were defined by Python and made available for us to use. However, in many cases when we are solving problems we need to create data objects that are related to the problem we are trying to solve. We need to create our own classes.

As an example, consider the concept of a mathematical point. In two dimensions, a point is two numbers (coordinates) that are treated collectively as a single object. Points are often written in parentheses with a comma separating the coordinates. For example, `(0, 0)` represents the origin, and `(x, y)` represents the point `x` units to the right and `y` units up from the origin. This `(x,y)` is the state of the point.

Thinking about our diagram above, we could draw a `point` object as shown here.

![](https://fopp.umsi.education/runestone/static/fopp/_images/objectpic2.png)

Some of the typical operations that one associates with points might be to ask the point for its x coordinate, `getX`, or to ask for its y coordinate, `getY`. You would want these types of functions available to prevent accidental changes to these instance variables since doing so would allow you to view the values without accessing them directly. You may also wish to calculate the distance of a point from the origin, or the distance of a point from another point, or find the midpoint between two points, or answer the question as to whether a point falls within a given rectangle or circle. We’ll shortly see how we can organize these together with the data.

![](https://fopp.umsi.education/runestone/static/fopp/_images/objectpic3.png)


Now that we understand what a `point` object might look like, we can define a new **class**. We’ll want our points to each have an `x` and a `y` attribute, so our first class definition looks like this.

```python
class Point:
	"""Point class for representing and manipulating x,y coordinates."""

	def __init__(self):
		"""Create a new point at the origin"""
		self.x = 0
		self.y = 0
```

Class definitions can appear anywhere in a program, but they are usually near the beginning (after the `import` statements). The syntax rules for a class definition are the same as for other compound statements. There is a header which begins with the keyword, `class`, followed by the name of the class, and ending with a colon.

If the first line after the class header is a string, it becomes the docstring of the class, and will be recognized by various tools. (This is also the way docstrings work in functions.)

Every class should have a method with the special name `__init__`. This **initializer method**, often referred to as the **constructor**, is automatically called whenever a new instance of `Point` is created. It gives the programmer the opportunity to set up the attributes required within the new instance by giving them their initial state values. The `self` parameter (you could choose any other name, but nobody ever does!) is automatically set to reference the newly created object that needs to be initialized.

So let’s use our new Point class now. This next part should look a little familiar, if you remember some of the syntax for how we created instances of the Turtle class, in the chapter on Turtle graphics.


```python
class Point:
    """Point class for representing and manipulating x,y coordinates."""

    def __init__(self):
        self.x = 0
        self.y = 0

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print("Nothing seems to have happend with the points")
```


**Output** :

```
Nothing seems to have happend with the points
```

During the initialization of the objects, we created two attributes called `x` and `y` for each object, and gave them both the value `0`. You will note that when you run the program, nothing happens. It turns out that this is not quite the case. In fact, two `Points` have been created, each having an x and y coordinate with value 0. However, because we have not asked the program to do anything with the points, we don’t see any other result.

![](https://fopp.umsi.education/runestone/static/fopp/_images/objectpic4.png)

The following program adds a few print statements. You can see that the output suggests that each one is a `Point object`. However, notice that the `is` operator returns `False` meaning that they are different objects (we will have more to say about this in a later section).

```python
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
```


**Output** :

```
<__main__.Point object at 0x10d34cfd0>
<__main__.Point object at 0x10d263eb8>
False
```

A function like `Point` that creates a new object instance is called a **constructor**. Every class automatically uses the name of the class as the name of the constructor function. The definition of the constructor function is done when you write the `__init__` function (method) inside the class definition.

It may be helpful to think of a class as a factory for making objects. The class itself isn’t an instance of a point, but it contains the machinery to make point instances. Every time you call the constructor, you’re asking the factory to make you a new object. As the object comes off the production line, its initialization method is executed to get the object properly set up with it’s factory default settings.

The combined process of “make me a new object” and “get its settings initialized to the factory default settings” is called **instantiation**.


-------
--------


#### 1.2. Adding Parameters to the Constructor

Our constructor so far can only create points at location `(0,0)`. To create a point at position (7, 6) requires that we provide some additional capability for the user to pass information to the constructor. Since constructors are simply specially named functions, we can use parameters (as we’ve seen before) to provide the specific information.

We can make our class constructor more generally usable by putting extra parameters into the `__init__` method, as shown in this example.

```python
class Point:
	""" Point class for representing and manipulating x,y coordinates. """

	def __init__(self, initX, initY):
		self.x = initX
		self.y = initY

p = Point(7,6)
print(p.x)
print(p.y)
```


**Output** :

```
7
6
```

Now when we create new points, we supply the x and y coordinates as parameters. When the point is created, the values of `initX` and `initY` are assigned to the state of the object, in the **instance variables** x and y.

This is a common thing to do in the `__init__` method for a class: take in some parameters and save them as instance variables. Why is this useful? Keep in mind that the parameter variables will go away when the method is finished executing. The instance variables, however, will still be accessible anywhere that you have a handle on the object instance. This is a way of saving those initial values that are provided when the class constructor is invoked.


Later on, you will see classes where the `__init__` method does more than just save parameters as instance variables. For example, it might parse the contents of those variables and do some computation on them, storing the results in instance variables. It might even make an Internet connection, download some content, and store that in instance variables.

![](https://fopp.umsi.education/runestone/static/fopp/_images/objectpic5.png)

-------
--------

**Check Your Understanding**

**Q1** : Create a class called `NumberSet` that accepts 2 integers as input, and defines two instance variables: `num1` and `num2`, which hold each of the input integers. Then, create an instance of `NumberSet` where its num1 is 6 and its num2 is 10. Save this instance to a variable `t`.


```python
class NumberSet():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

t = NumberSet(6, 10)
print(t)
print(t.num1)
print(t.num2)
print(t.num1, t.num2)
```


**Output** :

```
<__main__.NumberSet object at 0x1103e80b8>
6
10
6 10
```


#### 1.3. Adding Other Methods to a Class

The key advantage of using a class like `Point` rather than something like a simple tuple `(7, 6)` now becomes apparent. We can add methods to the `Point` class that are sensible operations for points. Had we chosen to use a tuple to represent the point, we would not have this capability. Creating a class like `Point` brings an exceptional amount of “organizational power” to our programs, and to our thinking. We can group together the sensible operations, and the kinds of data they apply to, and each instance of the class can have its own state.

A **method** behaves like a function but it is invoked on a specific instance. For example, with a list bound to variable L, `L.append(7)` calls the function append, with the list itself as the first parameter and 7 as the second parameter. Methods are accessed using dot notation. This is why `L.append(7)` has 2 parameters even though you may think it only has one: the list stored in the variable `L` is the first parameter value and 7 is the second.

Let’s add two simple methods to allow a point to give us information about its state. The `getX` method, when invoked, will return the value of the x coordinate.

The implementation of this method is straight forward since we already know how to write functions that return values. One thing to notice is that even though the `getX` method does not need any other parameter information to do its work, there is still one formal parameter, `self`. As we stated earlier, all methods defined in a class that operate on objects of that class will have `self` as their first parameter. Again, this serves as a reference to the object itself which in turn gives access to the state data inside the object.

```python
class Point:
	""" Point class for representing and manipulating x,y coordinates. """
	def __init__(self, initX, initY):
		self.x = initX
		self.y = initY

	def getX(self):
		return self.x

	def getY(self):
		return self.y

p = Point(7,6)
print(p.getX())
print(p.getY())
```


**Output** :

```
7
6
```


Note that the `getX` method simply returns the value of the instance variable x from the object self. In other words, the implementation of the method is to go to the state of the object itself and get the value of `x`. Likewise, the `getY` method looks almost the same.

Let’s add another method, `distanceFromOrigin`, to see better how methods work. This method will again not need any additional information to do its work, beyond the data stored in the instance variables. It will perform a more complex task.


```python
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
print(p.distanceFromOrigin())
```


**Output** :

```
9.219544457292887
```

Notice that the call of `distanceFromOrigin` does not explicitly supply an argument to match the self parameter. This is true of all method calls. The definition will always seem to have one additional parameter as compared to the invocation.

-------
--------

**Check Your Understanding**

**Q1** : Create a class called `Animal` that accepts two numbers as inputs and assigns them respevtively to two instance variables: `arms` and `legs`. Create a class method called `limbs` that, when called, returns the total number of limbs the animal has. To the variable name `spider`, assign an instance of `Animal` that has 4 arms and 4 legs. Call the limbs method on the `spider` instance and save the result to the variable name `spidlimbs`.


```python
class Animal():
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs

    def limbs(self):
        return self.arms + self.legs

spider = Animal(4,4)
spidlimbs = spider.limbs()
print(spidlimbs)
```


**Output** :

```
8
```



### Objects and Instances

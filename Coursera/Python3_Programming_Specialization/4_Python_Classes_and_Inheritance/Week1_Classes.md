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

#### 1.4. Objects as Arguments and Parameters

You can pass an object as an argument to a function, in the usual way.

Here is a simple function called `distance` involving our new `Point` objects. The job of this function is to figure out the distance between two points.

```python
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


def distance(point1, point2):
    xdiff = point2.getX()-point1.getX()
    ydiff = point2.getY()-point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

p = Point(4,3)
q = Point(0,0)

print(distance(q,p))
```


**Output** :

```
5.0
```


`distance` takes two points and returns the distance between them. Note that `distance` is **not** a method of the `Point` class. You can see this by looking at the indentation pattern. It is not inside the class definition. The other way we can know that `distance` is not a method of Point is that `self` is not included as a formal parameter. In addition, we do not invoke `distance` using the dot notation.

We could have made distance be a method of the `Point` class. Then, we would have called the first parameter self, and would have invoked it using the dot notation, as in the following code. Which way to implement it is a matter of coding style. Both work correctly. Most programmers choose whether to make functions be stand-alone or methods of a class based on whether the function semantically seems to be an operation that is performed on instances of the class. In this case, because distance is really a property of a pair of points and is symmetric (the distance from a to b is the same as that from b to a) it makes more sense to have it be a standalone function and not a method. Many heated discussions have occurred between programmers about such style decisions.


```python
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
```


**Output** :

```
5.0
```

-------
--------

#### 1.5. Converting an Object to a String

When we’re working with classes and objects, it is often necessary to print an object (that is, to print the state of an object). Consider the example below.

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
print(p)
```


**Output** :

```
<__main__.Point object at 0x105b57fd0>
```

The `print` function shown above produces a string representation of the Point `p`. The default functionality provided by Python tells you that `p` is an object of type `Point`. However, it does not tell you anything about the specific state of the point.

We can improve on this representation if we include a special method call `__str__`. Notice that this method uses the same naming convention as the constructor, that is two underscores before and after the name. It is common that Python uses this naming technique for special methods.

The `__str__` method is responsible for returning a string representation as defined by the class creator. In other words, you as the programmer, get to choose what a `Point` should look like when it gets printed. In this case, we have decided that the string representation will include the values of x and y as well as some identifying text. It is required that the `__str__` method create and return a string.

Whatever string the `__str__` method for a class returns, that is the string that will print when you put any instance of that class in a print statement. For that reason, the string that a class’s `__str__` method returns should usually include values of instance variables. If a point has `x` value 3 and `y` value 4, but another point has `x` value 5 and `y` value 9, those two Point objects should probably look different when you print them, right?

Take a look at the code below.

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

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

p = Point(7,6)
print(p)
```


**Output** :

```
x = 7, y = 6
```

When we run the program above you can see that the `print` function now shows the string that we chose.

Now, you ask, don’t we already have a `str` type converter that can turn our object into a string? Yes we do!

And doesn’t `print` automatically use this when printing things? Yes again!

However, as we saw earlier, these automatic mechanisms do not do exactly what we want. Python provides many default implementations for methods that we as programmers will probably want to change. When a programmer changes the meaning of a method we say that we **override** the method. Note also that the `str` type converter function uses whatever `__str__` method we provide.

-------
--------

**Check Your Understanding**

**Q1** : Create a class called `Cereal` that accepts three inputs: 2 strings and 1 integer, and assigns them to 3 instance variables in the constructor: `name`, `brand`, and `fiber`. When an instance of `Cereal` is printed, the user should see the following: “[name] cereal is produced by [brand] and has [fiber integer] grams of fiber in every serving!” To the variable name `c1`, assign an instance of `Cereal` whose name is `"Corn Flakes"`, brand is `"Kellogg's"`, and fiber is `2`. To the variable name `c2`, assign an instance of `Cereal` whose name is `"Honey Nut Cheerios"`, brand is `"General Mills"`, and fiber is `3`. Practice printing both!

```python
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
```


**Output** :

```
Corn Flakes cereal is produced by Kellogg's and has 2 grams of fiber in every serving!
Honey Nut Cheerios cereal is produced by General Mills and has 3 grams of fiber in every serving!
```


#### 1.6. Instances as Return Values

Functions and methods can return objects. This is actually nothing new since everything in Python is an object and we have been returning values for quite some time. (You can also have lists or tuples of object instances, etc.) The difference here is that we want to have the method create an object using the constructor and then return it as the value of the method.

Suppose you have a point object and wish to find the midpoint halfway between it and some other target point. We would like to write a method, let’s call it `halfway`, which takes another `Point` as a parameter and returns the `Point` that is halfway between the point and the target point it accepts as input.

```python
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
```


**Output** :

```
x = 4.0, y = 8.0
4.0
8.0
```

The resulting Point, `mid`, has an x value of 4 and a y value of 8. We can also use any other methods on `mid` since it is a `Point` object.

-------
--------


#### 1.7. Sorting Lists of Instances

You previously learned how to sort lists. Sorting lists of instances of a class is not fundamentally different from sorting lists of objects of any other type. There is a way to define a default sort order for instances, right in the class definition, but it requires defining a bunch of methods or one complicated method, so we won’t bother with that. Instead, you should just provide a key function as a parameter to sorted (or sort).

Previously, you have seen how to provide such a function when sorting lists of other kinds of objects. For example, given a list of strings, you can sort them in ascending order of their lengths by passing a key parameter. Note that if you refer to a function by name, you give the name of the function without parentheses after it, because you want the function object itself. The sorted function will take care of calling the function, passing the current item in the list. Thus, in the example below, we write `key=len` and not `key=len()`.


```python
L = ["Cherry", "Apple", "Blueberry"]

print(sorted(L, key=len))
print(sorted(L, key= lambda x : len(x)))
```


**Output** :

```
['Apple', 'Cherry', 'Blueberry']
['Apple', 'Cherry', 'Blueberry']
```

When each of the items in a list is an instance of a class, you need to provide a function that takes one instance as an input, and returns a number. The instances will be sorted by their numbers.

```python
class Fruit():
	def __init__(self, name, price):
		self.name = name
		self.price = price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]

for f in sorted(L, key= lambda x: x.price):
	print(f.name)
```


**Output** :

```
Apple
Cherry
Blueberry
```

Sometimes you will find it convenient to define a method for the class that does some computation on the data in an instance. In this case, our class is too simple to really illustrate that. But to simulate it, I’ve defined a method `sort_priority` that just returns the price that’s stored in the instance. Now, that method, sort_priority takes one instance as input and returns a number. So it is exactly the kind of function we need to provide as the key parameter for sorted. Here it can get a little confusing: to refer to that method, without actually invoking it, you can refer to `Fruit.sort_priority`. This is analogous to the code above that referred to `len` rather than invoking `len()`.


```python
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
```


**Output** :

```
-----sorted by price, referencing a class method-----
Apple
Cherry
Blueberry
---- one more way to do the same thing-----
Apple
Cherry
Blueberry
```

-------
--------


#### 1.8. Class Variables and Instance Variables

You have already seen that each instance of a class has its own namespace with its own instance variables. Two instances of the `Point` class each have their own instance variable `x`. Setting x in one instance doesn’t affect the other instance.

A class can also have class variables. A class variable is set as part of the class definition.

For example, consider the following version of the Point class. Here we have added a graph method that generates a string representing a little text-based graph with the Point plotted on the graph. It’s not a very pretty graph, in part because the y-axis is stretched like a rubber band, but you can get the idea from this.

Note that there is an assignment to the variable printed_rep on line 4. It is not inside any method. That makes it a class variable. It is accessed in the same way as instance variables. For example, on line 16, there is a reference to `self.printed_rep`. If you change line 4, you have it print a different character at the x,y coordinates of the Point in the graph.


```python
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
```


**Output** :

```
4
3 *
2
1
01234

3
2  *
1
0
9
8
7
6
5
4
3
2
1
01234567890123
```

To be able to reason about class variables and instance variables, it is helpful to know the rules that the python interpreter uses. That way, you can mentally simulate what the interpreter does.

**When the interpreter sees an expression of the form <obj>.<varname>, it:**
1. Checks if the object has an instance variable set. If so, it uses that value.
2. If it doesn’t find an instance variable, it checks whether the class has a class variable. If so it uses that value.
3. If it doesn’t find an instance or a class variable, it creates a runtime error (actually, it does one other check first, which you will learn about in the next chapter.)

**When the interpreter sees an assignment statement of the form <obj>.<varname> = <expr>, it:**
1. Evaluates the expression on the right-hand side to yield some python object;
2. Sets the instance variable <varname> of <obj> to be bound to that python object. Note that an assignment statement of this form never sets the class variable, it only sets the instance variable.

In order to set the class variable, you use an assignment statement of the form <varname> = <expr> at the top-level in a class definition, like on line 4 in the code above to set the class variable printed_rep.

**In case you are curious, method definitions also create class variables. Thus, in the code above, graph becomes a class variable that is bound to a function/method object. p1.graph() is evaluated by:**
* looking up p1 and finding that it’s an instance of Point
* looking for an instance variable called graph in p1, but not finding one
* looking for a class variable called graph in p1’s class, the Point class; it finds a function/method object
* Because of the () after the word graph, it invokes the function/method object, with the parameter self bound to the object p1 points to.

-------
--------


#### 1.9. Thinking About Classes and Instances

You can now imagine some reasons you may want to define a class. You have seen examples of creating types that are more complicated or specific than the ones built in to Python (like lists or strings). `Turtle`, with all the instance variables and methods you learned about using earlier in the semester, is a class that programmers defined which is now included in the Python language. In this chapter, we defined `Point` with some functionality that can make it easier to write programs that involve `x,y` coordinate `Point` instances. And shortly, you’ll see how you can define classes to represent objects in a game.

You can also use self-defined classes to hold data – for example, data you get from making a request to a REST API.

Before you decide to define a new class, there are a few things to keep in mind, and questions you should ask yourself:

* **What is the data that you want to deal with?** (Data about a bunch of songs from iTunes? Data about a bunch of tweets from Twitter? Data about a bunch of hashtag searches on Twitter? Two numbers that represent coordinates of a point on a 2-dimensional plane?)
* **What will one instance of your class represent?** In other words, which sort of new thing in your program should have fancy functionality? One song? One hashtag? One tweet? One point? The answer to this question should help you decide what to call the class you define.
* **What information should each instance have as instance variables?** This is related to what an instance represents. See if you can make it into a sentence. “Each instance represents one < song > and each < song > has an < artist > and a < title > as instance variables.” Or, “Each instance represents a < Tweet > and each < Tweet > has a < user (who posted it) > and < a message content string > as instance variables.”
* **What instance methods should each instance have?** What should each instance be able to do? To continue using the same examples: Maybe each song has a method that uses a lyrics API to get a long string of its lyrics. Maybe each song has a method that returns a string of its artist’s name. Or for a tweet, maybe each tweet has a method that returns the length of the tweet’s message. (Go wild!)
* **What should the printed version of an instance look like?** (This question will help you determine how to write the `__str__` method.) Maybe, “Each song printed out will show the song title and the artist’s name.” or “Each Tweet printed out will show the username of the person who posted it and the message content of the tweet.”

After considering those questions and making decisions about how you’re going to get start with a class definition, you can begin to define your class.

Remember that a class definition, like a function definition, is a general description of what every instance of the class should have. (Every Point has an `x` and a `y`.) The class instances are specific: e.g. the Point with a specific x and y >. You might have a Point with an `x` value of 3 and a` y` value of 2, so for that particular instance of the class `Point`, you’d pass in `3` and `2` to the constructor, the `__init__` method, like so: `new_point = Point(3,2)`, as you saw in the last sections.

-------
--------

#### 1.10. A Tamagotchi Game

There are also a lot of interesting ways to put user-defined classes to use that don’t involve data from the internet. Let’s pull all these mechanics together in a slightly more interesting way than we got with the Point class. Remember [Tamagotchis](https://en.wikipedia.org/wiki/Tamagotchi), the little electronic pets? As time passed, they would get hungry or bored. You had to clean up after them or they would get sick. And you did it all with a few buttons on the device.

We are going to make a simplified, text-based version of that. In your problem set and in the chapter on Inheritance <chap_inheritance> we will extend this further.

**First, let’s start with a class `Pet`. Each instance of the class will be one electronic pet for the user to take care of. Each instance will have a current state, consisting of three instance variables:**
* hunger, an integer
* oredom, an integer
* sounds, a list of strings, each a word that the pet has been taught to say

In the `__init__` method, hunger and boredom are initialized to random values between 0 and the threshold for being hungry or bored. The `sounds` instance variable is initialized to be a copy of the class variable with the same name. The reason we make a copy of the list is that we will perform destructive operations (appending new sounds to the list). If we didn’t make a copy, then those destructive operations would affect the list that the class variable points to, and thus teaching a sound to any of the pets would teach it to all instances of the class!

There is a `clock_tick` method which just increments the boredom and hunger instance variables, simulating the idea that as time passes, the pet gets more bored and hungry.

The `__str__` method produces a string representation of the pet’s current state, notably whether it is bored or hungry or whether it is happy. It’s bored if the boredom instance variable is larger than the threshold, which is set as a class variable.

To relieve boredom, the pet owner can either teach the pet a new word, using the `teach()` method, or interact with the pet, using the `hi()` method. In response to `teach()`, the pet adds the new word to its list of words. In response to the `hi()` method, it prints out one of the words it knows, randomly picking one from its list of known words. Both `hi()` and `teach()` cause an invocation of the `reduce_boredom()` method. It decrements the boredom state by an amount that it reads from the class variable `hunger_decrement`. The boredom state can never go below 0.

To relieve hunger, we call the `feed()` method.


```python
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
        # state += "Hunger {} Boredom {} Words {}".format(self.hunger, self.boredom, self.sounds)
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
```

Let’s try making a pet and playing with it a little. Add some of your own commands, too, and keep printing p1 to see what the effects are. If you want to directly inspect the state, try printing p1.boredom or p1.hunger.


```python
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
```

**Output** :

```
I'm Fido. I feel happy.
I'm Fido. I feel happy.
I'm Fido. I feel happy.
I'm Fido. I feel happy.
I'm Fido. I feel happy.
I'm Fido. I feel bored.
I'm Fido. I feel bored.
I'm Fido. I feel bored.
I'm Fido. I feel bored.
I'm Fido. I feel bored.
I'm Fido. I feel bored.
Mrrp
Mrrp
Mrrp
Mrrp
Boo
Mrrp
Mrrp
Mrrp
Mrrp
Boo
Mrrp
I'm Fido. I feel happy.
```

That’s all great if you want to interact with the pet by writing python code. Let’s make a game that non-programmers can play.

We will use the Listener Loop <chap_listener> pattern. At each iteration, we will display a text prompt reminding the user of what commands are available.

The user will have a list of pets, each with a name. The user can issue a command to adopt a new pet, which will create a new instance of Pet. Or the user can interact with an existing pet, with a Greet, Teach, or Feed command.

No matter what the user does, with each command entered, the clock ticks for all their pets. Watch out, if you have too many pets, you won’t be able to keep them all satisfied!


```python
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
```


**Output**

```
Quit
Adopt <petname_with_no_spaces_please>
Greet <petname>
Teach <petname> <word>
Feed <petname>

Choice: Adopt Jack

I'm Jack. I feel happy.

Quit
Adopt <petname_with_no_spaces_please>
Greet <petname>
Teach <petname> <word>
Feed <petname>

Choice: Teach Jack buuurrrpp

I'm Jack. I feel happy.

Quit
Adopt <petname_with_no_spaces_please>
Greet <petname>
Teach <petname> <word>
Feed <petname>

Choice: Greet Jack
Mrrp

I'm Jack. I feel happy.

Quit
Adopt <petname_with_no_spaces_please>
Greet <petname>
Teach <petname> <word>
Feed <petname>

Choice: Feed Jack

I'm Jack. I feel happy.

Quit
Adopt <petname_with_no_spaces_please>
Greet <petname>
Teach <petname> <word>
Feed <petname>

Choice: Teach Jack aaargghh

I'm Jack. I feel happy.

Quit
Adopt <petname_with_no_spaces_please>
Greet <petname>
Teach <petname> <word>
Feed <petname>

Choice: Greet Jack
Mrrp

I'm Jack. I feel happy.

Quit
Adopt <petname_with_no_spaces_please>
Greet <petname>
Teach <petname> <word>
Feed <petname>

Choice: Greet Jack
buuurrrpp

I'm Jack. I feel happy.

Quit
Adopt <petname_with_no_spaces_please>
Greet <petname>
Teach <petname> <word>
Feed <petname>

Choice: Quit
Exiting...
```

-------
--------

#### 1.11. Testing classes

To test a user-defined class, you will create test cases that check whether instances are created properly, and you will create test cases for each of the methods as functions, by invoking them on particular instances and seeing whether they produce the correct return values and side effects, especially side effects that change data stored in the instance variables. To illustrate, we will use the Point class that was used in the introduction to classes.

To test whether the class constructor (the `__init__`) method is working correctly, create an instance and then make tests to see whether its instance variables are set correctly. Note that this is a side effect test: the constructor method’s job is to set instance variables, which is a side effect. Its return value doesn’t matter.

A method like `distanceFromOrigin` in the `Point` class you saw does its work by computing a return value, so it needs to be tested with a return value test. A method like `move` in the `Turtle` class does its work by changing the contents of a mutable object (the point instance has its instance variable changed) so it needs to be tested with a side effect test.

Try adding some more tests in the code below, once you understand what’s there.

```python
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
```

**Output** :

```
Pass
Pass
Pass
Pass
Pass
```

-----
------

**Check your understanding**

**Q1** : For each function, you should create exactly one test case.

A. True <br>
B. False ✅ <br>


----

**Q2** : To test a method that changes the value of an instance variable, which kind of test case should you write?

A. return value test  <br>
B. side effect test ✅ <br>


----

**Q3** : To test the function maxabs, which kind of test case should you write?

```python
def maxabs(L):
   """L should be a list of numbers (ints or floats). The return value should be the maximum absolute value of the numbers in L."""
   return max(L, key=abs)
```

A. return value test  ✅ <br>
B. side effect test  <br>

----

**Q4** : We have usually used the `sorted` function, which takes a list as input and returns a new list containing the same items, possibly in a different order. There is also a method called `sort` for lists (e.g. `[1,6,2,4].sort()`). It changes the order of the items in the list itself, and it returns the value `None`. Which kind of test case would you use on the sort method?

A. return value test  <br>
B. side effect test  ✅ <br>


-----
-----


#### 1.12. Chapter Assessments & Exercises

#### Assessments

**A1**. Define a class called `Bike` that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, `color` and `price`. Assign to the variable `testOne` an instance of `Bike` whose color is **blue** and whose price is **89.99**. Assign to the variable `testTwo` an instance of `Bike` whose color is **purple** and whose price is **25.0**.


```python
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
```

**Output** :

```
blue
purple
89.99
25.0
```

-----

**A2**. Create a class called `AppleBasket` whose constructor accepts two inputs: a string reprsenting a color, and a number representing a quantity of apples. The constructor should initialize 2 instance variables: `apple_color` and `apple_quantity`. Write a class method called `increase` that increases the quantity by 1 each time it is invoked. You should also write a string method for this class that returns a string of the format: **A basket of QUANTITY# COLOR apples.** e.g. A basket of 4 red apples. or A basket of 50 blue apples. (Writing some test code that creates instances and assigns values to variables may help you solve this problem!)


```python
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
```

**Output** :

```
A basket of 12 green apples.
A basket of 15 green apples.
```

-----

**A3**. Define a class called `Bank` that accepts the name you want associated with your bank account in a string, and a float that represents the amount of money in the account. The constructor should initialize two instance variables from those inputs: `name` and `amt`. Add a string method so that when you print an instance of `Bank`, you see “Your account, [name goes here], has [start_amt goes here] dollars.” Create an instance of this class with `"Bob"` as the name and `100.0` as the amount. Save this to the variable `t1`.


```python
class Bank():
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt

    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name, str(self.amt))

t1 = Bank("Bob", 100.0)
print(t1)
```

**Output** :

```
Your account, Bob, has 100.0 dollars.
```

-----


----
----

#### Exercises


**Q1**. Add a method `reflect_x` to Point which returns a new Point, one which is the reflection of the point about the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)


```python
# Given
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

    def __str__(self):
        return str(self.x)+","+str(self.y)


# Solution
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

    def __str__(self):
        return str(self.x)+","+str(self.y)

    def reflect_x(self):
        return (self.x, -self.y)

print(Point(3, 5).reflect_x())
```

**Output** :

```
(3, -5)
```

-----


**Q2**.  Add a method called `move` that will take two parameters, call them `dx` and `dy`. The method will cause the point to move in the x and y direction the number of units given. (Hint: you will change the values of the state of the point)


```python
# Given
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

    # Put your new method here

    def __str__(self):
        return str(self.x)+","+str(self.y)


# Solution
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

p = Point(3, 5)
print(p.move(2,3))
```

**Output** :

```
(5, 8)
```

-----

# Python Functions, Files, and Dictionaries
*Coursera | Python 3 Programming Specialization | Course 2*

## Week 3 : Functions and Tuples

### Function Basics

#### 3.1. Defining Functions

**Introduction to Functions**

In Python, a function is a chunk of code that performs some operation that is meaningful for a person to think about as a whole unit, for example calculating a student’s GPA in a learning system or responding to the jump action in a video game. Once a function has been defined and you are satisfied that it does what it is supposed to do, you will start thinking about it in terms of the larger operation that it performs rather than the specific lines of code that make it work.

This breaking down of a task or problem is crucial to the successful implementation of any program of more than 50 or so lines (and plenty of smaller ones too). For example, the program that displays the Instagram landing page is made up of functions that:

* display the header bar
* display your friends’ posts
* display your friends’ stories
* display the ad at the bottom of the screen recommending you use the app

And each of those is made up of functions as well. For example, the function that displays your friends’ posts is a for loop that calls a function to:

* display a single post which in turn calls functions to:
* display the photo and name of the person posting the story
* display the photo itself
* display other users’ “likes” to the story
* display the comments on the story
* etc.

In this chapter you will learn about named functions, functions that can be referred to by name when you want to execute them.

#### Defining Functions

The syntax for creating a named function, a **function definition**, is:

```python
def name(parameters):
	statements
```

You can make up any names you want for the functions you create, except that you can’t use a name that is a Python keyword, and the names must follow the rules for legal identifiers that were given previously. The parameters specify what information, if any, you have to provide in order to use the new function. Another way to say this is that the parameters specify what the function needs to do its work.

There can be any number of statements inside the function, but they have to be indented from the def. In the examples in this book, we will use the standard indentation of four spaces. Function definitions are the third of several **compound statements** we will see, all of which have the same pattern:

1. A **header** line which begins with a keyword and ends with a colon.
2. A **body** consisting of one or more Python statements, each indented the same amount – 4 spaces is the Python standard – from the header line.

We’ve already seen the `for` statement which has the same structure, with an indented block of code, and the `if`, `elif`, and `else` statements that do so as well.

In a function definition, the keyword in the header is `def`, which is followed by the name of the function and some parameter names enclosed in parentheses. The parameter list may be empty, or it may contain any number of parameters separated from one another by commas. In either case, the parentheses are required.

We will come back to the parameters in a little while, but first let’s see what happens when a function is executed, using a function without any parameters to illustrate.

Here’s the definition of a simple function, hello.

```python
def hello():
	"""This function says hello and greets you"""
	print("Hello")
	print("Glad to meet you")
```

**docstrings**

If the first thing after the function header is a string (some tools insist that it must be a triple-quoted string), it is called a ***docstring*** and gets special treatment in Python and in some of the programming tools.

Another way to retrieve this information is to use the interactive interpreter, and enter the expression `<function_name>.__doc__`, which will retrieve the docstring for the function. So the string you write as documentation at the start of a function is retrievable by python tools at runtime. This is different from comments in your code, which are completely eliminated when the program is parsed.

By convention, Python programmers use docstrings for the key documentation of their functions.

We can apply functions to the turtle drawings we’ve done in the past as well.

```python
import turtle

def drawSquare(t, sz):
	"""Make turtle t draw a square of with side sz."""

	for i in range(4):
		t.forward(sz)
		t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.speed(1)
drawSquare(alex, 50)

wn.exitonclick()
```


**Output** :

![](https://media.giphy.com/media/L1JjCo0BnseZoP6Zoz/giphy.gif)


This function is named `drawSquare`. It has two parameters — one to tell the function which turtle to move around and the other to tell it the size of the square we want drawn. In the function definition they are called t and sz respectively. Make sure you know where the body of the function ends — it depends on the indentation and the blank lines don’t count for this purpose!


#### Function Invocation

Defining a new function does not make the function run. To execute the function, we need a **function call**. This is also known as a **function invocation**.

The way to invoke a function is to refer to it by name, followed by parentheses. Since there are no parameters for the function hello, we won’t need to put anything inside the parentheses when we call it. Once we’ve defined a function, we can call it as often as we like and its statements will be executed each time we call it.

```python
def hello():
	print("hello")
	print("Glad to meet you")

print(type(hello))
print(type("hello"))

hello()
print("Hey, that just printed two lines with one line of code!")
hello()
```

**Output**:

```
<class 'function'>
<class 'str'>
hello
Glad to meet you
Hey, that just printed two lines with one line of code!
hello
Glad to meet you
```

Let’s take a closer look at what happens when you define a function and when you execute the function. Try stepping through the code above.

First, note that in Step 1, when it executes line 1, it does not execute lines 2 and 3. Instead, as you can see in blue “Global variables” area, it creates a variable named hello whose value is a python function object. In the diagram that object is labeled hello() with a notation above it that it is a function.

At Step 2, the next line of code to execute is line 5. Just to emphasize that hello is a variable like any other, and that functions are python objects like any other, just of a particular type, line 5 prints out the type of the object referred to by the variable hello. It’s type is officially ‘function’.

Line 6 is just there to remind you of the difference between referring to the variable name (function name) hello and referring to the string “hello”.

At Step 4 we get to line 8, which has an invocation of the function. The way function invocation works is that the code block inside the function definition is executed in the usual way, but at the end, execution jumps to the point after the function invocation.

You can see that by following the next few steps. At Step 5, the red arrow has moved to line 2, which will execute next. We say that control has passed from the top-level program to the function hello. After Steps 5 and 6 print out two lines, at Step 7, control will be passed back to the point after where the invocation was started. At Step 8, that has happened.

The same process of invocation occurs again on line 10, with lines 2 and 3 getting executed a second time.

**Common Mistake with Functions**

It is a common mistake for beginners to forget their parenthesis after the function name. This is particularly common in the case where there parameters are not required. Because the hello function defined above does not require parameters, it’s easy to forget the parenthesis. This is less common, but still possible, when trying to call functions that require parameters.

----
----

**Check Your Understanding**

**Q1** : What is a function in Python?

A. A named sequence of statements. ✅ <br>
B. Any sequence of statements. <br>
C. A mathematical expression that calculates a value. <br>
D. A statement of the form x = 5 + 4. <br>


----
**Q2** : What is one main purpose of a function?

A. To improve the speed of execution <br>
B. To help the programmer organize programs into chunks that match how they think about the solution to the problem. ✅ <br>
C. All Python programs must be written using functions <br>
D. To calculate values <br>

----
**Q3** : How many lines will be output by executing this code?

```python
def hello():
	print("Hello")
	print("Glad to meet you")
```

A. 0 ✅ <br>
B. 1 <br>
C. 2 <br>

----
**Q3** : How many lines will be output by executing this code?

```python
def hello():
	print("Hello")
	print("Glad to meet you")

hello()
print("It works")
hello()
hello()
```

A. 0 <br>
B. 1 <br>
C. 3 <br>
D. 4 <br>
E. 7 ✅ <br>

----

#### 3.2. Function Parameters

Named functions are nice because, once they are defined and we understand what they do, we can refer to them by name and not think too much about what they do. With parameters, functions are even more powerful, because they can do pretty much the same thing on each invocation, but not exactly the same thing. The parameters can cause them to do something a little different.

The figure below shows this relationship. A function needs certain information to do its work. These values, often called **arguments** or **actual parameters** or **parameter values**, are passed to the function by the user.

![](https://fopp.umsi.education/runestone/static/fopp/_images/blackboxproc.png)

This type of diagram is often called a **black-box diagram** because it only states the requirements from the perspective of the user (well, the programmer, but the programmer who uses the function, who may be different than the programmer who created the function). The user must know the name of the function and what arguments need to be passed. The details of how the function works are hidden inside the “black-box”.

You have already been making function invocations with parameters. For example, when you write `len("abc")` or `len([3, 9, "hello"])`, len is the name of a function, and the value that you put inside the parentheses, the string “abc” or the list [3, 9, “hello”], is a parameter value.

When a function has one or more parameters, the names of the parameters appear in the function definition, and the values to assign to those parameters appear inside the parentheses of the function invocation. Let’s look at each of those a little more carefully.

In the definition, the parameter list is sometimes referred to as the **formal parameters** or **parameter names**. These names can be any valid variable name. If there is more than one, they are separated by commas.

In the function invocation, inside the parentheses one value should be provided for each of the parameter names. These values are separated by commas. The values can be specified either directly, or by any python expression including a reference to some other variable name.

That can get kind of confusing, so let’s start by looking at a function with just one parameter. The revised hello function personalizes the greeting: the person to greet is specified by the parameter.

```python
def hello2(s):
	print("Hello " + s)
	print("Glad to meet you")

hello2("Iman")
hello2("Jackie")
```


**Output** :


```
Hello Iman
Glad to meet you
Hello Jackie
Glad to meet you
```

First, notice that hello2 has one formal parameter, s. You can tell that because there is exactly one variable name inside the parentheses on line 1.

Next, notice what happened during Step 2. Control was passed to the function, just like we saw before. But in addition, the variable s was bound to a value, the string “Iman”. When it got to Step 7, for the second invocation of the function, s was bound to “Jackie”.

Function invocations always work that way. The expression inside the parentheses on the line that invokes the function is evaluated before control is passed to the function. The value is assigned to the corresponding formal parameter. Then, when the code block inside the function is executing, it can refer to that formal parameter and get its value, the value that was ‘passed into’ the function.

To get a feel for that, let’s invoke hello2 using some more complicated expressions. Try some of your own, too.

```python
def hello2(s):
	print("Hello " + s)
	print("Glad to meet you")

hello2("Iman" + " and Jackie")
hello3("Class " * 3)
```


**Output** :


```
Hello Iman and Jackie
Glad to meet you
Hello Class Class Class
Glad to meet you
```

Now let’s consider a function with two parameters. This version of hello takes a parameter that controls how many times the greeting will be printed.


```python
def hello3(s, n):
	greeting = "Hello {} ".format(s)
	print(greeting * n)

hello3("Wei", 4)
hello3("", 1)
hello3("Kitty", 11)
```


**Output** :


```
Hello Wei Hello Wei Hello Wei Hello Wei
Hello
Hello Kitty Hello Kitty Hello Kitty Hello Kitty Hello Kitty Hello Kitty Hello Kitty Hello Kitty Hello Kitty Hello Kitty Hello Kitty
```

That’s how function invocations always work. Each of the expressions, separated by commas, that are inside the parentheses are evaluated to produce values. Then those values are matched up positionally with the formal parameters. The first parameter name is bound to the first value provided. The second parameter name is bound to the second value provided. And so on.


----
----

**Check Your Understanding**

**Q1** : Which of the following is a valid function header (first line of a function definition)?

A. def greet(t): ✅  <br>
B. def greet: <br>
C. greet(t, n): <br>
D. def greet(t, n) <br>

----

**Q2** : What is the name of the following function?

```python
def print_many(x,y):
	"""Print out string x, y times."""
	for i in range(y):
		print(x)
```

A. def print_many(x, y):  <br>
B. print_many ✅ <br>
C. print_many(x, y)  <br>
D. Print out string x, y times.  <br>

----

**Q3** : What are the parameters of the following function?

```python
def print_many(x,y):
	"""Print out string x, y times."""
	for i in range(y):
		print(x)
```

A. i <br>
B. x <br>
C. x, y ✅ <br>
D. x, y, i <br>

----
**Q4** : Considering the function below, which of the following statements correctly invokes, or calls, this function (i.e., causes it to run)?

```python
def print_many(x,y):
	"""Print out string x, y times."""
	for i in range(y):
		print(x)

z = 3
```

A. print_many(x, y) <br>
B. print_many <br>
C. print_many("Greetings") <br>
D. print_many("Greetings", 10): <br>
E. print_many("Greetings", z) ✅ <br>

----

**Q5** : True or false: A function can be called several times by placing a function call in the body of a for loop.


A. True ✅ <br>
B. False <br>

----
**Q6** : What output will the following code produce?

```python
def cyu(s1,s2):
	if len(s1) > len(s2):
		print(s1)
	else:
		print(s2)

chu("Heloo", "Goodbye")
```

A. Hello <br>
B. Goodbye ✅ <br>
C. s1 <br>
D. s2 <br>

----


#### 3.3. Returning Values

![](https://fopp.umsi.education/runestone/static/fopp/_images/function_call.gif)

Not only can you pass a parameter value into a function, a function can also produce a value. You have already seen this in some previous functions that you have used. For example, `len` takes a list or string as a parameter value and returns a number, the length of that list or string. `range` takes an integer as a parameter value and returns a list containing all the numbers from 0 up to that parameter value.

Functions that return values are sometimes called **fruitful functions**. In many other languages, a function that doesn’t return a value is called a **procedure**, but we will stick here with the Python way of also calling it a function, or if we want to stress it, a non-fruitful function.

![](https://fopp.umsi.education/runestone/static/fopp/_images/blackboxfun.png)

How do we write our own fruitful function? Let’s start by creating a very simple mathematical function that we will call `square`. The square function will take one number as a parameter and return the result of squaring that number. Here is the black-box diagram with the Python code following.

![](https://fopp.umsi.education/runestone/static/fopp/_images/squarefun.png)



```python
def square(x):
	y = x * x
	return y

toSquare = 10
result = square(toSquare)
print("The result of {} squared is {}.".format(toSquare, result))
```


**Output** :


```
The result of 10 squared is 100.
```

The **return** statement is followed by an expression which is evaluated. Its result is returned to the caller as the “fruit” of calling this function. Because the return statement can contain any Python expression we could have avoided creating the **temporary variable** `y` and simply used return `x*x`. Try modifying the square function above to see that this works just the same. On the other hand, using **temporary variables** like `y` in the program above makes debugging easier. These temporary variables are referred to as **local variables**.


```python
def square(x):
	return x * x

toSquare = 10
result = square(toSquare)
print("The result of {} squared is {}.".format(toSquare, result))
```

**Output** :

```
The result of 10 squared is 100.
```

Notice something important here. The name of the variable we pass as an argument — `toSquare` — has nothing to do with the name of the formal parameter — `x`. It is as if `x = toSquare` is executed when `square` is called. It doesn’t matter what the value was named in the caller (the place where the function was invoked). Inside `square`, it’s name is `x`. You can see this very clearly in codelens, where the global variables and the local variables for the square function are in separate boxes.

There is one more aspect of function return values that should be noted. All Python functions return the special value `None` unless there is an explicit return statement with a value other than `None`. Consider the following common mistake made by beginning Python programmers. As you step through this example, pay very close attention to the return value in the local variables listing. Then look at what is printed when the function is over.


```python
def square(x):
	y = x * x
	print(y)

toSquare = 10
squareResult = square(toSquare)
print("The result of {} squared is {}.".format(toSquare, result))
```

**Output** :

```
100
The result of 10 squared is None.
```

The problem with this function is that even though it prints the value of the squared input, that value will not be returned to the place where the call was done. Instead, the value `None` will be returned. Since line 6 uses the return value as the right hand side of an assignment statement, `squareResult` will have `None` as its value and the result printed in line 7 is incorrect. Typically, functions will return values that can be printed or processed in some other way by the caller.

A return statement, once executed, immediately terminates execution of a function, even if it is not the last statement in the function. In the following code, when line 3 executes, the value 5 is returned and assigned to the variable x, then printed. Lines 4 and 5 never execute. Run the following code and try making some modifications of it to make sure you understand why “there” and 10 never print out.

```python
def weird():
	print("here")
	return 5
	print("there")
	return 10

x = weird()
print(x)
```

**Output** :

```
here
5
```

The fact that a return statement immediately ends execution of the code block inside a function is important to understand for writing complex programs, and it can also be very useful. The following example is a situation where you can use this to your advantage – and understanding this will help you understand other people’s code better, and be able to walk through code more confidently.

Consider a situation where you want to write a function to find out, from a class attendance list, whether anyone’s first name is longer than five letters, called `longer_than_five`. If there is anyone in class whose first name is longer than 5 letters, the function should return `True`. Otherwise, it should return `False`.

In this case, you’ll be using conditional statements in the code that exists in the **function body**, the code block indented underneath the function definition statement (just like the code that starts with the line `print("here")` in the example above – that’s the body of the function `weird`, above).

**Bonus challenge for studying**: After you look at the explanation below, stop looking at the code – just the description of the function above it, and try to write the code yourself! Then test it on different lists and make sure that it works. But read the explanation first, so you can be sure you have a solid grasp on these function mechanics.

First, an English plan for this new function to define called `longer_than_five`:

* You’ll want to pass in a list of strings (representing people’s first names) to the function.
* You’ll want to iterate over all the items in the list, each of the strings.
* As soon as you get to one name that is longer than five letters, you know the function should return `True` – yes, there is at least one name longer than five letters!
* And if you go through the whole list and there was no name longer than five letters, then the function should return `False`.

Now, the code:

```python
def longer_than_five(list_of_names):
	for name in list_of_names:
		if len(name) > 5:
			return True
	return False

list1 = ["Sam","Tera","Sal","Amita"]
list2 = ["Rey","Ayo","Lauren","Natalie"]

print(longer_than_five(list1))
print(longer_than_five(list2))
```

**Output** :

```
False
True
```

So far, we have just seen return values being assigned to variables. For example, we had the line `squareResult = square(toSquare)`. As with all assignment statements, the right hand side is executed first. It invokes the `square` function, passing in a parameter value 10 (the current value of `toSquare`). That returns a value 100, which completes the evaluation of the right-hand side of the assignment. 100 is then assigned to the variable `squareResult`. In this case, the function invocation was the entire expression that was evaluated.

Function invocations, however, can also be used as part of more complicated expressions. For example, s`quareResult = 2 * square(toSquare)`. In this case, the value 100 is returned and is then multiplied by 2 to produce the value 200. When python evaluates an expression like `x * 3`, it substitutes the current value of x into the expression and then does the multiplication. When python evaluates an expression like `2 * square(toSquare)`, it substitutes the return value 100 for entire function invocation and then does the multiplication.

To reiterate, when executing a line of code `squareResult = 2 * square(toSquare)`, the python interpreter does these steps:

1. It’s an assignment statement, so evaluate the right-hand side expression `2 * square(toSquare)`.
2. Look up the values of the variables square and toSquare: square is a function object and toSquare is 10
3. Pass 10 as a parameter value to the function, get back the return value 100
4. Substitute 100 for square(toSquare), so that the expression now reads `2 * 100`
4. Assign 200 to variable `squareResult`


----
----

**Check Your Understanding**

**Q1** : What is wrong with the following function definition:

```python
def addEm(x,y,z):
	return x+y+z
	print("the answer is", x+y+z)
```

A. You should never use a print statement in a function definition. <br>
B. You should not have any statements in a function after the return statement. Once the function gets to the return statement it will immediately stop executing the function. ✅ <br>
C. You must calculate the value of x+y+z before you return it. <br>
D. A function cannot return a number. <br>

----

**Q2** : What will the following function return?

```python
def addEm(x,y,z):
	print(x+y+z)
```

A. The value None ✅ <br>
B. The value of x+y+z <br>
C. The string 'x+y+z' <br>

----

**Q3** : What will the following code output?

```python
def square(x):
	y = x * x
	return y

print(square(5) + square(5))
```

A. 25 <br>
B. 50 ✅ <br>
C. 25 + 25 <br>

----

**Q4** : What will the following code output?

```python
def square(x):
	y = x * x
	return y

print(square(square(2)))
```

A. 8 <br>
B. 16 ✅ <br>
C. Error: can't put a function invocation inside parentheses <br>

----


**Q5** : What will the following code output?

```python
def cyu2(s1, s2):
	x = len(s1)
	y = len(s2)
	return x - y

z = cyu2("Yes", "no")

if z > 0:
	print("First one was longer")
else:
	print("Second one was at least as long")
```

A. 1 <br>
B. Yes <br>
C. First one was longer ✅ <br>
D. Second one was at least as long <br>
E. Error <br>

----

**Q6** : Which will print out first, square, g, or a number?

```python
def square(x):
	print("square")
	return x*x

def g(y):
	print("g")
	return y + 3

print(square(g(2)))
```

A. square <br>
B. g ✅ <br>
C. a number <br>

----

**Q7** : How many lines will the following code print?

```python
def show_me_numbers(list_of_ints):
	print(10)
	print("Next we'll accumulate the sum")
	accum = 0
	for num in list_of_ints:
		accum = accum + num
	return accum
	print("All done with accumulation!")

show_me_numbers([4,2,3])
```

A. 3 <br>
B. 2 ✅ <br>
C. None <br>

----

**Q8** : Write a function named `same` that takes a string as input, and simply returns that string.

```python
def same(str):
	return str

print(same("some string here"))
```

**Output**:

```
some string here
```

----

**Q9** : Write a function called `same_thing` that returns the parameter, unchanged.

```python
def same_thing(thing):
	return thing

print(same_thing(45))
print(same_thing("another string here"))
```

**Output**:

```
45
another string here
```

----

**Q10** : Write a function called `subtract_three` that takes an integer or any number as input, and returns that number minus three.

```python
def subtract_three(num):
	return num - 3

print(subtract_three(4))
```

**Output**:

```
1
```

----


**Q11** : Write a function called `change` that takes one number as its input and returns that number, plus 7.

```python
def change(num):
	return num + 7

print(change(7))
print(change(-4))
```

**Output**:

```
14
3
```

----

**Q12** : Write a function named `intro` that takes a string as input. Given the string “Becky” as input, the function should return: “Hello, my name is Becky and I love SI 106.”

```python
def intro(str):
	return "Hello, my name is {} and I love SI 106.".format(str)

print(intro("Becky"))
```

**Output**:

```
Hello, my name is Becky and I love SI 106.
```

----

**Q13** : Write a function called `s_change` that takes one string as input and returns that string, concatenated with the string ” for fun.”.

```python
def s_change(str):
	return str + " for fun."

print(s_change("Coding"))
```

**Output**:

```
Coding for fun.
```

----

**Q14** : Write a function called `decision` that takes a string as input, and then checks the number of characters. If it has over 17 characters, return “This is a long string”, if it is shorter or has 17 characters, return “This is a short string”.

```python
def decision(str):
	if len(str) > 17:
		return "This is a long string"
	else:
		return "This is a short string"

print(decision("Write a function called decision"))
print(decision("it has"))
```

**Output**:

```
This is a long string
This is a short string
```

----

#### 3.4. Decoding a Function


In general, when you see a function definition you will try figure out what the function does, but, unless you are writing the function, you won’t care how it does it.

For example, here is a summary of some functions we have seen already.

* `input` takes one parameter, a string. It is displayed to the user. Whatever the user types is returned, as a string.
* `int` takes one parameter. It can be of any type that can be converted into an integer, such as a floating point number or a string whose characters are all digits.

Sometimes, you will be presented with a function definition whose operation is not so neatly summarized as above. Sometimes you will need to look at the code, either the function definition or code that invokes the function, in order to figure out what it does.

To build your understanding of any function, you should aim to answer the following questions:

1. How many parameters does it have?
2. What is the type of values that will be passed when the function is invoked?
3. What is the type of the return value that the function produces when it executes?

If you try to make use of functions, ones you write or that others write, without being able to answer these questions, you will find that your debugging sessions are long and painful.

The first question is always easy to answer. Look at the line with the function definition, look inside the parentheses, and count how many variable names there are.

The second and third questions are not always so easy to answer. In Python, unlike some other programming languages, variables are not declared to have fixed types, and the same holds true for the variable names that appear as formal parameters of functions. You have to figure it out from context.

To figure out the types of values that a function expects to receive as parameters, you can look at the function invocations or you can look at the operations that are performed on the parameters inside the function.

Here are some clues that can help you determine the type of object associated with any variable, including a function parameter. If you see…

* `len(x)`, then x must be a string or a list. (Actually, it can also be a dictionary, in which case it is equivalent to the expression `len(x.keys())`. Later in the course, we will also see some other sequence types that it could be). x can’t be a number or a Boolean.
* `x - y`, x and y must be numbers (integer or float)
* `x + y`, x and y must both be numbers, both be strings, or both be lists
* `x[3]`, x must be a string or a list containing at least four items, or x must be a dictionary that includes 3 as a key.
* `x['3']`, x must be a dictionary, with ‘3’ as a key.
* `x[y:z]`, x must be a sequence (string or list), and y and z must be integers
* `x and y`, x and y must be Boolean
* `for x in y`, y must be a sequence (string or list) or a dictionary (in which case it’s really the dictionary’s keys); x must be a character if y is a string; if y is a list, x could be of any type.



----
----

**Check Your Understanding**

**Q1** : How many parameters does function cyu3 take?


```python
def cyu3(x, y, z):
	if x - y > 0:
		return y - 2
	else:
		z.append(y)
		return x + 3
```

A. 0 <br>
B. 1 <br>
C. 2 <br>
D. 3 ✅ <br>
E. Can't tell <br>

----


**Q2** : What are the possible types of variables x and y?


```python
def cyu3(x, y, z):
	if x - y > 0:
		return y - 2
	else:
		z.append(y)
		return x + 3
```

A. integer ✅ <br>
B. float ✅ <br>
C. list <br>
D. string <br>
E. Can't tell <br>

----

**Q3** : What are the possible types of variable z?


```python
def cyu3(x, y, z):
	if x - y > 0:
		return y - 2
	else:
		z.append(y)
		return x + 3
```

A. integer <br>
B. float <br>
C. list ✅ <br>
D. string <br>
E. Can't tell <br>

----

**Q4** : What are the possible types of the return value from cyu3?


```python
def cyu3(x, y, z):
	if x - y > 0:
		return y - 2
	else:
		z.append(y)
		return x + 3
```

A. integer ✅ <br>
B. float ✅ <br>
C. list <br>
D. string <br>
E. Can't tell <br>

----

#### 3.5. A Function that Accumulates

We have used the `len` function a lot already. If it weren’t part of python, our lives as programmers would have been a lot harder.

Well, actually, not that much harder. Now that we know how to define functions, we could define `len` ourselves if it did not exist. Previously, we have used the accumlator pattern to count the number of lines in a file. Let’s use that same idea and just wrap it in a function definition. We’ll call it `mylen` to distinguish it from the real `len` which already exists. We actually could call it len, but that wouldn’t be a very good idea, because it would replace the original len function, and our implementation may not be a very good one.


```python
def mylen(seq):
	c = 0
	for _ in seq:
		c = c + 1
	return c

print(mylen("hello"))
print(mylen([1, 2, 7]))
```

**Output** :

```
5
3
```

----
----

**Check Your Understanding**

**Q1** : Write a function named `total` that takes a list of integers as input, and returns the total value of all those integers added together.


```python
def total(alist):
	tot = 0
	for number in alist:
		tot += number
	return tot

list_a = [1, 4, 2, 8, 30]
list_b = [3, 2, 9, 7]
```

**Output** :

```
45
21
```

----

**Q2** : Write a function called `count` that takes a list of numbers as input and returns a count of the number of elements in the list.


```python
def count(alist):
	co = 0
	for number in alist:
		co += 1
	return co

list_a = [1, 4, 2, 8, 30]
list_b = [3, 2, 9, 7]

print(count(list_a))
print(count(list_b))
```

**Output** :

```
5
4
```

----

### Local and Global Variables, and Side Effects

#### 3.6. Local and Global Variables

#### Local Variables

An assignment statement in a function creates a local variable for the variable on the left hand side of the assignment operator. It is called local because this variable only exists inside the function and you cannot use it outside. For example, consider again the `square` function:

```python
def square(x):
	y = x * x
	return y

z = square(10)
print(y)
```

**Output** :

```
Traceback (most recent call last):
  File "Week3_Functions_and_Tuples.py", line 265, in <module>
    print(y)
NameError: name 'y' is not defined
```

Try running this in Codelens. When a function is invoked in Codelens, the local scope is separated from global scope by a blue box. Variables in the local scope will be placed in the blue box while global variables will stay in the global frame. If you press the ‘last >>’ button you will see an error message. When we try to use y on line 6 (outside the function) Python looks for a global variable named y but does not find one. This results in the error: `Name Error: 'y' is not defined.`

The variable `y` only exists while the function is being executed — we call this its **lifetime**. When the execution of the function terminates (returns), the local variables are destroyed. Codelens helps you visualize this because the local variables disappear after the function returns. Go back and step through the statements paying particular attention to the variables that are created when the function is called. Note when they are subsequently destroyed as the function returns.

Formal parameters are also local and act like local variables. For example, the lifetime of `x` begins when `square` is called, and its lifetime ends when the function completes its execution.

So it is not possible for a function to set some local variable to a value, complete its execution, and then when it is called again next time, recover the local variable. Each call of the function creates new local variables, and their lifetimes expire when the function returns to the caller.


#### Global Variables

Variable names that are at the top-level, not inside any function definition, are called global.

It is legal for a function to access a global variable. However, this is considered bad form by nearly all programmers and should be avoided. This subsection includes some examples that illustrate the potential interactions of global and local variables. These will help you understand exactly how python works. Hopefully, they will also convince you that things can get pretty confusing when you mix local and global variables, and that you really shouldn’t do it.

Look at the following, nonsensical variation of the square function.

```python
def badsquare(x):
	y = x ** power
	return y

power = 2
result = badsquare(10)
print(result)
```

**Output** :

```
100
```

Although the `badsquare` function works, it is silly and poorly written. We have done it here to illustrate an important rule about how variables are looked up in Python. First, Python looks at the variables that are defined as local variables in the function. We call this the **local scope**. If the variable name is not found in the local scope, then Python looks at the **global variables**, or global scope. This is exactly the case illustrated in the code above. `power` is not found locally in `badsquare` but it does exist globally. The appropriate way to write this function would be to pass power as a parameter. For practice, you should rewrite the badsquare example to have a second parameter called power.

There is another variation on this theme of local versus global variables. Assignment statements in the local function cannot change variables defined outside the function.

```python
def powerof(x,p):
	power = p
	y = x ** power
	return y

power = 3
result = powerof(10, 2)
print(result)
```

**Output** :

```
100
```

Now step through the code. What do you notice about the values of variable `power` in the local scope compared to the variable `power` in the global scope?

The value of `power` in the local scope was different than the global scope. That is because in this example `power` was used on the left hand side of the assignment statement `power = p`. When a variable name is used on the left hand side of an assignment statement Python creates a local variable. When a local variable has the same name as a global variable we say that the local shadows the global. A **shadow** means that the global variable cannot be accessed by Python because the local variable will be found first. This is another good reason not to use global variables. As you can see, it makes your code confusing and difficult to understand.

If you really want to change the value of a global variable inside a function, you can can do it by explicitly declaring the variable to be global, as in the example below. Again, you should not do this in your code. The example is here only to cement your understanding of how python works.

```python
def powerof(x,p):
	global power
	power = p
	y = x ** power
	return y

power = 3
result = powerof(10, 2)
print(result)
print(power)
```

**Output** :

```
100
2
```

To cement all of these ideas even further lets look at one final example. Inside the `square` function we are going to make an assignment to the parameter `x` There’s no good reason to do this other than to emphasize the fact that the parameter `x` is a local variable. If you step through the example in codelens you will see that although `x` is 0 in the local variables for `square`, the x in the global scope remains 2. This is confusing to many beginning programmers who think that an assignment to a formal parameter will cause a change to the value of the variable that was used as the actual parameter, especially when the two share the same name. But this example demonstrates that that is clearly not how Python operates.

```python
def square(x):
	y = x * x
	x = 0
	return y

x = 2
z = square(x)
print(z)
```

**Output** :

```
4
```

**Note**

WP: Scope

You may be asking yourself at this point when you should make some object a local variable and when should you make it a global variable. Generally, we do not recommend making variables global. Imagine you are trying to write a program that keeps track of money while purchasing groceries. You may make a variable that represents how much money the person has, called `wallet`. You also want to make a function called `purchase`, which will take the name of the item and its price, and then add the item to a list of groceries, and deduct the price from the amount stored in `wallet`. If you initialize wallet before the function as a variable within the global scope instead of passing it as a third parameter for `purchase`, then an error would occur because wallet would not be found in the local scope. Though there are ways to get around this, as outlined in this page, if your program was supposed to handle groceries for multiple people, then you would need to declare each wallet as a global variable in the functions that want to use wallet, and that would become very confusing and tedious to deal with.


----
----

**Check Your Understanding**

**Q1** : True or False: Local variables can be referenced outside of the function they were defined in.

A. True <br>
B. False ✅ <br>

----

**Q2** : Which of the following are local variables? Please, write them in order of what line they are on in the code.

```python
numbers = [1, 12, 13, 4]
def foo(bar):
	aug = str(bar) + "street"
	return aug

addresses = []
for item in numbers:
	addresses.append(foo(item))
```

**Answer** :

```
bar
aug
```

----

**Q3** : What is the result of the following code?

```python
def adding(x):
	y = 3
	z = y + x + x
	return z

def producing(x):
	z = x * y
	return z

print(producing(adding(4)))
```

A. 33 <br>
B. 12 <br>
C. There is an error in the code. ✅ <br>

-------

**Q4** : What is a variable’s scope?

A. Its value <br>
B. The range of statements in the code where a variable can be accessed. ✅ <br>
C. Its name <br>


----
**Q5** : What is a local variable?

A. A temporary variable that is only used inside a function ✅ <br>
B. The same as a parameter <br>
C. Another name for any variable <br>

----

**Q6** : Can you use the same name for a local variable as a global variable?

A. Yes, and there is no reason not to. <br>
B. Yes, but it is considered bad form. ✅ <br>
C. No, it will cause an error. <br>

----

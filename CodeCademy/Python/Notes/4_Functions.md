# 4. Functions
### 4.1. What Good are Functions?
You might have considered the situation where you would like to reuse a piece of code, just with a few different values. Instead of rewriting the whole code, it's much cleaner to define a function, which can then be used repeatedly.


##### Instructions
Check out the code in the editor. If you completed the **Tip Calculator** lesson, you'll remember going through and calculating tax and tip in one chunk of program. Here you can see we've `def`ined two functions: `tax` to calculate the tax on a bill, and `tip` to compute the tip.

See how much of the code you understand at first glance (we'll explain it all soon). When you're ready, click Run to continue.


```Python
#GIVEN
def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print("With tax: %f" % bill)
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print("With tip: %f" % bill)
  return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)


# OUTPUT
With tax: 108.000000
With tip: 124.200000

```



### 4.2. Function Junction
Functions are defined with three components:

1. The *header*, which includes the `def` keyword, the name of the function, and any *parameters* the function requires. Here's an example:

```python
def hello_world() : # There are no parameters
```

2. An optional comment that explains what the function does.

```python
"""Prints 'Hello World!' to the console."""
```

3. The body, which describes the procedures the function carries out. The body is *indented*, just like conditional statements.

```python
print("Hello World!")
```


Here's the full function pieced together:

```python
def hello_world():
  """Prints 'Hello World!' to the console."""
  print("Hello World!")
```

##### Instructions

Go ahead and create a function, `spam`, that `print`s the string `"Eggs!"` to the console. Don't forget to include a comment of your own choosing (enclose it in triple quotes!).

```Python
#GIVEN
# Define your spam function starting on line 5. You
# can leave the code on line 10 alone for now--we'll
# explain it soon!


# Define the spam function above this line.
spam()


# SOLUTION
def spam():
  """Let's print some eggs!"""
  print("Eggs!")

spam()

# OUTPUT
Eggs!
```


### 4.3. Call and Response
After defining a function, it must be *called* to be implemented. In the previous exercise, `spam()` in the last line told the program to look for the function called `spam` and execute the code inside it.


##### Instructions
We've set up a function, `square`. Call it on the number `10` (by putting `10` between the parentheses of `square()`) on line 10!


```Python
#GIVEN
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print("%d squared is %d." % (n, squared))
  return squared

# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses.

# SOLUTION
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print("%d squared is %d." % (n, squared))
  return squared

square(10)

# OUTPUT
10 squared is 100.
```


### 4.4. Parameters and Arguments
Let's take another look at the definition of the function square from the previous exercise:

```python
def square(n):
```

Here, `n` is a parameter of `square`. A parameter is a variable that is an input to a function. It says, *"Later, when `square` is used, you'll be able to input any value you want, but for now we'll call that future value n."* A function can have any number of parameters.

The values of the parameters passed into a function are known as the arguments. Recall in the previous example, we called:

```python
def square(10):
```

Here, the function `square` was called with the parameter `n` set to the argument `10`.

Typically, when you call a function, you should pass in the same number of arguments as there are parameters.

To summarize:

* When defining a function, placeholder variables are called parameters.
* When using, or calling, a function, inputs into the function are called arguments.


##### Instructions
Check out the function in the editor, `power`. It should take two arguments, a base and an exponent, and raise the first to the power of the second. It's currently broken, however, because its parameters are missing.

Replace the `___`s with the parameters `base` and `exponent` and then call the `power` function with a `base` of `37` and an `exponent` of `4`.


```Python
#GIVEN
def power(___, ___):  # Add your parameters here!
  result = base ** exponent
  print("%d to the power of %d is %d." % (base, exponent, result))

power(__, __)  # Add your arguments here!

# SOLUTION
def power(base, exponent):
  result = base ** exponent
  print("%d to the power of %d is %d." % (base, exponent, result))

power(37, 4)

# OUTPUT
37 to the power of 4 is 1874161.
```


### 4.5. Functions Calling Functions
We've seen functions that can print text or do simple arithmetic, but functions can be much more powerful than that. For example, a function can call another function:

```python
def fun_one(n):
  return n * 5

def fun_two(m):
  return fun_one(m) + 7
```


##### Instructions
Let's look at the two functions in the editor: `one_good_turn` (which adds `1` to the number it takes in as an argument) and `deserves_another` (which adds `2`).

Change the body of `deserves_another` so that it always adds `2` to the output of `one_good_turn`.


```Python
#GIVEN
def one_good_turn(n):
  return n + 1

def deserves_another(n):
  return n + 2

# SOLUTION
def one_good_turn(n):
  return n + 1

def deserves_another(n):
  return one_good_turn(n) + 2

print(one_good_turn(5))
print(deserves_another(5))

# OUTPUT
6
8
```


### 4.6. Practice Makes Perfect
Let's create a few more functions just for good measure.

```python
def shout(phrase):
  if phrase == phrase.upper():
    return "YOU'RE SHOUTING!"
  else:
    return "Can you speak up?"

print(shout("I'M INTERESTED IN SHOUTING"))
print(shout("I'm interested in shouting"))

# OUTPUT
YOU'RE SHOUTING!
Can you speak up?
```
The example above is just there to help you remember how functions are structured.

Don't forget the colon at the end of your function definition!

##### Instructions
First, `def` a function called `cube` that takes an argument called `number`. Don't forget the parentheses and the colon!

Make that function `return` the cube of that number (i.e. that number multiplied by itself and multiplied by itself once again).

Define a second function called `by_three` that takes an argument called `number`.

`if` that number is divisible by 3, `by_three` should call cube(number) and `return` its result. Otherwise, `by_three` should `return False`.

Don't forget that `if` and `else` statements need a `:` at the end of that line!


```Python
#SOLUTION
def cube(number):
  return number ** 3

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False

print(cube(2))
print(by_three(2))

print(cube(3))
print(by_three(3))


# OUTPUT
8
False
27
27
```


### 4.7. I Know Kung Fu
Remember `import this` from the first exercise in this course? That was an example of *importing* a module. A module is a file that contains definitions—including variables and functions—that you can use once it is imported.


##### Instructions
Before we try any fancy importing, let's see what Python already knows about square roots. On line 3 in the editor, ask Python to

```python
print(sqrt(25))
```

which we would expect to equal five.

Instead, it throws an error.


```Python
#SOLUTION
print(sqrt(25))

# OUTPUT
Traceback (most recent call last):
  File "python", line 3, in <module>
NameError: name 'sqrt' is not defined
```


### 4.8. Generic Imports

Did you see that? Python said: `NameError: name 'sqrt' is not defined.` Python doesn't know what square roots are—yet.

There is a Python module named `math` that includes a number of useful variables and functions, and `sqrt()` is one of those functions. In order to access `math`, all you need is the `import` keyword. When you simply import a module this way, it's called a generic import.

##### Instructions
You'll need to do two things here:

* Type `import math` on line 2 in the editor.
* Insert `math.` before `sqrt()` so that it has the form `math.sqrt()`. This tells Python not only to `import math`, but to get the `sqrt()` function from within `math`. Then hit Run to see what Python now knows.


```Python
# GIVEN
# Ask Python to print sqrt(25) on line 3.

print sqrt(25)


# SOLUTION
import math
print(math.sqrt(25))


# OUTPUT
5.0
```


### 4.9. Function Imports
Nice work! Now Python knows how to take the square root of a number.

However, we only really needed the `sqrt` function, and it can be frustrating to have to keep typing `math.sqrt()`.

It's possible to import only certain variables or functions from a given module. Pulling in just a single function from a module is called a *function import*, and it's done with the `from` keyword:


```python
from module import function
```
Now you can just type `sqrt()` to get the square root of a number—no more `math.sqrt()`!


##### Instructions
Let's import only the `sqrt` function from `math` this time. (You don't need the `()` after sqrt in the `from math import sqrt` bit.)


```Python
# SOLUTION
from math import sqrt
```



### 4.10. Universal Imports
Great! We've found a way to handpick the variables and functions we want from modules.

What if we still want all of the variables and functions in a module but don't want to have to constantly type `math.`?

Universal import can handle this for you. The syntax for this is:

```python
from module import *
```


##### Instructions
Use the power of `from module import *` to import everything from the `math` module on line 3 of the editor.


```Python
# SOLUTION
from math import *
```


### 4.11. Here Be Dragons
Universal imports may look great on the surface, but they're not a good idea for one very important reason: they fill your program with a ton of variable and function names without the safety of those names still being associated with the module(s) they came from.

If you have a function of your very own named `sqrt` and you `import math`, your function is safe: there is your `sqrt` and there is `math.sqrt`. If you do `from math import *`, however, you have a problem: namely, two different functions with the exact same name.

Even if your own definitions don't directly conflict with names from imported modules, if you `import *` from several modules at once, you won't be able to figure out which variable or function came from where.

For these reasons, it's best to stick with either `import module` and type `module.name` or just `import` specific variables and functions from various modules as needed.



##### Instructions

The code in the editor will show you everything available in the `math` module.

Click Run to check it out (you'll see `sqrt`, along with some other useful things like `pi`, `factorial`, and trigonometric functions.


```Python
# GIVEN
import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print(everything) # Prints 'em all!


# OUTPUT
'__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc'
```


### 4.12. On Beyond Strings
Now that you understand what functions are and how to import modules, let's look at some of the functions that are built in to Python (no modules required!).

You already know about some of the built-in functions we've used with strings, such as `.upper()`, `.lower()`, `str()`, and `len()`. These are great for doing work with strings, but what about something a little more analytic?



##### Instructions

What do you think the code in the editor will do? Click Run when you think you have an idea.


```Python
# GIVEN
def biggest_number(*args):
  print(max(args))
  return max(args)

def smallest_number(*args):
  print(min(args))
  return min(args)

def distance_from_zero(arg):
  print(abs(arg))
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)


# OUTPUT
10
-10
10
```


### 4.13. `max()`
The `max()` function takes any number of arguments and returns the largest one. ("Largest" can have odd definitions here, so it's best to use `max()` on integers and floats, where the results are straightforward, and not on other objects, like strings.)

For example, `max(1,2,3)` will return `3` (the largest number in the set of arguments).


##### Instructions
Try out the `max()` function on line 3 of the editor. You can provide any number of integer or float arguments to `max()`.


```Python
# GIVEN
# Set maximum to the max value of any set of numbers on line 3!
maximum =
print(maximum)

# SOLUTION
maximum = max(38,93,1,20,40)
print(maximum)

maximum = max(38,-93,1,20,40)
print(maximum)

# OUTPUT
93
40
```


### 4.14. `min()`

`min()` then returns the smallest of a given series of arguments.

##### Instructions

Go ahead and set minimum equal to the `min()` of any set of integers or floats you'd like.

```Python
# GIVEN
minimum =
print(minimum)


# SOLUTION
minimum = min(38,93,1,20,40)
print(minimum)

minimum = min(38,-93,1,20,40)
print(minimum)

# OUTPUT
1
-93
```

### 4.15. `abs()`

The `abs()` function returns the **absolute value** of the number it takes as an argument—that is, that number's distance from `0` on an imagined number line. For instance, `3` and `-3` both have the same absolute value: `3`. The `abs()` function always returns a positive value, and unlike `max()` and `min()`, it only takes a single number.

##### Instructions
Set absolute equal to the absolute value of -42 on line 1.

```Python
# GIVEN
absolute =
print(absolute)


# SOLUTION
absolute = abs(-42)
print(absolute)

# OUTPUT
42
```




### 4.16. `type()`
Finally, the `type()` function returns the type of the data it receives as an argument. If you ask Python to do the following:

```python
print(type(42))
print(type(4.2))
print(type("spam"))
```

Python will output:

```
<class 'int'>
<class 'float'>
<class 'str'>
```

##### Instructions
Have Python print out the type of an `int`, a `float`, and a `str` string in the editor. You can pick any values on which to call `type()`, so long as they produce one of each.

```Python
# SOLUTION
print(type(-23))
print(type(32.98))
print(type("Babe!"))

# OUTPUT
<class 'int'>
<class 'float'>
<class 'str'>
```



### 4.17. Review: Functions
Okay! Let's review functions.

```python
def speak(message):
  return message

if happy():
  speak("I'm happy!")
elif sad():
  speak("I'm sad.")
else:
  speak("I don't know what I'm feeling.")
```

Again, the example code above is just there for your reference!

##### Instructions
First, `def` a function, `shut_down`, that takes one argument `s`. Don't forget the parentheses or the colon!

Then, `if` the `shut_down` function receives an `s` equal to `"yes"`, it should `return "Shutting down"`

Alternatively, `elif` `s` is equal to `"no"`, then the function should `return "Shutdown aborted"`.

Finally, if `shut_down` gets anything other than those inputs, the function should `return "Sorry"`

```Python
# SOLUTION
def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"

print(shut_down("yes"))
print(shut_down("no"))
print(shut_down("what"))



# OUTPUT
Shutting down
Shutdown aborted
Sorry
```


### 4.18. Review: Modules

Good work! Now let's see what you remember about importing modules (and, specifically, what's available in the `math` module).


##### Instructions
Import the `math` module in whatever way you prefer. Call its `sqrt` function on the number `13689` and `print` that value to the console.

```Python
# SOLUTION
import math
print(math.sqrt(13689))

# or

from math import sqrt
print(sqrt(13689))

# OUTPUT
117.0
```


### 4.19. Review: Built-in Functions
Perfect! Last but not least, let's review the built-in functions you've learned about in this lesson.

```python
def is_numeric(num):
  return type(num) == int or type(num) == float:

max(2, 3, 4) # 4
min(2, 3, 4) # 2

abs(2) # 2
abs(-2) # 2
```


##### Instructions
First, `def` a function called `distance_from_zero`, with one argument (choose any argument name you like).

If the `type` of the argument is either `int` or `float`, the function should `return` the `abs`olute value of the function input.

Otherwise, the function should `return "Nope"`

```Python
# SOLUTION
def distance_from_zero(value):
  if type(value) == int or type(value) == float:
    return abs(value)
  else:
    return "Nope"

print(distance_from_zero(89))
print(distance_from_zero(89.98))
print(distance_from_zero("89"))


# OUTPUT
89
89.98
Nope
```

# Python Basics
*Coursera | Python 3 Programming Specialization | Course 1*


## Week 1 : Introduction to the Specialization
### Welcome to Python Basics!

Programming is giving a list of instructins for a computer to follow. In the contest of programming, this instructions are sometimes called algorithms.

Runestone Interactive Textbook : https://fopp.umsi.education/assignments/

The programming language you will be learning is Python. Python is an example of a **high-level language**; other high-level languages you might have heard of are C++, PHP, and Java.

As you might infer from the name high-level language, there are also **low-level languages**, sometimes referred to as machine languages or assembly languages. Loosely speaking, computers can only execute programs written in low-level languages. Thus, programs written in a high-level language have to be processed before they can run. This extra processing takes some time, which is a small disadvantage of high-level languages. However, the advantages to high-level languages are enormous.

First, it is much easier to program in a high-level language. Programs written in a high-level language take less time to write, they are shorter and easier to read, and they are more likely to be correct. Second, high-level languages are portable, meaning that they can run on different kinds of computers with few or no modifications. Low-level programs can run on only one kind of computer and have to be rewritten to run on another.

Due to these advantages, almost all programs are written in high-level languages. Low-level languages are used only for a few specialized applications.

Two kinds of programs process high-level languages into low-level languages: **interpreters** and **compilers**. An interpreter reads a high-level program and executes it, meaning that it does what the program says. It processes the program a little at a time, alternately reading lines and performing computations.

![](https://fopp.umsi.education/runestone/static/fopp/_images/interpret.png)

A compiler reads the program and translates it completely before the program starts running. In this case, the high-level program is called the **source code**, and the translated program is called the object code or the executable. Once a program is compiled, you can execute it repeatedly without further translation.

![](https://fopp.umsi.education/runestone/static/fopp/_images/compile.png)

Many modern languages use both processes. They are first compiled into a lower level language, called byte code, and then interpreted by a program called a virtual machine. Python uses both processes, but because of the way programmers interact with it, it is usually considered an interpreted language.

**More About Programs**

A **program** is a sequence of instructions that specifies how to perform a computation. The computation might be something as complex as rendering an html page in a web browser or encoding a video and streaming it across the network. It can also be a symbolic computation, such as searching for and replacing text in a document or (strangely enough) compiling a program.

The details look different in different languages, but a few basic instructions appear in just about every language.

***input***

Get data from the keyboard, a file, or some other device.

***output***

Display data on the screen or send data to a file or other device.

***math and logic***

Perform basic mathematical operations like addition and multiplication and logical operations like `and`, `or`, and `not`.

***conditional execution***

Check for certain conditions and execute the appropriate sequence of statements.

***repetition***

Perform some action repeatedly, usually with some variation.

Believe it or not, that’s pretty much all there is to it. Every program you’ve ever used, no matter how complicated, is made up of instructions that look more or less like these. Thus, we can describe programming as the process of breaking a large, complex task into smaller and smaller subtasks until the subtasks are simple enough to be performed with sequences of these basic instructions.


**A Typical First Program**

Traditionally, the first program written in a new language is called *Hello, World!* because all it does is display the words, Hello, World! In Python, the source code looks like this.

```python
print("Hello World!")
```
This is an example of using the `print` function, which doesn’t actually print anything on paper. It displays a value on the screen. In this case, the result is the phrase:

```
Hello World!
```

The quotation marks in the program mark the beginning and end of the value. They don’t appear in the result.

----

### Programming in Python

#### Values and Data Types

A ***value*** is one of the fundamental things — like a word or a number — that a program manipulates. Some values are `5` (the result when we add `2 + 3`), and `"Hello, World!"`. These objects are classified into different classes, or data types: 4 is an integer, and “Hello, World!” is a string, so-called because it contains a string or sequence of letters. You (and the interpreter) can identify strings because they are enclosed in quotation marks.

We can specify values directly in the programs we write. For example we can specify a number as a literal just by (literally) typing it directly into the program (e.g., `5` or `4.32`). In a program, we specify a word, or more generally a string of characters, by enclosing the characters inside quotation marks (e.g., `"Hello, World!"`).

During execution of a program, the Python interpreter creates an internal representation of literals that are specified in a program. It can then manipulate them, for examply by multiplying two numbers. We call the internal representations ***objects*** or just ***values***.

You can’t directly see the internal representations of values. You can, however, use the `print` function to see a printed representation in the output window.

The printed representation of a number uses the familiar decimal representation (reading Roman Numerals is a fun challenge in museums, but thank goodness the Python interpreter doesn’t present the number 2014 as MMXIV in the output window). Thus, the printed representation of a number shown in the output window is the same as the literal that you specify in a program.

The printed representation of a character string, however, is not exactly the same as the literal used to specify the string in a program. For the literal in a program, you enclose the string in quotation marks. The printed representation, in the output window, omits the quotation marks.

```python
print(3.2)
print("Hello World!")
```

**Output** :
```
3.2
Hello World!
```

***Note*** : **Literals** appear in programs. The Python interpreter turns literals into **values**, which have internal representations that people never get to see directly. **Outputs** are external representations of values that appear in the output window. When we are being careful, we will use the terms this way. Sometimes, however, we will get a little sloppy and refer to literals or external representations as values.


Numbers with a decimal point belong to a class called **float**, because these numbers are represented in a format called floating-point. At this stage, you can treat the words class and type interchangeably. We’ll come back to a deeper understanding of what a class is in later chapters.

You will soon encounter other types of objects as well, such as lists and dictionaries. Each of these has its own special representation for specifying an object as a literal in a program, and for displaying an object when you print it. For example, list contents are enclosed in square brackets `[ ]`. You will also encounter some more complicated objects that do not have very nice printed representations: printing those won’t be very useful.


#### Operators and Operands

| Operator | Operate | Form |
|:--:|:--:|:--:|
| `+` | addition | `a + b` |
| `-` | subtraction | `a - b` |
| `*` | multiplication | `a * b` |
| `/` | division | `a / b` |
| `//` | division without remainder | `a // b` |
| `%` | remainder | `a % b` |
| `**` | exponentiation | `a ** b` |

You can build complex expressions out of simpler ones using operators. Operators are special tokens that represent computations like addition, multiplication and division. The values the operator works on are called **operands**.

The following are all legal Python expressions whose meaning is more or less clear:

```python
20 + 32
5 ** 2
(5 + 9) * (15 - 7)
```

The tokens `+`, `-`, and `*`, and the use of parentheses for grouping, mean in Python what they mean in mathematics. The asterisk `(*)` is the token for multiplication, and `**` is the token for exponentiation. Addition, subtraction, multiplication, and exponentiation all do what you expect.

Remember that if we want to see the results of the computation, the program needs to specify that with the word `print`. The first three computations occur, but their results are not printed out.

In Python 3, which we will be using, the division operator `/` produces a floating point result if the result is not an integer (e.g., `1/2`). If you want truncated division, you can use the `//` operator.

```python
print(9 / 5)
print(5 / 9)
print(9 // 5)
```
**Output** :
```
1.8
0.5555555555555556
1
```


Pay particular attention to the examples above. Note that `9//5` truncates rather than rounding, so it produces the value 1 rather 2.

The integer division operator, `//`, also works on floating point numbers. It truncates to the nearest integer, but still produces a floating point result. Thus `7.0 // 3.0` is `2.0`.

```python
print(7.0 / 3.0)
print(7.0 // 3.0)
```

**Output** :

```
2.3333333333333335
2.0
```

The **modulus operator**, sometimes also called the **remainder operator** or **integer remainder operator** works on integers (and integer expressions) and yields the remainder when the first operand is divided by the second. In Python, the modulus operator is a percent sign (`%`). The syntax is the same as for other operators.

```python
print(7 // 3)  # This is the integer division operator
print(7 % 3)   # This is the remainder or modulus operator
```

**Output** :

```
2
1
```

In the above example, 7 divided by 3 is 2 when we use integer division and there is a remainder of 1.

The modulus operator turns out to be surprisingly useful. For example, you can check whether one number is divisible by another—if `x % y` is zero, then `x` is divisible by `y`. Also, you can extract the right-most digit or digits from a number. For example, `x % 10` yields the right-most digit of `x` (in base 10). Similarly `x % 100` yields the last two digits.

```python
print(18 / 4)
print(18.0 // 4)
print(18 % 4)
```

**Output** :

```
4.5
4.0
2
```

**Order of Operations**

When more than one operator appears in an expression, the order of evaluation depends on the **rules of precedence**. Python follows the same precedence rules for its mathematical operators that mathematics does.

1. ***Parentheses*** have the highest precedence and can be used to force an expression to evaluate in the order you want. Since expressions in parentheses are evaluated first, `2 * (3-1)` is 4, and `(1+1)**(5-2)` is 8. You can also use parentheses to make an expression easier to read, as in `(minute * 100) / 60`: in this case, the parentheses don’t change the result, but they reinforce that the expression in parentheses will be evaluated first.

2. ***Exponentiation*** has the next highest precedence, so `2**1+1` is 3 and not 4, and `3*1**3` is 3 and not 27. Can you explain why?

3. ***Multiplication and both division*** operators have the same precedence, which is higher than addition and subtraction, which also have the same precedence. So `2*3-1` yields 5 rather than 4, and `5-2*2` is 1, not 6.

4. Operators with the *same* precedence are evaluated from left-to-right. In algebra we say they are ***left-associative***. So in the expression `6-3+2`, the subtraction happens first, yielding 3. We then add 2 to get the result 5. If the operations had been evaluated from right to left, the result would have been `6-(3+2)`, which is 1.

```python
print(2 * (3-1))
print((1+1)**(5-2))
print(2**1+1)
print(3*1**3)
print(2*3-1)
print(5-2*2)
print(6-3+2)
print(6-(3+2))
```

**Output** :

```
4
8
3
3
5
1
5
1
```

**Note** : Due to some historical quirk, an exception to the left-to-right left-associative rule is the exponentiation operator `**`. A useful hint is to always use parentheses to force exactly the order you want when exponentiation is involved:

```python
print(2 ** 3 ** 2)		# the right-most ** operator gets done first!
print((2 ** 3) ** 2)	# use parentheses to force the order you want!
print(16 - 2 * 5 // 3 + 1)
```

**Output** :
```
512
64
14
```

**Note**

This is a second way that parentheses are used in Python. The first way you’ve already seen is that `()` indicates a function call, with the inputs going inside the parentheses. How can Python tell when parentheses specify to call a function, and when they are just forcing the order of operations for ambiguous operator expressions?

The answer is that if there’s a an expression to the left of the parentheses that evaluates to a function object, then the parentheses indicate a function call, and otherwise not. You will have to get used to making the same inference when you see parentheses: is this a function call, or just specifying precedence?


#### Function Calls

The Python interpreter can compute new values with function calls. You are familiar with the idea of functions from high school algebra. There you might define a function `f` by specifying how it transforms an input into an output, `f(x) = 3x + 2`. Then, you might write `f(5)` and expect to get the value 17.

Python adopts a similar syntax for invoking functions. If there is a named function `foo` that takes a single input, we can invoke foo on the value 5 by writing `foo(5)`.

There are many built-in functions available in Python. You’ll be seeing some in this chapter and the next couple of chapters.

Functions are like factories that take in some material, do some operation, and then send out the resulting object.

![](https://fopp.umsi.education/runestone/static/fopp/_images/function_object.png)

In this case, we refer to the materials as arguments or inputs and the resulting object is refered to as output or return value. This process of taking input, doing something, and then sending back the output is demonstrated in the gif below.

![](https://fopp.umsi.education/runestone/static/fopp/_images/function_calls.gif)

**Note**

Don’t confuse the “output value” of a function with the output window. The output of a function is a Python value and we can never really see the internal representation of a value. But we can draw pictures to help us imagine what values are, or we can print them to see an external representation in the output window.

To confuse things even more, `print` is actually a function. All functions produce output values. Only the `print` function causes things to appear in the output window.

It is also possible for programmers to define new functions in their programs. You will learn how to do that later in the course. For now, you just need to learn how to invoke, or call, a function, and understand that the execution of the function returns a computed value.

```python
def square(x):
   return x * x

def sub(x, y):
   return x - y
```

We’ve defined two functions above. The code is hidden so as not to bother you (yet) with how functions are defined. `square` takes a single input parameter, and returns that input multiplied by itself. `sub` takes two input parameters and returns the result of subtracting the second from the first. Obviously, these functions are not particularly useful, since we have the operators `*` and `-` available. But they illustrate how functions work. The visual below illustrates how the `square` function works.

![](https://fopp.umsi.education/runestone/static/fopp/_images/square_function.gif)

```python
def square(x):
   return x * x

def sub(x, y):
   return x - y
# If you are studying on local, because square() and sub() functions aren't defined you must add above codes on your worksheet

print(square(3))
square(4)
print(sub(6,4))
print(sub(5,9))
```
**Output** :

```
9
2
-4
```

Notice that when a function takes more than one input parameter, the inputs are separated by a comma. Also notice that the order of the inputs matters. The value before the comma is treated as the first input, the value after it as the second input.

Again, remember that when Python performs computations, the results are only shown in the output window if there’s a print statement that says to do that. In the activcode window above, `square(5)` produces the value 25 but we never get to see that in the output window, because it is not printed.

**Function calls as part of complex expressions**
Anywhere in an expression that you can write a literal like a number, you can also write a function invocation that produces a number.

For example:


```python
def square(x):
   return x * x

def sub(x, y):
   return x - y
# If you are studying on local, because square() and sub() functions weren't defined you must add above codes on your worksheet

print(square(3) + 2)
print(sub(square(3), square(1 + 1)))
```
**Output** :

```
11
5
```

**Functions are objects; parentheses invoke functions**
Remember the earlier mention that some kinds of Python objects don’t have a nice printed representation? Functions are themselves just objects. If you tell Python to print the function object, rather than printing the results of invoking the function object, you’ll get one of those not-so-nice printed representations.

Just typing the name of the function refers to the function as an object. Typing the name of the function followed by parentheses `()` invokes the function.

```python
def square(x):
   return x * x

def sub(x, y):
   return x - y
# If you are studying on local, because square() and sub() functions weren't defined you must add above codes on your worksheet

print(square)
print(square(3))
```
**Output** :

```
<function square at 0x105c0b268>
9
```

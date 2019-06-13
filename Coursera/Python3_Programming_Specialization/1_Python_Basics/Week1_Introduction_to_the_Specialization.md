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

#### Data Types

If you are not sure what class (data type) a value falls into, Python has a function called `type` which can tell you.


```python
print(type("Hello World!"))
print(type(17))
print(type(3.2))
```

```
<class 'str'>
<class 'int'>
<class 'float'>
```

What about values like `"17"` and `"3.2"`? They look like numbers, but they are in quotation marks like strings.


```python
print(type("17"))
print(type("3.2"))
```

```
<class 'str'>
<class 'str'>
```

They’re strings!

Strings in Python can be enclosed in either single quotes (`'`) or double quotes (`"`), or three of each (`'''` or `"""`)

```python
print(type('This is a string.'))
print(type("And so it is."))
print(type("""and this."""))
print(type('''and even this.'''))
```

```
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
```

Double quoted strings can contain single quotes inside them, as in `"Bruce's beard"`, and single quoted strings can have double quotes inside them, as in `'The knights who say "Ni!"'`. Strings enclosed with three occurrences of either quote symbol are called triple quoted strings. They can contain either single or double quotes:

```python
print("Bruce's beard")
print('She said "hi".')
print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')
```

```
Bruce's beard
She said "hi".
"Oh no", she exclaimed, "Ben's bike is broken!"
```

Triple quoted strings can even span multiple lines:

```python
print("""This message will span
several lines
of the text.""")
```

```
This message will span
several lines
of the text.
```

Python doesn’t care whether you use single or double quotes or the three-of-a-kind quotes to surround your strings. Once it has parsed the text of your program or command, the way it stores the value is identical in all cases, and the surrounding quotes are not part of the value.

```python
print('This is a string.')
print("""And so it is.""")
```

```
This is a string.
And so it is.
```

So the Python language designers usually chose to surround their strings by single quotes. What do you think would happen if the string already contained single quotes?

When you type a large integer, you might be tempted to use commas between groups of three digits, as in `42,000`. This is not a legal integer in Python, but it does mean something else, which is legal:

```python
print(42,500)
print(42.500)
print(42500)
```

```
42 500
42.5
42500
```

Well, that’s not what we expected at all! Because of the comma, Python chose to treat this as a pair of values. In fact, a print statement can print any number of values as long as you separate them by commas. Notice that the values are separated by spaces when they are displayed.

```python
print(42, 17, 56, 34, 11, 4.35, 32)
print(3.4, "hello, 45")
```

```
42 17 56 34 11 4.35 32
3.4 hello, 45
```

Remember not to put commas or spaces in your integers, no matter how big they are. Also revisit what we said in the previous chapter: formal languages are strict, the notation is concise, and even the smallest change might mean something quite different from what you intended.


#### Type Conversion Functions

Sometimes it is necessary to convert values from one type to another. Python provides a few simple functions that will allow us to do that. The functions `int`, `float` and `str` will (attempt to) convert their arguments into types `int`, `float` and `str` respectively. We call these type conversion functions.

The `int` function can take a floating point number or a string, and turn it into an int. For floating point numbers, it discards the decimal portion of the number - a process we call truncation towards zero on the number line. Let us see this in action:

```python
print(3.14, int(3.14))
print(3.9999, int(3.9999))
print(-3.9999, int(-3.9999))
print("2345", int("2345"))
print(17, int(17))
print(int("23bottless"))
```

**Output**:

```
3.14 3
3.9999 3
-3.9999 -3
2345 2345
17 17
Traceback (most recent call last):
    print(int("23bottless"))
ValueError: invalid literal for int() with base 10: '23bottless'
```

The last case shows that a string has to be a syntactically legal number, otherwise you’ll get one of those pesky runtime errors. Modify the example by deleting the `bottles` and rerun the program. You should see the integer `23`.

The type converter `float` can turn an integer, a float, or a syntactically legal string into a float.

```python
print(float("123.45"))
print(type(float("123.45")))
```

**Output**:

```
123.45
<class 'float'>
```

The type converter `str` turns its argument into a string. Remember that when we print a string, the quotes are removed in the output window. However, if we print the type, we can see that it is definitely `str`.

```python
print(str(17))
print(str(123.45))
print(type(str(123.45)))
```

**Output**:

```
17
123.45
<class 'str'>
```

One common operation where you might need to do a type conversion is when you are concatenating several strings together but want to include a numeric value as part of the final string. Because we can’t concatenate a string with an integer or floating point number, we will often have to convert numbers to strings before concatenating them.

![](https://fopp.umsi.education/runestone/static/fopp/_images/type_cast.gif)


#### Variables

One of the most powerful features of a programming language is the ability to manipulate **variables**. A variable is a name that refers to a value.

**Assignment statements** create new variables and also give them values to refer to.

```python
message = "What's up, Doc?"
n = 17
pi = 3.14159
```

This example makes three assignments. The first assigns the string value `"What's up, Doc?"` to a new variable named `message`. The second assigns the integer `17` to `n`, and the third assigns the floating-point number `3.14159` to a variable called `pi`.

The **assignment token**, =, should not be confused with equality (we will see later that equality uses the `==` token). The assignment statement links a name, on the left hand side of the operator, with a value, on the right hand side. This is why you will get an error if you enter:

```python
17 = n
```

**Tip** : When reading or writing code, say to yourself “n is assigned 17” or “n gets the value 17” or “n is a reference to the object 17” or “n refers to the object 17”. Don’t say “n equals 17”.

A common way to represent variables on paper is to write the name with an arrow pointing to the variable’s value. This kind of figure, known as a **reference diagram**, is often called a **state snapshot** because it shows what state each of the variables is in at a particular instant in time. (Think of it as the variable’s state of mind). This diagram shows the result of executing the assignment statements shown above.

![](https://fopp.umsi.education/runestone/static/fopp/_images/refdiagram1.png)

If your program includes a variable in any expression, whenever that expression is executed it will produce the value that is linked to the variable at the time of execution. In other words, evaluating a variable looks up its value.

```python
message = "What's up, Doc?"
n = 17
pi = 3.14159

print(message)
print(n)
print(pi)
```

**Output**:

```
What's up, Doc?
17
3.14159
```

We use variables in a program to “remember” things, like the current score at the football game. But variables are variable. This means they can change over time, just like the scoreboard at a football game. You can assign a value to a variable, and later assign a different value to the same variable.


**Note** : This is different from math. In algebra, if you give `x` the value 3, it cannot change to refer to a different value half-way through your calculations!

To see this, read and then run the following program. You’ll notice we change the value of `day` three times, and on the third assignment we even give it a value that is of a different type.

![](https://media.giphy.com/media/dUm64hoCJWNYp345iy/giphy.gif)

A great deal of programming is about having the computer remember things. For example, we might want to keep track of the number of missed calls on your phone. Each time another call is missed, we will arrange to update or change the variable so that it will always reflect the correct value.

Any place in a Python program where a number or string is expected, you can put a variable name instead. The python interpreter will substitute the value for the variable name.

For example, we can find out the data type of the current value of a variable by putting the variable name inside the parentheses following the function name `type`.

```python
message = "What's up, Doc?"
n = 17
pi = 3.14159

print(type(message))
print(type(n))
print(type(pi))
```

**Output**:

```
<class 'str'>
<class 'int'>
<class 'float'>
```

**Note** : If you have programmed in another language such as Java or C++, you may be used to the idea that variables have types that are declared when the variable name is first introduced in a program. Python doesn’t do that. Variables don’t have types in Python; values do. That means that it is acceptable in Python to have a variable name refer to an integer and later have the same variable name refer to a string. This is almost never a good idea, because it will confuse human readers (including you), but the Python interpreter will not complain.

#### Variable Names and Keywords

Variable names can be arbitrarily long. They can contain both letters and digits, but they have to begin with a letter or an underscore. Although it is legal to use uppercase letters, by convention we don’t. If you do, remember that case matters. `Bruce` and `bruce` are different variables.

**Caution** : Variable names can never contain spaces.

The underscore character (`_`) can also appear in a name. It is often used in names with multiple words, such as `my_name` or `price_of_tea_in_china`. There are some situations in which names beginning with an underscore have special meaning, so a safe rule for beginners is to start all names with a letter.

If you give a variable an illegal name, you get a syntax error. In the example below, each of the variable names is illegal.

```python
76trombones = "big parade"
more$ = 1000000
class = "Computer Science 101"
```

`76trombones` is illegal because it does not begin with a letter. `more$` is illegal because it contains an illegal character, the dollar sign. But what’s wrong with `class`?

It turns out that `class` is one of the Python keywords. Keywords define the language’s syntax rules and structure, and they cannot be used as variable names. Python has thirty-something keywords (and every now and again improvements to Python introduce or eliminate one or two):

| | | | | | |
|--|--|--|--|--|--|
| `and` | `as` | `assert` | `break` | `class` | `continue` |
| `def` | `del` | `elif` | `else` | `except` | `exec` |
| `finally` | `for` | `from` | `global` | `if` | `import` |
| `in` | `is` | `lambda` | `nonlocal` | `not` | `or` |
| `pass` | `raise` | `return` | `try` | `while` | `with` |
| `yield` | `True` | `False` | `None` | | |

You might want to keep this list handy. If the interpreter complains about one of your variable names and you don’t know why, see if it is on this list.


#### Choosing the Righ Variable Name
Programmers generally choose names for their variables that are meaningful to the human readers of the program — they help the programmer document, or remember, what the variable is used for. Beginning programmers sometimes think it is funny to use strange or obscene names for their variables. This is not good practice and will not amuse your professor. Get in the habit of using meaningful names right away.

**Caution**

Beginners sometimes confuse “meaningful to the human readers” with “meaningful to the computer”. So they’ll wrongly think that because they’ve called some variable `average` or `pi`, it will somehow automagically calculate an average, or automagically associate the variable pi with the value 3.14159. No! The computer doesn’t attach semantic meaning to your variable names.

So you’ll find some instructors who deliberately don’t choose meaningful names when they teach beginners — not because they don’t think it is a good habit, but because they’re trying to reinforce the message that you, the programmer, have to write some program code to calculate the average, or you must write an assignment statement to give a variable the value you want it to have.


#### Reassignment

As we have mentioned previously, it is legal to make more than one assignment to the same variable. A new assignment makes an existing variable refer to a new value (and stop referring to the old value).

```python
bruce = 5
print(bruce)

bruce = 7
print(bruce)
```

**Output**:

```
5
7
```

The first time `bruce` is printed, its value is 5, and the second time, its value is 7. The assignment statement changes the value (the object) that `bruce` refers to.

Here is what reassignment looks like in a reference diagram:

![](https://fopp.umsi.education/runestone/static/fopp/_images/reassign1.png)

It is important to note that in mathematics, a statement of equality is always true. If `a is equal to b` now, then `a will always equal to b`. In Python, an assignment statement can make two variables refer to the same object and therefore have the same value. They appear to be equal. However, because of the possibility of reassignment, they don’t have to stay that way:

```python
a = 5
b = a
print(a, b)

a = 3
print(a, b)
```

**Output**:

```
5 5
3 5
```

Line 4 changes the value of `a` but does not change the value of `b`, so they are no longer equal. We will have much more to say about equality in a later chapter.

**Developing your mental model of How Python Evaluates**

Its important to start to develop a good mental model of the steps the Python interpreter takes when evaluating an assignment statement. In an assignment statement, the interpreter first evaluates the code on the right hand side of the assignment operator. It then gives a name to whatever that is.

**Note** : In some programming languages, a different symbol is used for assignment, such as `<-` or `:=`. The intent is that this will help to avoid confusion. Python chose to use the tokens `=` for assignment, and `==` for equality. This is a popular choice also found in languages like C, C++, Java, and C#.


#### Statements and Expressions

A statement is an instruction that the Python interpreter can execute. You have only seen the assignment statement so far. Some other kinds of statements that you’ll see in future chapters are `while` statements, `for` statements, `if` statements, and `import` statements. (There are other kinds too!)

An **expression** is a combination of literals, variable names, operators, and calls to functions. Expressions need to be evaluated. The result of evaluating an expression is a value or object.

![](https://fopp.umsi.education/runestone/static/fopp/_images/expression_value_type.png)

If you ask Python to `print` an expression, the interpreter **evaluates** the expression and displays the result.

```python
print(1 + 1 + (2 * 3))
print(len("hello"))
```

**Output** :

```
8
5
```

In this example `len` is a built-in Python function that returns the number of characters in a string.

The evaluation of an expression produces a value, which is why expressions can appear on the right hand side of assignment statements. A literal all by itself is a simple expression, and so is a variable.

```python
y = 3.14
x = len("hello")
print(x)
print(y)
```

**Output** :

```
5
3.14
```

In a program, anywhere that a literal value (a string or a number) is acceptable, a more complicated expression is also acceptable. Here are all the kinds of expressions we’ve seen so far:

| Type of Expression | Examples |
|--|--|
| *literal* | `“Hello”` or `3.14` |
| *variable name* | `x` or `len` |
| *operator expression* | `<expression> operator-name <expression>` |
| *function call expressions* | `<expression>(<expressions separated by commas>)` |

Notice that operator expressions (like `+` and `*`) have sub-expressions before and after the operator. Each of these can themselves be simple or complex expressions. In that way, you can build up to having pretty complicated expressions.

```python
print(2 * len("hello") + len("goodbye"))
```

**Output** :

```
17
```

Similarly, when calling a function, instead of putting a literal inside the parentheses, a complex expression can be placed inside the parentheses.

```python
def square(x):
	return x * x

def sub(x, y):
	return x - y


x = 2
y = 1

print(square(y + 3))
print(square(y + square(x)))
print(sub(square(y), square(x)))
```

**Output** :

```
16
25
-3
```

With a function call, it’s even possible to have a complex expression before the left parenthesis, as long as that expression evaluates to a function object. For now, though, we will just use variable names (like square, sub, and len) that are directly bound to function objects.

It is important to start learning to read code that contains complex expressions. The Python interpreter examines any line of code and parses it into components. For example, if it sees an = symbol, it will try to treat the whole line as an assignment statement. It will expect to see a valid variable name to the left of the =, and will parse everything to the right of the = as an expression. It will try to figure out whether the right side is a literal, a variable name, an operator expression, or a function call expression. If it’s an operator expression, it will further try to parse the sub-expressions before and after the operator. And so on. You should learn to parse lines of code in the same way.

In order to evaluate an operator expression, the Python interpreter first completely evaluates the expression before the operator, then the one after, then combines the two resulting values using the operator. In order to evaluate a function call expression, the interpreter evaluates the expression before the parentheses (i.e., it looks up the name of the function). Then it tries to evaluate each of the expressions inside the parentheses. There may be more than one, separated by commas. The values of those expressions are passed as inputs to the function when the function is called.

If a function call expression is a sub-expression of some more complicated expression, as `square(x)` is in `sub(square(y), square(x))`, then the return value from `square(x)` is passed as an input to the `sub` function. This is one of the tricky things that you will have to get used to working out when you read (or write) code. In this example, the `square` function is called (twice) before the `sub` function is called, even though the `sub` function comes first when reading the code from left to right.


#### Updating Variables

One of the most common forms of reassignment is an update where the new value of the variable depends on the old. For example,

```python
x = x + 1
```

This means get the current value of x, add one, and then update x with the new value. The new value of x is the old value of x plus 1. Although this assignment statement may look a bit strange, remember that executing assignment is a two-step process. First, evaluate the right-hand side expression. Second, let the variable name on the left-hand side refer to this new resulting object. The fact that `x` appears on both sides does not matter. The semantics of the assignment statement makes sure that there is no confusion as to the result.

```python
x = 6
print(x)
x = x + 1
print(x)
```
**Output**:
```
6
7
```

If you try to update a variable that doesn’t exist, you get an error because Python evaluates the expression on the right side of the assignment operator before it assigns the resulting value to the name on the left. Before you can update a variable, you have to initialize it, usually with a simple assignment. In the above example, `x` was initialized to 6.

Updating a variable by adding something to it is called an **increment**; subtracting is called a **decrement**. Sometimes programmers talk about incrementing or decrementing without specifying by how much; when they do they usually mean by 1. Sometimes programmers also talk about **bumping** a variable, which means the same as incrementing it by 1.

Incrementing and decrementing are such common operations that programming languages often include special syntax for it. In Python `+=` is used for incrementing, and `-=` for decrementing. In some other languages, there is even a special syntax `++` and `--` for incrementing or decrementing by 1. Python does not have such a special syntax. To increment `x` by 1 you have to write `x += 1` or `x = x + 1`.

```python
x = 6
print(x)
x += 3
print(x)
x -= 1
print(x)
```

**Output**:
```
6
9
8
```

Imagine that we wanted to not increment by one each time but instead add together the numbers one through ten, but only one at a time.


```python
s = 1
print(s)
s = s + 2
print(s)
s = s + 3
print(s)
s = s + 4
print(s)
s = s + 5
print(s)
s = s + 6
print(s)
s = s + 7
print(s)
s = s + 8
print(s)
s = s + 9
print(s)
s = s + 10
print(s)
```

**Output**:
```
1
3
6
10
15
21
28
36
45
55
```

After the initial statement, where we assign `s` to 1, we can add the current value of `s` and the next number that we want to add (2 all the way up to 10) and then finally reassign that that value to `s` so that the variable is updated after each line in the code.

This will be tedious when we have many things to add together. Later you’ll read about an easier way to do this kind of task.


#### Hard-Coding

As you begin programming, you’ll see that there are many ways to solve problems. You’ll also find that one of the thrills of programming is how easily you can do things correctly that humans could easily make errors on. For example, you’ll learn how to write just a very small bit of code to find the 1047th character in a sentence that might be thousands of letters long, and you’ll learn how to do the exact same computation on many different pieces of data.

We’ll often tell you in this textbook not to hard-code answers. What does that mean?

Some things in programming you can only do by typing them out. As you’ve seen, when you have to assign a value to a variable, you simply type something like `xyz = 6`. No other way.

But in most cases, it’s best not to do computation in your head or write complete answers to programming problems out by hand. That’s where **hard-coding** comes in. “Don’t hard code” basically means, you should rely on your code, your logic, your program, and you should not write things out by hand or do computation in your head – even if you can do so easily.

When you are writing code or working on the answer to a programming exericse, you should ask yourself: Would my answer be correct even if the provided variables had different values? If the answer to that question is no, you’re probably hard- coding, which you should avoid – and there’s probably at least a slightly more concise way to construct your answer!

For example, in this following code, if you’re asked in an exercise to create a variable `zx` and assign it the value of the sum of the value of `y` and the value of `x`, writing `zx = 55` is hard-coding.

```python
x = 20
y = 35
abc = 62
```

The operation `20 + 35` may be easy math to do in your head or with a calculator, but when you learn to program, you want to train yourself to notice useful patterns of how to solve problems, which will make your life easier (perhaps beyond programming, even).

The correct way to answer that sort of exercise would be to write: `zx = y` + x (or `zx = x + y`, as you were just reminded of the order of operations). That is not hard-coding, and it will be correct no matter what the values of `x` and `y` are.

In the code above, if the value of `x` were `40`, `55` would not be the correct value for `zx` to have. But `zx = y + x` would still be absolutely correct.

Try as much as you can not to rely on your brilliant but fallible human brain to do computation when you program – use your brain to determine how to write the correct code to solve the problem for you!

#### Input

Our programs get more interesting if they don’t do exactly the same thing every time they run. One way to make them more interesting is to get input from the user. Luckily, in Python there is a built-in function to accomplish this task. It is called `input`.

```python
n = input("Please enter your name: ")
```

The input function allows the programmer to provide a **prompt string**. In the example above, it is “Please enter your name: “. When the function is evaluated, the prompt is shown (in the browser, look for a popup window). The user of the program can type some text and press `return`. When this happens the text that has been entered is returned from the `input` function, and in this case assigned to the variable `n`. Run this example a few times and try some different names in the input box that appears.


```python
n = input("Please enter your name: ")
print("Hello", n)
```

**Output** :

```
Please enter your name: Heval
Hello Heval
```

It is very important to note that the `input` function returns a string value. Even if you asked the user to enter their age, you would get back a string like `"17"`. It would be your job, as the programmer, to convert that string into an `int` or a `float`, using the int or float converter functions we saw earlier.


**Note** :We often use the word “input” (or, synonymously, argument) to refer to the values that are passed to any function. Do not confuse that with the `input` function, which asks the user of a program to type in a value. Like any function, `input` itself takes an input argument and produces an output. The input is a character string that is displayed as a prompt to the user. The output is whatever character string the user types.

This is analogous to the potential confusion of function “outputs” with the contents of the output window. Every function produces an output, which is a Python value. Only the print function puts things in the output window. Most functions take inputs, which are Python values. Only the input function invites users to type something.


Here is a program that turns a number of seconds into more human readable counts of hours, minutes, and seconds. A call to `input()` allows the user to enter the number of seconds. Then we convert that string to an integer. From there we use the division and modulus operators to compute the results.


```python
str_seconds = input("Please enter the number of seconds you wish to convert: ")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)
```

**Output** :

```
Please enter the number of seconds you wish to convert: 28329
Hrs= 7 mins= 52 secs= 9
```

The variable `str_seconds` will refer to the string that is entered by the user. As we said above, even though this string may be `7684`, it is still a string and not a number. To convert it to an integer, we use the int function. The result is referred to by `total_secs`. Now, each time you run the program, you can enter a new value for the number of seconds to be converted.


#### Chapter Assessments & Exercises

#### Assessments

**A1**. There is a function we are providing in for you in this problem called square. It takes one integer and returns the square of that integer value. Write code to assign a variable called xyz the value 5*5 (five squared). Use the square function, rather than just multiplying with `*`.


```python
xyz = square(5)
```

-----

**A2**. Write code to assign the number of characters in the string `rv` to a variable `num_chars`.


```python
rv = """Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore,
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    'Tis some visitor, I muttered, tapping at my chamber door;
    Only this and nothing more."""

# Write your code here!
num_chars = len(rv)
```

----
----

#### Exercises

**Q1**. Evaluate the following numerical expressions in your head, then use the active code window to check your results:

* 5 ** 2
* 9 * 5
* 15 / 12
* 12 / 15
* 15 // 12
* 12 // 15
* 5 % 2
* 9 % 5
* 15 % 12
* 12 % 15
* 6 % 6
* 0 % 7


```python
print(5 ** 2)
print(9 * 5)
print(15 / 12)
print(12 / 15)
print(15 // 12)
print(5 % 2)
print(9 % 5)
print(15 % 12)
print(12 % 15)
print(6 % 6)
print(0 % 7)
```

**Output** :

```
25
45
1.25
0.8
1
1
4
3
12
0
0
```

----

**Q2**. What is the order of the arithmetic operations in the following expression. Evaluate the expression by hand and then check your work.


```python
2 + (3 - 1) * 10 / 5 * (2 + 3)

print(2 + (3 - 1) * 10 / 5 * (2 + 3))
```

**Output** :

```
22.0
```
----

**Q3**. Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on the clock when the alarm goes off.


```python
time_now = int(input("What time now? "))
time_wait = int(input("How much time to wait? "))

clock = (time_now + time_wait) % 24
print(clock)
```

**Output** :

```
What time now? 12
How much time to wait? 17
5
```
----

**Q4**. It is possible to name the days 0 thru 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6). Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.


```python
holiday_start = int(input("Day of starting your holiday? "))
holiday_stay = int(input("How many days stay on holiday? "))

return_day = (holiday_start + holiday_stay) % 7
print(return_day)
```

**Output** :

```
Day of starting your holiday? 3
How many days stay on holiday? 10
6
```
----
**Q5**. Take the sentence: *All work and no play makes Jack a dull boy.* Store each word in a separate variable, then print out the sentence on one line using `print`.


```python
w1 = "All"
w2 = "work"
w3 = "and"
w4 = "no"
w5 = "play"
w6 = "makes"
w7 = "Jack"
w8 = "a"
w9 = "dull"
w10 = "boy."

print(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10)
```

**Output** :

```
All work and no play makes Jack a dull boy.
```
----
**Q6**. Add parentheses to the expression `6 * 1 - 2` to change its value from 4 to -6.


```python
print(6 * (1 - 2))
```

**Output** :

```
-6
```

----
**Q7**. The formula for computing the final amount if one is earning compound interest is given on Wikipedia as

![](https://fopp.umsi.education/runestone/static/fopp/_images/compoundInterest.png)

Write a Python program that assigns the principal amount of 10000 to variable `P`, assign to `n` the value 12, and assign to `r` the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, `t`, that the money will be compounded for. Calculate and print the final amount after `t` years.

```python
P = 10000
n = 12
r = 0.08
t = int(input("How many years? "))

A = P * ((1 + (r / n)) ** (n * t))
print(A)
```

**Output** :

```
How many years? 2
11728.879317453097
```


----
**Q8**. Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer.

```python
r = int(input("Enter the radius: "))
pi = 3.14

A = pi * (r ** 2)
print("The area of the circle is ", A)
```

**Output** :

```
Enter the radius: 3
The area of the circle is  28.26
```

----
**Q9**. Write a program that will compute the area of a rectangle. Prompt the user to enter the width and height of the rectangle. Print a nice message with the answer.

```python
w = int(input("What's the width? "))
l = int(input("What's the lenght? "))

A = w * l
print("The area of the rectangle is", A)
```

**Output** :

```
What's the width? 2
What's the lenght? 4
The area of the rectangle is 8
```

----
**Q10**. Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used. Print a nice message with the answer.

```python
driven_mile = int(input("Miles? "))
used_gallon = int(input("Gallon? "))

mpg = driven_mile / used_gallon
print("MPG of the car is", mpg)
```

**Output** :

```
Miles? 200
Gallon? 18
MPG of the car is 11.11111111111111
```

----
**Q11**. Write a program that will convert degrees celsius to degrees fahrenheit.

```python
c = int(input("What's the temperature on Celcius? "))
f = (((9 / 5)* c )+ 32)

print("It's", f, "Fahrenheit")
```

**Output** :

```
What's the temperature on Celcius? 30
It's 86.0 Fahrenheit
```

----
**Q12**. Write a program that will convert degrees fahrenheit to degrees celsius.

```python
f = int(input("What's the temperature on Fahrenheit? "))
c = (5 / 9) * (f - 32)

print("It's", c, "Celcius")
```

**Output** :

```
What's the temperature on Fahrenheit? 86
It's 30.0 Celcius
```

----
**Q13**. Piece together the code so that a user is asked for two numbers, and then the sum of those two numbers is printed out.

![](http://i66.tinypic.com/2vbnbf5.png)


----
**Q14**. Write a program that will convert gallons to liters. This program will also need to get input from a user to see how many gallons should be converted and the result should be printed to the user.

![](http://i63.tinypic.com/fvwz11.png)


----
**Q15**. Write a program that will convert table spoons to teaspons. This program will also need to get input from a user to see how many tablespoons should be converted and the result should be printed to the user.

![](http://i68.tinypic.com/15ve4p.png)


----

### Turtle Graphics

#### Our First Turtle Program
There are many modules in Python that provide very powerful features that we can use in our own programs. Some of these can send email or fetch web pages. Others allow us to perform complex mathematical calculations. In this chapter we will introduce a module that allows us to create a data object called a turtle that can be used to draw pictures.

Turtle graphics, as it is known, is based on a very simple metaphor. Imagine that you have a turtle that understands English. You can tell your turtle to do simple commands such as go forward and turn right. As the turtle moves around, if its tail is down touching the ground, it will draw a line (leave a trail behind) as it moves. If you tell your turtle to lift up its tail it can still move around but will not leave a trail. As you will see, you can make some pretty amazing drawings with this simple capability.

**Note** : The turtles are fun because they allow us to visualize what our code is doing, but the real purpose of the chapter is to teach ourselves a little more Python and to develop our theme of computational thinking. You’ll first draw simple geometric shapes with the turtles, and then we’ll summarize the concepts and syntax you’ve learned, in particular, classes, instances, and method invocations. These concepts are the building blocks of object-oriented programming, a paradigm for structuring a program that is widespread in every modern programming language.


Let’s try a couple of lines of Python code to create a new turtle and start drawing a simple figure like a rectangle. We will refer to our first turtle using the variable name alex, but remember that you can choose any name you wish as long as you follow the naming rules from the previous chapter.

The program as shown will only draw the first two sides of the rectangle. After line 4 you will have a straight line going from the center of the drawing canvas towards the right. After line 6, you will have a canvas with a turtle and a half drawn rectangle.

```python
import turtle             # allows us to use the turtles library
wn = turtle.Screen()      # creates a graphics window
alex = turtle.Turtle()    # create a turtle named alex
alex.forward(150)         # tell alex to move forward by 150 units
alex.left(90)             # turn by 90 degrees
alex.forward(75)          # complete the second side of a rectangle
```

**Output** :

![](https://media.giphy.com/media/LO1tp6QwEsQZdKmwo5/giphy.gif)

Here are a couple of things you’ll need to understand about this program.

The first line tells Python to load a **module** named `turtle`. That module brings us two new types that we can use: the `Turtle` type, and the `Screen` type. The dot notation `turtle.Turtle` means *“The Turtle type that is defined within the turtle module”*. (Remember that Python is case sensitive, so the module name, `turtle`, with a lowercase `t`, is different from the type `Turtle` because of the uppercase `T`.)

We then create and open what the turtle module calls a screen (we would prefer to call it a window, or in the case of this web version of Python simply a canvas), which we assign to variable `wn`. Every window contains a canvas, which is the area inside the window on which we can draw.

In line 3 we create a turtle. The variable `alex` is made to refer to this turtle. These first three lines set us up so that we are ready to do some drawing.

In lines 4-6, we instruct the object alex to move and to turn. We do this by invoking or activating alex’s methods — these are the instructions that all turtles know how to respond to.


**Mixed up programs**

**E1** : The following program uses a turtle to draw a capital L as shown in the picture to the left of this text, image of a navigational compass and a letter L which is drawn by Turtle but the lines are mixed up. The program should do all necessary set-up: import the turtle module, get the window to draw on, and create the turtle. Remember that the turtle starts off facing east when it is created. The turtle should turn to face south and draw a line that is 150 pixels long and then turn to face east and draw a line that is 75 pixels long. We have added a compass to the picture to indicate the directions north, south, west, and east.

![](https://fopp.umsi.education/runestone/static/fopp/_static/TurtleL4.png)

```python
import turtle
window = turtle.Screen()
ella = turtle.Turtle()
ella.right(90)
ella.forward(150)
ella.left(90)
ella.forward(75)
```


**E2** : The following program uses a turtle to draw a checkmark as shown to the left, image of a navigational compass and a checkmark which is drawn by Turtle. but the lines are mixed up. The program should do all necessary set-up: import the turtle module, get the window to draw on, and create the turtle. The turtle should turn to face southeast, draw a line that is 75 pixels long, then turn to face northeast, and draw a line that is 150 pixels long. We have added a compass to the picture to indicate the directions north, south, west, and east. Northeast is between north and east. Southeast is between south and east.

![](https://fopp.umsi.education/runestone/static/fopp/_static/TurtleCheckmark4.png)

```python
import turtle
window = turtle.Screen()
maria = turtle.Turtle()
maria.right(45)
maria.forward(75)
maria.left(90)
maria.forward(150)
```

**E3** : The following program uses a turtle to draw a single line to the west as shown to the left, image of a line moving in west direction drawn by Turtle. Turtle uses following steps: left turn of 180 degrees, and 75 pixels long line but the program lines are mixed up. The program should do all necessary set-up: import the turtle module, get the window to draw on, and create the turtle. The turtle should then turn to face west and draw a line that is 75 pixels long.

![](https://fopp.umsi.education/runestone/static/fopp/_static/TurtleLineToWest.png)

```python
import turtle
window = turtle.Screen()
jamal = turtle.Turtle()
jamal.left(180)
jamal.forward(75)
```


An object can have various methods — things it can do — and it can also have **attributes** — (sometimes called properties). For example, each turtle has a color attribute. The method invocation `alex.color("red")` will make alex red and the line that it draws will be red too.

The color of the turtle, the width of its pen(tail), the position of the turtle within the window, which way it is facing, and so on are all part of its current state. Similarly, the window object has a background color which is part of its state.

Quite a number of methods exist that allow us to modify the turtle and window objects. In the example below, we show just show a couple and have only commented those lines that are different from the previous example. Note also that we have decided to call our turtle object tess.


```python
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")        # set the window background color

tess = turtle.Turtle()
tess.color("blue")              # make tess blue
tess.pensize(3)                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas
```

![](https://media.giphy.com/media/KbwTqwDA5I3yBk18XB/giphy.gif)

The last line plays a very important role. The wn variable refers to the window shown above. When we invoke its `exitonclick` method, the program pauses execution and waits for the user to click the mouse somewhere in the window. When this click event occurs, the response is to close the turtle window and exit (stop execution of) the Python program.

Each time we run this program, a new drawing window pops up, and will remain on the screen until we click on it.

**Extend this program …**

1. Modify this program so that before it creates the window, it prompts the user to enter the desired background color.It should store the user’s responses in a variable, and modify the color of the window according to the user’s wishes. (Hint: you can find a list of permitted color names at https://www.w3schools.com/colors/colors_names.asp. It includes some quite unusual ones, like “PeachPuff” and “HotPink”.)
2. Do similar changes to allow the user, at runtime, to set tess’ color.
3. Do the same for the width of tess’ pen. Hint: your dialog with the user will return a string, but tess’ `pensize` method expects its argument to be an `int`. That means you need to convert the string to an int before you pass it to `pensize`.


#### Instances: A Herd of Turtles
Just like we can have many different integers in a program, we can have many turtles. Each of them is an independent object and we call each one an **instance** of the Turtle type (class). Each instance has its own attributes and methods — so alex might draw with a thin pink pen and be at some position, while tess might be going in her own direction with a fat black pen. So here is what happens when alex completes a square and tess completes her triangle:

```python
import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")


tess = turtle.Turtle()           # create tess and set his pen width
tess.pensize(5)

alex = turtle.Turtle()           # create alex
alex.color("hotpink")            # set his color

tess.forward(80)                 # Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete the triangle

tess.right(180)                  # turn tess around
tess.forward(80)                 # move her away from the origin so we can see alex

alex.forward(50)                 # make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()
```

**Output** :

![](http://i67.tinypic.com/nq4u93.png)

Here are some How to think like a computer scientist observations:

* There are 360 degrees in a full circle. If you add up all the turns that a turtle makes, no matter what steps occurred between the turns, you can easily figure out if they add up to some multiple of 360. This should convince you that alex is facing in exactly the same direction as he was when he was first created. (Geometry conventions have 0 degrees facing East and that is the case here too!)
* We could have left out the last turn for alex, but that would not have been as satisfying. If you’re asked to draw a closed shape like a square or a rectangle, it is a good idea to complete all the turns and to leave the turtle back where it started, facing the same direction as it started in. This makes reasoning about the program and composing chunks of code into bigger programs easier for us humans!
* We did the same with tess: she drew her triangle and turned through a full 360 degress. Then we turned her around and moved her aside. Even the blank line 18 is a hint about how the programmer’s mental chunking is working: in big terms, tess’ movements were chunked as “draw the triangle” (lines 12-17) and then “move away from the origin” (lines 19 and 20).
* One of the key uses for comments is to record your mental chunking, and big ideas. They’re not always explicit in the code.
* And, uh-huh, two turtles may not be enough for a herd, but you get the idea!


**Mixed up programs**

**E1** : The following program has one turtle, "jamal", draw a capital L in blue and then another, "tina", draw a line to the west in orange as shown to the left, image of a capital letter L in blue color drawn by one Turtle and a line to the west in orange color drawn by another Turtle. Both the Turtles have same starting point.. The program should do all set-up, have "jamal" draw the L, and then have "tina" draw the line. Finally, it should set the window to close when the user clicks in it.

![](https://fopp.umsi.education/runestone/static/fopp/_static/TwoTurtles1.png)

```python
import turtle
wn = turtle.Screen()

jamal = turtle.Turtle()
jamal.pensize(10)
jamal.color("blue")
jamal.right(90)
jamal.forward(150)
jamal.left(90)
jamal.forward(75)

tina = turtle.Turtle()
tina.pensize(10)
tina.color("orange")
tina.left(180)
tina.forward(75)

wn.exitonclick()
```


**E2** : The following program has one turtle, "jamal", draw a line to the north in blue and then another, "tina", draw a line to the east in orange as shown to the left, image of a line to the north in blue color drawn by one Turtle and a line to the east in orange drawn by another Turtle. Both the Turtles have a same starting point.. The program should import the turtle module, get the window to draw on, create the turtle "jamal", have it draw a line to the north, then create the turtle "tina", and have it draw a line to the east. Finally, it should set the window to close when the user clicks in it.


![](https://fopp.umsi.education/runestone/static/fopp/_static/TwoTurtlesL.png)

```python
import turtle
wn = turtle.Screen()

jamal = turtle.Turtle()
jamal.pensize(10)
jamal.color("blue")
jamal.pensize(10)
jamal.left(90)
jamal.forward(150)

tina = turtle.Turtle()
tina.pensize(10)
tina.color("orange")
tina.forward(150)

wn.exitonclick()
```

#### Object Oriented Concepts
It’s been fun drawing things with the turtles. In the process, we’ve slipped in some new concepts and terms. Let’s pull them out and examine them a little more carefully.

**User-fedined Classes**

First, just as Python provides a way to define new functions in your programs, it also provides a way to define new classes of objects. Later in the course you will learn how to define functions, and much later, new classes of objects. For now, you just need to understand how to use them.

**Instances**

Given a class like `Turtle` or `Screen`, we create a new instance with a syntax that looks like a function call, `Turtle()`. The Python interpreter figures out that Turtle is a class rather than a function, and so it creates a new instance of the class and returns it. Since the Turtle class was defined in a separate module, (confusingly, also named turtle), we had to refer to the class as turtle.Turtle. Thus, in the programs we wrote `turtle.Turtle()` to make a new turtle. We could also write `turtle.Screen()` to make a new window for our turtles to paint in.


**Attributes**

Each instance can have attributes, sometimes called **instance variables**. These are just like other variables in Python. We use assignment statements, with an =, to assign values to them. Thus, if alex and tess are variables bound to two instances of the class Turtle, we can assign values to an attribute, and we can look up those attributes. For example, the following code would print out 1100.

```python
alex.price = 500
tess.price = 600
print(alex.price + tess.price)
```

**Methods**

Classes have associated **methods**, which are just a special kind of function. Consider the expression `alex.forward(50)` The interpreter first looks up alex and finds that it is an instance of the class Turtle. Then it looks up the attribute forward and finds that it is a method. Since there is a left parenthesis directly following, the interpreter invokes the method, passing 50 as a parameter.

The only difference between a method invocation and other function calls is that the object instance itself is also passed as a parameter. Thus `alex.forward(50)` moves alex, while `tess.forward(50)` moves tess.

Some of the methods of the Turtle class set attributes that affect the actions of other methods. For example, the method pensize changes the width of the drawing pen, and the color method changes the pen’s color.

Methods return values, just as functions do. However, none of the methods of the Turtle class that you have used return useful values the way the `len` function does. Thus, it would not make sense to build a complex expression like `tess.forward(50) + 75`. It could make sense, however to put a complex expression inside the parentheses: `tess.forward(x + y)`


#### Repetition with a For Loop

Some of the programs we’ve seen so far are a bit tedious to type. If we want to make a repetitive pattern in our drawings, then it can take many lines of code. Thankfully, Python has a few ways for making this kind of task easier. For now you’ll get a brief preview of a helpful control structure and function in Python which you will learn about later.

The control structure is called a for loop. If you’ve learned other programming languages then you may be familiar with what it does but the structure may be new. A for loop allows Python to execute a program in a non-linear fashion. Instead of evaluating the code line by line until it reaches the end, once the program reaches a for loop, it will tell the program to execute a set of lines for n number of times. Once the program has executed the code insde of the for loop n number of times, the program will then continue to evaluate and execute whatever is below the for loop.

This is where the `range` function comes into play. Using the `range` function, you can specify how many times the contents inside of the for loop will execute. Here is a simple demonstration below of how this will work.

```python
print("This will execute first")

for _ in range(3):
	print("This line will execute three times")
	print("This line will also execute three times")

print("Now we are outside of the for loop!")
```

**Output** :

```
This will execute first
This line will execute three times
This line will also execute three times
This line will execute three times
This line will also execute three times
This line will execute three times
This line will also execute three times
Now we are outside of the for loop!
```

There are a few things to notice here for when you use this later on. First, is that the two print statements on line 4 and 5 are executed three times, but we don’t print line 4 three times and then print line 5 three times. Instead, we print line 4, then line 5. Once that is done the for loop iterates, or brings the program back to the beginning of the for loop, and continues to print out lines 4 and 5 again until it has printed them both a total of three times.

Second, these lines were printed the same number as is inside the `range` function. If we wanted to print them more or fewer times, then we would just need to change the number inside of the parentheses on line 3.

Finally, the whitespace is important here. All of the statements that were printed out multiple times were indented under the for loop. Once we stopped indenting those lines, then the program was outside of the for loop and it would continue to execute linearly. If you’d like to watch the execution, checkout the code above in codelens!

Now it’s time to combine this with the Turtle module. We can do a lot of cool stuff if we combine these two things! Below is code to do just that. Try to predict what the program will do before running it.


```python
import turtle
wn = turtle.Screen()

elan = turtle.Turtle()

distance = 50
for _ in range(10):
    elan.forward(distance)
    elan.right(90)
    distance = distance + 10
```

**Output** :

![](https://media.giphy.com/media/dt6osHbZoVmVhv1lVb/giphy.gif)


#### More Turtle Methods

Here are a few more things that you might find useful as you write programs that use turtles.

Turtle methods can use negative angles or distances. So tess.forward(-100) will move tess backwards, and tess.left(-30) turns her to the right. Additionally, because there are 360 degrees in a circle, turning 30 to the left will leave you facing in the same direction as turning 330 to the right! (The on-screen animation will differ, though — you will be able to tell if tess is turning clockwise or counter-clockwise!)

This suggests that we don’t need both a left and a right turn method — we could be minimalists, and just have one method. There is also a backward method. (If you are very nerdy, you might enjoy saying alex.backward(-100) to move alex forward!)

Reviewing a few basic facts about geometry and number lines, like we’ve done here is a good start if we’re going to play with turtles.

A turtle’s pen can be picked up or put down. This allows us to move a turtle to a different place without drawing a line. The methods are `up` and `down`. Note that the methods `penup` and `pendown` do the same thing.

```python
alex.up()
alex.forward(100)     # this moves alex, but no line is drawn
alex.down()
```

Every turtle can have its own shape. The ones available “out of the box” are `arrow`, `blank`, `circle`, `classic`, `square`, `triangle`, `turtle`.

```python
...
alex.shape("turtle")
...
```

You can speed up or slow down the turtle’s animation speed. (Animation controls how quickly the turtle turns and moves forward). Speed settings can be set between 1 (slowest) to 10 (fastest). But if you set the speed to 0, it has a special meaning — turn off animation and go as fast as possible.

```python
alex.speed(10)
```

A turtle can “stamp” its footprint onto the canvas, and this will remain after the turtle has moved somewhere else. Stamping works even when the pen is up.


```python
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

dist = 5
tess.up()                     # this is new
for _ in range(30):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(dist)          # move tess along
    tess.right(24)              # and turn her
    dist = dist + 2
wn.exitonclick()
```

![](https://media.giphy.com/media/H47RYWmB0yogcUiKT6/giphy.gif)

If you are curious about how far the turtle is traveling each time the for loop iterates, you can add a print statement inside of the for loop to print out the value of `dist`.

One more thing to be careful about. All except one of the shapes you see on the screen here are footprints created by `stamp`. But the program still only has one turtle instance — can you figure out which one is the real tess? (Hint: if you’re not sure, write a new line of code after the `for` loop to change tess’ color, or to put her pen down and draw a line, or to change her shape, etc.)

**Mixed up program**

**E1** : The following program uses the stamp method to create a circle of turtle shapes as shown to the left, image of a circle of turtle shapes but the lines are mixed up. The program should do all necessary set-up, create the turtle, set the shape to "turtle", and pick up the pen. Then the turtle should repeat the following ten times: go forward 50 pixels, leave a copy of the turtle at the current position, reverse for 50 pixels, and then turn right 36 degrees. After the loop, set the window to close when the user clicks in it.

![](https://fopp.umsi.education/runestone/static/fopp/_static/TurtleCircle.png)

```python
import turtle
wn = turtle.Screen()
jose = turtle.Turtle()
jose.shape("turtle")
jose.penup()

for size in range(10):
	jose.forward(50)
	jose.stamp()
	jose.forward(-50)
	jose.right(36)

wn.exitonclick()
```

**E2** : The following program uses the stamp method to create a line of turtle shapes as shown to the left, image of a line of turtle shapes but the lines are mixed up. The program should do all necessary set-up, create the turtle, set the shape to "turtle", and pick up the pen. Then the turtle should repeat the following three times: go forward 50 pixels and leave a copy of the turtle at the current position. After the loop, set the window to close when the user clicks in it.

![](https://fopp.umsi.education/runestone/static/fopp/_static/Turtle3Stamp.png)

```python
import turtle
wn = turtle.Screen()
nikea = turtle.Turtle()
nikea.shape("turtle")
nikea.penup()

for size in range(3):
	nikea.forward(50)
	nikea.stamp()

wn.exitonclick()
```

# 3. Conditionals & Control Flow
### 3.1. Go With the Flow
Just like in real life, sometimes we'd like our code to be able to make decisions.

The Python programs we've written so far have had one-track minds: they can add two numbers or `print` something, but they don't have the ability to pick one of these outcomes over the other.

Control flow gives us this ability to choose among outcomes based on what else is happening in the program.



##### Instructions

Check out the code in the editor. You'll see the type of program you'll be able to write once you've mastered control flow. Click Run to see what happens!

```Python
#GIVEN
def clinic():
    print("You've just entered the clinic!")
    print("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
      print("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right" or answer == "r":
      print("Of course this is the Argument Room, I've told you that already!")
    else:
      print("You didn't pick left or right! Try again.")
      clinic()

clinic()

# OUTPUT
You've just entered the clinic!
Do you take the door on the left or the right?
Type left or right and hit 'Enter'.
# input : left
This is the Verbal Abuse Room, you heap of parrot droppings!
# input : right
Of course this is the Argument Room, I've told you that already!
```


### 3.2. Compare Closely!

Let's start with the simplest aspect of control flow: comparators. There are six:

**Equal to (`==`)**

```
>>> 2 == 2
True
>>> 2 == 5
False
```

**Not equal to (`!=`)**

```
>>> 2 != 5
True
>>> 2 != 2
False
```

**Less than (`<`)**

```
>>> 2 < 5
True
>>> 5 < 2
False
```

**Less than or equal to (`<=`)**

```
>>> 2 <= 2
True
>>> 5 <= 2
False
```

**Greater than (`>`)**

```
>>> 5 > 2
True
>>> 2 > 5
False
```

**Greater than or equal to (`>=`)**

```
>>> 5 >= 5
True
>>> 2 >= 5
False
```

Comparators check if a value is (or is not) equal to, greater than (or equal to), or less than (or equal to) another value.

Note that `==` compares whether two things are equal, and `=` assigns a value to a variable.

##### Instructions

Set each variable to `True` or `False` depending on what you think the result will be. For example, `1 < 2` will be `True`, because one is less than two.

* Set `bool_one` equal to the result of `17 < 328`
* Set `bool_two` equal to the result of `100 == (2 * 50)`
* Set `bool_three` equal to the result of `19 <= 19`
* Set `bool_four` equal to the result of `-22 >= -18`
* Set `bool_five` equal to the result of `99 != (98 + 1)`


```Python
#GIVEN
# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two =

# Set this to True if 19 <= 19 or to False if it is not.
bool_three =

# Set this to True if -22 >= -18 or to False if it is not.
bool_four =

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five =



# SOLUTION
bool_one = True   
bool_two = True
bool_three = True
bool_four = False
bool_five = False
```


### 3.3. Compare... Closelier!

Excellent! It looks like you're comfortable with basic expressions and comparators.

But what about extreme expressions and comparators?


##### Instructions
Let's run through the comparators again with more complex expressions. Set each variable to `True` or `False` depending on what you think the result will be.

* Set `bool_one` to the result of `(20 - 10) > 15`
* Set `bool_two` to the result of `(10 + 17) == 3**16`
* Set `bool_three` to the result of `1**2 <= -1`
* Set `bool_four` to the result of `40 * 4 >= -4`
* Set `bool_five` to the result of `100 != 10**2`


```Python
#GIVEN
# Assign True or False as appropriate on the lines below!

# (20 - 10) > 15
bool_one = False    # We did this one for you!

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
bool_two =

# 1**2 <= -1
bool_three =

# 40 * 4 >= -4
bool_four =

# 100 != 10**2
bool_five =



# SOLUTION
bool_one = False    # We did this one for you!
bool_two = False
bool_three = False
bool_four = True
bool_five = False
```


### 3.4. How the Tables Have Turned

Comparisons result in either True or False, which are booleans as we learned before in Booleans exercise.

```python
# Make me true!
bool_one = 3 < 5
print(bool_one)
# Output : True
```
Let's switch it up: we'll give the boolean, and you'll write the expression, just like the example above.

##### Instructions
For each boolean value in the editor, write an expression that evaluates to that value. Remember, comparators are: `==`, `!=`, `>`, `>=`, `<`, and `<=`.

Use at least three different ones!

Don't just use `True` and `False`! That's cheating!


```Python
#GIVEN
# Create comparative statements as appropriate on the lines below!

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two =

# Make me true!
bool_three =

# Make me false!
bool_four =

# Make me true!
bool_five =


# SOLUTION
bool_one = 3 < 5  
bool_two = 2 != 2
bool_three = 2 == 2
bool_four = 2 < 2
bool_five = 2 <= 2

print(bool_one)
print(bool_two)
print(bool_three)
print(bool_four)
print(bool_five)

# OUTPUTS
True
False
True
False
True
```


### 3.5. To Be and/or Not to Be
Boolean operators compare statements and result in boolean values. There are three boolean operators:

1. `and`, which checks if both the statements are `True`;
2. `or`, which checks if at least one of the statements is `True`;
3. `not`, which gives the opposite of the statement.

We'll go through the operators one by one.

##### Instructions

Check out the truth tables to the right. They show the results of using AND, OR, and NOT boolean operators given the boolean inputs A and B.

![](http://i66.tinypic.com/14np7kj.png)



### 3.6. `And`

The boolean operator and returns `True` when the expressions on both sides of `and` are `true`. For instance:

* `1 < 2 and 2 < 3` is `True`;
* `1 < 2 and 2 > 3` is `False`.



##### Instructions

Let's practice with `and`. Assign each variable to the appropriate boolean value.

* Set `bool_one` equal to the result of
`False and False`
* Set `bool_two` equal to the result of
`-(-(-(-2))) == -2 and 4 >= 16 ** 0.5`
* Set `bool_three` equal to the result of
`19 % 4 != 300 / 10 / 10 and False`
* Set `bool_four` equal to the result of
`-(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2`
* Set bool_five equal to the result of
`True and True`

```Python
# SOLUTION
# False and False
bool_one = 2 != 2 and 2 >= 5
# False and True
bool_two = 2 > 5 and 2 < 5
# False and False
bool_three = 1 == -1 and 1 <= -1
# True and True
bool_four = 1 != -1 and 1 >= -1
# True and True
bool_five = 3 == 3 and 5 >= 5


print(bool_one)
print(bool_two)
print(bool_three)
print(bool_four)
print(bool_five)

# OUTPUTS
False
False
False
True
True
```


### 3.7. `Or`

The boolean operator or returns `True` when at least one expression on either side of or is true. For example:

* `1 < 2 or 2 > 3` is `True`;
* `1 > 2 or 2 > 3` is `False`.



##### Instructions

Time to practice with or!

* Set `bool_one` equal to the result of
`2 ** 3 == 108 % 100 or 'Cleese' == 'King Arthur'`
* Set `bool_two` equal to the result of
`True or False`
* Set `bool_three` equal to the result of
`100 ** 0.5 >= 50 or False`
* Set `bool_four` equal to the result of
`True or True`
* Set `bool_five` equal to the result of
`1 ** 100 == 100 ** 1 or 3 * 2 * 1 != 3 + 2 + 1`

```Python
# SOLUTION
# True or False = True
bool_one = 1 == 1 or 1 == -1
# True or False = True
bool_two = 1 > -1 or 1 < -1
# False or False = False
bool_three = 1 == -1 or 1 < -1
# True or True = True
bool_four = 1 == 1 or 1 > -1
# False or False = False
bool_five = 3 != 3 or 3 == -3


print(bool_one)
print(bool_two)
print(bool_three)
print(bool_four)
print(bool_five)

# OUTPUTS
True
True
False
True
False
```


### 3.8. `Not`
The boolean operator not returns `True` for false statements and `False` for true statements.

For example:

* `not False` will evaluate to `True`, while not `41 > 40` will return `False`.



##### Instructions

Let's get some practice with not.

* Set `bool_one` equal to the result of
`not True`
* Set `bool_two` equal to the result of
`not 3 ** 4 < 4 ** 3`
* Set `bool_three` equal to the result of
`not 10 % 3 <= 10 % 2`
* Set `bool_four` equal to the result of
`not 3 ** 2 + 4 ** 2 != 5 ** 2`
* Set `bool_five` equal to the result of
`not not False`

```Python
# SOLUTION
# False
bool_one = 1 == -1
# True
bool_two = 1 != -1
# True
bool_three = 1 > -1
# True
bool_four = 1 >= -1
# False
bool_five = 1 < -1

```


### 3.9. This and That (or This, But Not That!)

Boolean operators aren't just evaluated from left to right. Just like with arithmetic operators, there's an order of operations for boolean operators:

1. `not` is evaluated first;
2. `and` is evaluated next;
3. `or` is evaluated last.

For example, `True or not False and False` returns `True`. If this isn't clear, look at the Hint.

Parentheses `()` ensure your expressions are evaluated in the order you want. Anything in parentheses is evaluated as its own unit.

```python
b1 = True or not False and False
b2 = not False or True and False
b3 = False and True or not False
b4 = (True or not False) and False

print(b1)
print(b2)
print(b3)
print(b4)

# Output :
True
True
True
False
```

##### Instructions
Assign `True` or `False` as appropriate for `bool_one` through `bool_five`.

* Set `bool_one` equal to the result of
`False or not True and True`
* Set `bool_two` equal to the result of
`False and not True or True`
* Set `bool_three` equal to the result of
`True and not (False or False)`
* Set `bool_four` equal to the result of
`not not True or False and not True`
* Set `bool_five` equal to the result of
`False or not (True and True)`

```Python
# SOLUTION
# False
bool_one = 1 != 1
# True
bool_two = 1 != -1
# True
bool_three = 1 >= -1
# True
bool_four = -1 < 1
# False
bool_five = 1 <= -1

```


### 3.10. Mix 'n' Match

Great work! We're almost done with boolean operators.

```python
# Make me false
bool_one = (2 <= 2) and "Alpha" == "Bravo"
# Output : False
```

##### Instructions
This time we'll give the expected result, and you'll use some combination of boolean operators to achieve that result.

Remember, the boolean operators are `and`, `or`, and `not`. Use each one at least once!

```Python
# GIVEN
# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two =

# Make me false!
bool_three =

# Make me true!
bool_four =

# Make me true!
bool_five =


# SOLUTION
bool_one = (2 <= 2) and "Alpha" == "Bravo"
bool_two = 1 != -1 or 1 < -1
bool_three = not 1 > -1
bool_four = not -1 > 1
bool_five = 1 == 1 and -1 != 1

print(bool_one)
print(bool_two)
print(bool_three)
print(bool_four)
print(bool_five)


# Output
False
True
False
True
True
```


### 3.11. Conditional Statement Syntax

`if` is a conditional statement that executes some specified code after checking if its expression is `True`.

Here's an example of if statement syntax:

```python
if 8 < 9:
  print("Eight is less than nine!")

# Output : Eight is less than nine!
```

In this example, `8 < 9` is the checked expression and `print("Eight is less than nine!")` is the specified code.

Pay attention to the indentation before the `print` statement. This space, called ***white space***, is how Python knows we are entering a new block of code. Python accepts many different kinds of indentation to indicate blocks. In this lesson, we use four spaces but elsewhere you might encounter two-space indentation or tabs (which Python will see as different from spaces).

If the indentation from one line to the next is different and there is no command (like `if`) that indicates an incoming block then Python will raise an `IndentationError`. These errors could mean, for example, that one line had two spaces but the next one had three. Python tries to indicate where this error happened by printing the line of code it couldn't parse and using a `^` to point to where the indentation was different from what it expected.

##### Instructions
If you think the `print` statement will print to the console, set `response` equal to `'Y'`; otherwise, set response equal to `'N'`.

```Python
# GIVEN
response =

answer = "Left"
if answer == "Left":
    print("This is the Verbal Abuse Room, you heap of parrot droppings!")

# Will the above print statement print to the console?
# Set response to 'Y' if you think so, and 'N' if you think not.

# SOLUTION
response = 'Y'

answer = "Left"
if answer == "Left":
    print("This is the Verbal Abuse Room, you heap of parrot droppings!")


# OUTPUT :
This is the Verbal Abuse Room, you heap of parrot droppings!
```

### 3.12. If You're Having...

Let's get some practice with `if` statements. Remember, the syntax looks like this:

```python
if some_function():
  # block line one
  # block line two
  # et cetera
```

Looking at the example above, in the event that `some_function()` returns `True`, then the indented block of code after it will be executed. In the event that it returns `False`, then the indented block will be skipped.

Also, make sure you notice the colons at the end of the `if` statement. We've added them for you, but they're important.


##### Instructions
In the editor you'll see two functions. Don't worry about anything unfamiliar. We'll explain soon enough.

* Replace the underline on line 2 with an expression that returns `True`.
* Replace the underline on line 6 with an expression that returns `True`.

If you do it successfully, then both `"Success #1"` and `"Success #2"` are printed.

```Python
# GIVEN
def using_control_once():
    if _______:
        return "Success #1"

def using_control_again():
    if _______:
        return "Success #2"

print(using_control_once())
print(using_control_again())

# SOLUTION
def using_control_once():
    if "Blue" != "blue":
        return "Success #1"

def using_control_again():
    if 1**1 == 1:
        return "Success #2"
print(using_control_once())
print(using_control_again())


# OUTPUT :
Success #1
Success #2
```


### 3.13. Else Problems, I Feel Bad for You, Son...
The `else` statement complements the `if` statement. An `if/else` pair says: ***"If this expression is true, run this indented code block; otherwise, run this code after the else statement."***

Unlike `if`, `else` doesn't depend on an expression. For example:


```python
if 8 > 9:
  print("I don't printed!")
else:
  print("I get printed!")

# Output : I get printed!
```



##### Instructions
Complete the `else` statements to the right. Note the indentation for each line!

```Python
# GIVEN
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return        # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return        # Make sure this returns False



# SOLUTION
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False     

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False    
```


### 3.14. I Got 99 Problems, But a Switch Ain't One

`elif` is short for "else if." It means exactly what it sounds like: ***"otherwise, if the following expression is true, do this!"***

```python
if 8 > 9:
  print("I don't get printed!")
elif 8 < 9:
  print("I get printed!")
else:
  print("I also don't get printed!")

# Output : I get printed!
```



##### Instructions

On line 2, fill in the `if` statement to check if `answer` is greater than 5.

On line 4, fill in the `elif` so that the function outputs `-1` if `answer` is less than 5.

```Python
# GIVEN
def greater_less_equal_5(answer):
    if ________:
        return 1
    elif ________:          
        return -1
    else:
        return 0

print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))


# SOLUTION
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0

print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))

# OUTPUTS
-1
0
1
```


### 3.15. The Big If

Really great work! Here's what you've learned in this unit:

**Comparators**
```python
3 < 4
5 >= 5
10 == 10
12 != 13
```

**Boolean operators**
```python
True or False
(3 < 4) and (5 >= 5)
this() and not that()
```

**Conditional statements**
```python
if this_might_be_true():
  print("This really is true.")
elif that_might_be_true():
  print("That is true.")
else:
  print("None of the above.")
```

Let's get to the grand finale.

##### Instructions
In the workspace to your right, there is the outline of a function called `grade_converter()`.

The purpose of this function is to take a number grade (1-100), defined by the variable `grade`, and to return the appropriate letter grade (A, B, C, D, or F).

Your task is to complete the function by creating appropriate `if` and `elif` statements that will compare the input `grade` with a number and then return a letter grade.

Your function should return the following letter grades:

* 90 or higher should get an "A"
* 80 - 89 should get a "B"
* 70 - 79 should get a "C"
* 65 - 69 should get a "D"
* Anything below a 65 should receive an "F"

```Python
# GIVEN
# Complete the if and elif statements!
def grade_converter(grade):
    if _____:
        return "A"
    elif _____:
        return "B"
    elif _____:
        return "C"
    elif _____:
        return "D"
    else:
        return "F"

# This should print an "A"      
print(grade_converter(92))

# This should print a "C"
print(grade_converter(70))

# This should print an "F"
print(grade_converter(61))


# SOLUTION
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80 and grade <= 89:
        return "B"
    elif grade >= 70 and grade <= 79:
        return "C"
    elif grade >= 65 and grade <= 69:
        return "D"
    else:
        return "F"

print(grade_converter(92))
print(grade_converter(70))
print(grade_converter(61))

# OUTPUTS
A
C
F
```


## PygLatin
### 1. Break It Down
Now let's take what we've learned so far and write a Pig Latin translator.

Pig Latin is a language game, where you move the first letter of the word to the end and add "ay." So "Python" becomes "ythonpay." To write a Pig Latin translator in Python, here are the steps we'll need to take:

1. Ask the user to input a word in English.
2. Make sure the user entered a valid word.
3. Convert the word from English to Pig Latin.
4. Display the translation result.


### 2. Ahoy! (or Should I Say Ahoyay!)
Let's warm up by printing a welcome message for our translator users.

#### Instructions
Please print the phrase "Pig Latin".

```python
print("Pig Latin")
```


### 3. Input!
Next, we need to ask the user for input.

```python
name = input("What's your name?")
print(name)
```

In the above example, `input()` accepts a string, prints it, and then waits for the user to type something and press Enter (or Return).

In the interpreter, Python will ask:

```
What's your name?
```
Once you type in your name and hit Enter, it will be stored in `name`

#### Instructions
On line 4, use `input("Enter a word: ")` to ask the user to enter a word. Save the results of `input()` in a variable called `original`.

Click Run

Type a word in the console window and press Enter (or Return).

```python
# GIVEN
print('Welcome to the Pig Latin Translator!')

# SOLUTION
print('Welcome to the Pig Latin Translator!')
original = input("Enter a word:")

# OUTPUT
```

### 4. Check Yourself!

Next we need to ensure that the user actually typed something.

```python
empty_string = ""
if len(empty_string) > 0:
  # Run this block.
  # Maybe print something?
else:
  # That string must have been empty.
```

We can check that the user's string actually has characters!

#### Instructions

Write an `if` statement that verifies that the string has characters.

* Add an `if` statement that checks that `len(original)` is greater than zero. Don't forget the `:` at the end of the if statement!
* If the string actually has some characters in it, `print` the user's word.
* Otherwise (i.e. an `else:` statement), please `print "empty"`.

You'll want to run your code multiple times, testing an empty string and a string with characters. When you're confident your code works, continue to the next exercise.

```python
# GIVEN
print('Welcome to the Pig Latin Translator!')
original = input("Enter a word:")

# SOLUTION
print('Welcome to the Pig Latin Translator!')
original = input("Enter a word:")

if len(original) > 0:
  print("original")
else:
  print("empty")
```


### 5. Check Yourself!... Some More
Now we know we have a non-empty string. Let's be even more thorough and check that our string only contains letters.

Consider the following code:


```python
x = "J123"
x.isalpha()  # This will return 'False'
```
In the first line, we create a string with letters and numbers.

The second line then runs the method `.isalpha()` which returns `False` since the string contains non-letter characters.

You can use `.isalpha()` to check that a string doesn't contain any non-letter characters!


#### Instructions
Use `and` to add a second condition to your `if` statement. In addition to your existing check that the string contains characters, you should also use `.isalpha()` to make sure that it only contains letters.

Don't forget to keep the colon at the end of the `if` statement!

```python
# GIVEN
print('Welcome to the Pig Latin Translator!')
original = input("Enter a word:")

if len(original) > 0:
  print(original)
else:
  print("empty")

# SOLUTION
print('Welcome to the Pig Latin Translator!')
original = input("Enter a word:")

if len(original) > 0 and original.isalpha():
  print(original)
else:
  print("empty")
```


### 6. Pop Quiz!
When you finish one part of your program, it's important to test it multiple times, using a variety of inputs.


#### Instructions

Take some time to test your current code. Try some inputs that should pass and some that should fail. Enter some strings that contain non-alphabetical characters and an empty string.

When you're convinced your code is ready to go, click Next to move forward!


```python
# GIVEN
print('Welcome to the Pig Latin Translator!')
original = input("Enter a word:")

if len(original) > 0 and original.isalpha():
  print(original)
else:
  print("empty")
```


### 7. Ay B C

Now we can get ready to start translating to Pig Latin! Let's review the rules for translation:

You move the first letter of the word to the end and then append the suffix 'ay'.

Example: python -> ythonpay

Let's create a variable to hold our translation suffix.


#### Instructions
Create a variable named `pyg` and set it equal to the suffix `'ay'`.

```python
# SOLUTION
pyg = 'ay'
```

### 8. Word Up

Let's simplify things by making the letters in our word lowercase.

```python
the_string = "Hello"
the_string = the_string.lower()
```

The `.lower()` function does not modify the string itself, it simply returns a lowercase-version. In the example above, we store the result back into the same variable.

We also need to grab the first letter of the word.

```python
first_letter  = the_string[0]
second_letter = the_string[1]
third_letter  = the_string[2]
```

Remember that we start counting from zero, not one, so we access the first letter by asking for `[0]`.

#### Instructions

Inside your `if` statement:

* Create a new variable called `word` that holds the `.lower()`-case conversion of original.
* Create a new variable called `first` that holds `word[0]`, the first letter of word.

```python
# GIVEN
pyg = 'ay'

print('Welcome to the Pig Latin Translator!')
original = input("Enter a word:")

if len(original) > 0 and original.isalpha():
  print(original)
else:
  print("empty")


# SOLUTION
pyg = 'ay'

print('Welcome to the Pig Latin Translator!')
original = input("Enter a word:")

if len(original) > 0 and original.isalpha():
  print(original)
  word = original.lower()
  first = word[0]
else:
  print("empty")
```


### 9. Move it on Back

Now that we have the first letter stored, we need to add both the letter and the string stored in `pyg` to the end of the original string.

Remember how to concatenate (i.e. add) strings together?

```python
greeting = "Hello"
name = "D. Y."
welcome = greeting + name
```

#### Instructions

On a new line after where you created the `first` variable:

Create a new variable called `new_word` and set it equal to the concatenation of `word`, `first`, and `pyg`.

```python
# GIVEN
pyg = 'ay'

print('Welcome to the Pig Latin Translator!')
original = input("Enter a word:")

if len(original) > 0 and original.isalpha():
  print(original)
  word = original.lower()
  first = word[0]
else:
  print("empty")


# SOLUTION
pyg = 'ay'

print('Welcome to the Pig Latin Translator!')
original = input("Enter a word:")

if len(original) > 0 and original.isalpha():
  print(original)
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
else:
  print("empty")
```


### 10. Ending Up

Well done! However, now we have the first letter showing up both at the beginning and near the end.

```python
s = "Charlie"

print s[0]
# will print "C"

print s[1:4]
# will print "har"
```

1. First we create a variable `s` and give it the string `"Charlie"`
2. Next we access the first letter of `"Charlie"` using `s[0]`. Remember letter positions start at 0.
3. Then we access a slice of `"Charlie"` using `s[1:4]`. This returns everything from the letter at position 1 up till position 4.

We are going to slice the string just like in the 3rd example above.

#### Instructions

Set `new_word` equal to the slice from the 1st index all the way to the end of `new_word`. Use `[1:len(new_word)]` to do this.

```python
# GIVEN
pyg = 'ay'

print('Welcome to the Pig Latin Translator!')
original = input("Enter a word:")

if len(original) > 0 and original.isalpha():
  print(original)
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
else:
  print("empty")


# SOLUTION
pyg = 'ay'

print('Welcome to the Pig Latin Translator!')
original = input("Enter a word:")

if len(original) > 0 and original.isalpha():
  print(original)
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
else:
  print("empty")
```


### 11. Testing, Testing, is This Thing On?

Yay! You should have a fully functioning Pig Latin translator. Test your code thorougly to be sure everything is working smoothly.

You'll also want to take out any `print` statements you were using to help debug intermediate steps of your code. Now might be a good time to add some comments too! Making sure your code is clean, commented, and fully functional is just as important as writing it in the first place.


#### Instructions
When you're sure your translator is working just the way you want it, click Run Code to finish this project.


```python
# GIVEN
pyg = 'ay'

print('Welcome to the Pig Latin Translator!')
original = input("Enter a word:")

if len(original) > 0 and original.isalpha():
  print(original)
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
else:
  print("empty")


# SOLUTION
pyg = 'ay'

print('Welcome to the Pig Latin Translator!')
original = input("Enter a word:")

if len(original) > 0 and original.isalpha():
  print(original)
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print(new_word)
else:
  print("empty")
```

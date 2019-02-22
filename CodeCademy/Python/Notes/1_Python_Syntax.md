# 1. Python Syntax
## 1. Hello World!
If programming is the act of teaching a computer to have a conversation with a user, it would be most useful to first teach the computer how to speak. In Python, this is accomplished with the `print` statement.

```python
print("Hello, world!")
# Output : Hello, world!

print("Water—there is not a drop of water there! Were Niagara but a cataract of sand, would you travel your thousand miles to see it?")
# Output : Water—there is not a drop of water there! Were Niagara but a cataract of sand, would you travel your thousand miles to see it?
```

A ***print*** statement is the easiest way to get your Python program to communicate with you. Being able to command this communication will be one of the most valuable tools in your programming toolbox.

##### Instructions
Using a `print` statement, output a message of your choosing to the terminal.

```Python
print("Hi there!")
# Output : Hi there!
```


## 2. Print Statements
There are two different Python versions. Both Python 2 and Python 3 are used throughout the globe. The most significant difference between the two is how you write a `print` statement. In Python 3, print has parentheses.

```python
print("Hello World!")
print("Deep into distant woodlands winds a mazy way, reaching to overlapping spurs of mountains bathed in their hill-side blue.")
```

##### Instructions
Print something using Python 3's syntax.

```Python
print("Hi there!")
# Output : Hi there!
```

## 3. Strings
When printing things in Python, we are supplying a text block that we want to be printed. Text in Python is considered a specific type of data called a string. A string, so named because they're a series of letters, numbers, or symbols connected in order — as if threaded together by string. Strings can be defined in different ways:

```python
print("This is a good string")
print('You can use single quotes or double quotes for a string')
# Output :
# This is a good string
# You can use single quotes or double quotes for a string
```

Above we printed two things that are strings and then attempted to print two things that are not strings. While double-quotes (") and single-quotes (') are both acceptable ways to define a string, a string needs to be opened and closed by the same type of quote mark.

We can combine multiple strings using +, like so:

```python
print("This is " + "a good string")
# Output : This is a good string
```
##### Instructions
Try adding your name to the print statement with the `+` operator so that this Python program prints `"Hello [your_name]"`

```Python
# Given code :
print("Hello ")

# Solution :
print("Hello " + "Heval")
# Output : Hello Heval
```

## 4. Handling Errors
As we get more familiar with the Python programming language, we run into errors and exceptions. These are complaints that Python makes when it doesn't understand what you want it to do. Everyone runs into these issues, so it is a good habit to read and understand them. Here are some common errors that we might run into when printing strings:

```
print("Mismatched quotes will cause a SyntaxError')
print(Without quotes will cause a NameError)
```

If the quotes are mismatched Python will notice this and inform you that your code has an error in its syntax because the line ended (called an EOL) before the double-quote that was supposed to close the string appeared. The program will abruptly stop running with the following message:

`SyntaxError: EOL while scanning a string literal`

This means that a string wasn't closed, or wasn't closed with the same quote-character that started it.

Another issue you might run into is attempting to create a string without quotes at all. Python treats words not in quotes as commands, like the print statement. If it fails to recognize these words as defined (in Python or by your program elsewhere) Python will complain the code has a NameError. This means that Python found what it thinks is a command, but doesn't know what it means because it's not defined anywhere.


##### Instructions
We've written two print statements that will raise errors. One has mismatched quotes and the other has no quotes at all.

Fix the two print statements to successfully debug the program!

```
# Given code :
print("How do you make a hot dog stand?')
print(You take away its chair!)

# Solution :
print("How do you make a hot dog stand?")
print("You take away its chair!")

# Output :
How do you make a hot dog stand?
You take away its chair!
```

## 5. Variables
In Python, and when programming in general, we need to build systems for dealing with data that changes over time. That data could be the location of a plane, or the time of day, or the television show you're currently watching. The only important thing is that it may be different at different times. Python uses variables to define things that are subject to change.

```python
greeting_message = "Welcome to Codecademy!"
current_excercise = 5
```

In the above example, we defined a variable called `greeting_message` and set it equal to the string "Welcome to Codecademy!". It also defined a variable called `current_exercise` and set it equal to the number 5.

##### Instructions
Create a variable called `todays_date` and assign a value that will represent today's date to that variable.

```python
todays_date = "17 December 2018"
```

## Arithmetic
One thing computers are capable of doing exceptionally well is performing arithmetic. Addition, subtraction, multiplication, division, and other numeric calculations are easy to do in most programming languages, and Python is no exception. Some examples:

```Python
mirthful_addition = 12381 + 91817
amazing_subtraction = 981 - 312
trippy_multiplication = 38 * 902
happy_division = 540 / 45
sassy_combinations = 129 * 1345 + 120 / 6 - 12
```

Above are a number of arithmetic operations, each assigned to a variable. The variable will hold the final result of each operation. Combinations of arithmetical operators follow the usual order of operations.

Python also offers a companion to division called the modulo operator. The modulo operator is indicated by % and returns the remainder after division is performed.

```Python
is_this_number_odd = 15 % 2
is_this_number_divisible_by_seven = 133 % 7
```

In the above code block, we use the modulo operator to find the remainder of 15 divided by 2. Since 15 is an odd number the remainder is 1.

We also check the remainder of 133 / 7. Since 133 divided by 7 has no remainder, 133 % 7 evaluates to 0.

##### Instructions
1. Multiply two numbers together and assign the result to a variable called product.
2. What is the remainder when 1398 is divided by 11? Save the results in a variable called remainder.

```python
product = 2 * 6
remainder = 1398 % 11

# Output
12
1
```

## Updating Variables

Changing the contents of a variable is one of the essential operations. As the flow of a program progresses, data should be updated to reflect changes that have happened.

```python
fish_in_clarks_pond = 50

print("Catching fish")

number_of_fish_caught = 10
fish_in_clarks_pond = fish_in_clarks_pond - number_of_fish_caught
```

In the above example, we start with 50 fish in a local pond. After catching 10 fish, we update the number of fish in the pond to be the original number of fish in the pond minus the number of fish caught. At the end of this code block, the variable `fish_in_clarks_pond` is equal to 40.

Updating a variable by adding or subtracting a number to the original contents of the variable has its own shorthand to make it faster and easier to read.

```python
money_in_wallet = 40
sandwich_price = 7.50
sales_tax = .08 * sandwich_price

sandwich_price += sales_tax
money_in_wallet -= sandwich_price
```

In the above example, we use the price of a sandwich to calculate sales tax. After calculating the tax we add it to the total price of the sandwich. Finally, we complete the transaction by reducing our `money_in_wallet` by the cost of the sandwich (with tax).

##### Instructions
We're trying to figure out how much it rained in the past year! Update the `annual_rainfall` variable to include the values from September to December.

```python
- GIVEN CODE -
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06

- SOLUTION -
# Added lines after the given code
september_to_december_rainfall = september_rainfall + october_rainfall + november_rainfall + december_rainfall
annual_rainfall += september_to_december_rainfall

# Output
45.209999999999994
```


## Comments

Most of the time, code should be written in such a way that it is easy to understand on its own. However, if you want to include a piece of information to explain a part of your code, you can use the `#` sign. A line of text preceded by a `#` is called a comment. The machine does not run this code — it is only for humans to read. When you look back at your code later, comments may help you figure out what it was intended to do.

```python
# this variable counts how many rows of the spreadsheet we have:
row_count = 13
```


##### Instructions
Add a comment above the declaration of `city_pop` with a description of what you think the variable contains.

```python
- GIVEN CODE -
city_name = "St. Potatosburg"
city_pop = 340000

- SOLUTION -
city_name = "St. Potatosburg"
# The city population
city_pop = 340000
```


## Numbers

Variables can also hold numeric values. The simplest kind of number in Python is the integer, which is a whole number with no decimal point:

```python
int1 = 1
int2 = 10
int3 = -5
```

A number with a decimal point is called a float. You can define floats with numbers after the decimal point or by just including a decimal point at the end:

```python
float1 = 1.0
float2 = 10.
float3 = -5.5
```

You can also define a float using scientific notation, with `e` indicating the power of 10.

```python
# this evaluates to 150:
float4 = 1.5e2
```

##### Instructions
1. You are going shopping. Let's make a grocery list so that you can plan your budget. Store the number of cucumbers you want to buy in a variable called cucumbers. Make sure it's at least 1, and that it's the appropriate datatype! The store doesn't sell partial cucumbers.
2. Each cucumber costs 3.25 doubloons. Store the price per cucumber in a variable called `price_per_cucumber`.
3. Create a new variable called `total_cost` which is the product of how many cucumbers you are going to buy and the cost per cucumber.
4. Print out `total_cost`

```python
cucumbers = 5
price_per_cucumber = 3.25
total_cost = cucumbers * price_per_cucumber
print(total_cost)

# Output
16.25
```


## Two Types of Division
In Python, when we divide two integers, we get an integer as a result. When the quotient is a whole number, this works fine:


```python
quotient1 = 6/2
quotient2 = 7/2
print(quotient1)			# Output : 3.0
print(quotient2)			# Output : 3.5
```


##### Instructions
1. You have come home from the grocery store with 100 cucumbers to split amongst yourself and your 5 roommates (6 people total). Create a variable `cucumbers` that holds 100 and `num_people` that holds 6.
2. Create a variable called `whole_cucumbers_per_person` that is the integer result of dividing cucumbers by `num_people`. Print whole_cucumbers_per_person to the console.
3. You realize that the numbers don't divide evenly and you don't want to throw out the remaining cucumbers. Create a variable called `float_cucumbers_per_person` that holds the float result of dividing cucumbers by `num_people`. Print `float_cucumbers_per_person` to the console.

```python
# Python 2 version
cucumbers = 100
num_people = 6
whole_cucumbers_per_person = cucumbers / num_people
print whole_cucumbers_per_person
float_cucumbers_per_person = float(cucumbers) / num_people
print float_cucumbers_per_person
# Outputs :
# 16
# 16.6666666667

# Python 3 version
cucumbers = 100
num_people = 6
whole_cucumbers_per_person = cucumbers / num_people
print(whole_cucumbers_per_person)
# Output
# 16
```


## Multi-line Strings
We have seen how to define a string with single quotes and with double quotes. If we want a string to span multiple lines, we can also use triple quotes:


```python
address_string = """136 Whowho Rd
Apt 7
Whosville, WZ 44494"""
print(address_string)

# Output :
# 136 Whowho Rd
# Apt 7
# Whosville, WZ 44494
```
This address spans multiple lines, and is still contained in one variable, address_string.

When a string like this is not assigned to a variable, it works as a multi-line comment. This can be helpful as your code gets more complex:

```python
string1 = """The following piece of code does the following steps:
takes in some input
does An Important Calculation
returns the modified input and a string that says "Success!" or "Failure..."
"""
print(string1)

# Output :
# The following piece of code does the following steps:
# takes in some input
# does An Important Calculation
# returns the modified input and a string that says "Success!" or "Failure..."
```

##### Instructions
Create a variable called haiku and store this `haiku` as a multi-line string:

```python
haiku = """The old pond,
A frog jumps in:
Plop!"""
print(haiku)

# Output
# The old pond,
# A frog jumps in:
# Plop!
```

## Booleans
Sometimes we have a need for variables that are either true or false. This datatype, which can only ever take one of two values, is called a boolean. In Python, we define booleans using the keywords `True` and `False`:


```python
a = True
b = False
print(a, b)
# Output : True False
```
A boolean is actually a special case of an integer. A value of True corresponds to an integer value of 1, and will behave the same. A value of False corresponds to an integer value of 0.

##### Instructions
1. Someone has introduced themselves to you using comments in script.py. Read the comments and then create a variable called `age_is_12` and set it to be `True` or `False` depending on if this person's age is 12.
2. Create a variable called `name_is_maria` and set it to be `True` or `False` depending on if this person's name is Maria.

```python
- GIVEN -
# Hi! I'm Maria and I live in script.py.
# I'm an expert Python coder.
# I'm 21 years old and I plan to program cool stuff forever.

- SOLUTION -
age_is_12 = False
name_is_maria = True
print(age_is_12, name_is_maria)
# Output : False True
```

## ValueError
Python automatically assigns a variable the appropriate datatype based on the value it is given. A variable with the value 7 is an integer, 7. is a float, "7" is a string. Sometimes we will want to convert variables to different datatypes. For example, if we wanted to print out an integer as part of a string, we would want to convert that integer to a string first. We can do that using `str()`:


```python
age = 13
print("I am " + str(age) + " years old!")
# Output : I am 13 years old!
```
Similarly, if we have a string like "7" and we want to perform arithmetic operations on it, we must convert it to a numeric datatype. We can do this using `int()`:

```python
number1 = "100"
number2 = "10"

string_addition = number1 + number2
int_addition = int(number1) + int(number2)
print(string_addition)
print(int_addition)

# Output :
# 10010
# 110
```

If you use `int()` on a floating point number, it will round the number down. To preserve the decimal, you can use `float()`:

```python
string_num = "7.5"
print(float(string_num))

# Output : 7.5
```



##### Instructions
1. Create a variable called product that contains the result of multiplying the float value of `float_1` and `float_2`.
2. Create a string called `big_string` that says: `The product was X`

```python
- GIVEN -
float_1 = 0.25
float_2 = 40.0

- SOLUTION -
product = float_1 * float_2
big_string = "The product was " + str(product)
print(big_string)

# Output : The product was 10.0
```

## Review

Great! So far we’ve looked at:

* Print statements
* How to create, modify, and use variables
* Arithmetic operations like addition, subtraction, division, and multiplication
* How to use comments to make your code easy to understand
* Different data types, including strings, ints, floats, and booleans
* Converting between data types

```python

# Output : I am 13 years old!
```


##### Instructions
1. Let's apply all of the concepts you have learned one more time! Create a variable called `skill_completed` and set it equal to the string "Python Syntax".
2. Create a variable called `exercises_completed` and set it equal to 13. Create another variable called `points_per_exercise` and set it equal to 5.
3. Create a variable called `point_total` and set it equal to 100.
4. Update `point_total` to be what it was before plus the result of multiplying `exercises_completed` and points_per_exercise.
5. Add a comment above your declaration of `points_per_exercise` that says: `The amount of points for each exercise may change, because points don't exist yet`
6. Print a string to the console that says: `I got X points!` with the value of `point_total` where X is.

```python
skill_completed = "Python Syntax"
exercises_completed = 13
# The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5
point_total = 100
point_total += exercises_completed*points_per_exercise

print("I got "+str(point_total)+" points!")
# Output : I got 165 points!
```

# 2. Strings & Console Output
## 2.1. Strings
### 2.1.1. Strings
Another useful data type is the string. A string can contain letters, numbers, and symbols.

```python
name = "Ryan"
age = "19"
food = "cheese"
```

In the above example, we create a variable `name` and set it to the string value "Ryan".
We also set `age` to "19" and `food` to "cheese".
Strings need to be within quotes.

##### Instructions

Create a new variable brian and assign it the string "Hello life!".

```Python
# Set the variable brian on line 3!

brian = "Hello life!"
```

### 2.1.2 Practice
Excellent! Let's get a little practice in with strings.

##### Instructions

Set the following variables to their respective phrases:
* Set `caesar` to "Graham"
* Set `praline` to "John"
* Set `viking` to "Teresa"

```Python
# Assign your variables below, each on its own line!

caesar = "Graham"
praline = "John"
viking = "Teresa"

# Put your variables above this line

print(caesar)
print(praline)
print(viking)
```

### 2.1.3. Escaping characters
There are some characters that cause problems. For example:

```python
'There's a snake in my boot!'
```

This code breaks because Python thinks the apostrophe in 'There's' ends the string. We can use the backslash to fix the problem, like this:

```python
'There\'s a snake in my boot!'
```

##### Instructions

Fix the string in the editor!

```Python
#GIVEN
# The string below is broken. Fix it using the escape backslash!
'This isn't flying, this is falling with style!'

# SOLUTION
'This isn\'t flying, this is falling with style!'
```


### 2.1.4. Access by Index
Each character in a string is assigned a number. This number is called the index. Check out the diagram in the editor.

```python
c = "cats"[0]
n = "Ryan"[3]
```

In the above example, we create a new variable called `c` and set it to "c", the character at index zero of the string "cats".

Next, we create a new variable called `n` and set it to "n", the character at index three of the string "Ryan".

Notice that in the first "cat" example we are calling the 0th letter of "cat" and getting "c" in return. This is because in Python indices begin counting at 0. Therefore, in the string "cats", the first letter, "c", is at the 0th index and the last letter, "s", is at the 3rd index.

##### Instructions

On line 13, assign the variable `fifth_letter` equal to the fifth letter of the string "MONTY".

Remember that the fifth letter is not at index 5. Start counting your indices from zero.

```Python
#GIVEN
"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter =

print fifth_letter

# SOLUTION
fifth_letter = "MONTY"[4]

print(fifth_letter)
```


### 2.1.5. String methods
Great work! Now that we know how to store strings, let's see how we can change them using string methods.

String methods let you perform specific tasks for strings.

We'll focus on four string methods:

* `len()`
* `lower()`
* `upper()`
* `str()`

Let's start with `len()`, which gets the length (the number of characters) of a string!


##### Instructions

On line 1, create a variable named `parrot` and set it to the string "Norwegian Blue".

On line 2, type `len(parrot)` after the word `print`, like so: `print len(parrot)`. The output will be the number of characters in "Norwegian Blue"!

```Python
#GIVEN
print

# SOLUTION
parrot = "Norwegian Blue"
print(len(parrot))
# Output : 14
```



### 2.1.6. `lower()`
You can use the `lower()` method to get rid of all the capitalization in your strings. You call `lower()` like so:

```python
"Ryan".lower()
```
which will return `"ryan`".


##### Instructions

Call `lower()` on `parrot` (after print) on line 3 in the editor.

```Python
#GIVEN
parrot = "Norwegian Blue"
print

# SOLUTION
parrot = "Norwegian Blue"
print(parrot.lower())
# Output : norwegian blue
```


### 2.1.7. `upper()`
Now your string is 100% lower case! A similar method exists to make a string completely upper case.


##### Instructions

Call `upper()` on `parrot` (after print on line 3) in order to capitalize all the characters in the string!

```Python
#GIVEN
parrot = "norwegian blue"

print

# SOLUTION
parrot = "Norwegian Blue"
print(parrot.upper())
# Output : NORWEGIAN BLUE
```

### 2.1.8. `str()`
Now let's look at `str()`, which is a little less straightforward. The `str()` method turns non-strings into strings! For example:

```python
str(2)
```
would turn `2` into `"2"`.


##### Instructions

Create a variable `pi` and set it to 3.14 on line 4.

Call `str(pi)` on line 5, after `print`.

```Python
#GIVEN
"""Declare and assign your variable on line 4,
then call your method on line 5!"""

print

# SOLUTION
pi = 3.14
print(str(pi))
# Output : 3.14
```

### 2.1.9. Dot Notation
Let's take a closer look at why you use `len(string)` and `str(object)`, but dot notation (such as `"String".upper())` for the rest.

```python
lion = "roar"
len(lion)
lion.upper()
```
Methods that use dot notation only work with strings.
On the other hand, `len()` and `str()` can work on other data types.


##### Instructions

On line 3, call the `len()` function with the argument `ministry`.

On line 4, invoke the `ministry`'s `.upper()` function.

```Python
#GIVEN
ministry = "The Ministry of Silly Walks"

print
print

# SOLUTION
ministry = "The Ministry of Silly Walks"
print(len(ministry))
print(ministry.upper())
# Outputs :
# 27
# THE MINISTRY OF SILLY WALKS
```


### 2.1.10. Printing Strings
The area where we've been writing our code is called the **editor**.

The **console** (the window to the right of the editor) is where the results of your code is shown.

`print` simply displays your code in the console.


##### Instructions

Print "Monty Python" to the console.

```Python
print("Monty Python")
# Output : Monty Python
```


### 2.1.11. Printing Variables
Great! Now that we've printed strings, let's print variables


##### Instructions

Declare a variable called `the_machine_goes` and assign it the string value `"Ping!"` on line 5.

Go ahead and print `the_machine_goes` in line 6.

```Python
the_machine_goes = "Ping!"
print(the_machine_goes)
# Output : Ping!
```


### 2.1.12. String Concatenation
You know about strings, and you know about arithmetic operators. Now let's combine the two!

```python
print("Life " + "of " + "Brian")
```
This will print out the phrase `Life of Brian`.

The `+` operator between strings will 'add' them together, one after the other. Notice that there are spaces inside the quotation marks after `Life` and `of` so that we can make the combined string look like 3 words.

Combining strings together like this is called concatenation. Let's try concatenating a few strings together now!

##### Instructions

Let's give it a try. Print the concatenated strings `"Spam "`, `"and "`, `"eggs"` on line 3, just like the example above. Make sure you include the spaces at the end of `"Spam "` and `"and "`.


```Python
print("Spam " + "and " + "eggs")
# Output : Spam and eggs
```


### 2.1.13. Explicit String Conversion
Sometimes you need to combine a string with something that isn't a string. In order to do that, you have to convert the non-string into a string.

```python
print("I have " + str(2) + " coconuts!")
```
This will print `I have 2 coconuts!`.

The `str()` method converts non-strings into strings. In the above example, you convert the number `2` into a string and then you concatenate the strings together just like in the previous exercise.


##### Instructions

Run the code as-is. You get an error!

Use `str()` to turn 3.14 into a string. Then run the code again.


```Python
# GIVEN
print("The value of pi is around " + 3.14)

# SOLUTION
print("The value of pi is around " + str(3.14))
# Output : The value of pi is around 3.14
```


### 2.1.14. String Formatting with %, Part 1
When you want to print a variable with a string, there is a better method than concatenating strings together.

```python
name = "Mike"
print("Hello %s" % (name))
```
The `%` operator after the string is used to combine a string with variables. The `%` operator will replace the `%s` in the string with the string variable that comes after it.

If you'd like to print a variable that is an integer, you can "pad" it with zeros using `%02d`. The 0 means "pad with zeros", the 2 means to pad to 2 characters wide, and the d means the number is a signed integer (can be positive or negative).

```python
day = 6
print("03 - %s - 2019" %  (day))
# Output : 03 - 6 - 2019
print("03 - %02d - 2019" % (day))
# Output : 03 - 06 - 2019
```

##### Instructions

Take a look at the code in the editor. What do you think it'll do? Click Run when you think you know.


```Python
string_1 = "Camelot"
string_2 = "place"

print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))
# Output : Let's not go to Camelot. 'Tis a silly place.
```


### 2.1.15. String Formatting with %, Part 2
Remember, we used the `%` operator to replace the `%s` placeholders with the variables in parentheses.

```python
name = "Mike"
print("Hello %s" % (name))
```
You need the same number of `%s` terms in a string as the number of variables in parentheses:

```python
print("The %s who %s %s!" % ("Knights", "say", "Ni"))
#Output : The Knights who say Ni!
```

##### Instructions

Now it's your turn! We have `___` in the code to show you what you need to change!

1. Inside the string, replace the three `___` with `%s`.
2. After the string but before the three variables, replace the final `___` with a `%`.
3. Hit Run.
4. Answer the questions in the console as they pop up! Type in your answer and hit Enter.


```Python
# GIVEN
name = input("What is your name? ")
quest = input("What is your quest? ")
color = input("What is your favorite color? ")

print("Ah, so your name is ___, your quest is ___, " \
"and your favorite color is ___." ___ (name, quest, color))

# SOLUTION
print("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))
```

### 2.1.16. And Now, For Something Completely Familiar
Great job! You've learned a lot in this unit, including:

Three ways to create strings

```python
'Alpha'
"Bravo"
str(3)
```
String methods

```python
len("Charlie")
"Delta".upper()
"Echo".lower()
```

Printing a string

```python
print("Foxtrot")
```

Advanced printing techniques

```python
g = "Golf"
h = "Hotel"
print("%s, %s" % (g, h))
```

##### Instructions

Let's wrap it all up!

1. On line 3, create the variable `my_string` and set it to any string you'd like.
2. On line 4, use `len()` to print the length of `my_string`.
3. On line 5, print the `.upper()` case version of `my_string`.


```Python
my_string = "Learning code is fun!"
print(len(my_string))
print(my_string.upper())
# Output :
# 21
# LEARNING CODE IS FUN!
```

## Date And Time

### 2.2.1 The datetime Library
A lot of times you want to keep track of when something happened. We can do so in Python using `datetime`.

Here we'll use `datetime` to print the date and time in a nice format.

```python
from datetime import datetime
```

### 2.2.2 Getting the Current Date and Time
We can use a function called `datetime.now()` to retrieve the current date and time.

```python
from datetime import datetime
print(datetime.now())
# Output : 2019-01-02 08:09:32.934786
```
The first line imports the `datetime` library so that we can use it.

The second line will print out the current date and time.

##### Instructions

Create a variable called `now` and store the result of `datetime.now()` in it.

Then, print the value of `now`.


```Python
from datetime import datetime

now = datetime.now()
print(now)
# Output : 2019-01-02 05:10:49.099369
```

### 2.2.3 Extracting Information
Notice how the output looks like `2013-11-25 23:45:14.317454`. What if you don't want the entire date and time?

```python
from datetime import datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

print(now)
print(current_year)
print(current_month)
print(current_day)

# Output :
# 2019-01-02 08:13:43.496747
# 2019
# 1
# 2
```
You already have the first two lines.

In the third line, we take the year (and only the year) from the variable `now` and store it in `current_year`.

In the fourth and fifth lines, we store the month and day from `now`.

##### Instructions

On a new line, `print now.year`. Make sure you do it after setting the `now` variable!

Then, `print` out `now.month`.

Finally, `print` out `now.day`.


```Python
# GIVEN
from datetime import datetime
now = datetime.now()

# SOLUTION
from datetime import datetime
now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
# Output :
# 2019
# 1
# 2
```


### 2.2.4 Hot Date
What if we want to print today's date in the following format? `mm/dd/yyyy`. Let's use string substitution again!

```python
from datetime import datetime
now = datetime.now()

print('%02d-%02d-%04d' % (now.month, now.day, now.year))
# will print the current date as mm-dd-yyyy
```
Remember that the standalone `%` operator after the string will fill the `%02d` and `%04d` placeholders in the string on the left with the numbers and strings in the parentheses on the right.

`%02d` pads the month and day numbers with zeros to two places, and `%04d` pads the year to four places. This is one way dates are commonly displayed.

##### Instructions

Print the current date in the form of `mm/dd/yyyy`.

Change the string used above so that it uses a `/` character in between the `%02d` and `%04d` placeholders instead of a `-` character.


```Python
from datetime import datetime
now = datetime.now()

print('%02d/%02d/%04d' % (now.month, now.day, now.year))
# Output : 01/02/2019
```


### 2.2.5 Pretty Date
Nice work! Let's do the same for the hour, minute, and second.

```python
from datetime import datetime
now = datetime.now()

print(now.hour)
print(now.minute)
print(now.second)
```
In the above example, we just printed the current hour, then the current minute, then the current second.

We can again use the variable `now` to print the time.

##### Instructions

Similar to the last exercise, print the current time in the pretty form of `hh:mm:ss`.

1. Change the string that you are printing so that you have a `:` character in between the `%02d` placeholders.

2. Change the three things that you are printing from month, day, and year to `now.hour`, `now.minute`, and `now.second`.


```Python
# GIVEN
from datetime import datetime
now = datetime.now()

print('%02d-%02d-%04d' % (now.year, now.month, now.day))

# SOLUTION
print('%02d:%02d:%04d' % (now.hour, now.minute, now.second))
# Output : 08:28:0008
```


### 2.2.6 Grand Finale
We've managed to print the date and time separately in a very pretty fashion. Let's combine the two!

```python
from datetime import datetime
now = datetime.now()

print('%02d/%02d/%04d' % (now.month, now.day, now.year))
print('%02d:%02d:%02d' % (now.hour, now.minute, now.second))
```
The example above will print out the date, then on a separate line it will print the time.

Let's print them all on the same line in a single `print` statement!

##### Instructions

Print the date and time together in the form: `mm/dd/yyyy hh:mm:ss`.

To start, change the format string to the left of the `%` operator.

1. Ensure that it has five `%02d` and one `%04d` placeholder.
2. Put slashes and colons and a space between the placeholders so that they fit the format above.Then, change the variables in the parentheses to the right of the `%` operator.
3. Place the variables so that `now.month, now.day, now.year` are before `now.hour, now.minute, now.second`. Make sure that there is a `(` before the six placeholders and a `)` after them.


```Python
# GIVEN
from datetime import datetime
now = datetime.now()

print('%s:%s:%s' % (now.hour, now.minute, now.second))

# SOLUTION
print('%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
# Output : 01/02/2019 08:34:32
```

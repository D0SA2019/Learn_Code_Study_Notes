# 10. Advanced Topics in Python


### 10.1. Iterators for Dictionaries
Let's start with iterating over a dictionary. Recall that a dictionary is just a collection of keys and values.

```Python
d = {
	"Name": "Guidio",
	"Age": 56,
	"BDFL": True
}

print(d)
print(d.items())


# OUTPUT
{'Name': 'Guidio', 'Age': 56, 'BDFL': True}
dict_items([('Name', 'Guidio'), ('Age', 56), ('BDFL', True)])
```

Note that the `.items()` method doesn't return key/value pairs in any specific order.

##### Instructions
Create your own Python dictionary, `my_dict`, in the editor to the right with two or three key/value pairs.

Then `print` the result of calling the `my_dict.items()`


```Python
# SOLUTION
my_dict = {
	"Drink" : "Coffee",
	"Eat" : "Cake",
	"Think" : "Today's to-dos",
	"Learn" : "Python",
	"Develop" : "Project"
}

print(my_dict.items())


# OUTPUT
dict_items([('Drink', 'Coffee'), ('Eat', 'Cake'), ('Think', "Today's to-dos"), ('Learn', 'Python'), ('Develop', 'Project')])
```


### 10.2. keys() and values()
While `.items()` returns an array of *tuples* with each tuple consisting of a key/value pair from the dictionary:

* The `.keys()` method returns a list of the dictionary's keys, and
* The `.values()` method returns a list of the dictionary's values.

Again, these methods will not return the keys or values from the dictionary in any spesific order.

You can think of a tuple as an immutable (that is, unchangeable) list. Tuples are surrounded by `()`s and can contain any data type.  


##### Instructions
Remove your call to `.items()` and replace it with a call to `.keys()` and a call to `.values()`, each on its own line. Make sure to `print` both!


```Python
# GIVEN
my_dict = {
	"Drink" : "Coffee",
	"Eat" : "Cake",
	"Think" : "Today's to-dos",
	"Learn" : "Python",
	"Develop" : "Project"
}


# SOLUTION by adding
print(my_dict.keys())
print(my_dict.values())



# OUTPUT
dict_keys(['Drink', 'Eat', 'Think', 'Learn', 'Develop'])
dict_values(['Coffee', 'Cake', "Today's to-dos", 'Python', 'Project'])
```


### 10.3. The 'in' Operator
For iterating over lists, tuples, dictionaries and strings, Python also includes a special keyword : `in`. You can use `in` very `in`tuitively, like so:

```Python
for number in range(5):
	print(number, end=" ")


d = {
	"name": "Eric",
	"age": 26
}

for key in d:
	print(key, d[key], end=" ")

for letter in "Eric":
	print(letter, end=" ")


# OUTPUT
0 1 2 3 4 name Eric age 26 E r i c
```

1. In the example above, first we create and iterate through a range, printing out `0 1 2 3 4`. Note that the trailing comma ensures that we keep printing on the same line.
2. Next, we create a dictionary and iterate through, printing out `name Eric age 26`. Dicrionaries have no spesific order.
3. Finally, we iterate through the letters of a string, printing out `E r i c`.

##### Instructions

For each `key in my_dict:` `print` out the ley, then a space, then the value stored by that key. (You should use `print(a, b)` rather than `print(a + " " + b)`.)

```Python
# GIVEN
my_dict = {
	"Drink" : "Coffee",
	"Eat" : "Cake",
	"Think" : "Today's to-dos",
	"Learn" : "Python",
	"Develop" : "Project"
}

print(my_dict.keys())
print(my_dict.values())



# SOLUTION by adding to the end

for key in my_dict:
	print(key, my_dict[key])



# OUTPUT
Drink Coffee
Eat Cake
Think Today's to-dos
Learn Python
Develop Project
```


### 10.4. Building Lists

Let's say you wanted to build a list of the numbers from 0 to 50 (inclusive). We could do this pretty easily:

```Python
my_list = range(51)
print(my_list)

my_list = list(range(51))
print(my_list)


# OUTPUT
range(0, 51)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
```

But what if we wanted to generate a list according to some logic—for example, a list of all the even numbers from 0 to 50?

Python's answer to this is the **list comprehension**. List comprehensions are a powerful way to generate lists using the `for`/`in` and `if` keywords we've learned.

##### Instructions
Check out the list comprehension example in the editor. When you're pretty sure you know what it'll do, click Run to see it in action.


```Python
# GIVEN
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)


# OUTPUT
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
```


### 10.5. List Comprehension Syntax
Here's a simple example of list comprehension syntax:


```Python
new_list = [x for x in range(1,6)]
print(new_list)


# OUTPUT
[1, 2, 3, 4, 5]
```

This will create a `new_list` populated by the numbers one to five. If you want those numbers doubled, you could use:

```python
doubles = [x * 2 for x in range(1,6)]
print(doubles)


# OUTPUT
[2, 4, 6, 8, 10]
```

And if you only wanted the doubled numbers that are evenly divisible by three:

```python
doubles_by_3 = [x * 2 for x in range (1,6) if (x * 2) % 3 == 0]
print(doubles_by_3)


# OUTPUT
[6]
```

##### Instructions
Use a list comprehension to build a list called `even_squares` in the editor.

Your `even_squares` list should include the squares of the even numbers between 1 to 11. Your list should start `[4, 16, 36...]` and go from there.


```Python
# GIVEN
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = ________________________

print(even_squares)



# SOLUTION
even_squares = [x ** 2 for x in range (1,11) if (x ** 2) % 2 == 0]
print(even_squares)



# OUTPUT
4, 16, 36, 64, 100]
```


### 10.6. Now You Try!

Great work! Now it's time for you to create a list comprehension all on your own.

```Python
c = ['C' for x in range(5) if x < 3]
print(c)


# OUTPUT
['C', 'C', 'C']
```

The example above creates and prints out a list containing `['C', 'C', 'C']`.


##### Instructions
Use a list comprehension to create a list, `cubes_by_four`.

The comprehension should consist of the cubes of the numbers 1 through 10 only if the cube is evenly divisible by four.

Finally, `print` that list to the console.

Note that in this case, the cubed number should be evenly divisible by 4, not the original number.


```Python
# SOLUTION
cubes_by_four = [x ** 3 for x in range(1,11) if (x ** 3) % 4 == 0]
print(cubes_by_four)



# OUTPUT
[8, 64, 216, 512, 1000]
```


### 10.7. List Slicing Syntax
Sometimes we only want part of a Python list. Maybe we only want the first few elements; maybe we only want the last few. Maybe we want every other element!

List slicing allows us to access elements of a list in a concise manner. The syntax looks like this:

```Python
[start:end:stride]
```
Where `start` describes where the slice starts (inclusive), `end` is where it ends (exclusive), and `stride` describes the space between items in the sliced list. For example, a stride of `2` would select every other item from the original list to place in the sliced list.

##### Instructions
We've generated a list with a list comprehension in the editor to the right, and we're about to print a selection from the list using list slicing. Can you guess what will be printed out? Click Run when you think you know!


```Python
# GIVEN
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(l)
print(l[2:9:2])


# OUTPUT
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[9, 25, 49, 81]
```

### 10.8. Omitting Indices
If you don't pass a particular index to the list slice, Python will pick a default.


```Python
to_five = ['A', 'B', 'C', 'D', 'E']

print(to_five[3:])
print(to_five[:2])
print(to_five[::2])



# OUTPUT
['D', 'E']
['A', 'B']
['A', 'C', 'E']
```

1. The default starting index is `0`.
2. The default ending index is the end of the list.
3. The default stride is `1`.


##### Instructions
Use list slicing to `print` out every odd element of `my_list` from start to finish.

Omit the start and end index. You only need to specify a `stride`.

Check the Hint if you need help.


```Python
# GIVEN
my_list = range(1, 11) # List of numbers 1 - 10


# SOLUTION
my_list = list(range(1, 11))
print(my_list[::2])


# OUTPUT
[1, 3, 5, 7, 9]
```


### 10.9. Reversing a List
We have seen that a positive stride progresses through the list from left to right.

A *negative* stride progresses through the list from right to left.


```Python
letters = ['A', 'B', 'C', 'D', 'E']
print(letters[::-1])


# OUTPUT
['E', 'D', 'C', 'B', 'A']
```

##### Instructions
Create a variable called `backwards` and set it equal to the reversed version of `my_list`.

Make sure to reverse the list in the editor by passing your list slice a negative stride, like in the example above.


```Python
# GIVEN
my_list = range(1, 11)



# SOLUTION
my_list = list(range(1, 11))
backwards = my_list[::-1]

print(my_list)
print(backwards)



# OUTPUT
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```


### 10.10. Stride Length
A positive stride length traverses the list from left to right, and a negative one traverses the list from right to left.

Further, a stride length of 1 traverses the list "by ones," a stride length of 2 traverses the list "by twos," and so on.


##### Instructions
Create a variable, `backwards_by_tens`, and set it equal to the result of going backwards through `to_one_hundred` by tens. Go ahead and `print backwards_by_tens` to the console.


```Python
# GIVEN
to_one_hundred = range(101)



# SOLUTION
to_one_hundred = list(range(101))
backwards_by_tens = to_one_hundred[::-10]
print(backwards_by_tens)



# OUTPUT
[100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
```


### 10.11. Practice Makes Perfect
Great work! See? This list slicing business is pretty straightforward.

Let's do one more, just to prove you really know your stuff.


##### Instructions
Create a list, `to_21`, that's just the numbers from 1 to 21, inclusive.

Create a second list, `odds`, that contains only the odd numbers in the `to_21` list (1, 3, 5, and so on). Use list slicing for this one instead of a list comprehension.

Finally, create a third list, `middle_third`, that's equal to the middle third of `to_21`, from 8 to 14, inclusive.


```Python
# SOLUTION
to_21 = list(range(1,22))
odds = to_21[::2]
middle_third = to_21[7:14]

print(to_21)
print(odds)
print(middle_third)



# OUTPUT
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
[8, 9, 10, 11, 12, 13, 14]
```


### 10.12. Anonymous Functions
One of the more powerful aspects of Python is that it allows for a style of programming called **functional programming**, which means that you're allowed to pass functions around just as if they were variables or values. Sometimes we take this for granted, but not all languages allow this!

Check out the code at the right. See the `lambda` bit? Typing

```Python
lambda x: x % 3 == 0
```
Is the same as

```python
def by_three(x):
  return x % 3 == 0
```

Only we don't need to actually give the function a name; it does its work and returns a value without one. That's why the function the lambda creates is an *anonymous function*.

When we pass the lambda to `filter`, `filter` uses the lambda to determine what to filter, and the second argument (`my_list`, which is just the numbers 0 – 15) is the list it does the filtering on.

##### Instructions
Can you guess what the this code will print to the console? Click Run to see.



```Python
# GIVEN
my_list = range(16)
print(filter(lambda x: x % 3 == 0, my_list))



# SOLUTION
my_list = list(range(16))
filtered = list((filter(lambda x: x % 3 == 0, my_list)))
print(filtered)

# or
my_list = list(range(16))
print(list((filter(lambda x: x % 3 == 0, my_list))))



# OUTPUT
[0, 3, 6, 9, 12, 15]
```


### 10.13. Lambda Syntax
Lambda functions are defined using the following syntax:

```Python
my_list = list(range(16))
filter(lambda x: x % 3 == 0, my_list)
```

Lambdas are useful when you need a quick function to do some work for you.

If you plan on creating a function you'll use over and over, you're better off using `def` and giving that function a name.

##### Instructions
Fill in the first part of the `filter` function with a `lambda`. The `lambda` should ensure that only `"Python"` is returned by the `filter`.

Fill in the second part of the `filter` function with `languages`, the list to filter.


```Python
# GIVEN
languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print filter(_______, _______)



# SOLUTION
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(list(filter(lambda x: x == "Python", languages)))



# OUTPUT
['Python']
```


### 10.14. Try It!
All right! Time to test out `filter()` and `lambda` expressions.

```Python
cubes = [x ** 3 for x in range(1, 11)]
filter(lambda x: x % 3 == 0, cubes)
```
The example above is just a reminder of the syntax.


##### Instructions
Create a list, `squares`, that consists of the squares of the numbers 1 to 10. A list comprehension could be useful here!

Use `filter()` and a `lambda` expression to `print` out only the squares that are between 30 and 70 (inclusive).


```Python
# SOLUTION
squares = [x **2 for x in range(1,11)]
print(list(filter(lambda x: 30 <= x <= 70, squares)))


# OUTPUT
[36, 49, 64]
```


### 10.15. Iterating Over Dictionaries
First, let's review iterating over a `dict`.


##### Instructions

Call the appropriate method on `movies` such that it will `print` out all the *items* (hint, hint) in the dictionary—that is, each key and each value.


```Python
# GIVEN
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}


# SOLUTION by addint at the end
print(list(movies.items()))


# OUTPUT
[('Monty Python and the Holy Grail', 'Great'), ("Monty Python's Life of Brian", 'Good'), ("Monty Python's Meaning of Life", 'Okay')]
```


### 10.16. Comprehending Comprehensions
Good! Now let's take another look at list comprehensions.

```Python
squares = [x ** 2 for x in range(5)]
```

##### Instructions
Use a list comprehension to create a list, `threes_and_fives`, that consists only of the numbers between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.


```Python
# SOLUTION
threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
print(threes_and_fives)



# OUTPUT
[3, 5, 6, 9, 10, 12, 15]
```


### 10.17. List Slicing
Great! Next up: list slicing.

```Python
str = "ABCDEFGHIJ"
start, end, stride = 1, 6, 2
str[start:end:stride]
```
You can think of a Python string as a list of characters.

##### Instructions
The string in the editor is garbled in two ways:

1. Our message is backwards.
2. The letter we want is every other letter.

Use list slicing to extract the message and save it to a variable called `message`.


```Python
# GIVEN
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"



# SOLUTION
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]
print(message)


# OUTPUT
I am the secret message!
```

### 10.18. Lambda Expressions
Last but not least, let's look over some lambdas.

```Python
my_list = list(range(16))
filter(lambda x: x % 3 == 0, my_list)
```

We've given you another (slightly different) `garbled`. Sort it out with a `filter()` and a `lambda`.


##### Instructions
Create a new variable called `message`.

Set it to the result of calling `filter()` with the appropriate `lambda` that will filter out the `"X"`s. The second argument will be `garbled`.

Finally, `print` your `message` to the console.


```Python
# GIVEN
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"



# SOLUTION
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = "".join(filter(lambda x : x != "X", garbled))
print(message)



# OUTPUT
I am another secret message!
```

# 7. Lists and Functions

### 7.1. List accessing
This exercise goes over just pulling information from a list, which we've covered in a previous section!


##### Instructions

Please add the code to print out the second element in the list.

```Python
# GIVEN
n = [1, 3, 5]

# SOLUTION by add
print(n[1])

# OUTPUT
3
```



### 7.2. List element modification

You've already learned how to modify elements of a list in previous section. This exercise is just a recap of that!


##### Instructions
On line 3, multiply the second element of the `n` list by 5

Overwrite the second element with that result.

Make sure to print the list when you are done!


```Python
# GIVEN
n = [1, 3, 5]
print(n)


# SOLUTION
# long
n = [1, 3, 5]
second = n[1] * 5
n[1]=second
print(n)

# short
n = [1, 3, 5]
n[1] = n[1] * 5
print(n)

# OUTPUT
[1, 15, 5]
```

### 7.3. Appending to a list
Here, we'll quickly recap how to `.append()` elements to the end of a list.


##### Instructions

Append the number 4 to the end of the list `n`.

```Python
# GIVEN
n = [1, 3, 5]
print(n)


# SOLUTION
n = [1, 3, 5]
n.append(4)
print(n)


# OUTPUT
[1, 3, 5, 4]
```

### 7.4. Removing elements from lists
This exercise will expand on ways to remove items from a list. You can actually have a few options. For a list called `n` :

1. `n.pop(index)` will remove the item at `index` from the list and return it to you :

```python
n = [1, 3, 5]
n.pop(1)
print(n)


# Output
[1, 5]
```


2. `n.remove(item)` will remove the actual `item` şf şt finds it :

```python
n = [1, 3, 5]
n.remove(1)
print(n)


# Output
[3, 5]
```


3. `del(n[index])` is like `.pop(index)` in that it will remove the item at the given index, but it won't return it.

```python
n = [1, 3, 5]
del(n[1])
print(n)


# Output
[1, 5]
```

##### Instructions

Remove the first item from the list `n` using either `.pop()`, `.remove()` or `del()`


```Python
# GIVEN
n = [1, 3, 5]
print(n)


# SOLUTION
n = [1, 3, 5]
n.pop(0)
print(n)


# OUTPUT
[3, 5]
```


### 7.5. Changing the functionality of a function
In this exercise, you will just be making a minor change to a function to change what that function does.


##### Instructions
Change the function so the given argument is multiplied by 3 and returned.


```Python
# GIVEN
number = 5

def my_function(x):
  return x + 3

print(my_function(number))    # 8


# SOLUTION
number = 5

def my_function(x):
  return x * 3

print(my_function(number))


# OUTPUT
15
```


### 7.6. More than one argument
This exercise will recap how to use more than one argument in a function.


##### Instructions

Define a function called `add_function` that has 2 parameters `x` and `y` and adds them tıgether.


```Python
# GIVEN
m = 5
n = 13

print(add_function(m, n))


# SOLUTION
m = 5
n = 13

def add_function(x,y):
  return x + y

print(add_function(m, n))


# OUTPUT
18
```


### 7.7. Strings in functions
This is a basic recap on using strings in functions.


##### Instructions
Write a function called `string_function` that takes in a string argument (`s`) and then `return`s that argument concatenated with the word `'world'`. Don't add a space before `world`!


```Python
# GIVEN
n = "Hello"
print(string_function(n))


# SOLUTION
n = "Hello"

def string_function(s):
  return s + 'world'

print(string_function(n))


# OUTPUT
Helloworld
```


### 7.8. Passing a list to a function
You pass a list to a function the same way you pass any other argument to a function.



##### Instructions
Click Run to see that using a list as an argument in a function is essentially the same as using just a number or string!


```Python
# GIVEN
def list_function(x):
  return x

n = [3, 5, 7]
print(list_function(n))


# OUTPUT
[3, 5, 7]
```


### 7.9. Using an element from a list in a function

Passing a list to a function will store it in the argument (just like with a string or a number!)

```python
def first_item(items):
  print(items[0])

numbers = [2, 7, 9]
first_item(numbers)


# Output
2
```

1. In the example above, we define a function called `first_item`. It has one argument called `items`.
2. Inside the function, we `print` out the item stored at index zero of `items`.
3. After the function, we create a new list called `numbers`.
4. Finally, we call the `first_item` function with `numbers` as its argument, which prints out `2`.

##### Instructions
Change line 2 so that `list_function` returns only the item stored in index one of `x`, rather than the entire `x` list.


```Python
# GIVEN
def list_function(x):
  return x

n = [3, 5, 7]
print(list_function(n))


# SOLUTION
def list_function(x):
  return x[1]

n = [3, 5, 7]
print(list_function(n))


# OUTPUT
5
```


### 7.10. Modifying an element of a list in a function
Modifying an element in a list in a function is the same as if you were just modifying an element of a list outside a function.

```python
def double_first(n):
  n[0] = n[0] * 2

numbers = [1, 2, 3, 4]
double_first(numbers)
print(numbers)


# Output
[2, 2, 3, 4]
```
1. We create a list called `numbers`.
2. We use the `double_first` function to modify that list.
3. Finally, we print out [2, 2, 3, 4]


```python
# repeat element
numbers = [1, 2, 3, 4]
def repeat_first(n):
  return n.insert(n[0], n[0] * 1)

repeat_first(numbers)
print(numbers)

# Output
[1, 1, 2, 3, 4]
```

##### Instructions
Change `list_function` to :
* Add 3 to the item at index `1` of the list
* Store the result back into index `1`
* Return the list


```Python
# GIVEN
def list_function(x):
  return x[1]

n = [3, 5, 7]
print(list_function(n))



# SOLUTION
def list_function(x):
  x[1] = x[1] + 3
  return x

n = [3, 5, 7]
print(list_function(n))


# OUTPUT
[3, 8, 7]
```


### 7.11. List manipulation in functions
You can also append or delete items of a list inside a function just as if you were manipulating the list outside a function.

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)


# Output
[1, 2, 3, 4]
```
The example above is just a reminder of how to append items to a list.


##### Instructions
Define a function called `list_extender` that has one parameter `lst`.

Inside the function, append the number `9` to `lst`.

Then return the modified list.


```Python
# GIVEN
n = [3, 5, 7]
print(list_extender(n))


# SOLUTION
n = [3, 5, 7]

def list_extender(lst):
  lst.append(9)
  return lst

print(list_extender(n))


# OUTPUT
[3, 5, 7, 9]
```


### 7.12. Printing out a list item by item in a function
This exercise will go over how to utilize every element in a list in a function. You can use this existing code to complete the exercise and see how running this operatiion inside a function isn't much different from running this operation outside a function.


##### Instructions
Define a function called `print_list` that has one argument called `x`.

Inside that function, print out each element one by one. Use the existing code as a scaffold.

Then call your function with the argument `n`.


```Python
# GIVEN
n = [3, 5, 7]

for i in range(0, len(n)):
  print(n[i])


# SOLUTION
n = [3, 5, 7]

def print_list(x):
  for i in range(0, len(x)):
    print(x[i])

print_list(n)


# OUTPUT
3
5
7
```


### 7.13. Modifying each element in a list in a function
This exercise shows how to modify each element in a list. It is useful to do so in a function as you can easly put in a list of any lenght and get the same functionality. As you can see, `len(n)` is the enght of the list.


##### Instructions
Create a function called `double_list` that takes a single argument `x` (which will be a list) and multiplies each element by 2 and returns that list. Use the existing code as a scaffold.


```Python
# GIVEN
n = [3, 5, 7]

for i in range(0, len(n)):
  n[i] = n[i] * 2

print(double_list(n))



# SOLUTION
n = [3, 5, 7]

def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x

print(double_list(n))



# OUTPUT
[6, 10, 14]
```


### 7.14. Passing a range into a function
Okay! Range time. The Python `range()` function is just a shortcut for generating a list, so you can use ranges in all the same places you can use lists.


```python
range(6) # => [0, 1, 2, 3, 4, 5]
range(1, 6) # => [1, 2, 3, 4, 5]
range(1, 6, 3) # => [1, 4]
```
The `range` function has three different versions:

1. `range(stop)`
2. `range(start, stop)`
3. `range(start, stop, step)`

In all cases, the `range()` function returns a list of numbers from `start` up to (but not including) `stop`. Each item increases by `step`.

If omitted, `start` defaults to `0` and `step` defaults to `1`

##### Instructions
On line 6, replace the `____` with a `range()` that returns a list containing `[0, 1, 2]`


```Python
# GIVEN
def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print(my_function(____))



# SOLUTION
def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print(my_function(list(range(3))))



# OUTPUT
[0, 1, 2]
```


### 7.15. Iterating over a list in a function
Now that we've learned about `range`, we have two ways of iterating through a list.

**Method 1** - `for item in list:`

```python
for item in list:
  print(item)
```

**Method 2** -iterate through indexes:

```python
for i in range(len(list)):
  print(list[i])
```

Method 1 is useful to loop through the list but it's not possible to modify the list this way.

Method 2 uses indexes to loop though the list, making it possible to also modify the list if needed. Since we aren't modifying the list, feel free to use either one on this lesson!


##### Instructions

Create a function that returns the sum of a list of numbers.

* On line 3, define a function called `total` that accepts one argument called `numbers`. It will be a list.
* Inside the function, create a variable called `result` and set it to zero.
* Using one of the two methods above, iterate through the `numbers` list. For each number, add it to `result`.
* Finally `return result`.


```Python
# GIVEN
n = [3, 5, 7]



# SOLUTION
n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in numbers:
    result += i  
  return result

print(total(n))


# OUTPUT
15
```


### 7.16. Using strings in lists in functions
Now let's try working with strings!

```python
for item in list:
  print(item)

for i in range(len(list)):
  print(list[i])
```
The example above is just a reminder of the two methods for iterating over a list.


##### Instructions
Create a function that concatenates strings.

* Define a function called `join_strings` accepts an argument called `words`. It will be a list.
* Inside the function, create a variable called `result` and set it to `''`, an empty string.
* Iterate through the `words` list and concatenate each word to `result`.
* Finally, `return` the `result`

Don't add spaces between the joined strings!


```Python
# GIVEN
n = ["Michael", "Lieberman"]
print(join_strings(n))



# SOLUTION
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ""
  for word in words:
    result += word
  return result

print(join_strings(n))



# OUTPUT
MichaelLieberman
```


### 7.17. Using two lists as two arguments in a function
Using multiple lists in a function is no different from just using multiple arguments in a function!

```python
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)


# Output
[1, 2, 3, 4, 5, 6]
```
The example above is just a reminder of how to concatenate two lists.

##### Instructions

Create a function that joins two list together.

* On line 5, define a function called `join_lists` that has two arguments, `x` and `y`. They will bıth be lists.
* Inside that function, `return` the result of concatenating `x` and `y` together.


```Python
# GIVEN
m = [1, 2, 3]
n = [4, 5, 6]

print(join_lists(m, n))
# You want this to print [1, 2, 3, 4, 5, 6]



# SOLUTION
m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x,y):
  return x + y

print(join_lists(m, n))



# OUTPUT
[1, 2, 3, 4, 5, 6]
```


### 7.18. Using a list of lists in a function
Finally, this exercise shows how to make use of a single list that ccontains multiple lists and how to use them in a function.

```python
list_of_lists = [[1, 2, 3], [4, 5, 6]]

for lst in list_of_lists:
  for item in lst:
    print(item)
```
1. In the example above, we first create a list containing two items, each of which is a list of numbers.
2. Then, we iterate through out outer list.
3. For each of the two inner lists (as `lst`), we iterate through the numbers (as `item`) and print them out.

We end up printing out :

```
1
2
3
4
5
6
```


##### Instructions

Create a function called `flatten` that takes a single list and concatenates all the sublists that are part of it into a sinle list.

* On line 3, define a function called `flatten` with one argument called `lists`.
* Make a new, empty list calaled `results`.
* Iterate through `lists`. Call the looping variabe `numbers`.
* For each number, `.append()` it to `results`.
* Finally, `return results` from your function.


```Python
# GIVEN
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

print(flatten(n))



# SOLUTION
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
  results = list()
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results


print(flatten(n))


# OUTPUT
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

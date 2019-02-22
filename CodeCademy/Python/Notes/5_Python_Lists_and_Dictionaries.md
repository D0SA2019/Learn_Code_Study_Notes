# 5. Python Lists and Dictionaries
### 5.1. Introduction to Lists
Lists are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name. (Datatypes you've already learned about include strings, numbers, and booleans.)

You can assign items to a list with an expression of the form

```python
list_name = [item_1, item_2]
```
with the items in between brackets. A list can also be empty: `empty_list = []`.

Lists are very similar to strings, but there are a few key differences.

##### Instructions

The list `zoo_animals` has three items (check them out on line 1). Go ahead and add a fourth! Just enter the name of your favorite animal (as a "`string"`) on line 1, after the final comma but before the closing `]`.

```Python
#GIVEN
zoo_animals = ["pangolin", "cassowary", "sloth", ];
# One animal is missing!

if len(zoo_animals) > 3:
  print("The first animal at the zoo is the " + zoo_animals[0])
  print("The second animal at the zoo is the " + zoo_animals[1])
  print("The third animal at the zoo is the " + zoo_animals[2])
  print("The fourth animal at the zoo is the " + zoo_animals[3])


# SOLUTION
zoo_animals = ["pangolin", "cassowary", "sloth", "panda" ]

if len(zoo_animals) > 3:
  print("The first animal at the zoo is the " + zoo_animals[0])
  print("The second animal at the zoo is the " + zoo_animals[1])
  print("The third animal at the zoo is the " + zoo_animals[2])
  print("The fourth animal at the zoo is the " + zoo_animals[3])


# OUTPUT
The first animal at the zoo is the pangolin
The second animal at the zoo is the cassowary
The third animal at the zoo is the sloth
The fourth animal at the zoo is the panda
```


### 5.2. Access by Index

You can access an individual item on the list by its `index`. An index is like an address that identifies the item's place in the list. The index appears directly after the list name, in between brackets, like this: `list_name[index]`.

*List indices begin with 0, not 1!* You access the first item in a list like this: `list_name[0]`. The second item in a list is at index 1: `list_name[1]`. Computer scientists love to start counting from zero.



##### Instructions
Write a statement that prints the result of adding the second and fourth items of the list. Make sure to access the list by index!

```Python
#GIVEN
numbers = [5, 6, 7, 8]
print("Adding the numbers at indices 0 and 2...")
print(numbers[0] + numbers[2])
print("Adding the numbers at indices 1 and 3...")


# SOLUTION
numbers = [5, 6, 7, 8]
print("Adding the numbers at indices 0 and 2...")
print(numbers[0] + numbers[2])
print("Adding the numbers at indices 1 and 3...")
print(numbers[1] + numbers[3])


# OUTPUT
Adding the numbers at indices 0 and 2...
12
Adding the numbers at indices 1 and 3...
14
```


### 5.3. New Neighbors
A list index behaves like any other variable name! It can be used to access as well as assign values.

You saw how to access a list index like this:

```python
zoo_animals[0]
# Gets the value "pangolin"
```

You can see how assignment works on line 5:

```python
zoo_animals[2] = "hyena"
# Changes "sloth" to "hyena"
```

##### Instructions
Write an assignment statement that will replace the item that currently holds the value `"tiger"` with another animal (as a string). It can be any animal you like.


```Python
#GIVEN
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked
# the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!



# SOLUTION
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
print(zoo_animals)
zoo_animals[2] = "hyena"
print(zoo_animals)
zoo_animals[3] = "panda"
print(zoo_animals)



# OUTPUT
['pangolin', 'cassowary', 'sloth', 'tiger']
['pangolin', 'cassowary', 'hyena', 'tiger']
['pangolin', 'cassowary', 'hyena', 'panda']
```


### 5.4. Late Arrivals & List Length
A list doesn't have to have a fixed lenght. You can add items to the end of a list any time you like.

```python
letters = ["a", "b", "c"]
print(len(letters))
print(letters)
letters.append("d")
print(len(letters))
print(letters)

# Output
3
['a', 'b', 'c']
4
['a', 'b', 'c', 'd']
```

1. In the above example, we first create a list called `letters`.
2. Then, we add the string `"d"` to the end of the `letters` list.
3. Next, we print out `4`, the length of the `letters` list.
4. Finally, we print out `["a", "b", "c", "d"]`



##### Instructions
On lines 5,6, and 7, append three more items to the `suitcase` list, just like the second line of the example above. (Maybe bring a bathing suit?)

Then set `list_length` equal to the lenght of the suitcase list.


```Python
#GIVEN
suitcase = []
suitcase.append("sunglasses")

# Your code here!

list_length = ________ # Set this to the length of suitcase

print("There are %d items in the suitcase." % (list_length))
print(suitcase)



# SOLUTION
suitcase = []
suitcase.append("sunglasses")
suitcase.append("lotion")
suitcase.append("book")
suitcase.append("map")

list_length = len(suitcase)
print("There are %d items in the suitcase." % (list_length))
print(suitcase)


# OUTPUT
There are 4 items in the suitcase.
['sunglasses', 'lotion', 'book', 'map']
```


### 5.5. List Slicing
Sometimes, you only want to access a portion of a list. Consider the following code:

```python
letters = ["a", "b", "c", "d", "e"]
slice = letters[1:3]
print(slice)
print(letters)

# Output
['b', 'c']
['a', 'b', 'c', 'd', 'e']
```

What is this code doing?

First, we create a list called `letters`.

Then, we take a subsection of the list and store it in the `slice` list. We do this by defining the indices we want to include after the name of the list: `letters[1:3]`. In Python, when we specify a portion of a list in this manner, we include the element with the first index, `1`, but we exclude the element with the second index, `3`.

Next, we print out `slice`, which will print `["b", "c"]`. Remember, in Python indices always start at `0`, so the `1` element is actually `b`.

Finally, we print out `["a", "b", "c", "d", "e"]`, notice that we did not modify the original `letters` list.



##### Instructions
On line 7, create a list called `middle` containing only the two middle items from `suitcase`.

On line 10, create a ist called `last` made up only of the last two items from `suitcase`.


```Python
#GIVEN
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle =

# The last two items (index four and five)
last =  



# SOLUTION
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
first = suitcase[0:2]
middle = suitcase[2:4]
last =  suitcase [4:]
print(middle)
print(last)
print(suitcase)

# OUTPUT
['passport', 'laptop']
['suit', 'shoes']
['sunglasses', 'hat', 'passport', 'laptop', 'suit', 'shoes']
```


### 5.6. Slicing Lists and Strings
You can slice a string exactly like a list! In fact, you can think of strings as lists of characters: each character is a sequential item in the list, starting from index 0.

```python
my_list[:2]
# Grabs the first two items

my_list[3:]
# Grabs the fourth through last items
```

If your list slice includes the very first or last item in a list (or a string), the index for that item doesn't have to be included.



##### Instructions

Assign to `dog` a slice of `animals` from index 3 up until but not including index 6.

Assign to `frog` a slice of `animals` from index 6 until the end of the string.

```Python
#GIVEN
animals = "catdogfrog"
cat = animals[:3]
dog =
frog =


# SOLUTION
animals = "catdogfrog"
cat = animals[:3]
dog = animals[3:6]
frog = animals[6:]
print(cat)
print(dog)
print(frog)
print(animals)

# OUTPUT
cat
dog
frog
catdogfrog
```


### 5.7. Maintaining Order
Sometimes you need to search for an item in a list.

```python
animals = ["ant", "bat", "cat"]
print(animals.index("bat"))

# OUTPUT
1
```
1. First, we create a list called `animals` with three strings.
2. Then, we print the first index that contains the string `"bat"`, which will print `1`.

We can also `insert` items into a list.


```python
animals.insert(1, "dog")
print(animals)

# Output
['ant', 'dog', 'bat', 'cat']
```

1. We insert `"dog"` at index 1, which moves everything down by 1.
2. We print out `["ant", "dog", "bat", "cat"]`


##### Instructions
Use the `.index(item)` function to find the index of `"duck"`. Assign that result to a variable called `duck_index`.

Then, `.insert(index, item)` the string `"cobra"` at that index.


```Python
#GIVEN
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = # Use index() to find "duck"

# Your code here!

print(animals) # Observe what prints after the insert operation


# SOLUTION
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")
animals.insert(duck_index, "cobra")
print(animals)



# OUTPUT
['aardvark', 'badger', 'cobra', 'duck', 'emu', 'fennec fox']
```


### 5.8. For One and All
If you want to do something with every item in the list, you can use a `for` loop. If you've learned about `for` loops in JavaScripts, pay close attention! They're different in Python.

```python
for variable in list_name:
  # Do stuff
```

A variable name follows the `for` keyword; it will be assigned the value of each list item in turn.

Then in `list_name` designates `list_name` as the list the loop will work on. The line ends with a colon (`:`) and the indented code that follows it will be executed once per item in the list.



##### Instructions
Write a statement in the indented oart of the `part`-loop that prints a number equal to `2 * number` for every list item.


```Python
#GIVEN
my_list = [1,9,3,8,5,7]

for number in my_list:


# SOLUTION
my_list = [1,9,3,8,5,7]

for number in my_list:
  print(number * 2)



# OUTPUT
2
18
6
16
10
14
```


### 5.9. More with `for`
If your list is a jumbled mess, you may need to `sort()` it.

```python
animals = ["cat", "ant", "bat"]
animals.sort()

print(animals)
for animal in animals:
  print(animal)

# Output
['ant', 'bat', 'cat']
ant
bat
cat
```
1. First, we create a list called `animals` with three strings. The strings are not in alphabetical order.
2. Then, we sort `animals` into alphabetical order. Note that `.sort()` modifies the list rather than returning a new list.
3. Then, for each item in `animals`, we print that item out as `"ant", "bat", "cat"` on their own line each.



##### Instructions
Write a `for`-loop that iterates over `start_list` and `.append()`s each number squared (`x ** 2`) to `square_list`.

Then sort `square_list`


```Python
#GIVEN
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!

print(square_list)


# SOLUTION
start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
  square_list.append(number ** 2)

print(square_list)
square_list.sort()
print(square_list)


# OUTPUT
[25, 9, 1, 4, 16]
[1, 4, 9, 16, 25]
```



### 5.10. This Next Part is Key
A dictionary is similar to a ist, but you access values by looking up a *key* instead of an index. A key can be any string or number. Dictionaries are enclosed in curly braces, like so :

```python
d = {"key1" : 1, "key2" : 2, "key3" : 3}
```

This is a dictionary called `d` with three *key-value* pairs. The key `key1` points to the value `1`, `key2` to `2`, and so on.

Dictionaries are great for things like phone books (pairing a name with a phone number), login pages (pairing an e-mail adress with a username), and more!



##### Instructions

Print the values stored under the `"Sloath"` and `"Burmese Python"` *keys*. Accessing dictionary values by key is kust like accessing list values by index:

```python
residents["Puffin"] # Gets the value 104
```


```Python
#GIVEN
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print(residents['Puffin']) # Prints Puffin's room number
# Your code here!


# SOLUTION
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print(residents['Puffin'])
print(residents["Sloth"])
print(residents["Burmese Python"])

# OUTPUT
104
105
106
```


### 5.11. New Entries
Like Lists, Dictionaries are mutable. This means they can be changed after they are created. One advantage of this is that we can add new *key/value* pairs to the dictionary after it is created like so:

```python
dict_name[name_key] = new value
```

An empty pair of curl braces `{}` is an empty dictionary, just like an empty pair of `[]` is an empty list.

The lenght `len()` of a dictionary is the number of key-value pairs in it has. Each pair counts only once, even if the vaue is a ist. (That's right: you can put lists inside dictionaries!)


##### Instructions
Add at least three more key-value pairs to the `menu` variable, with the dish name (as a `"string"`) for the key and the price (a float or integer) as the value. Here's an example:

```python
menu["Spam"] = 2.50
```


```Python
#GIVEN
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print(menu['Chicken Alfredo'])

# Your code here: Add some dish-price pairs to menu!

print("There are " + str(len(menu)) + " items on the menu.")
print(menu)

# SOLUTION
menu = {}
menu['Chicken Alfredo'] = 14.50
print(menu['Chicken Alfredo'])

menu["Onion Soup"] = 6.70
menu["French Fries"] = 3.40
menu["Tiramisu"] = 7.50

print("There are " + str(len(menu)) + " items on the menu.")
print(menu)

# OUTPUT
14.5
There are 4 items on the menu.
{'Chicken Alfredo': 14.5, 'Onion Soup': 6.7, 'French Fries': 3.4, 'Tiramisu': 7.5}
```

### 5.12. Changing Your Mind
Because dictionaries are mutable, they can be changed in many ways. Items can be removed from a dictionary with the `del` command:

```python
del dict_name[key_name]
```
will remove the key `key_name` and its associated vaue from the dictionary.

A new value can be associated with a key by assigning a vaue to the key, like so:

```python
dict_name[key] = new_value
```


##### Instructions
Delete the `"Sloth"` and `"Bengal Tiger"` items from `zoo_animals` using `del`.

Set the value associated with `"Rockhopper Penguin"` to anything other than `"Arctic Exhibit"`.


```Python
#GIVEN
# key - animal_name : value - location
zoo_animals = { 'Unicorn' : 'Cotton Candy House', 'Sloth' : 'Rainforest Exhibit', 'Bengal Tiger' : 'Jungle House', 'Atlantic Puffin' : 'Arctic Exhibit', 'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
print(zoo_animals)



# SOLUTION
zoo_animals = { 'Unicorn' : 'Cotton Candy House', 'Sloth' : 'Rainforest Exhibit', 'Bengal Tiger' : 'Jungle House', 'Atlantic Puffin' : 'Arctic Exhibit', 'Rockhopper Penguin' : 'Arctic Exhibit'}

del zoo_animals['Unicorn']
del zoo_animals["Sloth"]
del zoo_animals["Bengal Tiger"]
zoo_animals["Rockhopper Penguin"] = "Desert Exhibit"

print(zoo_animals)

# OUTPUT
{'Atlantic Puffin': 'Arctic Exhibit', 'Rockhopper Penguin': 'Desert Exhibit'}
```





### 5.13. Remove a Few Things
Sometimes you need to remove somthing from a list.

```python
beatles = ["john", "paul", "george", "ringo", "stuart"]
beatles.remove("stuart")
print(beatles)

# Output
['john', 'paul', 'george', 'ringo']
```

1. We create a list called `beatles` with 5 strings.
2. Then, we remove the first item from `beatles` that matches the string `"stuart"` Note that `.remove(item)` does not return anything.
3. Finally, we print out that list just to see that `"stuart"` was actually removed.


##### Instructions

Remove `"dagger"` from the list of items stored in the `backpack` variable.


```Python
# GIVEN
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']

# SOLUTION
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove("dagger")
print(backpack)

# OUTPUT
['xylophone', 'tent', 'bread loaf']
```


### 5.14. It's Dangerous to Go Alone! Take This
Let's go over a few last notes about dictionaries.

```python
my_dict = {
  "fish" : ["c", "a", "r", "p"],
  "cash" : -4483,
  "luck" : "good"
}

print(my_dict["fish"][0])

# Output
c
```
1. In the example above, we created a dictionary that holds many types of values.
2. The key `"fish"` has a *list*, the key `"cash"` has an *int*, and the key `"luck"` has a *string*.
3. Finally, we print the letter `"c"`. When we access a value in the dictionary like `my_dict["fish"]`, we have direct access to that value (which happens to be a list). We can access the item at index `0` in the list stored by the key `"fish"`.


##### Instructions
Add a key to `inventory` called `pocket`

Set the value of `pocket` to be a list consisting of the strings `seashell`, `strange berry`, and `lint`

`.sort()` the items in the list stored under the `backpack` key

Then `.remove("dagger")` from the list of items stored under the `"backpack"` key

Add 50 to the number stored under the `"gold"` key


```python

```


```Python
#GIVEN
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here



# SOLUTION
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
inventory['pouch'].sort()
inventory["pocket"] = ["seashell", "strange berry", "lint"]
inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
inventory["gold"] += 50

print(inventory)

# OUTPUT
{'gold': 550, 'pouch': ['flint', 'gemstone', 'twine'], 'backpack': ['bedroll', 'bread loaf', 'xylophone'], 'burlap bag': ['apple', 'small ruby', 'three-toed sloth'], 'pocket': ['seashell', 'strange berry', 'lint']}
```


## A Day At The Supermarket

### 5.1. BeFOR We Begin
Before we begin our exercise, we should go over the Python `for` loop one more time. For now, we are only going to go over the `for` loop in terms of how it relates to *lists* and *dictionaries*. We'll explain more cool `for` loop uses in later courses.

`for` loops allow us to iterate through all of the elements in a list from the left-most (or zeroth element) to the right-most element. A sample loop would be structured as follows:

```python
a = ["list", "of", "some", "sort"]
for x in a:
  # Do something for every x
```

This loop will run all of the code in the indented block under the `for x in a:` statement. The item in the list that is currently being evaluated will be `x`. So running the following :

```python
for item in [1, 3, 21]:
  print(item)

# Output
1
3
21
```

The variable between `for` and `in` can be set to any variable name (currently `item`), but you should be careful to avoid using the word `list` as a variable, since that's a reserved word (that is, it means something special) in the Python language.

##### Instructions

Use a `for` loop to print out all of the elements in the list `names`.



```Python
#GIVEN
names = ["Adam","Alex","Mariah","Martine","Columbus"]


# SOLUTION
names = ["Adam","Alex","Mariah","Martine","Columbus"]

for name in names :
  print(name)


# OUTPUT
Adam
Alex
Mariah
Martine
Columbus
```


### 5.2. This is KEY!
You can also use a `for` loop ona dictionary to loop through its keys with the following:

```python
# A simple dictionary
d = {"foo" : "bar"}

for key in d:
  print(d[key])

# Output
bar
```
Note that dictionaries are *unordered*, meaning that any time you loop through a dictionary, you will go through every key, but you are not guaranteed to get tgem in any particular order.



##### Instructions
Use for a `for` loop to go through the `webster` dictionary and print out all of the definitions.



```Python
#GIVEN
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}



# SOLUTION
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}
for item in webster:
  print(webster[item])



# OUTPUT
A star of a popular children's cartoon show.
The sound a goat makes.
Goes on the floor.
A small amount
```




### 5.3. Control Flow and Looping
The blocks of code in a `for` loop can be as big or as small as they need to be.

While looping, you may want to perform different actions depending on the particular item in the list.

```python
numbers = [1, 3, 4, 7]
for number in numbers:
  if number > 6:
    print(number)
print("We printed 7.")


# Output
7
We printed 7.
```

1. In the above example, we create a list with 4 number in it.
2. Then we loop through the `numbers` list and store each item in the list in the variable `number`
3. On each loop, if `number` is greater than 6, we `print` it out. So we print `7`
4. Finally, we print out a sentence

Make sure to keep track of your indentation or you may get confused.



##### Instructions

Like step 2 above, loop through each item in the list called `a`.

Like step 3 above, `if` the number is even, `print` it out. You can test `if` the item `% 2 == 0` to help you out.


```Python
#GIVEN
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# SOLUTION
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for item in a :
  if item % 2 == 0:
    print(item)


# OUTPUT
0
2
4
6
8
10
12
```



### 5.4. Lists + Functions
Functions can also take *lists* as inputs and perform various operations on those lists.

```python
def count_small(numbers):
  total = 0
  for n in numbers:
    if n < 10:
      total = total + 1
  return total

lotto = [4, 8, 15, 16, 23, 42]
small = count_small(lotto)
print(small)

# Output
2
```

1. In the above example, we define a function `count_small` that has one parameter, `numbers`
2. We initialize a variable `total` that we can use in the `for` loop.
3. For each item `n` in `numbers`, if `n` is less than 10, we increment `total`.
4. After the `for` loop, we return `total`.
5. After the function definition, we create an array of numbers called `lotto`.
6. We call the `count_smal`l function, pass in `lotto`, and store the returned result in `small`.
7. Finally, we print out the returned result, which is `2` since only `4` and `8` are less than 10.


##### Instructions
Write a function that counts how many times the string `"fizz"` appears in a list.

* Write a function called `fizz_coun`t that takes a list `x` as input.
* Create a variable `count` to hold the ongoing count. Initialize it to zero.
* `for` each `item in x:`, `if` that item is equal to the string `"fizz"` then increment the `count` variable.
* After the loop, please `return` the `count` variable.

For example, `fizz_count(["fizz","cat","fizz"]`) should return 2.



```Python
# SOLUTION
def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count += 1
  return count

fizz_count(["fizz", "cat", "fizz"])
print(fizz_count(["fizz", "cat", "fizz"]))

# OUTPUT
2
```



### 5.5. String Looping
As we've mentioned, *string* are like lists with characters as elements. You can loop through strings the same way you loop through lists! While we won't ask you to that in this section, we've put an example in the editor of how looping through a string might work.


##### Instructions

Run the code to see string iteration in action.


```Python
#GIVEN
for letter in "Codecademy":
  print(letter)

# Empty lines to make the output pretty
print("")
print("")

word = "Programming is fun!"

for letter in word:
  # Only print out the letter i
  if letter == "i":
    print(letter)



# OUTPUT
C
o
d
e
c
a
d
e
m
y


i
i
```




### 5.6. Your Own Store
Okay—on to the core of our project.

Congratulations! You are now the proud owner of your very own Codecademy brand supermarket.

```python
animal_counts = {
  "ant": 3,
  "bear": 6,
  "crow": 2
}
```
In the example above, we create a new dictionary called `animal_counts` with three entries. One of the entries has the key `"ant"` and the value `3`.



##### Instructions
Create a new dictionary called `prices` using `{}` format like the example above.

Put these values in your `prices` dictionary, in between the `{}`:

```python
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
```
Yeah, this place is really expensive. (Your supermarket subsidizes the zoo from the last course.)


```Python
# SOLUTION
prices = {
  "banana": 4,
	"apple": 2,
	"orange": 1.5,
	"pear": 3
}

```



### 5.7. Investing in Stock
Good work! As a store manager, you’re also in charge of keeping track of your stock/inventory.


##### Instructions

Create a `stock` dictionary with the values below.

```Python
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
```


```Python
#GIVEN
prices = {
  "banana": 4,
	"apple": 2,
	"orange": 1.5,
	"pear": 3
}



# SOLUTION

prices = {
  "banana": 4,
	"apple": 2,
	"orange": 1.5,
	"pear": 3
}


stock = {
  "banana": 6,
	"apple": 0,
	"orange": 32,
	"pear": 15
}

```


### 5.8. Keeping Track of the Produce
Now that you have all of your product info, you should print out all of your inventory information.

```python
once  = {'a': 1, 'b': 2}
twice = {'a': 2, 'b': 4}
for key in once:
  print("Once: %s" % once[key])
  print("Twice: %s" % twice[key])
```

1. In the above example, we create two dictionaries, `once` and `twice`, that have the same keys.
2. Because we know that they have the same keys, we can loop through one dictionary and `print` values from both `once` and `twice`.


##### Instructions

Loop through each key in prices.

Like the example above, for each key, print out the key along with its price and stock information.

Print the answer in EXACTLY the following format:

```Python
apple
price: 2
stock: 0
```
Like the example above, because you know that the `prices` and `stock` dictionary have the same keys, you can access the `stock` dictionary while you are looping through `prices`.

When you're printing, make sure to use the syntax from the example above, with `%s`.

```Python
#GIVEN
prices = {
  "banana": 4,
	"apple": 2,
	"orange": 1.5,
	"pear": 3
}


stock = {
  "banana": 6,
	"apple": 0,
	"orange": 32,
	"pear": 15
}


# SOLUTION
prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for food in prices:
  print(food)
  print("price: %s" % prices[food])
  print("stock: %s" % stock[food])


# OUTPUT
banana
price: 4
stock: 6
apple
price: 2
stock: 0
orange
price: 1.5
stock: 32
pear
price: 3
stock: 15
```







### 5.9. Something of Value
For paperwork and accounting purposes, let's record the total value of your inventory. It's nice to know what we're worth!



##### Instructions

Let's determine how much money you would make if you sold all of your food.

* Create a variable called `total` and set it to zero.
* Loop through the `prices` dictionary.
* For each key in `prices`, multiply the number in `prices` by the number in `stock`. Print that value into the console and then add it to `total`.
* Finally, outside your loop, `print total`.


```Python
#GIVEN
prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

for key in prices:
  print(key)
  print("price: %s" % prices[key])
  print("stock: %s" % stock[key])



# SOLUTION
prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

total = 0
for key in prices:
  print(key)
  print("price: %s" % prices[key])
  print("stock: %s" % stock[key])
  total += prices[key] * stock[key]

print(total)


# OUTPUT
banana
price: 4
stock: 6
apple
price: 2
stock: 0
orange
price: 1.5
stock: 32
pear
price: 3
stock: 15
117.0
```



### 5.10. Shopping at the Market
Great work! Now we're going to take a step back from the management side and take a look through the eyes of the shopper.

In order for customers to order online, we are going to have to make a consumer interface. Don't worry: it's easier than it sounds!


##### Instructions

First, make a list called `groceries` with the values `"banana"`,`"orange"`, and `"apple"`.


```Python
# SOLUTION
groceries = ["banana", "orange", "apple"]

```





### 5.11. Making a Purchase
Good! Now you're going to need to know how much you’re paying for all of the items on your grocery list.

```python
def sum(numbers):
  total = 0
  for number in numbers:
    total += number
  return total

n = [1, 2, 5, 10, 13]
print(sum(n))
```

1. In the above example, we first define a function called `sum` with a parameter `numbers`.
2. We initialize the variable `total` which we will use as our running sum.
3. For each number in the list, we add that number to the running sum `total`.
4. At the end of the function, we return the running sum.
5. After the function, we create, `n`, a list of numbers.
6. Finally, we call the `sum(numbers)` function with the variable `n` and print the result.



##### Instructions

Define a function `compute_bill` that takes one argument `food` as input.

In the function, create a variable `total` with an initial value of zero.

For each item in the `food` list, add the price of that item to `total`.

Finally, `return` the `total`.

Ignore whether or not the item you're billing for is in stock.Note that your function should work for any food list.


```Python
#GIVEN
shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# SOLUTION
shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}


def compute_bill(food):
  total = 0
  for item in food:
    total += prices[item]
  return total

```



### 5.12. Stocking Out
Now you need your `compute_bill` function to take the stock/inventory of a particular item into account when computing the cost.

Ultimately, if an item isn't in stock, then it shouldn't be included in the total. You can't buy or sell what you don't have!




##### Instructions
Make the following changes to your `compute_bill` function:

While you loop through each item of `food`, only add the price of the item to `total` `if` the item's `stock` count is greater than zero.

`if` the item is in stock and after you add the price to the `total`, subtract one from the item's `stock` count.



```Python
#GIVEN
shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
def compute_bill(food):
  total = 0
  for item in food:
    total += prices[item]
  return total



# SOLUTION
shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0 :
      total += prices[item]
      stock[item] -=1
  return total


```


### 5.13. Let's Check Out!
Perfect! You've done a great job with lists and dictionaries in this project. You've practiced:

* Using `for` loops with lists and dictionaries
* Writing functions with loops, lists, and dictionaries
* Updating data in response to changes in the environment (for instance, decreasing the number of bananas in `stock` by 1 when you sell one).

Thanks for shopping at the Codecademy supermarket!



##### Instructions


Print your result and click Run to finish this course.


```Python
#GIVEN
shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0 :
      total += prices[item]
      stock[item] -=1
  return total
```

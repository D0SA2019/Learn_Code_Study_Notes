# Python Functions, Files, and Dictionaries
*Coursera | Python 3 Programming Specialization | Course 2*

## Week 5 : Sorting

### Sorting Basics
#### 5.1. Invoking `.sort` and `sorted`

When we first introduced lists, we noted the existence of a method sort. When invoked on a list, the order of items in the list is changed. If no optional parameters are specified, the items are arranged in whatever the natural ordering is for the item type. For example, if the items are all integers, then smaller numbers go earlier in the list. If the items are all strings, they are arranged in alphabetic order.

```python
L1 = [1, 7, 4, -2, 3]
L2 = ["Cherry", "Apple", "Blueberry"]

L1.sort()
print(L1)
L2.sort()
print(L2)
```

**Output**:

```
[-2, 1, 3, 4, 7]
['Apple', 'Blueberry', 'Cherry']
```

Note that the sort method does **not** return a sorted version of the list. In fact, it returns the value None. But the list itself has been modified. This kind of operation that works by having a side effect on the list can be quite confusing.

In this course, we will generally use an alternative way of sorting, the function `sorted` rather than the method `sort`. Because it is a function rather than a method, it is invoked on a list by passing the list as a parameter inside the parentheses, rather than putting the list before the period. More importantly, `sorted` does not change the original list. Instead, it returns a new list.

```python
L2 = ["Cherry", "Apple", "Blueberry"]

L3 = sorted(L2)
print(L3)
print(sorted(L2))
print(L2)

L2.sort()
print(L2)
print(L2.sort())
```

**Output**:

```
['Apple', 'Blueberry', 'Cherry']
['Apple', 'Blueberry', 'Cherry']
['Cherry', 'Apple', 'Blueberry']

['Apple', 'Blueberry', 'Cherry']
None
```

----
----


#### 5.2. Optional Reverse Parameter

The sorted function takes some optional parameters (see the Optional Parameters page). The first optional parameter is a key function, which will be described in the next section. The second optional parameter is a Boolean value which determines whether to sort the items in reverse order. By default, it is False, but if you set it to True, the list will be sorted in reverse order.

```python
L2 = ["Cherry", "Apple", "Blueberry"]
print(sorted(L2, reverse=True))
```

**Output**:

```
['Cherry', 'Blueberry', 'Apple']
```

**Note** : This is a situation where it is convenient to use the keyword mechanism for providing optional parameters. It is possible to provide the value True for the reverse parameter without naming that parameter, but then we would have to provide a value for the second parameter as well, rather than allowing the default parameter value to be used. We would have had to write `sorted(L2, None, True)`. That’s a lot harder for humans to read and understand.


----
----

**Check Your Understanding** :

**Q1** : Sort the list, `lst` from largest to smallest. Save this new list to the variable `lst_sorted`.

```python
# Given
lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]

# Solution
lst_sorted = sorted(lst, reverse=True)
print(lst)
print(lst_sorted)
```

**Output** :

```
[3, 5, 1, 6, 7, 2, 9, -2, 5]
[9, 7, 6, 5, 5, 3, 2, 1, -2]
```

-----


#### 5.3. Optional Key Parameter

If you want to sort things in some order other than the “natural” or its reverse, you can provide an additional parameter, the key parameter. For example, suppose you want to sort a list of numbers based on their absolute value, so that -4 comes after 3? Or suppose you have a dictionary with strings as the keys and numbers as the values. Instead of sorting them in alphabetic order based on the keys, you might like to sort them in order based on their values.

First, let’s see an example, and then we’ll dive into how it works.

First, let’s define a function absolute that takes a number and returns its absolute value. (Actually, python provides a built-in function `abs` that does this, but we are going to define our own, for reasons that will be explained in a minute.)

```python
L1 = [1, 7, 4, -2, 3]

def absolute(x):
	if x >= 0:
		return x
	else:
		return -x

print(absolute(3))
print(absolute(-119))

for y in L1:
	print(absolute(y))
```

**Output**:

```
3
119
1
7
4
2
3
```

Now, we can pass the absolute function to sorted in order to specify that we want the items sorted in order of their absolute value, rather than in order of their actual value.


```python
L1 = [1, 7, 4, -2, 3]

def absolute(x):
	if x >= 0:
		return x
	else:
		return -x

L2 = sorted(L1, key=absolute)
print(L2)

print(sorted(L1, reverse=True, key=absolute))
```

**Output**:

```
[1, -2, 3, 4, 7]
[7, 4, 3, -2, 1]
```

What’s really going on there? We’ve done something pretty strange. Before, all the values we have passed as parameters have been pretty easy to understand: numbers, strings, lists, Booleans, dictionaries. Here we have passed a function object: absolute is a variable name whose value is the function. When we pass that function object, it is not automatically invoked. Instead, it is just bound to the formal parameter key of the function sorted.

We are not going to look at the source code for the built-in function sorted. But if we did, we would find somewhere in its code a parameter named key with a default value of None. When a value is provided for that parameter in an invocation of the function sorted, it has to be a function. What the sorted function does is call that key function once for each item in the list that’s getting sorted. It associates the result returned by that function (the absolute function in our case) with the original value. Think of those associated values as being little post-it notes that decorate the original values. The value 4 has a post-it note that says 4 on it, but the value -2 has a post-it note that says 2 on it. Then the sorted function rearranges the original items in order of the values written on their associated post-it notes.

To illustrate that the absolute function is invoked once on each item, during the execution of sorted, I have added some print statements into the code.

```python
L1 = [1, 7, 4, -2, 3]

def absolute(x):
    print("--- figuring out what to write on the post-it note for " + str(x))
    if x >= 0:
        return x
    else:
        return -x

print("About to call sorted")
L2 = sorted(L1, key=absolute)
print("Finished execution of sorted")
print(L2)
```

**Output**:

```
About to call sorted
--- figuring out what to write on the post-it note for 1
--- figuring out what to write on the post-it note for 7
--- figuring out what to write on the post-it note for 4
--- figuring out what to write on the post-it note for -2
--- figuring out what to write on the post-it note for 3
Finished execution of sorted
[1, -2, 3, 4, 7]
```


Note that this code never explicitly calls the absolute function at all. It passes the absolute function as a parameter value to the sorted function. Inside the sorted function, whose code we haven’t seen, that function gets invoked.

**Note** : It is a little confusing that we are reusing the word key so many times. The name of the optional parameter is `key`. We will usually pass a parameter value using the keyword parameter passing mechanism. When we write `key=some_function` in the function invocation, the word key is there because it is the name of the parameter, specified in the definition of the sort function, not because we are using keyword-based parameter passing.


----
----

**Check Your Understanding** :

**Q1** : You will be sorting the following list by each element’s second letter a to z. Create a function to use when sorting that takes a string as input and return the second letter of that string and name it `second_let`. Create a variable called `func_sort` and assign the sorted list to it. Do not use lambda.

```python
# Given
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']


# Solution
def second_let(somestr):
	return somestr[1]

func_sort = sorted(ex_lst, key=second_let)
print(func_sort)
```

**Output** :

```
['dance', 'zebra', 'hi', 'how are you', 'apple', 'bye']
```

-----

**Q2** : Below, we have provided a list of strings called `nums`. Write a function called `last_char` that takes a string as input, and returns only its last character. Use this function to sort the list `nums` by the last digit of each number, from highest to lowest, and save this as a new list called `nums_sorted`.

```python
# Given
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char():

nums_sorted =



# Solution
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(astring):
	return astring[-1]

nums_sorted = sorted(nums, reverse=True, key=last_char)
print(nums_sorted)
```

**Output** :

```
['19', '14378', '8907', '16', '1005', '44', '33', '32', '871', '1450']
```

-----

**Q3** : Once again, sort the list `nums` based on the last digit of each number from highest to lowest. However, now you should do so by writing a lambda function. Save the new list as `nums_sorted_lambda`.

```python
# Given
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']


# Solution
nums_sorted_lambda = sorted(nums, reverse=True, key=lambda x: x[-1])
print(nums_sorted_lambda)
```

**Output** :

```
['19', '14378', '8907', '16', '1005', '44', '33', '32', '871', '1450']
```

-----


### Sorting Dictionaries, Breaking Ties

#### 5.4. Sorting A Dictionary's Keys

Previously, you have used a dictionary to accumulate counts, such as the frequencies of letters or words in a text. For example, the following code counts the frequencies of different numbers in the list.


```python
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}

for x in L:
	if x in d:
		d[x] = d[x] + 1
	else:
		d[x] = 1

print(d)

for x in d.keys():
	print("{} appears {} times".format(x, d[x]))
```

**Output**:

```
{'E': 2, 'F': 1, 'B': 2, 'A': 2, 'D': 4, 'I': 2, 'C': 1}
E appears 2 times
F appears 1 times
B appears 2 times
A appears 2 times
D appears 4 times
I appears 2 times
C appears 1 times
```


The dictionary’s keys are not sorted in any particular order. In fact, you may get a different order of output than someone else running the same code. We can force the results to be displayed in some fixed ordering, by sorting the keys.


```python
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}

for x in L:
	if x in d:
		d[x] += 1
	else:
		d[x] = 1

y = sorted(d.keys())

for k in y:
	print("{} appears {} times".format(k, d[k]))
```

**Output**:

```
A appears 2 times
B appears 2 times
C appears 1 times
D appears 4 times
E appears 2 times
F appears 1 times
I appears 2 times
```

With a dictionary that’s maintaining counts or some other kind of score, we might prefer to get the outputs sorted based on the count rather than based on the items. The standard way to do that in python is to sort based on a property of the key, in particular its value in the dictionary.

Here things get a little confusing because we have two different meaning of the word “key”. One meaning is a key in a dictionary. The other meaning is the parameter name for the function that you pass into the sorted function.

Remember that the key function always takes as input one item from the sequence and returns a property of the item. In our case, the items to be sorted are the dictionary’s keys, so each item is one key from the dictionary. To remind ourselves of that, we’ve named the parameter in tha lambda expression k. The property of key k that is supposed to be returned is its associated value in the dictionary. Hence, we have the lambda expression `lambda k: d[k]`.

```python
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}

for x in L:
	if x in d:
		d[x] += 1
	else:
		d[x] = 1

y = sorted(d.keys(), key=lambda k: d[k], reverse=True)

for k in y:
    print("{} appears {} times".format(k, d[k]))
```

**Output**:

```
D appears 4 times
E appears 2 times
B appears 2 times
A appears 2 times
I appears 2 times
F appears 1 times
C appears 1 times
```

Here’s a version of that using a named function.

```python
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

def g(k):
    return d[k]

y =(sorted(d.keys(), key=g, reverse=True))

for k in y:
    print("{} appears {} times".format(k, d[k]))
```

**Output**:

```
D appears 4 times
E appears 2 times
B appears 2 times
A appears 2 times
I appears 2 times
F appears 1 times
C appears 1 times
```

**Note** : When we sort the keys, passing a function with `key=lambda x: d[x]` does not specify to sort the keys of a dictionary. The lists of keys are passed as the first parameter value in the invocation of sort. The key parameter provides a function that says how to sort them.

An experienced programmer would probably not even separate out the sorting step. And they might take advantage of the fact that when you pass a dictionary to something that is expecting a list, its the same as passing the list of keys.

```python
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

for k in sorted(d, key=lambda k: d[k], reverse=True):
      print("{} appears {} times".format(k, d[k]))
```

**Output**:

```
D appears 4 times
E appears 2 times
B appears 2 times
A appears 2 times
I appears 2 times
F appears 1 times
C appears 1 times
```

Eventually, you will be able to read code like that and immediately know what it’s doing. For now, when you come across something confusing, like line 11, try breaking it down. The function `sorted` is invoked. Its first parameter value is a dictionary, which really means the keys of the dictionary. The third parameter, the key function, decorates the dictionary key with a post-it note containing that key’s value in dictionary d. The last parameter, True, says to sort in reverse order.

There is another way to sort dictionaries, by calling `.items()` to extract a sequence of (key, value) tuples, and then sorting that sequence of tuples. But it’s better to learn the pythonic way of doing it, sorting the dictionary keys using a key function that takes one key as input and looks up the value in the dictionary.

----
----

**Check Your Understanding** :

**Q1** : Which of the following will sort the keys of d in ascending order of their values (i.e., from lowest to highest)?

```python
L = [4, 5, 1, 0, 3, 8, 8, 2, 1, 0, 3, 3, 4, 3]

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

def g(k, d):
    return d[k]

ks = d.keys()
```

A. sorted(ks, key=g) <br>
B. sorted(ks, key=lambda x: g(x, d)) ✅ <br>
C. sorted(ks, key=lambda x: d[x]) ✅ <br>

-----

**Q2** : Sort the following dictionary based on the keys so that they are sorted a to z. Assign the resulting value to the variable `sorted_keys`.

```python
# Given
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

# Solution
sorted_keys = sorted(dictionary)
print(sorted_keys)
```

**Output** :

```
['Chairs', 'Firepit', 'Flowers', 'Grill', 'Lights', 'Trees']
```

-----


**Q3** : Below, we have provided the dictionary `groceries`, whose keys are grocery items, and values are the number of each item that you need to buy at the store. Sort the dictionary’s keys into alphabetical order, and save them as a list called `grocery_keys_sorted`.

```python
# Given
groceries = {'apples': 5,
							'pasta': 3,
							'carrots': 12,
							'orange juice': 2,
							'bananas': 8,
							'popcorn': 1,
							'salsa': 3,
							'cereal': 4,
							'coffee': 5,
							'granola bars': 15,
							'onions': 7,
							'rice': 1,
							'peanut butter': 2,
							'spinach': 9}


# Solution
grocery_keys_sorted = sorted(groceries)
print(grocery_keys_sorted)
```

**Output** :

```
['apples', 'bananas', 'carrots', 'cereal', 'coffee', 'granola bars', 'onions', 'orange juice', 'pasta', 'peanut butter', 'popcorn', 'rice', 'salsa', 'spinach']
```

-----

**Q4** : Sort the following dictionary’s keys based on the value from highest to lowest. Assign the resulting value to the variable `sorted_values`.

```python
# Given
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}



# Solution
sorted_values = sorted(dictionary, key=lambda k: dictionary[k], reverse=True)
print(sorted_values)
```

**Output** :

```
['Trees', 'Lights', 'Flowers', 'Chairs', 'Grill', 'Firepit']
```

-----


#### 5.5. Breaking Ties

What happens when two items are “tied” in the sort order? For example, suppose we sort a list of words by their lengths. Which five letter word will appear first?

The answer is that the python interpreter will sort the tied items in the same order they were in before the sorting.

What if we wanted to sort them by some other property, say alphabetically, when the words were the same length? Python allows us to specify multiple conditions when we perform a sort by returning a tuple from a key function.

First, let’s see how python sorts tuples. We’ve already seen that there’s a built-in sort order, if we don’t specify any key function. For numbers, it’s lowest to highest. For strings, it’s alphabetic order. For a sequence of tuples, the default sort order is based on the default sort order for the first elements of the tuples, with ties being broken by the second elements, and then third elements if necessary, etc. For example,


```python
tups = [('A', 3, 2),
        ('C', 1, 4),
        ('B', 3, 1),
        ('A', 2, 4),
        ('C', 1, 2)]

for tup in sorted(tups):
	print(tup)
```

**Output**:

```
('A', 2, 4)
('A', 3, 2)
('B', 3, 1)
('C', 1, 2)
('C', 1, 4)
```

In the code below, we are going to sort a list of fruit words first by their length, smallest to largest, and then alphabetically to break ties among words of the same length. To do that, we have the key function return a tuple whose first element is the length of the fruit’s name, and second element is the fruit name itself.


```python
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']

new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))

for fruit in new_order:
  print(fruit)
```

**Output**:

```
kiwi
pear
apple
mango
peach
papaya
blueberry
```

Here, each word is evaluated first on it’s length, then by its alphabetical order. Note that we could continue to specify other conditions by including more elements in the tuple.

What would happen though if we wanted to sort it by largest to smallest, and then by alphabetical order?

```python
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']

new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name), reverse=True)

for fruit in new_order:
  print(fruit)
```

**Output**:

```
blueberry
papaya
peach
mango
apple
pear
kiwi
```

Do you see a problem here? Not only does it sort the words from largest to smallest, but also in reverse alphabetical order! Can you think of any ways you can solve this issue?

One solution is to add a negative sign in front of `len(fruit_name)`, which will convert all positive numbers to negative, and all negative numbers to positive. As a result, the longest elements would be first and the shortest elements would be last.

```python
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']

new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))

for fruit in new_order:
  print(fruit)
```

**Output**:

```
blueberry
papaya
apple
mango
peach
kiwi
pear
```

We can use this for any numerical value that we want to sort, however this will not work for strings.


----
----

**Check Your Understanding** :

**Q1** : What will the sorted function sort by?

```python
weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

sorted_weather = sorted(weather, key=lambda w: (w, weather[w]['temp']))
```

A. first city name (alphabetically), then temperature (lowest to highest) ✅ <br>
B. first temperature (highest to lowest), then city name (alphabetically) <br>
C. first city name (alphabetically), then temperature (highest to lowest) <br>
D. first temperature (lowest to highest), then city name (alphabetically) <br>

-----

**Q2** : What how will the following data be sorted?

```python
weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

sorted_weather = sorted(weather, key=lambda w: (w, -weather[w]['temp']), reverse=True)
```

A. first city name (reverse alphabetically), then temperature (lowest to highest) ✅ <br>
B. first temperature (highest to lowest), then city name (alphabetically) <br>
C. first city name (reverse alphabetically), then temperature (highest to lowest) <br>
D. first temperature (lowest to highest), then city name (alphabetically) <br>
E. first city name (alphabetically), then temperature (lowest to highest) <br>


-----


#### 5.6. Way of the Programmer: When to Use a Lambda Expression

Though you can often use a lambda expression or a named function interchangeably when sorting, it’s generally best to use lambda expressions until the process is too complicated, and then a function should be used. For example, in the following examples, we’ll be sorting a dictionary’s keys by properties of its values. Each key is a state name and each value is a list of city names.

For our first sort order, we want to sort the states in order by the length of the first city name. Here, it’s pretty easy to compute that property. `states[state]` is the list of cities associated with a particular state. So If `state` is a list of city strings, `len(states[state][0])` is the length of the first city name. Thus, we can use a lambda expression:

```python
states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: len(states[state][0])))
```

**Output**:

```
['Washington', 'Minnesota', 'Michigan']
```

That’s already pushing the limits of complex a lambda expression can be before it’s reall hard to read (or debug).

For our second sort order, the property we want to sort by is the number of cities that begin with the letter ‘S’. The function defining this property is harder to express, requiring a filter and count accumulation pattern. So we are better off defining a separate, named function. Here, we’ve chosen to make a lambda expression that looks up the value associated with the particular state and pass that value to the named function s_cities_count. We could have passed just the key, but then the function would have to look up the value, and it would be a little confusing, from the code, to figure out what dictionary the key is supposed to be looked up in. Here, we’ve done the lookup right in the lambda expression, which makes it a little bit clearer that we’re just sorting the keys of the states dictionary based on a property of their values. It also makes it easier to reuse the counting function on other city lists, even if they aren’t embedded in that particular states dictionary.

```python
def s_cities_count(city_list):
  ct = 0
  for city in city_list:
    if city[0] == "S":
      ct += 1
  return ct


states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
            "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
            "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: s_cities_count(states[state])))
```

**Output**:

```
['Michigan', 'Washington', 'Minnesota']
```

At this point in the course, we don’t even know how to do such a filter and accumulation as part of a lambda expression. There is a way, using something called list comprehensions, but we haven’t covered that yet.

There will be other situations that are even more complicated than this. In some cases, they may be too complicated to solve with a lambda expression at all! You can always fall back on writing a named function when a lambda expression will be too complicated.


----
----

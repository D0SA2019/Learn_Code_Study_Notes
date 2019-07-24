# Data Collection and Processing with Python
*Coursera | Python 3 Programming Specialization | Course 3*

## Week 2 : Map, Filter, and List Comprehensions

### Map and Filter
#### 2.1. Map

We have frequently taken a list and produced another list from it that contains either a subset of the items or a transformed version of each item. When each item is transformed we say that the operation is a **mapping**, or just a **map** of the original list. When some items are omitted, we call it a **filter**.

Python provides built-in functions `map` and `filter`. Python also provides a new syntax, called **list comprehensions**, that lets you express a mapping and/or filtering operation. Just as with named functions and lambda expressions, some students seem to find it easier to think in terms of the map and filter functions, while other students find it easier to read and write list comprehensions. You’ll learn both ways; one may even help you understand the other. Most python programmers use list comprehensions, so make sure you learn to read those. In this course, you can choose to learn to write list comprehensions or to use map and filter, whichever you prefer. You should learn to read both list comprehensions and map/filter.

Other common accumulator patterns on lists aggregate all the values into a single value.

Map, and filter are commands that you would use in high-performance computing on big datasets.

---

You previously were introduced to accumulating a list by transforming each of the elements. Here we revisit that pattern.

The following function produces a new list with each item in the original list doubled. It is an example of a mapping, from the original list to a new list of the same length, where each element is doubled.

```python
def doubleStuff(a_list):
	"""Return a new list in which contains doubles of the elements in a_list. """
	new_list = []
	for value in a_list:
		new_elem = 2 * value
		new_list.append(new_elem)
	return new_list

things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)
```


**Output** :

```
[2, 5, 9]
[4, 10, 18]
```

The `doubleStuff` function is an example of the accumulator pattern, in particular the mapping pattern. On line 3, `new_list` is initialized. On line 5, the doubled value for the current item is produced and on line 6 it is appended to the list we’re accumulating. Line 7 executes after we’ve processed all the items in the original list: it returns the `new_list`. Once again, codelens helps us to see the actual references and objects as they are passed and returned.

This pattern of computation is so common that python offers a more general way to do mappings, the `map` function, that makes it more clear what the overall structure of the computation is. `map` takes two arguments, a function and a sequence. The function is the mapper that transforms items. It is automatically applied to each item in the sequence. You don’t have to initialize an accumulator or iterate with a for loop at all.

**Note** : Technically, in a proper Python 3 interpreter, the `map` function produces an “iterator”, which is like a list but produces the items as they are needed. Most places in Python where you can use a list (e.g., in a for loop) you can use an “iterator” as if it was actually a list. So you probably won’t ever notice the difference. If you ever really need a list, you can explicitly turn the output of map into a list: `list(map(...))`. In the runestone environment, `map` actually returns a real list, but to make this code compatible with a full python environment, we always convert it to a list.

As we did when passing a function as a parameter to the `sorted` function, we can specify a function to pass to `map` either by referring to a function by name, or by providing a lambda expression.

```python
def triple(value):
	return 3*value

def tripleStuff(a_list):
	new_seq = map(triple, a_list)
	return list(new_seq)

def quadrupleStuff(a_list):
	new_seq = map(lambda value: 4*value, a_list)
	return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)

things4 = quadrupleStuff(things)
print(things4)
```


**Output** :

```
[6, 15, 27]
[8, 20, 36]
```

Of course, once we get used to using the `map` function, it’s no longer necessary to define functions like `tripleStuff` and `quadrupleStuff`.

```python
things = [2, 5, 9]

things4 = list(map(lambda value: 4*value, things))
print(things4)

print(list(map(lambda value: 5*value, [1, 2, 3])))
```


**Output** :

```
[8, 20, 36]
[5, 10, 15]
```

-------
--------

**Check Your Understanding**

**Q1** : Using map, create a list assigned to the variable `greeting_doubled` that doubles each element in the list `lst`.

```python
# Given
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]


# Solution
greeting_doubled = list(map(lambda x: x*2, lst))
print(greeting_doubled)
```

**Output** :

```
[['hi', 'bye', 'hi', 'bye'], 'hellohello', 'goodbyegoodbye', [9, 2, 9, 2], 8]
```

------


**Q2** : Below, we have provided a list of strings called `abbrevs`. Use map to produce a new list called `abbrevs_upper` that contains all the same strings in upper case.

```python
# Given
abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]



# Solution
abbrevs_upper = list(map(lambda x: x.upper(), abbrevs))
print(abbrevs_upper)
```

**Output** :

```
['USA', 'ESP', 'CHN', 'JPN', 'MEX', 'CAN', 'RUS', 'RSA', 'JAM']
```

------

#### 2.2. Filter

Now consider another common pattern: going through a list and keeping only those items that meet certain criteria. This is called a filter.

```python
def keep_evens(nums):
	new_list = []
	for num in nums:
		if num % 2 == 0:
			new_list.append(num)
	return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))
```


**Output** :

```
[4, 6, 0]
```

Again, this pattern of computation is so common that Python offers a more compact and general way to do it, the `filter` function. `filter` takes two arguments, a function and a sequence. The function takes one item and return True if the item should. It is automatically called for each item in the sequence. You don’t have to initialize an accumulator or iterate with a for loop.

```python
def keep_evens(nums):
	new_seq = filter(lambda num: num % 2 == 0, nums)
	return list(new_seq)

print(keep_evens([3, 4, 6, 7, 0, 1]))
```


**Output** :

```
[4, 6, 0]
```

-------
--------

**Check Your Understanding**

**Q1** : Write code to assign to the variable `filter_testing` all the elements in `lst_check` that have a w in them using filter.

```python
# Given
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']



# Solution
filter_testing = list(filter(lambda x: "w" in x, lst_check))
print(filter_testing)
```

**Output** :

```
['watermelon', 'kiwi', 'strawberries']
```

------

**Q2** : Using filter, filter `lst` so that it only contains words containing the letter “o”. Assign to variable `lst2`. Do not hardcode this.

```python
# Given
lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]


# Solution
lst2 = list(filter(lambda x: "o" in x, lst))
print(lst2)
```

**Output** :

```
['halloween', 'wagon', 'moon']
```

------



### List Comprehensions

#### 2.3. List Comprehensions

Python provides an alternative way to do `map` and `filter` operations, called a **list comprehension**. Many programmers find them easier to understand and write. List comprehensions are concise ways to create lists from other lists. The general syntax is:


```python
[<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]
```

where the if clause is optional. For example,

```python
things = [2, 5, 9]
yourlist = [value * 2 for value in things]
print(yourlist)
```

**Output** :

```
[4, 10, 18]
```

The transformer expression is `value * 2`. The item variable is `value` and the sequence is `things`. This is an alternative way to perform a mapping operation. As with `map`, each item in the sequence is transformed into an item in the new list. Instead of the iteration happening automatically, however, we have adopted the syntax of the for loop which may make it easier to understand.

Just as in a regular for loop, the part of the statement `for value in things` says to execute some code once for each item in things. Each time that code is executed, `value` is bound to one item from `things`. The code that is executed each time is the transformer expression, `value * 2`, rather than a block of code indented underneath the for statement. The other difference from a regular for loop is that each time the expression is evaluated, the resulting value is appended to a list. That happens automatically, without the programmer explicitly initializing an empty list or appending each item.

The `if` clause of a list comprehension can be used to do a filter operation. To perform a pure filter operation, the expression can be simply the variable that is bound to each item. For example, the following list comprehension will keep only the even numbers from the original list.

```python
def keep_evens(nums):
	new_list = [num for num in nums if num % 2 == 0]
	return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))
```

**Output** :

```
[4, 6, 0]
```

You can also combine `map` and `filter` operations by chaining them together, or with a single list comprehension.


```python
things = [3, 4, 6, 7, 0, 1]

print(list(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things))))
print([x * 2 for x in things if x % 2 == 0])
```

**Output** :

```
[8, 12, 0]
[8, 12, 0]
```

-------
--------

**Check Your Understanding**

**Q1** : What is printed by the following statements?

```python
alist = [4,2,8,6,5]
blist = [num*2 for num in alist if num%2==1]
print(blist)
```

A. [4,2,8,6,5]  <br>
B. [8,4,16,12,10]  <br>
C. 10  <br>
D. [10]  ✅ <br>

------

**Q2** : The for loop below produces a list of numbers greater than 10. Below the given code, use list comprehension to accomplish the same thing. Assign it the the variable `lst2`. Only one line of code is needed.

```python
# Given
L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)


# Solution
lst2 = [x for x in L if x > 10]
print(lst2)
```


**Output** :

```
[12, 34, 21, 42]
[12, 34, 21, 42]
```

------

**Q3** : Write code to assign to the variable `compri` all the values of the key `name` in any of the sub-dictionaries in the dictionary `tester`. Do this using a list comprehension.

```python
# Given
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},
									{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'},
									{'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'},
									{'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'},
									{'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'},
									{'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}


# Solution
compri = [x["name"] for x in tester["info"]]
print(compri)
```


**Output** :

```
['Lauren', 'Ayo', 'Kathryn', 'Nick', 'Gladys', 'Adam']
```

------


### Zip

#### 2.4. Zip

One more common pattern with lists, besides accumulation, is to step through a pair of lists (or several lists), doing something with all of the first items, then something with all of the second items, and so on. For example, given two lists of numbers, you might like to add them up pairwise, taking [3, 4, 5] and [1, 2, 3] to yield [4, 6, 8].

One way to do that with a for loop is to loop through the possible index values.


```python
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []

for i in range(len(L1)):
	L3.append(L1[i] + L2[i])

print(L3)
```

**Output** :

```
[4, 6, 8]
```

You have seen this idea previously for iterating through the items in a single list. In many other programming languages that’s really the only way to iterate through the items in a list. In Python, however, we have gotten used to the for loop where the iteration variable is bound successively to each item in the list, rather than just to a number that’s used as a position or index into the list.

Can’t we do something similar with pairs of lists? It turns out we can.

The `zip` function takes multiple lists and turns them into a list of tuples (actually, an iterator, but they work like lists for most practical purposes), pairing up all the first items as one tuple, all the second items as a tuple, and so on. Then we can iterate through those tuples, and perform some operation on all the first items, all the second items, and so on.

```python
L1 = [3, 4, 5]
L2 = [1, 2, 3]

L4 = list(zip(L1, L2))
print(L4)
```

**Output** :

```
[(3, 1), (4, 2), (5, 3)]
```

Here’s what happens when you loop through the tuples.

```python
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []
L4 = list(zip(L1, L2))

for (x1, x2) in L4:
	L3.append(x1 + x2)

print(L3)
```

**Output** :

```
[4, 6, 8]
```

Or, simplifying and using a list comprehension:

```python
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = [x1 + x2 for (x1,x2) in list(zip(L1,L2))]
print(L3)
```

**Output** :

```
[4, 6, 8]
```

Or, using `map` and not unpacking the tuple :


```python
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = list(map(lambda x: x[0] + x[1], zip(L1, L2)))
print(L3)
```

**Output** :

```
[4, 6, 8]
```

Consider a function called possible, which determines whether a word is still possible to play in a game of hangman, given the guesses that have been made and the current state of the blanked word.

Below we provide function that fulfills that purpose.



```python
def possible(word, blanked, guesses_made):
	if len(word) != len(blanked):
		return False

	for i in range(len(word)):
		bc = blanked[i]
		wc = word[i]
		if bc == "_" and wc in guesses_made:
			return False
		elif bc != "_" and bc!= wc:
			return False
	return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))
```

**Output** :

```
True
False
```

However, we can rewrite that using zip, to be a little more comprehensible.

```python
def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for (bc, wc) in zip(blanked, word):
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))
```

**Output** :

```
True
False
```

-------
--------

**Check Your Understanding**

**Q1** : Below we have provided two lists of numbers, `L1` and `L2`. Using zip and list comprehension, create a new list, `L3`, that sums the two numbers if the number from `L1` is greater than 10 and the number from `L2` is less than 5. This can be accomplished in one line of code.

```python
# Given
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]


# Solution
L3 = [(x+y) for (x,y) in list(zip(L1,L2)) if x>10 and y<5]
print(L3)
```

**Output** :

```
[18, 57, 103]
```


------

# Data Collection and Processing with Python
*Coursera | Python 3 Programming Specialization | Course 3*

## Week 1 : Nested Data and Nested Iteration

### Nested Data and Nested Iteration

#### 1.1. Nested Lists

The lists we have seen so far have had numbers or strings as items. We’ve snuck in a few more complex items, but without ever explicitly discussing what it meant to have more complex items.

In fact, the items in a list can be any type of python object. For example, we can have a list of lists.

```python
nested1 = [["a", "b", "c"], ["d", "e"], ["f", "g", "h"]]
print(nested1[0])
print(len(nested1))
print(len(nested1[1]))
nested1.append(["i"])
for L in nested1:
	print(L)
```


**Output** :

```
['a', 'b', 'c']
3
2
['a', 'b', 'c']
['d', 'e']
['f', 'g', 'h']
['i']
```

Line 2 prints out the first item from the list that `nested1` is bound to. That item is itself a list, so it prints out with square brackets. It has length 3, which prints out on line 3. Line 5 adds a new item to `nested1`. It is a list with one element, ‘i’ (it a list with one element, it’s not just the string ‘i’).

Codelens gives a you a reference diagram, a visual display of the contents of nested1.


When you get to step 5 of the execution, take a look at the object that variable nested1 points to. It is a list of three items, numbered 0, 1, and 2. The item in slot 1 is small enough that it is shown right there as a list containing items “d” and “e”. The item in slot 0 didn’t quite fit, so it is shown in the figure as a pointer to another separate list; same thing for the item in slot 2, the list `['f', 'g', 'h']`.

There’s no special meaning to whether the list is shown embedded or with a pointer to it: that’s just CodeLens making the best use of space that it can. In fact, if you go on to step 5, you’ll see that, with the addition of a fourth item, the list [‘i’], CodeLens has chosen to show all four lists embedded in the top-level list.

With a nested list, you can make complex expressions to get or set a value in a sub-list.

```python
nested1 = [["a", "b", "c"], ["d", "e"], ["f", "g", "h"]]
y = nested1[1]
print(y)
print(y[0])

print([10, 20, 30][1])
print(nested1[1][0])
```


**Output** :

```
['d', 'e']
d
20
d
```

Lines 1-4 above probably look pretty natural to you. Line 5 illustrates the left to right processing of expressions. `nested1[1]` evaluates to the second inner list, so `nested1[1][1]` evaluates to its second element, `'e'`. Line 6 is just a reminder that you index into a literal list, one that is written out, the same way as you can index into a list referred to by a variable. `[10, 20, 30]` creates a list. `[1]` indexes into that list, pulling out the second item, 20.

Just as with a function call where the return value can be thought of as replacing the text of the function call in an expression, you can evaluate an expression like that in line 7 from left to right. Because the value of `nested1[1]` is the list `['d', 'e']`, `nested1[1][0]` is the same as `['d', 'e'][0]`. So line 7 is equivalent to lines 2 and 4; it is a simpler way of pulling out the first item from the second list.

At first, expressions like that on line 7 may look foreign. They will soon feel more natural, and you will end up using them a lot. Once you are comfortable with them, the only time you will write code like lines 2-4 is when you aren’t quite sure what your data’s structure is, and so you need to incrementally write and debug your code. Often, you will start by writing code like lines 2-4, then, once you’re sure it’s working, replace it with something like line 7.

You can change values in such lists in the usual ways. You can even use complex expressions to change values. Consider the following

```python
nested1 = [["a", "b", "c"], ["d", "e"], ["f", "g", "h"], ["i"]]
print(nested1)
nested1[1] = [1, 2, 3]
print(nested1)
nested1[1][0] = 100
print(nested1)
```


**Output** :

```
[['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h'], ['i']]
[['a', 'b', 'c'], [1, 2, 3], ['f', 'g', 'h'], ['i']]
[['a', 'b', 'c'], [100, 2, 3], ['f', 'g', 'h'], ['i']]
```

The complex items in a list do not have to be lists. They can be tuples or dictionaries. The items in a list do not all have to be the same time, but you will drive yourself crazy if you have lists of objects of varying types. Save yourself some headaches and don’t do that. Here’s a list of dictionaries and some operations on them.

```python
nested2 = [{'a': 1, 'b': 3}, {'a': 5, 'c': 90, 5: 50}, {'b': 3, 'c': "yes"}]
print(nested2)
print(nested2[1])
print(nested2[1]["c"])
nested2[1]["c"] = 7
print(nested2[1])
print(nested2[2])
nested2[2]["c"] = "no"
print(nested2[2])
print(nested2)
```

**Output** :

```
[{'a': 1, 'b': 3}, {'a': 5, 'c': 90, 5: 50}, {'b': 3, 'c': 'yes'}]
{'a': 5, 'c': 90, 5: 50}
90
{'a': 5, 'c': 7, 5: 50}
{'b': 3, 'c': 'yes'}
{'b': 3, 'c': 'no'}
[{'a': 1, 'b': 3}, {'a': 5, 'c': 7, 5: 50}, {'b': 3, 'c': 'no'}]
```

You can even have a list of functions (!).

```python
def square(x):
	return x*x

L = [square, absi lambda x: x+1]

print("***names***")
for f in L:
	print(f)

print("***call each of them***")
for f in L:
	print(f(-2))

print("***just the first one in the list***")
print(L[0])
print(L[0](3))
```

**Output** :

```
***names***
<function square at 0x102479268>
<built-in function abs>
<function <lambda> at 0x10264cd90>
***call each of them***
4
2
-1
***just the first one in the list***
<function square at 0x102479268>
9
```

Here, `L` is a list with three items. All those items are functions. The first is the function square that is defined on lines 1 and 2. The second is the built-in python function abs. The third is an anonymous function that returns one more than its input.

In the first for loop, we do not call the functions, we just output their printed representations. The output `<function square>` confirms that square truly is a function object.

In the second for loop, we call each of the functions, passing in the value -2 each time and printing whatever value the function returns.

The last two lines just emphasize that there’s nothing special about lists of functions. They follow all the same rules for how python treats any other list. Because `L[0]` picks out the function square, `L[0](3)` calls the function square, passing it the parameter 3.

-------
--------

**Check Your Understanding**

**Q1** : Below, we have provided a list of lists. Use indexing to assign the element ‘horse’ to the variable name `idx1`.

```python
# Given
animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]


# Solution
idx1 = animals[1][0]
print(idx1)
```

**Output** :

```
horse
```

------


**Q2** : Using indexing, retrieve the string ‘willow’ from the list and assign that to the variable `plant`.

```python
# Given
data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]



# Solution
plant = data[7][0][0]
print(plant)
```

**Output** :

```
willow
```

------


#### 1.2. Nested Dictionaries


Just as lists can contain items of any type, the value associated with a key in a dictionary can also be an object of any type. In particular, it is often useful to have a list or a dictionary as a value in a dictionary. And of course, those lists or dictionaries can also contain lists and dictionaries. There can be many layers of nesting.

Only the values in dictionaries can be objects of arbitrary type. The keys in dictionaries must be one of the immutable data types (numbers, strings, tuples).



-------
--------

**Check Your Understanding**

**Q1** : Which of the following is a legal assignment statement, after the following code executes?

```python
d = {'key1': {'a': 5, 'c': 90, 5: 50}, 'key2':{'b': 3, 'c': "yes"}}
```

A. `d[5] = {1: 2, 3: 4}`  ✅ <br>
B. `d[{1:2, 3:4}] = 5`  <br>
C. `d['key1']['d'] = d['key2']`  <br>
D. `d[key2] = 3`  <br>

------

**Q1** : Extract the value associated with the key color and assign it to the variable `color`. Do not hard code this.

```python
# Given
info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }


# Solution
color = info["personal_data"]["physical_features"]["color"]
print(color)
```

**Output** :

```
{'eye': 'blue', 'hair': 'brown'}
```

------

#### 1.3. JSON Format and the JSON Module

JSON stands for JavaScript Object Notation. It looks a lot like the representation of nested dictionaries and lists in python when we write them out as literals in a program, but with a few small differences (e.g., the word null instead of None). When your program receives a JSON-formatted string, generally you will want to convert it into a python object, a list or a dictionary.

Again, python provides a module for doing this. The module is called json. We will be using two functions in this module, `loads` and `dumps`.

`json.loads()` takes a string as input and produces a python object (a dictionary or a list) as output.

Consider, for example, some data that we might get from Apple’s iTunes, in the JSON format:

```python
import json
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)

print("")

print(type(d))
print(d.keys())
print(d["resultCount"])
print(d)
```

**Output** :

```



{
 "resultCount":25,
 "results": [
{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}

<class 'dict'>
dict_keys(['resultCount', 'results'])
25
{'resultCount': 25, 'results': [{'wrapperType': 'track', 'kind': 'podcast', 'collectionId': 10892}]}
```

The other function we will use is `dumps`. It does the inverse of `loads`. It takes a python object, typically a dictionary or a list, and returns a string, in JSON format. It has a few other parameters. Two useful parameters are `sort_keys` and `indent`. When the value `True` is passed for the `sort_keys` parameter, the keys of dictionaries are output in alphabetic order with their values. The `indent` parameter expects an integer. When it is provided, dumps generates a string suitable for displaying to people, with newlines and indentation for nested lists or dictionaries. For example, the following function uses `json.dumps` to make a human-readable printout of a nested data structure.


```python
import json
def pretty(obj):
	return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, 5: 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print("")
print(pretty(d))
```

**Output** :

```
{'key1': {'c': True, 'a': 90, 5: 50}, 'key2': {'b': 3, 'c': 'yes'}}

{
  "key1": {
    "c": true,
    "a": 90,
    "5": 50
  },
  "key2": {
    "b": 3,
    "c": "yes"
  }
}
```

-------
--------

**Check Your Understanding**

**Q1** : Because we can only write strings into a file, if we wanted to convert a dictionary d into a json-formatted string so that we could store it in a file, what would we use?

A. json.loads(d) <br>
B. json.dumps(d) ✅ <br>
C. d.json() <br>


------

**Q2** : Say we had a JSON string in the following format. How would you convert it so that it is a python list?

```python
entertainment = """[{"Library Data": {"count": 3500, "rows": 10, "locations": 3}}, {"Movie Theater Data": {"count": 8, "rows": 25, "locations": 2}}]"""
```

A. entertainment.json() <br>
B. json.dumps(entertainment) <br>
C. json.loads(entertainment) ✅ <br>

------


### Nested Iteration

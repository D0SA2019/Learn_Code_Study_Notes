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

#### 1.4. Nested Iteration

When you have nested data structures, especially lists and/or dictionaries, you will frequently need nested for loops to traverse them.

```python
nested1 = [["a", "b", "c"], ["d", "e"], ["f", "g", "h"]]
for x in nested1:
	print("level1: ")
	for y in x:
		print("    level2: " + y)
```

**Output** :

```
level1:
    level2: a
    level2: b
    level2: c
level1:
    level2: d
    level2: e
level1:
    level2: f
    level2: g
    level2: h
```

Line 3 executes once for each top-level list, three times in all. With each sub-list, line 5 executes once for each item in the sub-list

-------
--------

**Check Your Understanding**

**Q1** : Now try rearranging these code fragments to make a function that counts all the *leaf* items in a nested list like nested1 above, the items at the lowest level of nesting (8 of them in nested1).

![](https://raw.githubusercontent.com/hevalhazalkurt/Learn_Code_Study_Notes/master/Coursera/Python3_Programming_Specialization/3_Data_Collection_and_Processing_with_Python/images/countleaves.png)

------

**Q2** : Below, we have provided a list of lists that contain information about people. Write code to create a new list that contains every person’s last name, and save that list as `last_names`.


```python
# Given
info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]



# Solution
last_names = []

for celeb in info:
	last_names.append(celeb[1])

print(last_names)
```

**Output** :

```
['Turner', 'Damon', 'Wiig', 'Phelps', 'Obama']
```

----

**Q3** : Below, we have provided a list of lists named `L`. Use nested iteration to save every string containing “b” into a new list named `b_strings`.


```python
# Given
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]




# Solution
b_strings = []

for lst in L:
	for item in lst:
		if "b" in item:
			b_strings.append(item)

print(b_strings)
```

**Output** :

```
['bananas', 'blueberries', 'cucumbers', 'green beans', 'root beer', 'cranberry juice']
```

----

#### 1.5. Structuring Nested Data

When constructing your own nested data, it is a good idea to keep the structure consistent across each level. For example, if you have a list of dictionaries, then each dictionary should have the same structure, meaning the same keys and the same type of value associated with a particular key in all the dictionaries. The reason for this is because any deviation in the structure that is used will require extra code to handle those special cases. The more the structure deviates, the more you will have to use special cases.

For example, let’s reconsider this nested iteration, but suppose not all the items in the outer list are lists.

```python
nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
	print("level1: ")
	for y in x:
		print("    level2: {}".format(y))
```

**Output** :

```
level1:
Traceback (most recent call last):
  File "Week1_Nested_Data_and_Nested_Iteration.py", line 180, in <module>
    for y in x:
TypeError: 'int' object is not iterable
```

Now the nested iteration fails.

We can solve this with special casing, a conditional that checks the type.

```python
nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
	print("level1")
	if type(x) is list:
		for y in x:
			print("     level2: {}".format(y))
	else:
		print(x)
```

**Output** :

```
level1
1
level1
2
level1
     level2: a
     level2: b
     level2: c
level1
     level2: d
     level2: e
level1
     level2: f
     level2: g
     level2: h
```

You can imagine how many special case if-thens we’d need, and how complicated the code would get, if we had many layers of nesting but not always a consistent structure.


-------
--------


#### 1.6. Deep and Shallow Copies

Earlier when we discussed cloning and aliasing lists we had mentioned that simply cloning a list using `[:]` would take care of any issues with having two lists unintentionally connected to each other. That was definitely true for making shallow copies (copying a list at the highest level), but as we get into nested data, and nested lists in particular, the rules become a bit more complicated. We can have second-level aliasing in these cases, which means we need to make deep copies.

When you copy a nested list, you do not also get copies of the internal lists. This means that if you perform a mutation operation on one of the original sublists, the copied version will also change. We can see this happen in the following nested list, which only has two levels.


```python
original = [["dogs", "puppies"], ["cats", "kittens"]]
copied_version = original[:]
print(copied_version)
print(copied_version is original)
print(copied_version == original)

original[0].append(["canines"])
print(original)
print("----Now look at the copied version----")
print(copied_version)
```

**Output** :

```
[['dogs', 'puppies'], ['cats', 'kittens']]
False
True
[['dogs', 'puppies', ['canines']], ['cats', 'kittens']]
----Now look at the copied version----
[['dogs', 'puppies', ['canines']], ['cats', 'kittens']]
```

Assuming that you don’t want to have aliased lists inside of your nested list, then you’ll need to perform nested iteration.


```python
original = [["dogs", "puppies"], ["cats", "kittens"]]
copied_outer_list = []

for inner_list in original:
	copied_inner_list = []
	for item in inner_list:
		copied_inner_list.append(item)
	copied_outer_list.append(copied_inner_list)

print(copied_outer_list)

original[0].append(["canines"])
print(original)
print("----Now look at the copied version----")
print(copied_outer_list)
```

**Output** :

```
[['dogs', 'puppies'], ['cats', 'kittens']]
[['dogs', 'puppies', ['canines']], ['cats', 'kittens']]
----Now look at the copied version----
[['dogs', 'puppies'], ['cats', 'kittens']]
```

Or, equivalently, you could take advantage of the slice operator to do the copying of the inner list.


```python
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
	copied_inner_list = inner_list[:]
	copied_outer_list.append(copied_inner_list)
print(copied_outer_list)

original[0].append(["canines"])
print(original)
print("----Now look at the copied version----")
print(copied_outer_list)
```

**Output** :

```
[['dogs', 'puppies'], ['cats', 'kittens']]
[['dogs', 'puppies', ['canines']], ['cats', 'kittens']]
----Now look at the copied version----
[['dogs', 'puppies'], ['cats', 'kittens']]
```

This process above works fine when there are only two layers or levels in a nested list. However, if we want to make a copy of a nested list that has more than two levels, then we recommend using the `copy` module. In the copy module there is a method called `deepcopy` that will take care of the operation for you.


```python
import copy
original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]

shallow_copy_version = original[:]
deeply_copied_version = copy.deepcopy(original)

original.append("Hi there")
original[0].append(["marsupials"])

print("---- Original ----")
print(original)
print("---- Depp copy ----")
print(deeply_copied_version)
print("---- Shallow copy -----")
print(shallow_copy_version)
```

**Output** :

```
[['canines', ['dogs', 'puppies'], ['marsupials']], ['felines', ['cats', 'kittens']], 'Hi there']
---- Depp copy ----
[['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
---- Shallow copy -----
[['canines', ['dogs', 'puppies'], ['marsupials']], ['felines', ['cats', 'kittens']]]
```

-------
--------

#### 1.7. Extracting from Nested Data

A common problem, especially when dealing with data returned from a web site, is to extract certain elements from deep inside a nested data structure. In principle, there’s nothing more difficult about pulling something out from deep inside a nested data structure: with lists, you use `[]` to index or a for loop to get them them all; with dictionaries, you get the value associated with a particular key using `[]` or iterate through all the keys, accessing the value for each. But it’s easy to get lost in the process and think you’ve extracted something different than you really have. Because of this, we have created a usable technique to help you during the debugging process.

Follow the system described below and you will have success with extracting nested data. The process involves the following steps:

1. Understand the nested data object.
2. Extract one object at the next level down.
3. Repeat the process with the extracted object

Understand. Extract. Repeat.

To illustrate this, we will walk through extracting information from data formatted in a way that it’s return by the Twitter API. This nested dictionary results from querying Twitter, asking for three tweets matching “University of Michigan”. As you’ll see, it’s quite a daunting data structure, even when printed with nice indentation as it’s shown below.

```python
res = {
  "search_metadata": {
    "count": 3,
    "completed_in": 0.015,
    "max_id_str": "536624519285583872",
    "since_id_str": "0",
    "next_results": "?max_id=536623674942439424&q=University%20of%20Michigan&count=3&include_entities=1",
    "refresh_url": "?since_id=536624519285583872&q=University%20of%20Michigan&include_entities=1",
    "since_id": 0,
    "query": "University+of+Michigan",
    "max_id": 536624519285583872
  },
  "statuses": [
    {
      "contributors": None,
      "truncated": False,
      "text": "RT @mikeweber25: I'm decommiting from the university of Michigan thank you Michigan for the love and support I'll remake my decision at the\u2026",
      "in_reply_to_status_id": None,
      "id": 536624519285583872,
      "favorite_count": 0,
      "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
      "retweeted": False,
      "coordinates": None,
      "entities": {
        "symbols": [],
        "user_mentions": [
          {
            "id": 1119996684,
            "indices": [
              3,
              15
            ],
            "id_str": "1119996684",
            "screen_name": "mikeweber25",
            "name": "Mikey"
          }
        ],
        "hashtags": [],
        "urls": []
      },
      "in_reply_to_screen_name": None,
      "in_reply_to_user_id": None,
      "retweet_count": 2014,
      "id_str": "536624519285583872",
      "favorited": False,
      "retweeted_status": {
        "contributors": None,
        "truncated": False,
        "text": "I'm decommiting from the university of Michigan thank you Michigan for the love and support I'll remake my decision at the army bowl",
        "in_reply_to_status_id": None,
        "id": 536300265616322560,
        "favorite_count": 1583,
        "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
        "retweeted": False,
        "coordinates": None,
        "entities": {
          "symbols": [],
          "user_mentions": [],
          "hashtags": [],
          "urls": []
        },
        "in_reply_to_screen_name": None,
        "in_reply_to_user_id": None,
        "retweet_count": 2014,
        "id_str": "536300265616322560",
        "favorited": False,
        "user": {
          "follow_request_sent": False,
          "profile_use_background_image": True,
          "profile_text_color": "666666",
          "default_profile_image": False,
          "id": 1119996684,
          "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme9/bg.gif",
          "verified": False,
          "profile_location": None,
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/534465900343083008/A09dIq1d_normal.jpeg",
          "profile_sidebar_fill_color": "252429",
          "entities": {
            "description": {
              "urls": []
            }
          },
          "followers_count": 5444,
          "profile_sidebar_border_color": "FFFFFF",
          "id_str": "1119996684",
          "profile_background_color": "C0DEED",
          "listed_count": 36,
          "is_translation_enabled": False,
          "utc_offset": None,
          "statuses_count": 6525,
          "description": "Mike Weber (U.S Army All American) DETROIT CTSENIOR State Champion",
          "friends_count": 693,
          "location": "",
          "profile_link_color": "0084B4",
          "profile_image_url": "http://pbs.twimg.com/profile_images/534465900343083008/A09dIq1d_normal.jpeg",
          "following": False,
          "geo_enabled": False,
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/1119996684/1416261575",
          "profile_background_image_url": "http://abs.twimg.com/images/themes/theme9/bg.gif",
          "name": "Mikey",
          "lang": "en",
          "profile_background_tile": False,
          "favourites_count": 1401,
          "screen_name": "mikeweber25",
          "notifications": False,
          "url": None,
          "created_at": "Fri Jan 25 18:45:53 +0000 2013",
          "contributors_enabled": False,
          "time_zone": None,
          "protected": False,
          "default_profile": False,
          "is_translator": False
        },
        "geo": None,
        "in_reply_to_user_id_str": None,
        "lang": "en",
        "created_at": "Sat Nov 22 23:28:41 +0000 2014",
        "in_reply_to_status_id_str": None,
        "place": None,
        "metadata": {
          "iso_language_code": "en",
          "result_type": "recent"
        }
      },
      "user": {
        "follow_request_sent": False,
        "profile_use_background_image": True,
        "profile_text_color": "333333",
        "default_profile_image": False,
        "id": 2435537208,
        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
        "verified": False,
        "profile_location": None,
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/532694075947110400/oZEP5XNQ_normal.jpeg",
        "profile_sidebar_fill_color": "DDEEF6",
        "entities": {
          "description": {
            "urls": []
          }
        },
        "followers_count": 161,
        "profile_sidebar_border_color": "C0DEED",
        "id_str": "2435537208",
        "profile_background_color": "C0DEED",
        "listed_count": 0,
        "is_translation_enabled": False,
        "utc_offset": None,
        "statuses_count": 524,
        "description": "Delasalle '17 Baseball & Football.",
        "friends_count": 255,
        "location": "",
        "profile_link_color": "0084B4",
        "profile_image_url": "http://pbs.twimg.com/profile_images/532694075947110400/oZEP5XNQ_normal.jpeg",
        "following": False,
        "geo_enabled": False,
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/2435537208/1406779364",
        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
        "name": "Andrew Brooks",
        "lang": "en",
        "profile_background_tile": False,
        "favourites_count": 555,
        "screen_name": "31brooks_",
        "notifications": False,
        "url": None,
        "created_at": "Wed Apr 09 14:34:41 +0000 2014",
        "contributors_enabled": False,
        "time_zone": None,
        "protected": False,
        "default_profile": True,
        "is_translator": False
      },
      "geo": None,
      "in_reply_to_user_id_str": None,
      "lang": "en",
      "created_at": "Sun Nov 23 20:57:10 +0000 2014",
      "in_reply_to_status_id_str": None,
      "place": None,
      "metadata": {
        "iso_language_code": "en",
        "result_type": "recent"
      }
    },
    {
      "contributors": None,
      "truncated": False,
      "text": "RT @Plantedd: The University of Michigan moved a big Bur Oak yesterday. 65ft tall. 350+ tons. http://t.co/v2Y6vl3f9e",
      "in_reply_to_status_id": None,
      "id": 536624216305848320,
      "favorite_count": 0,
      "source": "<a href=\"http://tapbots.com/tweetbot\" rel=\"nofollow\">Tweetbot for i\u039fS</a>",
      "retweeted": False,
      "coordinates": None,
      "entities": {
        "symbols": [],
        "user_mentions": [
          {
            "id": 462890283,
            "indices": [
              3,
              12
            ],
            "id_str": "462890283",
            "screen_name": "Plantedd",
            "name": "David Wong"
          }
        ],
        "hashtags": [],
        "urls": [],
        "media": [
          {
            "source_status_id_str": "526276522374889472",
            "expanded_url": "http://twitter.com/Plantedd/status/526276522374889472/photo/1",
            "display_url": "pic.twitter.com/v2Y6vl3f9e",
            "url": "http://t.co/v2Y6vl3f9e",
            "media_url_https": "https://pbs.twimg.com/media/B021tLsIYAADq21.jpg",
            "source_status_id": 526276522374889472,
            "id_str": "526276519308845056",
            "sizes": {
              "small": {
                "h": 191,
                "resize": "fit",
                "w": 340
              },
              "large": {
                "h": 576,
                "resize": "fit",
                "w": 1024
              },
              "medium": {
                "h": 337,
                "resize": "fit",
                "w": 600
              },
              "thumb": {
                "h": 150,
                "resize": "crop",
                "w": 150
              }
            },
            "indices": [
              94,
              116
            ],
            "type": "photo",
            "id": 526276519308845056,
            "media_url": "http://pbs.twimg.com/media/B021tLsIYAADq21.jpg"
          }
        ]
      },
      "in_reply_to_screen_name": None,
      "in_reply_to_user_id": None,
      "retweet_count": 27,
      "id_str": "536624216305848320",
      "favorited": False,
      "retweeted_status": {
        "contributors": None,
        "truncated": False,
        "text": "The University of Michigan moved a big Bur Oak yesterday. 65ft tall. 350+ tons. http://t.co/v2Y6vl3f9e",
        "in_reply_to_status_id": None,
        "id": 526276522374889472,
        "favorite_count": 25,
        "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
        "retweeted": False,
        "coordinates": None,
        "entities": {
          "symbols": [],
          "user_mentions": [],
          "hashtags": [],
          "urls": [],
          "media": [
            {
              "expanded_url": "http://twitter.com/Plantedd/status/526276522374889472/photo/1",
              "display_url": "pic.twitter.com/v2Y6vl3f9e",
              "url": "http://t.co/v2Y6vl3f9e",
              "media_url_https": "https://pbs.twimg.com/media/B021tLsIYAADq21.jpg",
              "id_str": "526276519308845056",
              "sizes": {
                "small": {
                  "h": 191,
                  "resize": "fit",
                  "w": 340
                },
                "large": {
                  "h": 576,
                  "resize": "fit",
                  "w": 1024
                },
                "medium": {
                  "h": 337,
                  "resize": "fit",
                  "w": 600
                },
                "thumb": {
                  "h": 150,
                  "resize": "crop",
                  "w": 150
                }
              },
              "indices": [
                80,
                102
              ],
              "type": "photo",
              "id": 526276519308845056,
              "media_url": "http://pbs.twimg.com/media/B021tLsIYAADq21.jpg"
            }
          ]
        },
        "in_reply_to_screen_name": None,
        "in_reply_to_user_id": None,
        "retweet_count": 27,
        "id_str": "526276522374889472",
        "favorited": False,
        "user": {
          "follow_request_sent": False,
          "profile_use_background_image": True,
          "profile_text_color": "333333",
          "default_profile_image": False,
          "id": 462890283,
          "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
          "verified": False,
          "profile_location": None,
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/1791926707/Plantedd_Logo__square__normal.jpg",
          "profile_sidebar_fill_color": "DDEEF6",
          "entities": {
            "url": {
              "urls": [
                {
                  "url": "http://t.co/ZOnsCHvoKt",
                  "indices": [
                    0,
                    22
                  ],
                  "expanded_url": "http://www.plantedd.com",
                  "display_url": "plantedd.com"
                }
              ]
            },
            "description": {
              "urls": []
            }
          },
          "followers_count": 2598,
          "profile_sidebar_border_color": "C0DEED",
          "id_str": "462890283",
          "profile_background_color": "C0DEED",
          "listed_count": 61,
          "is_translation_enabled": False,
          "utc_offset": 0,
          "statuses_count": 8157,
          "description": "Hello, I'm the supervillain behind Plantedd. We're an online market for plant lovers plotting to take over the world by making it simple to find and buy plants.",
          "friends_count": 2664,
          "location": "UK",
          "profile_link_color": "0084B4",
          "profile_image_url": "http://pbs.twimg.com/profile_images/1791926707/Plantedd_Logo__square__normal.jpg",
          "following": False,
          "geo_enabled": False,
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/462890283/1398254314",
          "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
          "name": "David Wong",
          "lang": "en",
          "profile_background_tile": False,
          "favourites_count": 371,
          "screen_name": "Plantedd",
          "notifications": False,
          "url": "http://t.co/ZOnsCHvoKt",
          "created_at": "Fri Jan 13 13:46:46 +0000 2012",
          "contributors_enabled": False,
          "time_zone": "Edinburgh",
          "protected": False,
          "default_profile": True,
          "is_translator": False
        },
        "geo": None,
        "in_reply_to_user_id_str": None,
        "possibly_sensitive": False,
        "lang": "en",
        "created_at": "Sun Oct 26 07:37:55 +0000 2014",
        "in_reply_to_status_id_str": None,
        "place": None,
        "metadata": {
          "iso_language_code": "en",
          "result_type": "recent"
        }
      },
      "user": {
        "follow_request_sent": False,
        "profile_use_background_image": True,
        "profile_text_color": "2A48AE",
        "default_profile_image": False,
        "id": 104940733,
        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme17/bg.gif",
        "verified": False,
        "profile_location": None,
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/2878477539/78e20432088b5ee2addc9ce3362fd461_normal.jpeg",
        "profile_sidebar_fill_color": "6378B1",
        "entities": {
          "description": {
            "urls": []
          }
        },
        "followers_count": 149,
        "profile_sidebar_border_color": "FBD0C9",
        "id_str": "104940733",
        "profile_background_color": "0C003D",
        "listed_count": 18,
        "is_translation_enabled": False,
        "utc_offset": 0,
        "statuses_count": 16031,
        "description": "Have you any dreams you'd like to sell?",
        "friends_count": 248,
        "location": "",
        "profile_link_color": "0F1B7C",
        "profile_image_url": "http://pbs.twimg.com/profile_images/2878477539/78e20432088b5ee2addc9ce3362fd461_normal.jpeg",
        "following": False,
        "geo_enabled": False,
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/104940733/1410032966",
        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme17/bg.gif",
        "name": "Heather",
        "lang": "en",
        "profile_background_tile": False,
        "favourites_count": 777,
        "screen_name": "froyoho",
        "notifications": False,
        "url": None,
        "created_at": "Thu Jan 14 21:37:54 +0000 2010",
        "contributors_enabled": False,
        "time_zone": "London",
        "protected": False,
        "default_profile": False,
        "is_translator": False
      },
      "geo": None,
      "in_reply_to_user_id_str": None,
      "possibly_sensitive": False,
      "lang": "en",
      "created_at": "Sun Nov 23 20:55:57 +0000 2014",
      "in_reply_to_status_id_str": None,
      "place": None,
      "metadata": {
        "iso_language_code": "en",
        "result_type": "recent"
      }
    },
    {
      "contributors": None,
      "truncated": False,
      "text": "RT @NotableHistory: Madonna, 18 year old freshman at the University of Michigan, 1976 http://t.co/x2dm1G67ea",
      "in_reply_to_status_id": None,
      "id": 536623674942439425,
      "favorite_count": 0,
      "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
      "retweeted": False,
      "coordinates": None,
      "entities": {
        "symbols": [],
        "user_mentions": [
          {
            "id": 844766941,
            "indices": [
              3,
              18
            ],
            "id_str": "844766941",
            "screen_name": "NotableHistory",
            "name": "OnThisDay & Facts"
          }
        ],
        "hashtags": [],
        "urls": [],
        "media": [
          {
            "source_status_id_str": "536610190334779392",
            "expanded_url": "http://twitter.com/NotableHistory/status/536610190334779392/photo/1",
            "display_url": "pic.twitter.com/x2dm1G67ea",
            "url": "http://t.co/x2dm1G67ea",
            "media_url_https": "https://pbs.twimg.com/media/B3EXbQkCMAEipwM.jpg",
            "source_status_id": 536610190334779392,
            "id_str": "536235587703812097",
            "sizes": {
              "small": {
                "h": 487,
                "resize": "fit",
                "w": 340
              },
              "large": {
                "h": 918,
                "resize": "fit",
                "w": 640
              },
              "medium": {
                "h": 860,
                "resize": "fit",
                "w": 600
              },
              "thumb": {
                "h": 150,
                "resize": "crop",
                "w": 150
              }
            },
            "indices": [
              86,
              108
            ],
            "type": "photo",
            "id": 536235587703812097,
            "media_url": "http://pbs.twimg.com/media/B3EXbQkCMAEipwM.jpg"
          }
        ]
      },
      "in_reply_to_screen_name": None,
      "in_reply_to_user_id": None,
      "retweet_count": 9,
      "id_str": "536623674942439425",
      "favorited": False,
      "retweeted_status": {
        "contributors": None,
        "truncated": False,
        "text": "Madonna, 18 year old freshman at the University of Michigan, 1976 http://t.co/x2dm1G67ea",
        "in_reply_to_status_id": None,
        "id": 536610190334779392,
        "favorite_count": 13,
        "source": "<a href=\"https://ads.twitter.com\" rel=\"nofollow\">Twitter Ads</a>",
        "retweeted": False,
        "coordinates": None,
        "entities": {
          "symbols": [],
          "user_mentions": [],
          "hashtags": [],
          "urls": [],
          "media": [
            {
              "expanded_url": "http://twitter.com/NotableHistory/status/536610190334779392/photo/1",
              "display_url": "pic.twitter.com/x2dm1G67ea",
              "url": "http://t.co/x2dm1G67ea",
              "media_url_https": "https://pbs.twimg.com/media/B3EXbQkCMAEipwM.jpg",
              "id_str": "536235587703812097",
              "sizes": {
                "small": {
                  "h": 487,
                  "resize": "fit",
                  "w": 340
                },
                "large": {
                  "h": 918,
                  "resize": "fit",
                  "w": 640
                },
                "medium": {
                  "h": 860,
                  "resize": "fit",
                  "w": 600
                },
                "thumb": {
                  "h": 150,
                  "resize": "crop",
                  "w": 150
                }
              },
              "indices": [
                66,
                88
              ],
              "type": "photo",
              "id": 536235587703812097,
              "media_url": "http://pbs.twimg.com/media/B3EXbQkCMAEipwM.jpg"
            }
          ]
        },
        "in_reply_to_screen_name": None,
        "in_reply_to_user_id": None,
        "retweet_count": 9,
        "id_str": "536610190334779392",
        "favorited": False,
        "user": {
          "follow_request_sent": False,
          "profile_use_background_image": True,
          "profile_text_color": "333333",
          "default_profile_image": False,
          "id": 844766941,
          "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/458461302696837121/rGlGdWsc.png",
          "verified": False,
          "profile_location": None,
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/481243404320251905/gCr1cVP2_normal.png",
          "profile_sidebar_fill_color": "DDFFCC",
          "entities": {
            "url": {
              "urls": [
                {
                  "url": "http://t.co/9fTPk5A4wh",
                  "indices": [
                    0,
                    22
                  ],
                  "expanded_url": "http://notablefacts.com/",
                  "display_url": "notablefacts.com"
                }
              ]
            },
            "description": {
              "urls": []
            }
          },
          "followers_count": 73817,
          "profile_sidebar_border_color": "FFFFFF",
          "id_str": "844766941",
          "profile_background_color": "9AE4E8",
          "listed_count": 485,
          "is_translation_enabled": False,
          "utc_offset": -21600,
          "statuses_count": 38841,
          "description": "On This Day in History, Historical Pictures & other Interesting Facts....Historyfollower@gmail.com",
          "friends_count": 43594,
          "location": "",
          "profile_link_color": "0084B4",
          "profile_image_url": "http://pbs.twimg.com/profile_images/481243404320251905/gCr1cVP2_normal.png",
          "following": False,
          "geo_enabled": False,
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/844766941/1411076349",
          "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/458461302696837121/rGlGdWsc.png",
          "name": "OnThisDay & Facts",
          "lang": "en",
          "profile_background_tile": True,
          "favourites_count": 1383,
          "screen_name": "NotableHistory",
          "notifications": False,
          "url": "http://t.co/9fTPk5A4wh",
          "created_at": "Tue Sep 25 03:08:59 +0000 2012",
          "contributors_enabled": False,
          "time_zone": "Central Time (US & Canada)",
          "protected": False,
          "default_profile": False,
          "is_translator": False
        },
        "geo": None,
        "in_reply_to_user_id_str": None,
        "possibly_sensitive": False,
        "lang": "en",
        "created_at": "Sun Nov 23 20:00:13 +0000 2014",
        "in_reply_to_status_id_str": None,
        "place": None,
        "metadata": {
          "iso_language_code": "en",
          "result_type": "recent"
        }
      },
      "user": {
        "follow_request_sent": False,
        "profile_use_background_image": True,
        "profile_text_color": "333333",
        "default_profile_image": False,
        "id": 818185729,
        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
        "verified": False,
        "profile_location": None,
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/486215801498640384/rz9o7LnF_normal.jpeg",
        "profile_sidebar_fill_color": "DDEEF6",
        "entities": {
          "description": {
            "urls": []
          }
        },
        "followers_count": 302,
        "profile_sidebar_border_color": "C0DEED",
        "id_str": "818185729",
        "profile_background_color": "C0DEED",
        "listed_count": 0,
        "is_translation_enabled": False,
        "utc_offset": None,
        "statuses_count": 395,
        "description": "Formerly with California Dept of General Services, now freelancing around the Sacramento area...",
        "friends_count": 1521,
        "location": "Citrus Heights, CA",
        "profile_link_color": "0084B4",
        "profile_image_url": "http://pbs.twimg.com/profile_images/486215801498640384/rz9o7LnF_normal.jpeg",
        "following": False,
        "geo_enabled": True,
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/818185729/1383764759",
        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
        "name": "M Duncan",
        "lang": "en",
        "profile_background_tile": False,
        "favourites_count": 6544,
        "screen_name": "MDuncan95814",
        "notifications": False,
        "url": None,
        "created_at": "Tue Sep 11 21:02:09 +0000 2012",
        "contributors_enabled": False,
        "time_zone": None,
        "protected": False,
        "default_profile": True,
        "is_translator": False
      },
      "geo": None,
      "in_reply_to_user_id_str": None,
      "possibly_sensitive": False,
      "lang": "en",
      "created_at": "Sun Nov 23 20:53:48 +0000 2014",
      "in_reply_to_status_id_str": None,
      "place": None,
      "metadata": {
        "iso_language_code": "en",
        "result_type": "recent"
      }
    }
  ]
}
```

***Understand*** :

At any level of the extraction process, the first task is to make sure you understand the current object you have extracted. There are few options here.

1. Print the entire object. If it’s small enough, you may be able to make sense of the printout directly. If it’s a little bit larger, you may find it helpful to “pretty-print” it, with indentation showing the level of nesting of the data. We don’t have a way to pretty-print in our online browser-based environment, but if you’re running code with a full Python interpreter, you can use the dumps function in the json module. For example:

```python
import json
print(json.dumps(res, indent=2))
```

2. If printing the entire object gives you something that’s too unwieldy, you have other options for making sense of it.
    * Copy and paste it to a site like https://jsoneditoronline.org/ which will let you explore and collapse levels
    * Print the type of the object.
    * If it’s a dictionary:
      - print the keys
    * If it’s a list:
      - print its length
      - print the type of the first item
      - print the first item if it’s of manageable size


```python
import json
print(json.dumps(res, indent=2)[:100])
print("------------------")
print(type(res))
print(res.keys())
```

**Output** :

```
{
  "search_metadata": {
    "count": 3,
    "completed_in": 0.015,
    "max_id_str": "5366245192855
------------------
<class 'dict'>
dict_keys(['search_metadata', 'statuses'])
```

***Extract*** :

In the extraction phase, you will be diving one level deeper into the nested data.

1. If it’s a dictionary, figure out which key has the value you’re looking for, and get its value. For example: `res2 = res['statuses']`
2. If it’s a list, you will typically be wanting to do something with each of the items (e.g., extracting something from each, and accumulating them in a list). For that you’ll want a for loop, such as `for res2 in res`. During your exploration phase, however, it will be easier to debug things if you work with just one item. One trick for doing that is to iterate over a slice of the list containing just one item. For example, `for res2 in res[:1]`.

```python
print(type(res))
print(res.keys())
res2 = res["statuses"]
```

***Repeat*** :

Now you’ll repeat the Understand and Extract processes at the next level.

First understand.

```python
print(type(res))
print(res.keys())
res2 = res["statuses"]
print("------ Level 2 -------")
print(type(res2))
print(len(res2))
```

**Output** :

```
<class 'dict'>
dict_keys(['search_metadata', 'statuses'])
------ Level 2 -------
<class 'list'>
3
```

It’s a list, with three items, so it’s a good guess that each item represents one tweet.

Now extract. Since it’s a list, we’ll want to work with each item, but to keep things manageable for now, let’s use the trick for just looking at the first item. Later we’ll switch to processing all the items.

```python
print(type(res))
print(res.keys())
res2 = res["statuses"]
print("------ Level 2 -------")
print(type(res2))
print(len(res2))

for res3 in res2[:1]:
  print("----- Level 3: a tweet -----")
  print(json.dumps(res3, indent=2)[:30])
```

**Output** :

```
<class 'dict'>
dict_keys(['search_metadata', 'statuses'])
------ Level 2 -------
<class 'list'>
3
----- Level 3: a tweet -----
{
  "contributors": null,
  "t
```

First understand.

```python
print(type(res))
print(res.keys())
res2 = res["statuses"]
print("------ Level 2 -------")
print(type(res2))
print(len(res2))

for res3 in res2[:1]:
  print("----- Level 3: a tweet -----")
  print(json.dumps(res3, indent=2)[:30])
  print(type(res3))
  print(res3.keys())
```

**Output** :

```
<class 'dict'>
dict_keys(['search_metadata', 'statuses'])
------ Level 2 -------
<class 'list'>
3
----- Level 3: a tweet -----
{
  "contributors": null,
  "t
<class 'dict'>
dict_keys(['contributors', 'truncated', 'text', 'in_reply_to_status_id', 'id', 'favorite_count', 'source', 'retweeted', 'coordinates', 'entities', 'in_reply_to_screen_name', 'in_reply_to_user_id', 'retweet_count', 'id_str', 'favorited', 'retweeted_status', 'user', 'geo', 'in_reply_to_user_id_str', 'lang', 'created_at', 'in_reply_to_status_id_str', 'place', 'metadata'])
```

Then extract. Let’s pull out the information about who sent each of the tweets. Probably that’s the value associated with the ‘user’ key.

```python
print(type(res))
print(res.keys())
res2 = res["statuses"]
print("------ Level 2 -------")
print(type(res2))
print(len(res2))

for res3 in res2[:1]:
  print("----- Level 3: a tweet -----")
  print(json.dumps(res3, indent=2)[:30])
  res4 = res3["user"]  
```

Understand.

```python
print(type(res))
print(res.keys())
res2 = res["statuses"]
print("------ Level 2 -------")
print(type(res2))
print(len(res2))

for res3 in res2[:1]:
  print("----- Level 3: a tweet -----")
  print(json.dumps(res3, indent=2)[:30])
  res4 = res3["user"]  
  print("----Level 4: the user who wrote the tweet----")
  print(type(res4))
  print(res4.keys())
```

**Output** :

```
<class 'dict'>
dict_keys(['search_metadata', 'statuses'])
------ Level 2 -------
<class 'list'>
3
----- Level 3: a tweet -----
{
  "contributors": null,
  "t
----Level 4: the user who wrote the tweet----
<class 'dict'>
dict_keys(['follow_request_sent', 'profile_use_background_image', 'profile_text_color', 'default_profile_image', 'id', 'profile_background_image_url_https', 'verified', 'profile_location', 'profile_image_url_https', 'profile_sidebar_fill_color', 'entities', 'followers_count', 'profile_sidebar_border_color', 'id_str', 'profile_background_color', 'listed_count', 'is_translation_enabled', 'utc_offset', 'statuses_count', 'description', 'friends_count', 'location', 'profile_link_color', 'profile_image_url', 'following', 'geo_enabled', 'profile_banner_url', 'profile_background_image_url', 'name', 'lang', 'profile_background_tile', 'favourites_count', 'screen_name', 'notifications', 'url', 'created_at', 'contributors_enabled', 'time_zone', 'protected', 'default_profile', 'is_translator'])
```

Extract. Let’s print out the user’s screen name and when their account was created.


```python
import json
# print(type(res))
# print(res.keys())
res2 = res['statuses']
# print("----Level 2: a list of tweets-----")
# print(type(res2)) # it's a list!
# print(len(res2))  # looks like one item representing each of the three tweets
for res3 in res2[:1]:
   print("----Level 3: a tweet----")
   # print(json.dumps(res3, indent=2)[:30])
   res4 = res3['user']
   print("----Level 4: the user who wrote the tweet----")
   # print(type(res4)) # it's a dictionary
   # print(res4.keys())
   print(res4['screen_name'], res4['created_at'])

```

**Output** :

```
----Level 3: a tweet----
----Level 4: the user who wrote the tweet----
31brooks_ Wed Apr 09 14:34:41 +0000 2014
```

Now, we may want to go back have it extract for all the items rather than only the first item in res2.

```python
import json
# print(type(res))
# print(res.keys())
res2 = res['statuses']
#print("----Level 2: a list of tweets-----")
#print(type(res2)) # it's a list!
#print(len(res2))  # looks like one item representing each of the three tweets
for res3 in res2:
   #print("----Level 3: a tweet----")
   #print(json.dumps(res3, indent=2)[:30])
   res4 = res3['user']
   #print("----Level 4: the user who wrote the tweet----")
   #print(type(res4)) # it's a dictionary
   #print(res4.keys())
   print(res4['screen_name'], res4['created_at'])
```

**Output** :

```
31brooks_ Wed Apr 09 14:34:41 +0000 2014
froyoho Thu Jan 14 21:37:54 +0000 2010
MDuncan95814 Tue Sep 11 21:02:09 +0000 2012
```

***Reflections*** :

Notice that each time we descend a level in a dictionary, we have a `[]` picking out a key. Each time we look inside a list, we will have a for loop. If there are lists at multiple levels, we will have nested for loops.

Once you’ve figured out how to extract everything you want, you may choose to collapse things with multiple extractions in a single expression. For example, we could have this shorter version.

```python
for res3 in res["statuses"]:
  print(res3["user"]["screen_name"], res3["user"]["created_at"])
```

**Output**:

```
31brooks_ Wed Apr 09 14:34:41 +0000 2014
froyoho Thu Jan 14 21:37:54 +0000 2010
MDuncan95814 Tue Sep 11 21:02:09 +0000 2012
```

Even with this compact code, we can still count off how many levels of nesting we have extracted from, in this case four. `res[‘statuses’]` says we have descended one level (in a dictionary). for `res3` in… says we are have descended another level (in a list). `[‘user’]` is descending one more level, and `[‘screen_name’]` is descending one more level.

-------
--------

### 1.8. Chapter Assessments & Exercises

#### Assessments

**A1**. The variable `nested` contains a nested list. Assign ‘snake’ to the variable `output` using indexing.


```python
# Given
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]


# Solution
output = nested[1][2]
print(output)
```

**Output** :

```
snake
```

-----

**A2**. Below, a list of lists is provided. Use in and not in tests to create variables with Boolean values. See comments for further instructions.



```python
# Given
lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
#Test to see if 4 is in the second list of lst. Save to variable ``four``
#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``


# Solution
yellow = "yellow" in lst[2]
print(yellow)

four = 4 in lst[1]
print(four)

orange = "orange" in lst[0]
print(orange)
```

**Output** :

```
True
False
True
```

-----

**A3**. Below, we’ve provided a list of lists. Use in statements to create variables with Boolean values - see the ActiveCode window for further directions.



```python
# Given
L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
# Test if [5, 8, 7] is in the list L. Save to variable name test2
# Test if 6.6 is in the third element of list L. Save to variable name test3


# Solution
test1 = "hola" in L
print(test1)

test2 = [5,8,7] in L
print(test2)

test3 = 6.6 in L[2]
print(test3)
```

**Output** :

```
False
True
True
```

-----

**A4**. Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.



```python
# Given
nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]],
					'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.



# Solution
data = "data" in nested.keys()
print(data)

twentyfour = 24 in nested.keys()
print(twentyfour)

whole = "whole" not in nested["window"]
print(whole)

physics = "physics" in nested.keys()
print(physics)
```

**Output** :

```
True
False
False
False
```

-----


**A5**. The variable `nested_d` contains a nested dictionary with the gold medal counts for the top four countries in the past three Olympics. Assign the value of Great Britain’s gold medal count from the London Olympics to the variable `london_gold`. Use indexing. Do not hardcode.



```python
# Given
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19},
						'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22},
						'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}



# Solution
london_gold = 0

for medals in nested_d["London"]:
	if medals == "Great Britain":
		london_gold += nested_d["London"][medals]

print(london_gold)
```

**Output** :

```
29
```

-----


**A6**. Below, we have provided a nested dictionary. Index into the dictionary to create variables that we have listed in the ActiveCode window.



```python
# Given
sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'],
				'diving': ['springboard', 'platform', 'synchronized'],
				'track': ['sprint', 'distance', 'jumps', 'throws'],
				'gymnastics': {
											'women':['vault', 'floor', 'uneven bars', 'balance beam'],
											'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
# Assign the string 'platform' to the name v2
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
# Assign the string 'rings' to the name v4


# Solution
v1 = sports["swimming"][2]
print(v1)

v2 = sports["diving"][1]
print(v2)

v3 = sports["gymnastics"]["women"]
print(v3)

v4 = sports["gymnastics"]["men"][3]
print(v4)
```

**Output** :

```
backstroke
platform
['vault', 'floor', 'uneven bars', 'balance beam']
rings
```

-----


**A7**. Given the dictionary, `nested_d`, save the medal count for the USA from all three Olympics in the dictionary to the list `US_count`.



```python
# Given
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19},
						'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22},
						'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []


# Solution
for oly in nested_d.keys():
	for country in nested_d[oly]:
		if country == "USA":
			US_count.append(nested_d[oly]["USA"])

print(US_count)
```

**Output** :

```
[36, 46, 35]
```

-----


**A8**. Iterate through the contents of `l_of_l` and assign the third element of sublist to a new list called `third`.


```python
# Given
l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]



# Solution
third = []

for lst in l_of_l:
	third.append(lst[2])

print(third)
```

**Output** :

```
['blue', 'blood orange', 'lavender', 'mac n cheese']
```

-----



**A9**. Given below is a list of lists of athletes. Create a list, `t`, that saves only the athlete’s name if it contains the letter “t”. If it does not contain the letter “t”, save the athlete name into list `other`.


```python
# Given
athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]



# Solution
t = []
other = []

for lst in athletes:
	for athlete in lst:
		if "t" in athlete:
			t.append(athlete)
		else:
			other.append(athlete)

print(t)
print(other)
```

**Output** :

```
['Lochte', 'Bolt', 'Eaton', 'Dalton']
['Phelps', 'Schooling', 'Ledecky', 'Franklin', 'Felix', 'Gardner', 'Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak']
```

-----


----
----

#### Exercises


**Q1**. Iterate through the list so that if the character `‘m’` is in the string, then it should be added to a new list called `m_list`. Hint: Because this isn’t just a list of lists, think about what type of object you want your data to be stored in. Conditionals may help you.


```python
# Given
d = ['good morning', 'hello', 'chair', 'python', ['music', 'flowers', 'facebook', 'instagram', 'snapchat', ['On my Own', 'monster', 'Words dont come so easily', 'lead me right']], 'Stressed Out', 'Pauver Coeur', 'Reach for Tomorrow', 'mariners song', 'Wonder sleeps here']


# Solution
for item in d:
	if type(item) is list:
		for inner_item in item:
			if type(inner_item) is list:
				for inner_item2 in inner_item:
					if "m" in inner_item2:
						m_list.append(inner_item2)
			else:
				if "m" in inner_item:
					m_list.append(inner_item)
	else:
		if "m" in item:
			m_list.append(item)

print(m_list)
```

**Output** :

```
['good morning', 'music', 'instagram', 'On my Own', 'monster', 'Words dont come so easily', 'lead me right', 'Reach for Tomorrow', 'mariners song']
```

-----

**Q2**. The nested dictionary, `pokemon`, shows the number of various Pokemon that each person has caught while playing Pokemon Go. Find the total number of rattatas, dittos, and pidgeys caught and assign to the variables `r`, `d`, and `p` respectively. Do not hardcode. Note: Be aware that not every trainer has caught a ditto.


```python
# Given
pokemon = {'Trainer1':
          {'normal': {'rattatas':15, 'eevees': 2, 'ditto':1}, 'water': {'magikarps':3}, 'flying': {'zubats':8, 'pidgey': 12}},
          'Trainer2':
          {'normal': {'rattatas':25, 'eevees': 1}, 'water': {'magikarps':7}, 'flying': {'zubats':3, 'pidgey': 15}},
          'Trainer3':
          {'normal': {'rattatas':10, 'eevees': 3, 'ditto':2}, 'water': {'magikarps':2}, 'flying': {'zubats':3, 'pidgey': 20}},
          'Trainer4':
          {'normal': {'rattatas':17, 'eevees': 1}, 'water': {'magikarps':9}, 'flying': {'zubats':12, 'pidgey': 14}}}




# Solution
r = 0
d = 0
p = 0

for trainer in pokemon:
	types = ["normal", "water","flying"]
	for typ in types:
		for it in pokemon[trainer][typ]:
			if it == "rattatas":
				r+= pokemon[trainer][typ]["rattatas"]
			elif it == "ditto":
				d += pokemon[trainer][typ]["ditto"]
			elif it == "pidgey":
				p += pokemon[trainer][typ]["pidgey"]

print(r)
print(d)
print(p)
```

**Output** :

```
67
3
61
```

-----

**Q3**. Below, we have provided a nested list called `big_list`. Use nested iteration to create a dictionary, `word_counts`, that contains all the words in `big_list` as keys, and the number of times they occur as values.


```python
# Given
big_list = [[['one', 'two'], ['seven', 'eight']],
						[['nine', 'four'], ['three', 'one']],
						[['two', 'eight'], ['seven', 'four']],
						[['five', 'one'], ['four', 'two']],
						[['six', 'eight'], ['two', 'seven']],
						[['three', 'five'], ['one', 'six']],
						[['nine', 'eight'], ['five', 'four']],
						[['six', 'three'], ['four', 'seven']]]




# Solution
word_counts = {}

def w_counter(alist):
	for item in alist:
		if type(item) is list:
			w_counter(item)
		else:
			if item in word_counts:
				word_counts[item] += 1
			else:
				word_counts[item] = 1

w_counter(big_list)
print(word_counts)
```

**Output** :

```
{'one': 4, 'two': 4, 'seven': 4, 'eight': 4, 'nine': 2, 'four': 5, 'three': 3, 'five': 3, 'six': 3}
```

-----

**Q4**. Provided is a dictionary that contains pokemon go player data, where each player reveals the amount of candy each of their pokemon have. If you pooled all the data together, which pokemon has the highest number of candy? Assign that pokemon to the variable `most_common_pokemon`.


```python
# Given
pokemon_go_data = {'bentspoon':
                  {'Rattata': 203, 'Pidgey': 120, 'Drowzee': 89, 'Squirtle': 35, 'Pikachu': 3, 'Eevee': 34, 'Magikarp': 300, 'Paras': 38},
                  'Laurne':
                  {'Pidgey': 169, 'Rattata': 245, 'Squirtle': 9, 'Caterpie': 38, 'Weedle': 97, 'Pikachu': 6, 'Nidoran': 44, 'Clefairy': 15, 'Zubat': 79, 'Dratini': 4},
                  'picklejarlid':
                  {'Rattata': 32, 'Drowzee': 15, 'Nidoran': 4, 'Bulbasaur': 3, 'Pidgey': 56, 'Weedle': 21, 'Oddish': 18, 'Magmar': 6, 'Spearow': 14},
                  'professoroak':
                  {'Charmander': 11, 'Ponyta': 9, 'Rattata': 107, 'Belsprout': 29, 'Seel': 19, 'Pidgey': 93, 'Shellder': 43, 'Drowzee': 245, 'Tauros': 18, 'Lapras': 18}}





# Solution
pokemons = {}

for item in pokemon_go_data.keys():
	#print(pokemon_go_data[item])
	for poke in pokemon_go_data[item]:
		if poke in pokemons:
			pokemons[poke] += pokemon_go_data[item][poke]
		else:
			pokemons[poke] = pokemon_go_data[item][poke]

most_common_pokemon = sorted(pokemons, reverse=True, key=lambda x: pokemons[x])[0]
print(most_common_pokemon)
```

**Output** :

```
Rattata
```

-----

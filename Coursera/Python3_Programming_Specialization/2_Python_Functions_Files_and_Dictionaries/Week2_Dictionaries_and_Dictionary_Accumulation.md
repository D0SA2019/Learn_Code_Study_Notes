# Python Functions, Files, and Dictionaries
*Coursera | Python 3 Programming Specialization | Course 2*

## Week 2 : Dictionaries and Dictionary Accumulation

### Dictionary Mechanics

#### 2.1. Dictionaries

The compound data types we have studied in detail so far — strings and lists — are sequential collections. This means that the items in the collection are ordered from left to right and they use integers as indices to access the values they contain. This also means that looking for a particular value requires scanning the many items in the list until you find the desired value.

Data can sometimes be organized more usefully by associating a key with the value we are looking for. For example, if you are asked for the page number for the start of chapter 5 in a large textbook, you might flip around the book looking for the chapter 5 heading. If the chapter number appears in the header or footer of each page, you might be able to find the page number fairly quickly but it’s generally easier and faster to go to the index page and see that chapter 5 starts on page 78.

This sort of direct look up of a value in Python is done with an object called a Dictionary. Dictionaries are a different kind of collection. They are Python’s built-in **mapping** type. A map is an unordered, associative collection. The association, or mapping, is from a **key**, which can be of any immutable type (e.g., the chapter name and number in the analogy above), to a **value** (the starting page number), which can be any Python data object. You’ll learn how to use these collections in the following chapter.

To provide an example of this new kind of datatype, we will create a dictionary to translate English words into Spanish. For this dictionary, the keys are strings and the values will also be strings.

One way to create a dictionary is to start with the empty dictionary and add **key-value pairs**. The empty dictionary is denoted `{}`.

```python
eng2sp = {}
eng2sp["one"] = "uno"
eng2sp["two"] = "dos"
eng2sp["three"] = "tres"
print(eng2sp)
```

**Output** :

```
{'one': 'uno', 'two': 'dos', 'three': 'tres'}
```

The first assignment creates an empty dictionary named `eng2sp`. The other assignments add new key-value pairs to the dictionary. The left hand side gives the dictionary and the key being associated. The right hand side gives the value being associated with that key. We can print the current value of the dictionary in the usual way. The key-value pairs of the dictionary are separated by commas. Each pair contains a key and a value separated by a colon.

The order of the pairs may not be what you expected. Python uses complex algorithms, designed for very fast access, to determine where the key-value pairs are stored in a dictionary. For our purposes we can think of this ordering as unpredictable.

Another way to create a dictionary is to provide a bunch of key-value pairs using the same syntax as the previous output.


```python
eng2sp = {"one" : "uno", "two" : "dos", "three" : "tres"}
print(eng2sp)
```

**Output** :

```
{'one': 'uno', 'two': 'dos', 'three': 'tres'}
```


It doesn’t matter what order we write the pairs. The values in a dictionary are accessed with keys, not with indices, so there is no need to care about ordering.

Here is how we use a key to look up the corresponding value.

```python
eng2sp = {"three" : "tres", "one" : "uno", "two" : "dos"}
value = eng2sp["two"]
print(value)
print(eng2sp["one"])
```

**Output** :

```
dos
uno
```

----
----

**Check Your Understanding**

**Q1** : A dictionary is an unordered collection of key-value pairs.

A. False <br>
B. True ✅ <br>

----

**Q2** : What is printed by the following statements?

```python
mydict = {"cat" : 12, "dog" : 6, "elephant" : 23}
print(mydict["dog"])
```

A. 12 <br>
B. 6 ✅ <br>
C. 23 <br>
D. Error, you cannot use the index operator with a dictionary. <br>

----

**Q3** : Create a dictionary that keeps track of the USA’s Olympic medal count. Each key of the dictionary should be the type of medal (gold, silver, or bronze) and each key’s value should be the number of that type of medal the USA’s won. Currently, the USA has 33 gold medals, 17 silver, and 12 bronze. Create a dictionary saved in the variable `medals` that reflects this information.

```python
medals = {"gold": 33, "silver": 17, "bronze": 12}
print(medals)
print(medals["silver"])
```

**Output** :

```
{'gold': 33, 'silver': 17, 'bronze': 12}
17
```

----

**Q4** : You are keeping track of olympic medals for Italy in the 2016 Rio Summer Olympics! At the moment, Italy has 7 gold medals, 8 silver metals, and 6 bronze medals. Create a dictionary called `olympics` where the keys are the types of medals, and the values are the number of that type of medals that Italy has won so far.


```python
olympics = {"gold" : 7,
						"silver" : 8,
						"bronze" : 6}
print(olympics)
print(olympics["gold"])
```

**Output** :

```
{'gold': 7, 'silver': 8, 'bronze': 6}
7
```

----

#### 2.2. Dictionary Operations

The `del` statement removes a key-value pair from a dictionary. For example, the following dictionary contains the names of various fruits and the number of each fruit in stock. If someone buys all of the pears, we can remove the entry from the dictionary

```python
inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print(inventory)

del inventory["pears"]
print(inventory)
```

**Output** :

```
{'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
{'apples': 430, 'bananas': 312, 'oranges': 525}
```

Dictionaries are mutable, as the delete operation above indicates. As we’ve seen before with lists, this means that the dictionary can be modified by referencing an association on the left hand side of the assignment statement. In the previous example, instead of deleting the entry for `pears`, we could have set the inventory to `0`.

```python
inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print(inventory)

inventory["pears"] = 0
print(inventory)
```

**Output** :

```
{'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
{'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 0}
```

**Note** : Setting the value associated with pears to 0 has a different effect than removing the key-value pair entirely with del.

Similarily, a new shipment of 200 bananas arriving could be handled like this. Notice that there are now 512 bananas— the dictionary has been modified. Note also that the `len` function also works on dictionaries. It returns the number of key-value pairs.

```python
inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print(inventory)

inventory["bananas"] = inventory["bananas"] + 200
print(inventory)

numItems = len(inventory)
print(numItems)
```

**Output** :

```
{'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
{'apples': 430, 'bananas': 512, 'oranges': 525, 'pears': 217}
4
```

Notice that there are now 512 bananas—the dictionary has been modified. Note also that the `len` function also works on dictionaries. It returns the number of key-value pairs.

----
----

**Check Your Understanding**

**Q1** : What is printed by the following statements?

```python
mydict = {"cat": 12, "dog": 6, "elephant": 23}
mydict["mouse"] = mydict["cat"] + mydict["dog"]
print(mydict["mouse"])
```

A. 12 <br>
B. 0 <br>
C. 18 ✅ <br>
D. Error, there is no entry with mouse as the key. <br>

----

**Q2** : Update the value for “Phelps” in the dictionary `swimmers` to include his medals from the Rio Olympics by adding 5 to the current value (Phelps will now have 28 total medals). Do not rewrite the dictionary.

```python
# Given
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}


# Solution
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
print(swimmers)

swimmers["Phelps"] = swimmers["Phelps"] + 5
print(swimmers)
```

**Output** :

```
{'Manuel': 4, 'Lochte': 12, 'Adrian': 7, 'Ledecky': 5, 'Dirado': 4, 'Phelps': 23}
{'Manuel': 4, 'Lochte': 12, 'Adrian': 7, 'Ledecky': 5, 'Dirado': 4, 'Phelps': 28}
```

----


#### 2.3. Dictionary Methods

Dictionaries have a number of useful built-in methods. The following table provides a summary and more details can be found in the [Python Documentation](http://docs.python.org/py3k/library/stdtypes.html#mapping-types-dict).

| Method | Parameters | Description |
|--|--|--|
| `.keys` | none | Returns a view of the keys in the dictionary |
| `.values` | none | Returns a view of the values in the dictionary |
| `.items` | none | Returns a view of the key-value pairs in the dictionary |
| `.get` | key | Returns the value associated with key; None otherwise |
| `.get` | key, alt| Returns the value associated with key; alt otherwise |


As we saw earlier with strings and lists, dictionary methods use dot notation, which specifies the name of the method to the right of the dot and the name of the object on which to apply the method immediately to the left of the dot. The empty parentheses in the case of `keys` indicate that this method takes no parameters. If `x` is a variable whose value is a dictionary, `x.keys` is the method object, and `x.keys()` invokes the method, returning a view of the value.

The keys method returns the keys, not necessarily in the same order they were added to the dictionary or any other particular order.


```python
inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

for akey in inventory.keys():
	print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(ks)
```

**Output** :

```
Got key apples which maps to value 430
Got key bananas which maps to value 312
Got key oranges which maps to value 525
Got key pears which maps to value 217
['apples', 'bananas', 'oranges', 'pears']
```

It’s so common to iterate over the `keys` in a dictionary that you can omit the keys method call in the `for` loop — iterating over a dictionary implicitly iterates over its keys.


```python
inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

for k in inventory:
	print("Got key", k)
```

**Output** :

```
Got key apples
Got key bananas
Got key oranges
Got key pears
```

The `values` and `items` methods are similar to `keys`. They return the objects which can be iterated over. Note that the item objects are tuples containing the key and the associated value.

```python
inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

print(list(inventory.values()))
print(list(inventory.items()))

for k in inventory:
	print("Got", k, "that maps to", inventory[k])
```

**Output** :

```
[430, 312, 525, 217]
[('apples', 430), ('bananas', 312), ('oranges', 525), ('pears', 217)]
Got apples that maps to 430
Got bananas that maps to 312
Got oranges that maps to 525
Got pears that maps to 217
```

**Note** : Technically, `.keys()`, .`values()`, and `.items()` don’t return actual lists. Like the range function described previously, in python 3 they return objects that produce the items one at a time, rather than producing and storing all of them in advance as a list. Unless the dictionary has a whole lot of keys, this won’t make a difference for performance. In any case, as with the range function, it is safe for you to think of them as returning lists, for most purposes. For the python interpreter built into this textbook, they actually do produce lists. In a native python interpreter, if you print out `type(inventory.keys())`, you will find that it is something other than an actual list. If you want to get the first key, `inventory.keys()[0]` works in the online textbook, but in a real python interpreter, you need to make the collection of keys into a real list before using `[0]` to index into it: `list(inventory.keys())[0]`.

The `in` and `not in` operators can test if a key is in the dictionary:


```python
inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

print("apples" in inventory)
print("cherries" in inventory)

if "bananas" in inventory:
	print(inventory["bananas"])
else:
	print("We have no bananas")
```

**Output** :

```
True
False
312
```

This operator can be very useful since looking up a non-existent key in a dictionary causes a runtime error.

The `get` method allows us to access the value associated with a key, similar to the `[ ]` operator. The important difference is that `get` will not cause a runtime error if the key is not present. It will instead return None. There exists a variation of `get` that allows a second parameter that serves as an alternative return value in the case where the key is not present. This can be seen in the final example below. In this case, since “cherries” is not a key, return 0 (instead of None).

```python
inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))
print(inventory.get("cherries, 0"))
print(inventory.get("cherries, 999"))
print(inventory)
```

**Output** :

```
430
None
0
999
{'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217
```

----
----

**Check Your Understanding**

**Q1** : What is printed by the following statements?

```python
mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
answer = mydict.get("cat") // mydict.get("dog")
print(answer)
```

A. 2 ✅ <br>
B. 0.5 <br>
C. bear <br>
D. Error, divide is not a valid operation on dictionaries. <br>

---

**Q2** : What is printed by the following statements?

```python
mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
print("dog" in mydict)
```

A. True ✅ <br>
B. False <br>


----

**Q3** : What is printed by the following statements?

```python
mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
print(23 in mydict)
```

A. True <br>
B. False ✅ <br>


----
**Q4** : What is printed by the following statements?

```python
total = 0
mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
for akey in mydict:
	if len(akey) > 3:
		total = total + mydict[akey]
print(total)
```

A. 18 <br>
B. 43 ✅ <br>
C. 0 <br>
D. 61 <br>

-----

**Q5** : Every four years, the summer Olympics are held in a different country. Add a key-value pair to the dictionary `places` that reflects that the 2016 Olympics were held in Brazil. Do not rewrite the entire dictionary to do this!



```python
# Given
places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}


# Solution
places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}
places["Brazil"] = 2016
print(places)
```

**Output** :

```
{'Australia': 2000, 'Greece': 2004, 'China': 2008, 'England': 2012, 'Brazil': 2016}
```

----

**Q6** : We have a dictionary of the specific events that Italy has won medals in and the number of medals they have won for each event. Assign to the variable `events` a list of the keys from the dictionary `medal_events`. Do not hard code this.



```python
# Given
medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}


# Solution
medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
events = list(medal_events.keys())
print(events)
```

**Output** :

```
['Shooting', 'Fencing', 'Judo', 'Swimming', 'Diving']
```

----

#### 2.4. Aliasing and Copying with Dictionaries

Because dictionaries are mutable, you need to be aware of aliasing (as we saw with lists). Whenever two variables refer to the same dictionary object, changes to one affect the other. For example, `opposites` is a dictionary that contains pairs of opposites.



```python
opposites = {"up": "down", "right": "wrong", "true": "false"}
alias = opposites
print(alias is opposites)

alias["right"] = "left"
print(opposites["right"])
```

**Output** :

```
True
left
```

As you can see from the `is` operator, `alias` and `opposites` refer to the same object.

If you want to modify a dictionary and keep a copy of the original, use the dictionary `copy` method. Since acopy is a copy of the dictionary, changes to it will not effect the original.

```python
opposites = {"up": "down", "right": "wrong", "true": "false"}
alias = opposites
acopy = opposites.copy()
acopy["right"] = "left"
print(opposites)
print(acopy)
```

**Output** :

```
{'up': 'down', 'right': 'wrong', 'true': 'false'}
{'up': 'down', 'right': 'left', 'true': 'false'}
```

----
----

**Check Your Understanding**

**Q1** : What is printed by the following statements?

```python
mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
yourdict = mydict
yourdict["elephant"] = 999
print(mydict["elephant"])
```

A. 23 <br>
B. None <br>
C. 999 ✅ <br>
D. Error, there are two different keys named elephant. <br>


----


### Dictionary Accumulation

#### 2.5. Dictionary Accumulation


You have previously seen the accumulator pattern; it goes through the items in a sequence, updating an accumulator variable each time. Rather than accumulating a single result, it’s possible to accumulate many results. Suppose, for example, we wanted to find out which letters are used most frequently in English.

Suppose we had a reasonably long text that we thought was representative of general English usage. For our purposes in the this chapter, we will use the text of the Sherlock Holmes story, “A Study in Scarlet”, by Sir Arthur Conan Doyle. The text actually includes a few lines about the source of the transcription (Project Gutenberg), but those will not materially affect our analyses so we will just leave them in. You can access this text within this chapter with the code `open('scarlet.txt', 'r')`.


If we want to find out how often the letter ‘t’ occurs, we can accumulate the result in a count variable.


```python
f = open("scarlet.txt", "r")
txt = f.read()

t_count = 0
for c in txt:
	if c == "t":
		t_count = t_count + 1
print("t: " + str(t_count) + " occurrences")
```

**Output** :

```
t: 15946 occurrences
```

We can accumulate counts for more than one character as we traverse the text. Suppose, for example, we wanted to compare the counts of ‘t’ and ‘s’ in the text.


```python
f = open("scarlet.txt", "r")
txt = f.read()

t_count = 0
s_count = 0

for c in txt:
	if c == "t":
		t_count = t_count + 1
	elif c == "s":
		s_count = s_count + 1

print("t: " + str(t_count) + " occurrences")
print("s: " + str(s_count) + " occurrences")
```

**Output** :

```
t: 15946 occurrences
s: 11047 occurrences
```

OK, but you can see this is going to get tedious if we try to accumulate counts for all the letters. We will have to initialize a lot of accumulators, and there will be a very long if..elif..elif statement. Using a dictionary, we can do a lot better.

One dictionary can hold all of the accumulator variables. Each key in the dictionary will be one letter, and the corresponding value will be the count so far of how many times that letter has occurred.


```python
f = open("scarlet.txt", "r")
txt = f.read()

x = {}
x["t"] = 0
x["s"] = 0

for c in txt:
	if c == "t":
		x["t"] = x["t"] + 1
	elif c == "s":
		x["s"] = x["s"] + 1

print("t: " + str(x["t"]) + " occurrences")
print("s: " + str(x["s"]) + " occurrences")
```

**Output** :

```
t: 15946 occurrences
s: 11047 occurrences
```

This hasn’t really improved things yet, but look closely at lines 8-11 in the code above. Whichever character we’re seeing, t or s, we’re incrementing the counter for that character. So lines 9 and 11 could really be the same.


```python
f = open("scarlet.txt", "r")
txt = f.read()

x = {}
x['t'] = 0  
x['s'] = 0
for c in txt:
    if c == 't':
        x[c] = x[c] + 1
    elif c == 's':
        x[c] = x[c] + 1

print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")
```

**Output** :

```
t: 15946 occurrences
s: 11047 occurrences
```

Lines 9 and 11 above may seem a little confusing at first. Previously, our assignment statements referred directly to keys, with `x['s']` and `x['t']`. Here we are just using a variable `c` whose value is ‘s’ or ‘t’, or some other character.

If that made perfect sense to you, skip the next two paragraphs. Otherwise, read on. Let’s break down that line in a little more detail.

First, note that, as with all assignment statements, the right side is evaluated first. In this case `x[c]` has to be evaluated. As with all expressions, we first have to substitute values for variable names. `x` is a variable bound to a dictionary. `c` is a variable bound to one letter from the string that `txt` is bound to (that’s what the for statement says to do: execute lines 8-11 once for each character in txt, with the variable c bound to the current character on each iteration.) So, let’s suppose that the current character is the letter `s` (we are on line 11). Then `x[c]` looks up the value associated with the key ‘s’ in the dictionary x. If all is working correctly, that value should be the number of times ‘s’ has previously occurred. For the sake of argument, suppose it’s 25. Then the right side evaluates to 25 + 1, 26.

Now we have assigned the value 26 to `x[c]`. That is, in dictionary x, we set the value associated with the key ‘s’ (the current value of the variable c) to be 26. In other words, we have incremented the value associated with the key ‘s’ from 25 to 26.

We can do better still. One other nice thing about using a dictionary is that we don’t have to prespecify what all the letters will be. In this case, we know in advance what the alphabet for English is, but later in the chapter we will count the occurrences of words, and we do not know in advance all the of the words that may be used. Rather than pre-specifying which letters to keep accumulator counts for, we can start with an empty dictionary and add a counter to the dictionary each time we encounter a new thing that we want to start keeping count of.

```python
f = open("scarlet.txt", "r")
txt = f.read()

x = {}
for c in txt:
	if c not in x:
		x[c] = 0

	x[c] = x[c] + 1

print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")
print(x)
```

**Output** :

```
t: 15946 occurrences
s: 11047 occurrences
{'P': 72, 'a': 14830, 'r': 10862, 't': 15946, ' ': 42642, 'O': 101, 'n': 12598, 'e': 23485, ':': 31, 'S': 290, 'u': 5155, 'd': 8457, 'y': 3399, 'i': 11589, 'c': 4492, 'l': 6952, 'B': 115, 'g': 3673, 'R': 60, 'p': 2963, 'f': 3882, 'o': 14062, 'm': 4728, 'h': 12317, 's': 11047, 'J': 110, 'H': 477, '.': 2412, 'W': 268, ',': 2959, 'M': 163, 'D': 147, 'L': 181, 'A': 261, '\n': 1645, 'C': 129, '1': 18, 'k': 1348, 'I': 1209, '8': 5, '7': 5, 'U': 27, 'v': 1786, 'N': 138, 'b': 2477, 'w': 4492, 'F': 109, 'T': 526, 'j': 127, "'": 461, 'z': 108, 'G': 111, '-': 259, 'E': 83, '"': 1697, 'x': 290, '—': 116, 'q': 137, '?': 208, 'Y': 162, '!': 85, ';': 100, 'V': 11, 'æ': 1, '2': 14, 'K': 10, '4': 9, 'Q': 1, '3': 12, '9': 3, '6': 7, '5': 3, '0': 2, ']': 2, 'ñ': 4, 'Z': 2, '[': 1, '^': 1, 'é': 1, '(': 1, ')': 1}
```

Notice that in the for loop, we no longer need to explicitly ask whether the current letter is an ‘s’ or ‘t’. The increment step on line 11 works for the counter associated with whatever the current character is. Our code is now accumulating counts for all letters, not just ‘s’ and ‘t’.

Note that the print statements at the end pick out the specific keys ‘t’ and ‘s’. We can generalize that, too, to print out the occurrence counts for all of the characters, using a for loop to iterate through the keys in x.

```python
f = open('scarlet.txt', 'r')
txt = f.read()

letter_counts = {}
for c in txt:
	if c not in letter_counts:
		letter_counts[c] = 0
	letter_counts[c] = letter_counts[c] + 1

for c in letter_counts.keys():
	print(c + ": " + str(letter_counts[c]) + " occurrences")

print(letter_counts)
```

**Output** :

```
P: 72 occurrences
a: 14830 occurrences
r: 10862 occurrences
t: 15946 occurrences
 : 42642 occurrences
O: 101 occurrences
n: 12598 occurrences
e: 23485 occurrences
:: 31 occurrences
S: 290 occurrences
u: 5155 occurrences
d: 8457 occurrences
y: 3399 occurrences
i: 11589 occurrences
c: 4492 occurrences
l: 6952 occurrences
B: 115 occurrences
g: 3673 occurrences
R: 60 occurrences
p: 2963 occurrences
f: 3882 occurrences
o: 14062 occurrences
m: 4728 occurrences
h: 12317 occurrences
s: 11047 occurrences
J: 110 occurrences
H: 477 occurrences
.: 2412 occurrences
W: 268 occurrences
,: 2959 occurrences
M: 163 occurrences
D: 147 occurrences
L: 181 occurrences
A: 261 occurrences

: 1645 occurrences
C: 129 occurrences
1: 18 occurrences
k: 1348 occurrences
I: 1209 occurrences
8: 5 occurrences
7: 5 occurrences
U: 27 occurrences
v: 1786 occurrences
N: 138 occurrences
b: 2477 occurrences
w: 4492 occurrences
F: 109 occurrences
T: 526 occurrences
j: 127 occurrences
': 461 occurrences
z: 108 occurrences
G: 111 occurrences
-: 259 occurrences
E: 83 occurrences
": 1697 occurrences
x: 290 occurrences
—: 116 occurrences
q: 137 occurrences
?: 208 occurrences
Y: 162 occurrences
!: 85 occurrences
;: 100 occurrences
V: 11 occurrences
æ: 1 occurrences
2: 14 occurrences
K: 10 occurrences
4: 9 occurrences
Q: 1 occurrences
3: 12 occurrences
9: 3 occurrences
6: 7 occurrences
5: 3 occurrences
0: 2 occurrences
]: 2 occurrences
ñ: 4 occurrences
Z: 2 occurrences
[: 1 occurrences
^: 1 occurrences
é: 1 occurrences
(: 1 occurrences
): 1 occurrences
```

Note that only those letters that actually occur in the text are shown. Some punctuation marks that are possible in English, but were never used in the text, are omitted completely. The blank line partway through the output may surprise you. That’s actually saying that the newline character, `\\n`, appears 1645 times in the text. In other words, there are 1645 lines of text in the file. Let’s test that hypothesis.

```python
f = open("scarlet.txt", "r")
txt_lines = f.readlines()

print(len(txt_lines))
print(txt_lines[70:85])
```

**Output** :

```
1645
['"No. Heaven knows what the objects of his studies are. But here we are, and you must form your own impressions about him." As he spoke, we turned down a narrow lane and passed through a small side-door, which opened into a wing of the great hospital. It was familiar ground to me, and I needed no guiding as we ascended the bleak stone staircase and made our way down the long corridor with its vista of whitewashed wall and dun-coloured doors. Near the further end a low arched passage branched away from it and led to the chemical laboratory.\n', '\n', 'This was a lofty chamber, lined and littered with countless bottles. Broad, low tables were scattered about, which bristled with retorts, test-tubes, and little Bunsen lamps, with their blue flickering flames. There was only one student in the room, who was bending over a distant table absorbed in his work. At the sound of our steps he glanced round and sprang to his feet with a cry of pleasure, "I have found it! I have found it," he shouted to my companion, running towards us with a test-tube in his hand. "I have found a re-agent which is precipitated by hoemoglobin, and by nothing else." Had he discovered a gold mine, greater delight could not have shone upon his features.\n', '\n', '"Dr Watson, Mr Sherlock Holmes," said Stamford, introducing us.\n', '\n', '"How are you?" he said cordially, gripping my hand with a strength for which I should hardly have given him credit. "You have been in Afghanistan, I perceive."\n', '\n', '"How on earth did you know that?" I asked in astonishment.\n', '\n', '"Never mind," said he, chuckling to himself. "The question now is about hæmoglobin. No doubt you see the significance of this discovery of mine?"\n', '\n', '"It is interesting, chemically, no doubt," I answered, "but practically—"\n', '\n', '"Why, man, it is the most practical medico-legal discovery for years. Don\'t you see that it gives us an infallible test for blood stains. Come over here now!" He seized me by the coat-sleeve in his eagerness, and drew me over to the table at which he had been working. "Let us have some fresh blood," he said, digging a long bodkin into his finger, and drawing off the resulting drop of blood in a chemical pipette. "Now, I add this small quantity of blood to a litre of water. You perceive that the resulting mixture has the appearance of pure water. The proportion of blood cannot be more than one in a million. I have no doubt, however, that we shall be able to obtain the characteristic reaction." As he spoke, he threw into the vessel a few white crystals, and then added some drops of a transparent fluid. In an instant the contents assumed a dull mahogany colour, and a brownish dust was precipitated to the bottom of the glass jar.\n']
```

----
----

**Check Your Understanding**

**Q1** : Which of the following will print out True if there are more occurrences of e than t in the text of A Study in Scarlet, and False if t occurred more frequently (assumming that the previous code, from dict_accum_5, has already run.)

A. print txt['e'] > txt['t'] <br>
B. print x['e'] > x['t'] ✅ <br>
C. print x[e] > x[t] <br>
D. print x[c] > txt[c] <br>
E. print e[x] > t[x] <br>

---

**Q2** : Provided is a string saved to the variable name `sentence`. Split the string into a list of words, then create a dictionary that contains each word and the number of times it occurs. Save this dictionary to the variable name `word_counts`.

```python
# Given
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."



# Solution
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
lst = sentence.split()
word_counts = {}

for word in lst:
	if word not in word_counts:
		word_counts[word] = 0
	word_counts[word] += 1

print(word_counts)
```

**Output** :

```
{'The': 1, 'dog': 1, 'chased': 1, 'the': 3, 'rabbit': 2, 'into': 1, 'forest': 1, 'but': 1, 'was': 1, 'too': 1, 'quick.': 1}
```

----

**Q3** : Create a dictionary called `char_d` from the string `stri`, so that the key is a character and the value is how many times it occurs.

```python
# Given
stri = "what can I do"



# Solution
stri = "what can I do"
char_d = {}

for char in stri:
	if char not in char_d:
		char_d[char] = 0
	char_d[char] += 1

print(char_d)
```

**Output** :

```
{'w': 1, 'h': 1, 'a': 2, 't': 1, ' ': 3, 'c': 1, 'n': 1, 'I': 1, 'd': 1, 'o': 1}
```

----

#### 2.6. Accumulating Results From a Dictionary

Just as we have iterated through the elements of a list to accumulate a result, we can also iterate through the keys in a dictionary, accumulating a result that may depend on the values associated with each of the keys.

For example, suppose that we wanted to compute a Scrabble score for the Study in Scarlet text. Each occurrence of the letter ‘e’ earns one point, but ‘q’ earns 10. We have a second dictionary, stored in the variable `letter_values`. Now, to compute the total score, we start an accumulator at 0 and go through each of the letters in the counts dictionary. For each of those letters that has a letter value (no points for spaces, punctuation, capital letters, etc.), we add to the total score.


```python
f = open("scarlet.txt", "r")
txt = f.read()

x = {}
for c in txt:
	if c not in x:
		x[c] = 0
	x[c] = x[c] + 1

letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}

tot = 0
for y in x:
	if y in letter_values:
		tot = tot + letter_values[y] * x[y]

print(tot)
print(letter_values)
```

**Output** :

```
317940
```

Line 18 is the tricky one. We are updating the variable tot to have its old number plus the score for the current letter times the number of occurrences of that letter. Try changing some of the letter values and see how it affects the total. Try changing txt to be just a single word that you might play in Scrabble.


----
----

**Check Your Understanding**

**Q1** : The dictionary `travel` contains the number of countries within each continent that Jackie has traveled to. Find the total number of countries that Jackie has been to, and save this number to the variable name `total`. Do not hard code this!


```python
# Given
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}



# Solution
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total = 0

for v in travel:
	total = total + travel[v]
print(total)
```

**Output** :

```
19
```

-----


**Q2** : Write a program that finds the key in a dictionary that has the maximum value. If two keys have the same maximum value, it’s OK to print out either one. Fill in the skeleton code


```python
# Given
d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = d.keys()
# initialize variable best_key_so_far to be the first key in d
for k in ks:
    # check if the value associated with the current key is
    # bigger than the value associated with the best_key_so_far
    # if so, save the current key as the best so far

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))



# Solution
d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = d.keys()
big_number = None
best_key_so_far = None
for k in ks:
	if big_number == None:
		big_number = d[k]
		best_key_so_far = k
	elif d[k] >= big_number :
		big_number = d[k]
		best_key_so_far = k
	else:
		pass

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))
```

**Output** :

```
key e has the highest value, 312
```

-----


**Q3** : Create a dictionary called `d` that keeps track of all the characters in the string `placement` and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to `min_value`.


```python
# Given
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."



# Solution
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}
min_val = None
min_value = None

for char in placement:
	if char not in d:
		d[char] = 0
	d[char] += 1

print(d)

for key in d:
	if min_val == None:
		min_val = d[key]
		min_value = key
	elif d[key] < min_val:
		min_val = d[key]
		min_value = key
	else:
		pass

print(min_value)
```

**Output** :

```
{'B': 2, 'e': 17, 'a': 12, 'c': 8, 'h': 4, 's': 10, ' ': 27, 'r': 7, 'o': 10, 'l': 8, 'p': 6, 't': 8, 'v': 3, 'i': 13, 'n': 7, 'g': 2, 'w': 3, 'M': 3, 'k': 2, 'd': 2, '.': 2, 'x': 1}
x
```

-----


**Q4** : Create a dictionary called `lett_d` that keeps track of all of the characters in the string `product` and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to `max_value`.


```python
# Given
product = "iphone and android phones"


# Solution
product = "iphone and android phones"
lett_d = {}
max_value = None
value = None

for char in product:
	if char not in lett_d:
		lett_d[char] = 0
	lett_d[char] += 1

print(lett_d)

for key in lett_d:
	if value == None:
		value = lett_d[key]
		max_value = key
	elif value <= lett_d[key]:
		value = lett_d[key]
		max_value = key
print(value)
print(max_value)
```

**Output** :

```
{'i': 2, 'p': 2, 'h': 2, 'o': 3, 'n': 4, 'e': 2, ' ': 3, 'a': 2, 'd': 3, 'r': 1, 's': 1}
4
n
```

-----


**Q5** : `schedule` is a dictionary where a class name is a key and its value is how many credits it was worth. Go through and accumulate the total number of credits that have been earned so far and assign that to the variable `total_credits`. Do not hardcode.


```python
# Given
schedule = {"UARTS 150": 3,
						"SPANISH 103": 4,
						"ENGLISH 125": 4,
						"SI 110": 4,
						"ENS 356": 2,
						"WOMENSTD 240": 4,
						"SI 106": 4,
						"BIO 118": 3,
						"SPANISH 231": 4,
						"PSYCH 111": 4,
						"LING 111": 3,
						"SPANISH 232": 4,
						"STATS 250": 4,
						"SI 206": 4,
						"COGSCI 200": 4,
						"AMCULT 202": 4,
						"ANTHRO 101": 4}


# Solution
total_credits = 0

for k in schedule:
	total_credits += schedule[k]

print(total_credits)
```

**Output** :

```
63
```

-----

#### 2.7. Chapter Assessments & Exercises

#### Assessments

**A1**. At the halfway point during the Rio Olympics, the United States had 70 medals, Great Britain had 38 medals, China had 45 medals, Russia had 30 medals, and Germany had 17 medals. Create a dictionary assigned to the variable `medal_count` with the country names as the keys and the number of medals the country had as each key’s value.


```python
medal_count = {"United States": 70, "Great Britain": 38, "China": 45, "Russia": 30, "Germany": 17}
print(medal_count)
```

**Output** :

```
{'United States': 70, 'Great Britain': 38, 'China': 45, 'Russia': 30, 'Germany': 17}
```

-----

**A2**. Given the dictionary `swimmers`, add an additional key-value pair to the dictionary with `"Phelps"` as the key and the integer `23` as the value. Do not rewrite the entire dictionary.

```python
# Given
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4}


# Solution
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4}
swimmers["Phelps"] = 23
print(swimmers)
```

**Output** :

```
{'Manuel': 4, 'Lochte': 12, 'Adrian': 7, 'Ledecky': 5, 'Dirado': 4, 'Phelps': 23}
```

-----

**A3**. Add the string “hockey” as a key to the dictionary `sports_periods` and assign it the value of 3. Do not rewrite the entire dictionary.

```python
# Given
sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2}


# Solution
sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2}
sports_periods["hockey"]=3
print(sports_periods)
```

**Output** :

```
{'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2, 'hockey': 3}
```

-----

**A4**. The dictionary `golds` contains information about how many gold medals each country won in the 2016 Olympics. But today, Spain won 2 more gold medals. Update `golds` to reflect this information.

```python
# Given
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}


# Solution
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
golds["Spain"] += 2
print(golds["Spain"])
```

**Output** :

```
21
```

-----


**A3**. Add the string “hockey” as a key to the dictionary `sports_periods` and assign it the value of 3. Do not rewrite the entire dictionary.

```python
# Given
sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2}


# Solution
sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2}
sports_periods["hockey"]=3
print(sports_periods)
```

**Output** :

```
{'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2, 'hockey': 3}
```

-----

**A5**.  Create a list of the countries that are in the dictionary `golds`, and assign that list to the variable name `countries`. Do not hard code this.

```python
# Given
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}


# Solution
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
countries = list(golds.keys())
print(countries)
```

**Output** :

```
['Italy', 'USA', 'Brazil', 'China', 'Spain', 'Canada', 'Argentina', 'England']
```

-----


**A6**. Provided is the dictionary, `medal_count`, which lists countries and their respective medal count at the halfway point in the 2016 Rio Olympics. Using dictionary mechanics, assign the medal count value for `"Belarus"` to the variable `belarus`. Do not hardcode this.

```python
# Given
medal_count = {'United States': 70,
								'Great Britain':38,
								'China':45,
								'Russia':30,
								'Germany':17,
								'Italy':22,
								'France': 22,
								'Japan':26,
								'Australia':22,
								'South Korea':14,
								'Hungary':12,
								'Netherlands':10,
								'Spain':5,
								'New Zealand':8,
								'Canada':13,
								'Kazakhstan':8,
								'Colombia':4,
								'Switzerland':5,
								'Belgium':4,
								'Thailand':4,
								'Croatia':3,
								'Iran':3,
								'Jamaica':3,
								'South Africa':7,
								'Sweden':6,
								'Denmark':7,
								'North Korea':6,
								'Kenya':4,
								'Brazil':7,
								'Belarus':4,
								'Cuba':5,
								'Poland':4,
								'Romania':4,
								'Slovenia':3,
								'Argentina':2,
								'Bahrain':2,
								'Slovakia':2,
								'Vietnam':2,
								'Czech Republic':6,
								'Uzbekistan':5}



# Solution
belarus = medal_count["Belarus"]
print(belarus)
```

**Output** :

```
4
```

-----

**A6**. The dictionary `total_golds` contains the total number of gold medals that countries have won over the course of history. Use dictionary mechanics to find the number of golds Chile has won, and assign that number to the variable name `chile_golds`. Do not hard code this!

```python
# Given
total_golds = {"Italy": 114,
								"Germany": 782,
								"Pakistan": 10,
								"Sweden": 627,
								"USA": 2681,
								"Zimbabwe": 8,
								"Greece": 111,
								"Mongolia": 24,
								"Brazil": 108,
								"Croatia": 34,
								"Algeria": 15,
								"Switzerland": 323,
								"Yugoslavia": 87,
								"China": 526,
								"Egypt": 26,
								"Norway": 477,
								"Spain": 133,
								"Australia": 480,
								"Slovakia": 29,
								"Canada": 22,
								"New Zealand": 100,
								"Denmark": 180,
								"Chile": 13,
								"Argentina": 70,
								"Thailand": 24,
								"Cuba": 209,
								"Uganda": 7,  
								"England": 806,
								"Denmark": 180,
								"Ukraine": 122,
								"Bahamas": 12}




# Solution
chile_golds = total_golds["Chile"]
print(chile_golds)
```

**Output** :

```
13
```

-----


**A7**. Provided is a dictionary called `US_medals` which has the first 70 metals that the United States has won in 2016, and in which category they have won it in. Using dictionary mechanics, assign the value of the key `"Fencing`" to a variable `fencing_value`. Remember, do not hard code this.


```python
# Given
US_medals = {"Swimming": 33,
							"Gymnastics": 6,
							"Track & Field": 6,
							"Tennis": 3,
							"Judo": 2,
							"Rowing": 2,
							"Shooting": 3,
							"Cycling - Road": 1,
							"Fencing": 4,
							"Diving": 2,
							"Archery": 2,
							"Cycling - Track": 1,
							"Equestrian": 2,
							"Golf": 1,
							"Weightlifting": 1}





# Solution
fencing_value = US_medals["Fencing"]
print(fencing_value)
```

**Output** :

```
4
```

-----

**A8**. The dictionary `Junior` shows a schedule for a junior year semester. The key is the course name and the value is the number of credits. Find the total number of credits taken this semester and assign it to the variable `credits`. Do not hardcode this – use dictionary accumulation!


```python
# Given
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}


# Solution
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0

for k in Junior:
    credits += Junior[k]
print(credits)
```

**Output** :

```
18
```

-----

**A9**. Create a dictionary, `freq`, that displays each character in string `str1` as the key and its frequency as the value.


```python
# Given
str1 = "peter piper picked a peck of pickled peppers"


# Solution
str1 = "peter piper picked a peck of pickled peppers"
freq = {}

for char in str1:
	if char not in freq:
		freq[char] = 0
	freq[char] += 1
print(freq)
```

**Output** :

```
{'p': 9, 'e': 8, 't': 1, 'r': 3, ' ': 7, 'i': 3, 'c': 3, 'k': 3, 'd': 2, 'a': 1, 'o': 1, 'f': 1, 'l': 1, 's': 1}
```

-----

**A10**. Provided is a string saved to the variable name `s1`. Create a dictionary named `counts` that contains each letter in `s1` and the number of times it occurs.


```python
# Given
s1 = "hello"


# Solution
s1 = "hello"
counts = {}

for char in s1:
	if char not in counts:
		counts[char] = 0
	counts[char] += 1

print(counts)
```

**Output** :

```
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

-----
-----

**A11**. Create a dictionary, `freq_words`, that displays each word in string `str1` as the key and its frequency as the value.


```python
# Given
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"


# Solution
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}

for word in str1.split():
	if word not in freq_words:
		freq_words[word] = 0
	freq_words[word] += 1

print(freq_words)
```

**Output** :

```
{'I': 2, 'wish': 2, 'with': 2, 'all': 1, 'my': 1, 'heart': 1, 'to': 1, 'fly': 1, 'dragons': 1, 'in': 1, 'a': 1, 'land': 1, 'apart': 1}
```

-----

**A12**. Create a dictionary called `wrd_d` from the string `sent`, so that the key is a word and the value is how many times you have seen that word.


```python
# Given
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"


# Solution
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d = {}

for word in sent.split():
	if word not in wrd_d:
		wrd_d[word] = 0
	wrd_d[word] += 1
print(wrd_d)
```

**Output** :

```
{'Singing': 1, 'in': 2, 'the': 2, 'rain': 2, 'and': 1, 'playing': 1, 'are': 1, 'two': 1, 'entirely': 1, 'different': 1, 'situations': 1, 'but': 1, 'both': 1, 'can': 1, 'be': 1, 'good': 1}
```

-----


**A13**. Create the dictionary `characters` that shows each character from the string `sally` and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable `best_char`.


```python
# Given
sally = "sally sells sea shells by the sea shore"


# Solution
sally = "sally sells sea shells by the sea shore"
characters = {}
best_char = None

for c in sally:
	if c not in characters:
		characters[c] = 0
	characters[c] += 1

for i in list(characters.keys()):
	if best_char == None:
		best_char = i
	else:
		if characters[i] >= characters[best_char]:
			best_char = i

print(best_char, characters[best_char])
```

**Output** :

```
s 8
```

-----


**A14**. Do the same as above but now find the least frequent letter. Create the dictionary `characters` that shows each character from string `sally` and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable `worst_char`.


```python
# Given
sally = "sally sells sea shells by the sea shore"


# Solution
sally = "sally sells sea shells by the sea shore"
characters = {}
worst_char = None

for c in sally:
	if c not in characters:
		characters[c] = 0
	characters[c] += 1

for i in list(characters.keys()):
	if worst_char == None:
		worst_char = i
	else:
		if characters[i] <= characters[worst_char]:
			worst_char = i

print("The least frequent letter is", worst_char, "and it appears", characters[worst_char], "times")
```

**Output** :

```
The least frequent letter is r and it appears 1 times
```

-----

**A15**. Create a dictionary named `letter_counts` that contains each letter and the number of times it occurs in `string1`. Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.


```python
# Given
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."



# Solution
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
letter_counts = {}

for c in string1.lower():
	if c not in letter_counts:
		letter_counts[c] = 0
	letter_counts[c] += 1

print(letter_counts)
```

**Output** :

```
{'t': 19, 'h': 11, 'e': 29, 'r': 12, ' ': 53, 'i': 14, 's': 15, 'a': 17, 'd': 7, 'n': 15, 'f': 9, 'o': 17, 'm': 4, ',': 4, 'w': 6, 'c': 3, 'k': 2, 'l': 11, 'u': 8, '.': 4, 'v': 3, 'y': 1, 'g': 1, 'b': 1}
```

-----


**A16**. Create a dictionary called `low_d` that keeps track of all the characters in the string `p` and notes how many times each character was seen. Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.


```python
# Given
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."




# Solution
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d = {}

for c in p.lower():
	if c not in low_d:
		low_d[c] = 0
	low_d[c] += 1

print(low_d)
```

**Output** :

```
{'s': 5, 'u': 7, 'm': 3, 'e': 12, 'r': 3, ' ': 20, 'i': 3, 'a': 6, 'g': 3, 't': 9, 'o': 8, 'd': 1, '.': 2, 'y': 1, 'h': 6, 'v': 1, 'b': 2, 'c': 2, 'f': 3, 'l': 1, 'n': 1}
```

-----

----
----

#### Exercises


**Q1**. Predict what will print out from the following code. If a line causes a run-time error, comment it out and see whether the rest of your predictions were correct.


```python
d = {'apples': 15, 'grapes': 12, 'bananas': 35}
# print(d['banana'])
d['oranges'] = 20
print(len(d))
print('grapes' in d)
# print(d['pears'])
print(d.get('pears', 0))
fruits = d.keys()
print(fruits)
del d['apples']
print('apples' in d)
```

**Output** :

```
4
True
0
dict_keys(['apples', 'grapes', 'bananas', 'oranges'])
False
```

-----

**Q2**. Here’s a table of English to Pirate translations

|English|	Pirate|
|--|--|
|sir|	matey|
|hotel|	fleabag inn|
|student|	swabbie|
|boy|	matey|
|madam|	proud beauty|
|professor|	foul blaggart|
|restaurant|	galley|
|your	|yer|
|excuse	|arr|
|students	|swabbies|
|are|	be|
|lawyer	|foul blaggart|
|the|	th’|
|restroom|	head|
|my	|me|
|hello|	avast|
|is|	be|
|man|	matey|

Write a program that asks the user for a sentence in English and then translates that sentence to Pirate.

```python
pirish = {
			"sir": "matey",
			"hotel": "fleabag inn",
			"student": "swabbie",
			"boy": "matey",
			"madam": "proud beauty",
			"professor": "foul blaggart",
			"restaurant": "galley",
			"your": "yer",
			"excuse": "arr",
			"students": "swabbies",
			"are": "be",
			"lawyer": "foul blaggart",
			"the": "th’",
			"restroom": "head",
			"my": "me",
			"hello": "avast",
			"is": "be",
			"man": "matey",
}

sentence = input("Enter a sentence : ").split()
translated = []

for word in sentence:
	if word in pirish:
		word = pirish[word]
	translated.append(word)

pirate_sentence = " ".join(translated)
print(pirate_sentence)
```

**Output** :

```
Enter a sentence : Oo hello sir ! Where is the restaurant restroom ? Hi madam ! Will you excuse me ? I just gonna kill your lawyer !
Oo avast matey ! Where be th’ galley head ? Hi proud beauty ! Will you arr me ? I just gonna kill yer foul blaggart !
```

-----


**Q3**. Write a program that finds the most used 7 letter word in scarlet.txt.


```python
# Given
f = open('scarlet.txt', 'r')


# Solution
f = open('scarlet.txt', 'r')
text = f.read()
word_list = text.split()
words = {}
seven_letters = []
most_used = None

for word in word_list:
	if word not in words:
		words[word] = 0
	words[word] += 1

for wrd in words:
	if len(wrd) >= 7:
		seven_letters.append(wrd)

for wd in seven_letters:
	if most_used == None:
		most_used = wd
	else :
		if words[wd] > words[most_used]:
			most_used = wd
		else:
			pass
print(most_used)
print(words[most_used])
```

**Output** :

```
through
57
```

----

-----


**Q4**. Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored. A sample run of the program might look this this:

![](http://i67.tinypic.com/6elp1z.png)


```python
sentence = input("Please enter a sentence: ").lower()
chars = {}

for char in sentence:
	if char not in chars:
		chars[char] = 0
	chars[char] += 1

ord_chars = list(chars.keys())
ord_chars.sort()

for it in ord_chars:
	print("{} {}".format(it, chars[it]))
```

**Output** :

```
Please enter a sentence: ThiS is String with Upper and lower case Letters.
  8
. 1
a 2
c 1
d 1
e 5
g 1
h 2
i 4
l 2
n 2
o 1
p 2
r 4
s 5
t 5
u 1
w 2
```

----

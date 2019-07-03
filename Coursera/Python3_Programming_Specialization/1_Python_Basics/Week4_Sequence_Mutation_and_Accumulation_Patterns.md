# Python Basics
*Coursera | Python 3 Programming Specialization | Course 1*

## Week 4 : Sequence Mutation and Accumulation Patterns

### Sequence Mutation

#### Mutability

Some Python collection types - strings and lists so far - are able to change and some are not. If a type is able to change, then it is said to be mutable. If the type is not able to change then it is said to be immutable. This will be expanded below.


#### Lists are Mutable
Unlike strings, lists are **mutable**. This means we can change an item in a list by accessing it directly as part of the assignment statement. Using the indexing operator (square brackets) on the left side of an assignment, we can update one of the list items.


```python
fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)
```

**Output** :

```
['banana', 'apple', 'cherry']
['pear', 'apple', 'orange']
```

An assignment to an element of a list is called **item assignment**. Item assignment does not work for strings. Recall that strings are immutable.

By combining assignment with the slice operator we can update several elements at once.

```python
alist = ["a", "b", "c", "d", "e", "f"]
alist[1:3] = ["x", "y"]
print(alist)
```

**Output** :

```
['a', 'x', 'y', 'd', 'e', 'f']
```

We can also remove elements from a list by assigning the empty list to them.

```python
alist = ["a", "b", "c", "d", "e", "f"]
alist[1:3] = []
print(alist)
```

**Output** :

```
['a', 'd', 'e', 'f']
```

We can even insert elements into a list by squeezing them into an empty slice at the desired location.


```python
alist = ["a", "d", "f"]
alist[1:1] = ["b", "c"]
print(alist)

alist[4:4] = ["e"]
print(alist)
```

**Output** :

```
['a', 'b', 'c', 'd', 'f']
['a', 'b', 'c', 'd', 'e', 'f']
```



#### Strings are Immutable

One final thing that makes strings different from some other Python collection types is that you are not allowed to modify the individual characters in the collection. It is tempting to use the `[]` operator on the left side of an assignment, with the intention of changing a character in a string. For example, in the following code, we would like to change the first letter of `greeting`.


```python
greeting = "Hello, world!"
greeting[0] = "J"
print(greeting)
```

**Output** :

```
Traceback (most recent call last):
  File "Week4_Sequence_Mutation_and_Accumulation_Patterns.py", line 37, in <module>
    greeting[0] = "J"
TypeError: 'str' object does not support item assignment
```

Instead of producing the output `Jello, world!`, this code produces the runtime error `TypeError: 'str' object does not support item assignment`.

Strings are **immutable**, which means you cannot change an existing string. The best you can do is create a new string that is a variation on the original.


```python
greeting = "Hello, world!"
newGreeting = "J" + greeting[1:]
print(newGreeting)
print(greeting)
```

**Output** :

```
Jello, world!
Hello, world!
```

The solution here is to concatenate a new first letter onto a slice of greeting. This operation has no effect on the original string.

While it’s possible to make up new variable names each time we make changes to existing values, it could become difficult to keep track of them all.


```python
phrase = "many moons"
print(phrase)
phrase_expanded = phrase + " and many stars"
print(phrase_expanded)
phrase_larger = phrase_expanded + " litter"
print(phrase_larger)
phrase_complete = "M" + phrase_larger[1:] + " the night sky."
print(phrase_complete)
excited_phrase_complete = phrase_complete[:-1] + "!"
print(excited_phrase_complete)
```

**Output** :

```
many moons
many moons and many stars
many moons and many stars litter
Many moons and many stars litter the night sky.
Many moons and many stars litter the night sky!
```

The more that you change the string, the more difficult it is to come up with a new variable to use. It’s perfectly acceptable to re-assign the value to the same variable name in this case.


#### Tuples are Immutable

As with strings, if we try to use item assignment to modify one of the elements of a tuple, we get an error. In fact, that’s the key difference between lists and tuples: tuples are like immutable lists. None of the operations on lists that mutate them are available for tuples. Once a tuple is created, it can’t be changed.

```python
julia[0] = 'X'  # TypeError: 'tuple' object does not support item assignment
```

----
----

**Check Your Understanding**

**E1** : What is printed by the following statements?

```python
alist = [4, 2, 8, 6, 5]
alist[2] = True
print(alist)
```

A. [4,2,True,8,6,5] <br>
B. [4,2,True,6,5] ✅ <br>
C. Error, it is illegal to assign <br>

---

**E2** : What is printed by the following statements:

```python
s = "Ball"
s[0] = "C"
print(s)
```

A. Ball <br>
B. Call <br>
C. Error ✅ <br>

---


#### List Element Deletion

Using slices to delete list elements can be awkward and therefore error-prone. Python provides an alternative that is more readable. The `del` statement removes an element from a list by using its position.

```python
a = ["one", "two", "three"]
del a[1]
print(a)

alist = ["a", "b", "c", "d", "d", "f"]
del alist[1:5]
print(alist)
```


**Output** :

```
['one', 'three']
['a', 'f']
```

As you might expect, `del` handles negative indices and causes a runtime error if the index is out of range. In addition, you can use a slice as an index for `del`. As usual, slices select all the elements up to, but not including, the second index.


#### Objects and References

If we execute these assignment statements,


```python
a = "banana"
b = "banana"
```

we know that `a` and `b` will refer to a string with the letters `"banana"`. But we don’t know yet whether they point to the same string.

There are two possible ways the Python interpreter could arrange its internal states:

![](https://fopp.umsi.education/runestone/static/fopp/_images/refdiag1.png)

or

![](https://fopp.umsi.education/runestone/static/fopp/_images/refdiag2.png)

In one case, `a` and `b` refer to two different string objects that have the same value. In the second case, they refer to the same object. Remember that an object is something a variable can refer to.

We can test whether two names refer to the same object using the `is` operator. The `is` operator will return true if the two references are to the same object. In other words, the references are the same. Try our example from above.

```python
a = "banana"
b = "banana"

print(a is b)
```

**Output** :

```
True
```

The answer is `True`. This tells us that both `a` and `b` refer to the same object, and that it is the second of the two reference diagrams that describes the relationship. Python assigns every object a unique id and when we ask `a is b` what python is really doing is checking to see if `id(a) == id(b)`.

```python
a = "banana"
b = "banana"

print(id(a))
print(id(b))
```

**Output** :

```
4344270384
4344270384
```

Since strings are immutable, the Python interpreter often optimizes resources by making two names that refer to the same string value refer to the same object. You shouldn’t count on this (that is, use `==` to compare strings, not `is`), but don’t be surprised if you find that two variables,each bound to the string “banana”, have the same id..

This is not the case with lists, which never share an id just because they have the same contents. Consider the following example. Here, `a` and `b` refer to two different lists, each of which happens to have the same element values. They need to have different ids so that mutations of list `a` do not affect list `b`.

```python
a = [81, 82, 83]
b = [81, 82, 83]

print(a is b)

print(a == b)

print(id(a))
print(id(b))
```

**Output** :

```
False
True
4485664648
4487463176
```

The reference diagram for this example looks like this:

![](https://fopp.umsi.education/runestone/static/fopp/_images/refdiag3.png)


`a` and `b` have equivalent values but do not refer to the same object. Because their contents are equivalent, `a==b` evaluates to `True`; because they are not the same object, `a is b` evaluates to `False`.

----


#### Aliasing

Since variables refer to objects, if we assign one variable to another, both variables refer to the same object:

```python
a = [81, 82, 83]
b = a

print(a is b)
```

**Output** :

```
True
```

In this case, the reference diagram looks like this:

![](https://fopp.umsi.education/runestone/static/fopp/_images/refdiag4.png)


Because the same list has two different names, `a` and `b`, we say that it is **aliased**. Changes made with one alias affect the other. In the codelens example below, you can see that `a` and `b` refer to the same list after executing the assignment statement `b = a`.


```python
a = [81, 82, 83]
b = [81, 82, 83]

print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)
```

**Output** :

```
False
True
True
[5, 82, 83]
```

Although this behavior can be useful, it is sometimes unexpected or undesirable. In general, it is safer to avoid aliasing when you are working with mutable objects. Of course, for immutable objects, there’s no problem. That’s why Python is free to alias strings and integers when it sees an opportunity to economize.

-----
------


**Check Your Understanding**

**E1** : What is the value of y after the following code has been evaluated:

```python
w = ["Jamboree", "get-together", "party"]
y = ["celebration"]
y = w
```

A. ['Jamboree', 'get-together', 'party'] ✅ <br>
B. ['celebration'] <br>
C. ['celebration', 'Jamboree', 'get-together', 'party'] <br>
D. ['Jamboree', 'get-together', 'party', 'celebration'] <br>

---

**E2** : What is printed by the following statements?

```python
alist = [4, 2, 8, 6, 5]
blist = alist
blist[3] = 999
print(alist)
```

A. [4,2,8,6,5] <br>
B. [4,2,8,999,5] ✅<br>

---


#### Cloning Lists

If we want to modify a list and also keep a copy of the original, we need to be able to make a copy of the list itself, not just the reference. This process is sometimes called **cloning**, to avoid the ambiguity of the word copy.

The easiest way to clone a list is to use the slice operator.

Taking any slice of `a` creates a new list. In this case the slice happens to consist of the whole list.


```python
a = [81, 82, 83]

b = a[:]
print(a == b)
print(a is b)

b[0] = 5
print(a)
print(b)
```

**Output** :

```
True
False
[81, 82, 83]
[5, 82, 83]
```

Now we are free to make changes to `b` without worrying about `a`.

-----
------


**Check Your Understanding**

**E1** : What is printed by the following statements?

```python
alist = [4, 2, 8, 6, 5]
blist = alist * 2
blist[3] = 999
print(alist)
```

A. [4,2,8,999,5,4,2,8,6,5] <br>
B. [4,2,8,999,5] <br>
C. [4,2,8,6,5] ✅ <br>

---



### Methods on Strings and Lists

#### Methods on Lists

You’ve seen some methods already, like the `count` and `index` methods. Methods are either mutating or non-mutating. Mutating methods are ones that change the object after the method has been used. Non-mutating methods do not change the object after the method has been used.

The `count` and `index` methods are both non-mutating. Count returns the number of occurances of the argument given but does not change the original string or list. Similarly, index returns the leftmost occurance of the argument but does not change the original string or list. Below we’ll talk about list methods in general. Keep an eye out for methods that are mutating!

#### List Methods

The dot operator can also be used to access built-in methods of list objects. `append` is a list method which adds the argument passed to it to the end of the list. Continuing with this example, we show several other list methods. Many of them are easy to understand.



```python
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)

print(mylist.count(12))
print(mylist.count(5))

print(mylist.index(3))
print(mylist.index(27))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)

mylist.pop(0)
print(mylist)
```

**Output** :

```
[5, 27, 3, 12]
[5, 12, 27, 3, 12]
2
1
3
2
[12, 3, 27, 12, 5]
[3, 5, 12, 12, 27]
[3, 12, 12, 27]
27
[3, 12, 12]
[12, 12]
```

There are two ways to use the `pop` method. The first, with no parameter, will remove and return the last item of the list. If you provide a parameter for the position, `pop` will remove and return the item at that position. Either way the list is changed.

The following table provides a summary of the list methods shown above. The column labeled `result` gives an explanation as to what the return value is as it relates to the new value of the list. The word **mutator** means that the list is changed by the method but nothing is returned (actually `None` is returned). A **hybrid** method is one that not only changes the list but also returns a value as its result. Finally, if the result is simply a return, then the list is unchanged by the method.

Be sure to experiment with these methods to gain a better understanding of what they do.


| Method | Parameters | Result | Descriptiion |
|--|--|--|--|
| `append` | item | mutator | Adds a new item to the end of a list |
| `insert` | position, item | mutator | Inserts a new item at the position given |
| `pop` | none | hybrid | Removes and returns the last item |
| `pop` | position | hybrid | Removes and returns the item at position |
| `sort` | none | mutator | Modifies a list to be sorted |
| `reverse` | none | mutator | Modifies a list to be in reverse order |
| `index` | item | return idx | Returns the position of first occurence of item |
| `count` | item | return ct | Returns the number of ccurences of item |
| `remove` | item | mutator | Removes the first occurence of item |


Details for these and others can be found in the [Python Documentation](http://docs.python.org/py3k/library/stdtypes.html#sequence-types-str-bytes-bytearray-list-tuple-range).


It is important to remember that methods like `append`, `sort`, and `reverse` all return `None`. They change the list; they don’t produce a new list. So, while we did reassignment to increment a number, as in `x = x + 1`, doing the analogous thing with these operations will lose the entire list contents (see line 8 below).

```python
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist = mylist.sort()			# probably an error
print(mylist)
```

**Output** :

```
None
```

-----
------


**Check Your Understanding**

**E1** : What is printed by the following statements?

```python
alist = [4, 2, 8, 6, 5]
alist.append(True)
alist.append(False)
print(alist)
```

A. [4,2,8,6,5,False,True] <br>
B. [4,2,8,6,5,True,False] ✅<br>
C. [True,False,4,2,8,6,5] <br>

---

#### Append vs. Concatenate

The `append` method adds a new item to the end of a list. It is also possible to add a new item to the end of a list by using the concatenation operator. However, you need to be careful.

Consider the following example. The original list has 3 integers. We want to add the word “cat” to the end of the list.


```python
origlist = [45, 32, 88]
origlist.append("cat")
print(origlist)
```

**Output** :

```
[45, 32, 88, 'cat']
```

Here we have used `append` which simply modifies the list. In order to use concatenation, we need to write an assignment statement that uses the accumulator pattern:

```python
origlist = origlist + ["cat"]
```

Note that the word “cat” needs to be placed in a list since the concatenation operator needs two lists to do its work.

It is also important to realize that with append, the original list is simply modified. On the other hand, with concatenation, an entirely new list is created.

This might be difficult to understand since these two lists appear to be the same. In Python, every object has a unique identification tag. Likewise, there is a built-in function that can be called on any object to return its unique id. The function is appropriately called id and takes a single parameter, the object that you are interested in knowing about. You can see in the example below that a real id is usually a very large integer value (corresponding to an address in memory). In the textbook though the number will likely be smaller.


```
>>> alist = [4, 5, 6]
>>> id(alist)
4300840544
>>>
```

```python
origlist = [45, 32, 88]
print("origlist:", origlist)
print("the identifier:", id(origlist))
newlist = origlist + ["cat"]
print("newlist:", newlist)
print("the identifier:", id(newlist))
origlist.append("cat")
print("origlist:", origlist)
print("the identifier:", id(origlist))
```

**Output** :

```
origlist: [45, 32, 88]
the identifier: 4496656328
newlist: [45, 32, 88, 'cat']
the identifier: 4496655560
origlist: [45, 32, 88, 'cat']
the identifier: 4496656328
```

Note how even though `newlist` and `origlist` appear the same, they have different identifiers.

We have previously described `x += 1` as a shorthand for `x = x + 1`. With lists, += is actually a little different. In particular, origlist `+= [“cat”]` appends `“cat”` to the end of the original list object.

We can use append or concatenate repeatedly to create new objects. If we had a string and wanted to make a new list, where each element in the list is a character in the string, where do you think you should start? In both cases, you’ll need to first create a variable to store the new object.

```python
st = "Warmth"
a = []
```

Then, character by character, you can add to the empty list. The process looks different if you concatentate as compared to using append.

```python
st = "Warmth"
a = []
b = a + [st[0]]
c = b + [st[1]]
d = c + [st[2]]
e = d + [st[3]]
f = e + [st[4]]
g = f + [st[5]]
print(g)
```

**Output** :

```
['W', 'a', 'r', 'm', 't', 'h']
```


```python
st = "Warmth"
a = []
a.append(st[0])
a.append(st[1])
a.append(st[2])
a.append(st[3])
a.append(st[4])
a.append(st[5])
print(a)
```

**Output** :

```
['W', 'a', 'r', 'm', 't', 'h']
```

This might become tedious though, and difficult if the length of the string is long. Can you think of a better way to do this?

-----
------


**Check Your Understanding**

**E1** : What is printed by the following statements?

```python
alist = [4, 2, 8, 6, 5]
alist = alist + 999
print(alist)
```

A. [4,2,8,6,5,999] <br>
B. Error, you cannot concatenate a list with an integer. ✅ <br>


---


#### Non-Mutating Methods on Strings

There are a wide variety of methods for string objects. Try the following program.

```python
ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt)
print(ss)
```

**Output** :

```
HELLO, WORLD
hello, world
Hello, World
```

In this example, `upper` is a method that can be invoked on any string object to create a new string in which all the characters are in uppercase. `lower` works in a similar fashion changing all characters in the string to lowercase. (The original string `ss` remains unchanged. A new string `tt` is created.)

You’ve already seen a few methods, such as `count` and `index`, that work with strings and are non-mutating. In addition to those and `upper` and `lower`, the following table provides a summary of some other useful string methods. There are a few activecode examples that follow so that you can try them out.


| Method | Parameters | Descriptiion |
|--|--|--|
| `upper` | none | Returns a string in all uppercase |
| `lower` | none | Returns a string in all lowercase |
| `count` | item | Returns the number of occurences of item |
| `index` | item | Returns the leftmost index where the substring item is found and causes a runtime error if item is not found|
| `strip` | none | Returns a string with the leading and trailing whitespace removed |
| `replace` | old, new | Replaces all occurrences of old substring with new |
| `format` | substitutions | Involved! See string format method, below |


You should experiment with these methods so that you understand what they do. Note once again that the methods that return strings do not change the original. You can also consult the [Python documentation for strings](http://docs.python.org/3/library/stdtypes.html#string-methods).

```python
ss = "     Hello, World     "

els = ss.count("l")
print(els)

print("***" + ss.strip() + "***")

news = ss.replace("o", "***")
print(news)
```

**Output** :

```
3
***Hello, World***
     Hell***, W***rld
```


```python
food = "banana bread"
print(food.upper())
```

**Output** :

```
BANANA BREAD
```

-----
------


**Check Your Understanding**

**E1** : What is printed by the following statements?

```python
s = "python rocks"
print(s.count("0") + s.count("p"))
```

A. 0 <br>
B. 2 <br>
C. 3 ✅ <br>

---


**E2** : What is printed by the following statements?

```python
s = "python rocks"
print(s[1]*s.index("n"))
```

A. yyyyy  ✅ <br>
B. 55555 <br>
C. n <br>
D. Error, you cannot combine all those things together. <br>

---


#### String Format Method

Until now, we have created strings with variable content using the + operator to concatenate partial strings together. That works, but it’s very hard for people to read or debug a code line that includes variable names and strings and complex expressions. Consider the following:


```python
name = "Rodney Dangerfield"
score = -1    # No respect!
print("Hello " + name + ". Your score is " + str(score))
```

**Output** :

```
Hello Rodney Dangerfield. Your score is -1
```

Or perhaps more realistically:

```python
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]

for person in scores:
  name = person[0]
  score = person[1]
  print("Hello " + name + ". Your score is " + str(score))
```

**Output** :

```
Hello Rodney Dangerfield. Your score is -1
Hello Marlon Brando. Your score is 1
Hello You. Your score is 100
```

In this section, you will learn to write that in a more readable way:


```python
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]

for person in scores:
  name = person[0]
  score = person[1]
  print("Hello {}. Your score is {}.".format(name, score))
```

**Output** :

```
Hello Rodney Dangerfield. Your score is -1.
Hello Marlon Brando. Your score is 1.
Hello You. Your score is 100.
```

In grade school quizzes a common convention is to use fill-in-the blanks. For instance,

Hello _____!

and you can fill in the name of the person greeted, and combine given text with a chosen insertion. We use this as an analogy: Python has a similar construction, better called fill-in-the-braces. The string method `format`, makes substitutions into places in a string enclosed in braces. Run this code:

```python
person = input("Your name: ")
greeting = "Hello {}!".format(person)
print(greeting)
```

**Output** :

```
Your name: Heval
Hello Heval!
```


There are several new ideas here!

The string for the `format` method has a special form, with braces embedded. Such a string is called a format string. Places where braces are embedded are replaced by the value of an expression taken from the parameter list for the `format` method. There are many variations on the syntax between the braces. In this case we use the syntax where the first (and only) location in the string with braces has a substitution made from the first (and only) parameter.

In the code above, this new string is assigned to the identifier `greeting`, and then the string is printed.

The identifier `greeting` was introduced to break the operations into a clearer sequence of steps. However, since the value of `greeting` is only referenced once, it can be eliminated with the more concise version:

```python
person = input("Enter your name: ")
print("Hello {}!".format(person))
```

**Output** :

```
Enter your name: Heval
Hello Heval!
```

There can be multiple substitutions, with data of any type. Next we use floats. Try original price $2.50 with a 7% discount:


```python
origPrice = float(input("Enter the original price: $"))
discount = float(input("Enter discount percentage: "))
newPrice = (1 - discount/100)*origPrice
calculation = "${} discounted by {}% is ${}.".format(origPrice, discount, newPrice)
print(calculation)
```

**Output** :

```
Enter the original price: $20
Enter discount percentage: 20
$20.0 discounted by 20.0% is $16.0.
```

It is important to pass arguments to the `format` method in the correct order, because they are matched positionally into the `{}` places for interpolation where there is more than one.

If you used the data suggested, this result is not satisfying. Prices should appear with exactly two places beyond the decimal point, but that is not the default way to display floats.

Format strings can give further information inside the braces showing how to specially format data. In particular floats can be shown with a specific number of decimal places. For two decimal places, put `:.2f` inside the braces for the monetary values:


```python
origPrice = float(input("Enter the original price: $"))
discount = float(input("Enter discount percentage: "))
newPrice = (1 - discount/100)*origPrice
calculation = "${:.2f} discounted by {}% is ${:.2f}.".format(origPrice, discount, newPrice)
print(calculation)
```

**Output** :

```
Enter the original price: $20
Enter discount percentage: 20
$20.00 discounted by 20.0% is $16.00.
```

The 2 in the format modifier can be replaced by another integer to round to that specified number of digits.

This kind of format string depends directly on the order of the parameters to the format method. There are other approaches that we will skip here, such as explicitly numbering substitutions.

It is also important that you give `format` the same amount of arguments as there are `{}` waiting for interpolation in the string. If you have a `{}` in a string that you do not pass arguments for, you may not get an error, but you will see a weird `undefined` value you probably did not intend suddenly inserted into your string. You can see an example below.

For example,

```python
name = "Sally"
greeting = "Nice to meet you"
s = "Hello, {}. {}."

print(s.format(name, greeting))
print(s.format(greeting, name))
print(s.format(name))   # 2 {}s, only one interpolation item! Not ideal.
```

**Output** :

```
Hello, Sally. Nice to meet you.
Hello, Nice to meet you. Sally.
Traceback (most recent call last):
  File "Week4_Sequence_Mutation_and_Accumulation_Patterns.py", line 300, in <module>
    print(s.format(name))
IndexError: tuple index out of range
```

A technical point: Since braces have special meaning in a format string, there must be a special rule if you want braces to actually be included in the final formatted string. The rule is to double the braces: `{{` and `}}`. For example mathematical set notation uses braces. The initial and final doubled braces in the format string below generate literal braces in the formatted string:


```python
a = 5
b = 9
setStr = "The set is {{{}, {}}}.".format(a, b)
print(setStr)
```

**Output** :

```
The set is {5, 9}.
```

Unfortunately, at the time of this writing, the ActiveCode format implementation has a bug, printing doubled braces, but standard Python prints `{5, 9}`.

----
-----

**Check Your Understanding**


**E1** : What is printed by the following statements?

```python
x = 2
y = 6
print("sum of {} and {} is {}; product: {}.".format(x, y, x+y, x*y))
```

A. Nothing - it causes an error  <br>
B. sum of {} and {} is {}; product: {}. 2 6 8 12  <br>
C. sum of 2 and 6 is 8; product: 12. ✅  <br>
D. sum of {2} and {6} is {8}; product: {12}.  <br>

---

**E2** : What is printed by the following statements?

```python
v = 2.34567
print("{:.1f} {:.2f} {:.7f}".format(v, v, v))
```

A. 2.34567 2.34567 2.34567 <br>
B. 2.3 2.34 2.34567 <br>
C. 2.3 2.35 2.3456700 ✅  <br>

---



### Accumulating Lists and Strings

#### The Accumulator Pattern with Lists

We can accumulate values into a list rather than accumulating a single numeric value. Consider, for example, the following program which transforms a list into a new list by squaring each of the values.

```python
nums = [3, 5, 8]
accum = []
for w in nums:
	x = w ** 2
	accum.append(x)
print(accum)
```

**Output** :

```
[9, 25, 64]
```

Here, we **initialize** the accumulator variable to be an empty list, on line 2.

We **iterate** through the sequence (line 3). On each iteration we transform the item by squaring it (line 4).

The **update** step appends the new item to the list which is stored in the accumulator variable (line 5). The update happens using the .append(), which mutates the list rather than using a reassignment. Instead, we could have written `accum = accum + [x]`, or `accum += [x]`. In either case, we’d need to concatenate a list containing x, not just x itself.

At the end, we have accumulated a new list of the same length as the original, but with each item transformed into a new item. This is called a mapping operation, and we will revisit it in a later chapter.

Note how this differs from mutating the original list, as you saw in a previous section.

----
-----

**Check Your Understanding**


**E1** : What is printed by the following statements?

```python
alist = [4, 2, 8, 6, 5]
blist = []
for item in alist:
	blist.append(item+5)
print(blist)
```

A. [4,2,8,6,5]  <br>
B. [4,2,8,6,5,5]  <br>
C. [9,7,13,11,10]  ✅ <br>
D. Error, you cannot concatenate inside an append.  <br>

---

**E2** : What is printed by the following statements?

```python
lst = [3, 0, 9, 4, 1, 7]
new_list = []
for i in range(len(lst)):
	new_list.append(lst[i]+5)
print(new_list)
```

A. [8,5,14,9,6]  <br>
B. [8,5,14,9,6,12]  ✅ <br>
C. [3,0,9,4,1,7,5]  <br>
D. Error, you cannot concatenate inside an append.  <br>


---


**E3** : For each word in the list `verbs`, add an -ing ending. Save this new list in a new list, `ing`.

```python
# Given
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]



# Solution
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = []
for word in verbs:
    word = word + "ing"
    ing.append(word)
print(ing)
```

**Output**:

```
['kayaking', 'crying', 'walking', 'eating', 'drinking', 'flying']
```


---

**E4** : Given the list of numbers, `numbs`, create a new list of those same numbers increased by 5. Save this new list to the variable `newlist`.

```python
# Given
numbs = [5, 10, 15, 20, 25]


# Solution
numbs = [5, 10, 15, 20, 25]
newlist = []

for num in numbs:
    num += 5
    newlist.append(num)
print(newlist)
```

**Output**:

```
[10, 15, 20, 25, 30]
```

---


**E5** : Now do the same as in the previous problem, but do not create a new list. Overwrite the list numbs so that each of the original numbers are increased by 5.

```python
# Given
numbs = [5, 10, 15, 20, 25]


# Solution
numbs = [5, 10, 15, 20, 25]

for num in numbs:
    new_num = num + 5
    numbs.remove(num)
    numbs.append(new_num)
print(numbs)
```

**Output**:

```
[10, 15, 20, 25, 30]
```

---


**E6** : For each number in `lst_nums`, multiply that number by 2 and append it to a new list called `larger_nums`.

```python
# Given
lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]


# Solution
lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]
larger_nums = []
for number in lst_nums:
    number = number * 2
    larger_nums.append(number)
print(larger_nums)
```

**Output**:

```
[8, 58, 10.6, 20, 4, 3634, 3934, 18, 62.64]
```

---




### The Way of the Programmer




### Python Basics - Final Course Assignment

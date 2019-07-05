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


#### The Accumulator Pattern with Strings

We can also accumulate strings rather than accumulating numbers, as you’ve seen before. The following program isn’t particularly useful for data processing, but we will see more useful things later that accumulate strings.


```python
s = input("Enter some text")
ac = ""

for c in s:
	ac = ac + c + "-" + c + "-"
print(ac)
```

**Output** :

```
Enter some text: hello world
h-h-e-e-l-l-l-l-o-o- - -w-w-o-o-r-r-l-l-d-d-
```

Look carefully at line 4 in the above program (`ac = ac + c + "-" + c + "-`"). In words, it says that the new value of `ac` will be the old value of `ac` concatenated with the current character, a dash, then the current character and a dash again. We are building the result string character by character.

Take a close look also at the initialization of `ac`. We start with an empty string and then begin adding new characters to the end. Also note that I have given it a different name this time, `ac` instead of `accum`. There’s nothing magical about these names. You could use any valid variable and it would work the same (try substituting x for ac everywhere in the above code).

----
-----

**Check Your Understanding**


**E1** : What is printed by the following statements:

```python
s = "ball"
r = ""

for item in s:
	r = item.upper() + r

print(r)
```

A. [4,2,8,6,5]  <br>
B. [4,2,8,6,5,5]  <br>
C. [9,7,13,11,10]  ✅ <br>
D. Error, you cannot concatenate inside an append.  <br>

---

**E2** : For each character in the string already saved in the variable `str1`, add each character to a list called `chars`.

```python
# Given
str1 = "I love python"


# Solution
str1 = "I love python"
chars = []

for char in str1:
    chars.append(char)

print(chars)
```

**Output**:

```
['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n']
```

---

**E3** : Assign an empty string to the variable `output`. Using the `range` function, write code to make it so that the variable `output` has 35 `a` s inside it (like "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"). Hint: use the accumulation pattern!

```python
output = ""

for a in range(35):
    output = output + "a"

print(output)
```

**Output**:

```
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

---


#### The Accumulator Pattern with Strings

We can also accumulate strings rather than accumulating numbers, as you’ve seen before. The following program isn’t particularly useful for data processing, but we will see more useful things later that accumulate strings.


```python
s = input("Enter some text")
ac = ""

for c in s:
	ac = ac + c + "-" + c + "-"
print(ac)
```

**Output** :

```
Enter some text: hello world
h-h-e-e-l-l-l-l-o-o- - -w-w-o-o-r-r-l-l-d-d-
```

Look carefully at line 4 in the above program (`ac = ac + c + "-" + c + "-`"). In words, it says that the new value of `ac` will be the old value of `ac` concatenated with the current character, a dash, then the current character and a dash again. We are building the result string character by character.

Take a close look also at the initialization of `ac`. We start with an empty string and then begin adding new characters to the end. Also note that I have given it a different name this time, `ac` instead of `accum`. There’s nothing magical about these names. You could use any valid variable and it would work the same (try substituting x for ac everywhere in the above code).

----
-----

**Check Your Understanding**


**E1** : What is printed by the following statements:

```python
s = "ball"
r = ""

for item in s:
	r = item.upper() + r

print(r)
```

A. [4,2,8,6,5]  <br>
B. [4,2,8,6,5,5]  <br>
C. [9,7,13,11,10]  ✅ <br>
D. Error, you cannot concatenate inside an append.  <br>

---

**E2** : For each character in the string already saved in the variable `str1`, add each character to a list called `chars`.

```python
# Given
str1 = "I love python"


# Solution
str1 = "I love python"
chars = []

for char in str1:
    chars.append(char)

print(chars)
```

**Output**:

```
['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n']
```

---

**E3** : Assign an empty string to the variable `output`. Using the `range` function, write code to make it so that the variable `output` has 35 `a` s inside it (like "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"). Hint: use the accumulation pattern!

```python
output = ""

for a in range(35):
    output = output + "a"

print(output)
```

**Output**:

```
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

---



### The Way of the Programmer

#### Accumulator Pattern Strategies

**When to Use it**

When children first encounter word problems in their math classes, they find it difficult to translate those words into arithmetic expressions involving addition, subtraction, multiplication, and division. Teachers offer heuristics. If the problem says “how many…altogether”, that’s an addition problem. If it says “how many are left”, that’s going to be a subtraction problem.

Learning to use the accumulator pattern can be similarly confusing. The first step is to recognizing something in the problem statement that suggests an accumulation pattern. Here are a few. You might want to try adding some more of your own.


| Phrase | Accumulation Pattern |
|--|--|
| how many | count accumulation |
| how frequently | |
| total | sum accumulation |
| a list of | list accumulation |
| concatenate | string accumulation |
| join together | |


For example, if the problem is to compute the total distance traveled in a series of small trips, you would want to accumulate a sum. If the problem is to make a list of the cubes of all the numbers from 1-25, you want a list accumulation, starting with an empty list and appending one more cube each time. If the problem is to make a comma separated list of all the people invited to a party, you should think of concatenating them; you could start with an empty string and concatenate one more person on each iteration through a list of name.


**Before Writing it**

Before writing any code, we recommend that you first answer the following questions:

* What sequence will you iterate through as you accumulate a result? It could be a range of numbers, the letters in a string, or some existing list that you have just as a list of names.
* What type of value will you accumulate? If your final result will be a number, your accumulator will start out with a number and always have a number even as it is updated each time. Similarly, if your final result will be a list, start with a list. If your final result will be a string, you’ll probably want to start with a string; one other option is to accumulate a list of strings and then use the .join() method at the end to concatenate them all together.

We recommend writing your answers to these questions in a comment. As you encounter bugs and have to look things up, it will help remind you of what you were trying to implement. Sometimes, just writing the comment can help you to realize a potential problem and avoid it before you ever write any code.


**Choosing Good Accumulator and Iterator Variable Names**

The final piece of advice regarding accumulation strategies is to be intentional when choosing variable names for the accumulator and iterator variables. A good name can help remind you of what the value is assigned to the variable as well as what you should have by the end of your code. While it might be tempting at first to use a short variable name, such as `a` or `x`, if you run into any bugs or look at your code later, you may have trouble understanding what you intended to do and what your code is actually doing.

For the accumulator variable, one thing that can help is to make the variable name end with “so_far”. The prefix can be something that helps remind you of what you’re supposed to end up with. For example: count_so_far, total_so_far, or cubes_so_far.

As mentioned previously in a previous Way of the Programmer segment, 👩‍💻 Naming Variables in For Loops, the iterator variable should be a singular noun. It should describe what one item in the original sequence, not what one item in the final result will be. For example, when accumulating the cubes of the numbers from 1-25, don’t write for cube in range(25):. Instead, write for num in range(25):. If you name the iterator variable cube you run the risk of getting confused that it has already been cubed, when that’s an operation that you still have to write in your code.


----
-----

**Check Your Understanding**


**E1** : Does the following prompt require an accumulation pattern? If so, what words indicate that? For each string in `wrds`, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called `past_wrds`.

A. Yes; "save... to a list" ✅ <br>
B. Yes; "add 'ed' to the end of the word"  <br>
C. No <br>

---

**E2** : Does the following prompt require an accumulation pattern? If so, what words indicate that? Write code to sum up all of the numbers in the list `seat_counts`. Store that number in the variable `total_seat_counts`.

A. Yes; "to sum up" ✅ <br>
B. Yes; "numbers in the list" <br>
C. No <br>

---

**E3** : Does the following prompt require an accumulation pattern? If so, what words indicate that? Write code to print out each character of the string `my_str` on a separate line.

A. Yes; "print out each" <br>
B. Yes; "on a separate line" <br>
C. No ✅<br>

---

**E4** : Does the following prompt require an accumulation pattern? If so, what words indicate that? Write code that will count the number of vowels in the sentence `s` and assign the result to the variable `num_vowels`.

A. Yes; "vowels in the sentence" <br>
B. Yes; "code that will count" ✅ <br>
C. No <br>

---

**E5** : What type should be used for the accumulator variable in the following prompt? Write code that will count the number of vowels in the sentence `s` and assign the result to the variable `num_vowels`.

A. string <br>
B. list <br>
C. integer ✅ <br>
D. none, there is no accumulator variable. <br>


---

**E6** : What sequence will you iterate through as you accumulate a result in the following prompt? Write code that will count the number of vowels in the sentence `s` and assign the result to the variable `num_vowels`.

A. num_vowels <br>
B. s ✅ <br>
C. the prompt does not say <br>


---


**E7** : What type should be used for the accumulator variable in the following prompt? For each string in `wrds`, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called `past_wrds`.

A. string <br>
B. list ✅ <br>
C. integer <br>
D. none, there is no accumulator variable. <br>

---

**E8** :  What sequence will you iterate through as you accumulate a result in the following prompt? For each string in `wrds`, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called `past_wrds`.

A. wrds ✅ <br>
B. past_wrds <br>
C. the prompt does not say <br>

---

**E9** :  What type should be used for the accumulator variable in the following prompt? Write code to sum up all of the numbers in the list `seat_counts`. Store that number in the variable `total_seat_counts`.

A. string <br>
B. list <br>
C. integer ✅ <br>
D. none, there is no accumulator variable. <br>

---

**E10** :  What sequence will you iterate through as you accumulate a result in the following prompt? Write code to sum up all of the numbers in the list `seat_counts`. Store that number in the variable `total_seat_counts`.

A. seat_counts ✅ <br>
B. total_seat_counts <br>
C. the prompt does not say <br>

---

**E11** :  What type should be used for the accumulator variable in the following prompt? Write code to print out each character of the string `my_str` on a separate line.

A. string <br>
B. list <br>
C. integer <br>
D. none, there is no accumulator variable. ✅ <br>

---

**E12** :  What sequence will you iterate through as you accumulate a result in the following prompt? Write code to print out each character of the string `my_str` on a separate line.

A. my_str ✅ <br>
B. my_str.split() <br>
C. the prompt does not say <br>

---

**E13** :  Which of these are good alternatives to the accumulator variable and iterator variable names for the following prompt? For each string in `wrds`, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list `called past_wrds`.

A. Accumulator Variable: wrds_so_far ; Iterator Variable: wrd ✅ <br>
B. Accumulator Variable: wrds_so_far ; Iterator Variable: x <br>
C. Accumulator Variable: changed_wrds ; Iterator Variable: ed <br>

---

**E14** :  Which of these are good alternatives to the accumulator variable and iterator variable names for the following prompt? Write code that will count the number of vowels in the sentence `s` and assign the result to the variable `num_vowels`.

A. Accumulator Variable: count_so_far ; Iterator Variable: l <br>
B. Accumulator Variable: total_so_far ; Iterator Variable: letter ✅<br>
C. Accumulator Variable: n_v ; Iterator Variable: letter <br>

---


**E15** :  Which of these are good alternatives to the accumulator variable and iterator variable names for the following prompt? Write code to sum up all of the numbers in the list `seat_counts`. Store that number in the variable `total_seat_counts`.

A. Accumulator Variable: total_so_far ; Iterator Variable: seat <br>
B. Accumulator Variable: total_seats_so_far ; Iterator Variable: seat_count ✅ <br>
C. Accumulator Variable: count ; Iterator Variable: n <br>

---

**E16** :  Which of these are good alternatives to the accumulator variable and iterator variable names for the following prompt? Write code to print out each character of the string `my_str` on a separate line.

A. Accumulator Variable: character_so_far ; Iterator Variable: char <br>
B. Accumulator Variable: no variable needed ; Iterator Variable: c <br>
C. Accumulator Variable: no variable needed ; Iterator Variable: char ✅ <br>

---

#### Don’t Mutate A List That You Are Iterating Through

So far we’ve shown you how to iterate through a list:

```python
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

for color in colors:
	print(color)
```

**Output** :

```
Red
Orange
Yellow
Green
Blue
Indigo
Violet
```

As well as accumulate a list by appending or deleting items!


```python
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
initials = []

for color in colors:
	initials.append(color[0])

print(initials)
```

**Output** :

```
['R', 'O', 'Y', 'G', 'B', 'I', 'V']
```

You may be tempted now to iterate through a list and accumulate some data into it or delete data from it, however that often becomes very confusing. In the following code we will filter out all words that begin with P, B, or T.


```python
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Purple", "Pink", "Brown", "Teal", "Turquois", "Peach", "Beige"]

for position in range(len(colors)):
    color = colors[position]
    print(color)
    if color[0] in ["P", "B", "T"]:
        del colors[position]

print(colors)
```

**Output** :

```
Red
Orange
Yellow
Green
Blue
Violet
Purple
Brown
Turquois
Beige
Traceback (most recent call last):
  File "Week4_Sequence_Mutation_and_Accumulation_Patterns.py", line 430, in <module>
    color = colors[position]
IndexError: list index out of range
```

In the code above, we iterated through `range(len(colors))` because it made it easier to locate the position of the item in the list and delete it. However, we run into a problem because as we delete content from the list, the list becomes shorter. Not only do we have an issue indexing on line 4 after a certain point, but we also skip over some strings because they’ve been moved around. To see this more easily, try walking through this code in codelens. Note that each time we iterate through the list python does not reevaluate the iterator variable.

We can also try to accumulate a list that we’re iterating through as well. What do you think will happen here?


```python
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

for color in colors:
	if color[0] in ["A", "E", "I", "O", "U"]:
		colors.append(color)

print(colors)
```

Though there is not an error, the behavior may not be expected. When we come across a color that begins with a vowel, that color is added to the end of the list. Again, because Python does not reevaluate the iterator variable we are not stuck adding colors that start with vowels for an infinite number of times. That’s good in this case! Ultimately though, it can be confusing to write code like this. We recommend not iterating over a list that you will be mutating within the for loop.




### Python Basics - Final Course Assignment

#### Chapter Assessments & Exercises

#### Assessments

**A1**. Which of these is a correct reference diagram following the execution of the following code?


```python
lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
lst.remove('pluto')
first_three = lst[:3]
```

I. ![](https://fopp.umsi.education/runestone/static/fopp/_images/week3a1_1.png)

II. ![](https://fopp.umsi.education/runestone/static/fopp/_images/week3a1_2.png)

A. I. ✅  <br>
B. II. <br>
C. Neither is the correct reference diagram. <br>

-----

**A2**. Which method would you use to figure out the position of an item in a list?

A. .pop() <br>
B. .insert() <br>
C. .count() <br>
D. .index() ✅  <br>

-----


**A3**. Which method is best to use when adding an item to the end of a list?

A. .insert() ✅ <br>
B. .pop() <br>
C. .append() <br>
D. .remove() <br>


-----


**A4**. Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list `sports`.

```python
# Given
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']



# Solution
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']

sports.insert(2, "horseback riding")
print(sports)
```

**Output** :

```
['cricket', 'football', 'horseback riding', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
```

-----

**A5**. Write code to take ‘London’ out of the list `trav_dest`.

```python
# Given
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']



# Solution
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
del trav_dest[trav_dest.index("London")]
print(trav_dest)
```

**Output** :

```
['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
```

-----


**A6**. Write code to add ‘Guadalajara’ to the end of the list `trav_dest` using a list method.

```python
# Given
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']


# Solution
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']

trav_dest.append("Guadalajara")
print(trav_dest)
```

**Output** :

```
['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne', 'Guadalajara']
```

-----

**A7**. What will be the value of `a` after the following code has executed?

```python
a = ["holiday", "celebrate!"]
quiet = a
quiet.append("company")
print(a)
```

**Output** :

```
["holiday", "celebrate!", "company"]
```

-----

**A8**. Could aliasing cause potential confusion in this problem?

```python
b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)
```

**Output** :

```
['q', 'i']
```

A. yes ✅ <br>
B. no <br>

-----


**A9**. Could aliasing cause potential confusion in this problem?

```python
sent = "Holidays can be a fun time when you have good company!"
phrase = sent
phrase = phrase + " Holidays can also be fun on your own!"
```


A. yes <br>
B. no ✅ <br>

-----


**A10**. Which of these is a correct reference diagram following the execution of the following code?

```python
x = ["dogs", "cats", "birds", "reptiles"]
y = x
x += ['fish', 'horses']
y = y + ['sheep']
```

I. ![](https://fopp.umsi.education/runestone/static/fopp/_images/week3a3_1.png)

II. ![](https://fopp.umsi.education/runestone/static/fopp/_images/week3a3_2.png)

III. ![](https://fopp.umsi.education/runestone/static/fopp/_images/week3a3_3.png)

IV. ![](https://fopp.umsi.education/runestone/static/fopp/_images/week3a3_4.png)


A. I. <br>
B. II. <br>
C. III. <br>
D. IV. ✅<br>

-----

**A11**. Which of these is a correct reference diagram following the execution of the following code?

```python
sent = "The mall has excellent sales right now."
wrds = sent.split()
wrds[1] = 'store'
new_sent = " ".join(wrds)
```

I. ![](https://fopp.umsi.education/runestone/static/fopp/_images/week3a2_1.png)

II. ![](https://fopp.umsi.education/runestone/static/fopp/_images/week3a2_2.png)

III. ![](https://fopp.umsi.education/runestone/static/fopp/_images/week3a2_3.png)

IV. ![](https://fopp.umsi.education/runestone/static/fopp/_images/week3a2_4.png)


A. I. ✅ <br>
B. II. <br>
C. III. <br>
D. IV. <br>

-----

**A12**. Write code to find the postion of the string “Tony” in the list `awards` and save that information in the variable `pos`.

```python
# Given
awards = ['Emmy', 'Tony', 'Academy', 'Grammy']



# Solution
awards = ['Emmy', 'Tony', 'Academy', 'Grammy']
pos = awards.index("Tony")
print(pos)
```

**Output** :

```
1
```

-----


**A13**. Which of these is the accumulator variable?

```python
byzo = 'hello world!'
c = 0
for x in byzo:
    z = x + "!"
    print(z)
    c = c + 1
```

A. byzo <br>
B. x <br>
C. z <br>
D. c  ✅<br>

-----

**A14**. Which of these is the sequence?

```python
cawdra = ['candy', 'daisy', 'pear', 'peach', 'gem', 'crown']
t = 0
for elem in cawdra:
    t = t + len(elem)
```

A. cawdra ✅<br>
B. elem <br>
C. t <br>

-----

**A15**. Which of these is the iterator (loop) variable?

```python
lst = [5, 10, 3, 8, 94, 2, 4, 9]
num = 0
for item in lst:
    num += item
```

A. item ✅<br>
B. lst <br>
C. num <br>

-----


**A16**. What is the iterator (loop) variable in the following?

```python
rest = ["sleep", 'dormir', 'dormire', "slaap", 'sen', 'yuxu', 'yanam']
let = ''
for phrase in rest:
    let += phrase[0]
```

The iterator variable is : `phrase`

-----

**A17**. Currently there is a string called `str1`. Write code to create a list called `chars` which should contain the characters from `str1`. Each character in `str1` should be its own element in the list `chars`.

```python
# Given
str1 = "I love python"


# Solution
str1 = "I love python"
chars = []

for char in str1:
    chars.append(char)
print(chars)
```

**Output** :

```
['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n']
```

-----


**A18**. Given that we want to accumulate the total sum of a list of numbers, which of the following accumulator patterns would be appropriate?

I.
```python
nums = [4, 5, 2, 93, 3, 5]
s = 0
for n in nums:
    s = s + 1
```

II.
```python
nums = [4, 5, 2, 93, 3, 5]
s = 0
for n in nums:
    s = n + n
```

III.
```python
nums = [4, 5, 2, 93, 3, 5]
s = 0
for n in nums:
    s = s + n
```

A. I. <br>
B. II. <br>
C. III. ✅<br>
D. none of the above would be appropriate for the problem. <br>


-----

**A19**. Given that we want to accumulate the total number of strings in the list, which of the following accumulator patterns would be appropriate?

1.
```python
lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
s = 0
for n in lst:
    s = s + n
```

2.
```python
lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
for item in lst:
    s = 0
    if type(item) == type("string"):
        s = s + 1
```

3.
```python
lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
s = ""
for n in lst:
    s = s + n
```

4.
```python
lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
s = 0
for item in lst:
    if type(item) == type("string"):
        s = s + 1
```

A. 1. <br>
B. 2. <br>
C. 3. <br>
D. 4. ✅<br>
E. none of the above would be appropriate for the problem. <br>

-----

**A20**. Which of these are good names for an accumulator variable? Select as many as apply.

A. sum <br>
B. x <br>
C. total ✅<br>
D. accum ✅<br>
E. none of the above <br>

-----

**A21**. Which of these are good names for an iterator (loop) variable? Select as many as apply.

A. item ✅<br>
B. y <br>
C. elem ✅<br>
D. char ✅<br>
E. none of the above <br>

-----


**A22**. Which of these are good names for a sequence variable? Select as many as apply.

A. num_lst ✅<br>
B. p <br>
C. sentence ✅<br>
D. names ✅<br>
E. none of the above <br>

-----

**A23**. Given the following scenario, what are good names for the accumulator variable, iterator variable, and sequence variable? You are writing code that uses a list of sentences and accumulates the total number of sentences that have the word ‘happy’ in them.

A. accumulator variable: x | iterator variable: s | sequence variable: lst <br>
B. accumulator variable: total | iterator variable: s | sequence variable: lst <br>
C. accumulator variable: x | iterator variable: sentences | sequence variable: sentence_lst <br>
D. accumulator variable: total | iterator variable: sentence |sequence variable: sentence_lst ✅ <br>
E. none of the above <br>

-----


**A24**. For each character in the string saved in `ael`, append that character to a list that should be saved in a variable `app`.

```python
# Given
ael = "python!"


# Solution
ael = "python!"
app = []

for char in ael:
    app.append(char)
print(app)
```

**Output** :

```
['p', 'y', 't', 'h', 'o', 'n', '!']
```

-----

**A25**. For each string in `wrds`, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called `past_wrds`.

```python
# Given
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]



# Solution
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []

for word in wrds:
    word = word + "ed"
    past_wrds.append(word)
print(past_wrds)
```

**Output** :

```
['ended', 'worked', 'played', 'started', 'walked', 'looked', 'opened', 'rained', 'learned', 'cleaned']
```

-----

**A26**. Write code to create a **list of word lengths** for the words in `original_str` using the accumulation pattern and assign the answer to a variable `num_words_list`. (You should use the `len` function).

```python
# Given
original_str = "The quick brown rhino jumped over the extremely lazy fox"



# Solution
original_str = "The quick brown rhino jumped over the extremely lazy fox"
num_words_list = []
list_str = original_str.split()

for word in list_str:
    num_words_list.append(len(word))

print(num_words_list)
```

**Output** :

```
[3, 5, 5, 5, 6, 4, 3, 9, 4, 3]
```

-----
**A27**. Create an empty string and assign it to the variable `lett`. Then using range, write code such that when your code is run, `lett` has 7 b’s ("`bbbbbbb`").

```python
lett = ""

for b in range(7):
    lett = lett + "b"

print(lett)
```

**Output** :

```
bbbbbbb
```

-----


**A28**. Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value `a_scores`.

```python
# Given
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"



# Solution
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

scores = scores.split()
a_scores = 0

for score in scores:
    if int(score) >= 90:
        a_scores += 1
print(a_scores)
```

**Output** :

```
10
```

-----

**A29**. Write code that uses the string stored in `org` and creates an acronym which is assigned to the variable `acro`. Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list `stopwords`. For example, if `org` was assigned the string “hello to world” then the resulting acronym should be `“HW”`.

```python
# Given
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"


# Solution
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro = ""

org_list = org.split()

for word in org_list:
    if word.lower() in stopwords:
        pass
    else:
        acro_word = word[0].upper()
        acro = acro + acro_word
print(acro)
```

**Output** :

```
OHSE
```

-----

-----

**A30**. Write code that uses the string stored in `sent` and creates an acronym which is assigned to the variable `acro`. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list `stopwords`. For example, if `sent` was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.

```python
# Given
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"



# Solution
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = ""
sent_list = sent.split()

for word in sent_list:
    if word.lower() in stopwords:
        pass
    elif word == sent_list[-1]:
        acro_word = word[:2].upper()
        acro = acro + acro_word
    else:
        acro_word = word[:2].upper()
        acro = acro + acro_word + ". "
print(acro)
```

**Output** :

```
WA. EA. AI. AR. VI
```

-----

**A31**. A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if `p_phrase` is a palindrome by reversing it and then checking if the reversed version is equal to the original. Assign the reversed version of `p_phrase` to the variable `r_phrase` so that we can check your work.

```python
# Given
p_phrase = "was it a car or a cat I saw"


# Solution
p_phrase = "was it a car or a cat I saw"
r_phrase = []
lst = p_phrase.split()

for word in lst:
    r_phrase.append(word[::-1])

r_phrase.reverse()
r_phrase = " ".join(r_phrase)
print(r_phrase)
```

**Output** :

```
was I tac a ro rac a ti saw
```

-----

**A32**. Provided is a list of data about a store’s inventory where each item in the list represents the name of an item, how much is in stock, and how much it costs. Print out each item in the list with the same formatting, using the .format method (not string concatenation). For example, the first print statment should read `The store has 12 shoes, each for 29.99 USD`.

```python
# Given
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]



# Solution
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for items in inventory:
    item, number, price = items.split(",")
    print("The store has {} {}, each for {} USD.".format(number.strip(), item, price.strip()))
```

**Output** :

```
The store has 12 shoes, each for 29.99 USD.
The store has 20 shirts, each for 9.99 USD.
The store has 25 sweatpants, each for 15.00 USD.
The store has 13 scarves, each for 7.75 USD.
```

-----

----
----

#### Exercises

**Q1**. For each word in the list `verbs`, add an -ing ending. Overwrite the old list so that `verbs` has the same words with `ing` at the end of each one.

```python
# Given
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]



# Solution
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
len_verbs = len(verbs)
for i in range(len_verbs):
    verbing = verbs[i] + "ing"
    verbs.append(verbing)
del verbs[:len_verbs]
print(verbs)
```

**Output** :

```
['kayaking', 'crying', 'walking', 'eating', 'drinking', 'flying']
```


----

**Q2**. In XYZ University, upper level math classes are numbered 300 and up. Upper level English classes are numbered 200 and up. Upper level Psychology classes are 400 and up. Create two lists, `upper` and `lower`. Assign each course in `classes` to the correct list, `upper` or `lower`. HINT: remember, you can convert some strings to different types!

```python
# Given
classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]



# Solution
classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]
upper = []
lower = []

for clas in classes:
    cls = clas.split()
    if cls[0] == "MATH":
        if int(cls[1]) >= 300 :
            upper.append(clas)
        else:
            lower.append(clas)
    elif cls[0] == "ENG":
        if int(cls[1]) >= 200 :
            upper.append(clas)
        else:
            lower.append(clas)
    elif cls[0] == "PSYCH":
        if int(cls[1]) >= 400 :
            upper.append(clas)
        else:
            lower.append(clas)
print(upper)
print(lower)
```

**Output** :

```
['PSYCH 412', 'MATH 300', 'MATH 404', 'ENG 201', 'PSYCH 508', 'ENG 220']
['MATH 150', 'PSYCH 111', 'PSYCH 313', 'MATH 206', 'ENG 100', 'ENG 103', 'ENG 125', 'ENG 124']
```

----

**Q3**. Starting with the list `myList = [76, 92.3, ‘hello’, True, 4, 76]`, write Python statements to do the following:


a. Append “apple” and 76 to the list. <br>
b. Insert the value “cat” at position 3.<br>
c. Insert the value 99 at the start of the list. <br>
d. Find the index of “hello”. <br>
e. Count the number of 76s in the list. <br>
f. Remove the first occurrence of 76 from the list. <br>
g. Remove True from the list using `pop` and `index`.<br>



```python
# Given
myList = [76, 92.3, 'hello', True, 4, 76]


# Solution
myList = [76, 92.3, 'hello', True, 4, 76]
myList.append("apple")
myList.append(76)
myList.insert(3, "cat")
myList.insert(0, 99)
print(myList.index("hello"))
print(myList.count(76))
myList.remove(76)
myList.pop(myList.index(True))
print(myList)
```

**Output** :

```
3
3
[99, 92.3, 'hello', 'cat', 4, 76, 'apple', 76]
```

----


**Q4**. The module `keyword` determines if a string is a keyword. e.g. `keyword.iskeyword(s)` where `s` is a string will return either `True` or `False`, depending on whether or not the string is a Python keyword. Import the `keyword` module and test to see whether each of the words in list `test` are keywords. Save the respective answers in a list, `keyword_test`.


```python
# Given
test = ["else", "integer", "except", "elif"]


# Solution
import keyword
test = ["else", "integer", "except", "elif"]
keyword_test = []

for word in test:
    val = keyword.iskeyword(word)
    keyword_test.append(val)

print(keyword_test)
```

**Output** :

```
[True, False, True, True]
```


----


**Q5**. The `string` module provides sequences of various types of Python characters. It has an attribute called `digits` that produces the string ‘0123456789’. Import the module and assign this string to the variable `nums`. Below, we have provided a list of characters called `chars`. Using `nums` and `chars`, produce a list called `is_num` that consists of tuples. The first element of each tuple should be the character from `chars`, and the second element should be a Boolean that reflects whether or not it is a Python digit.


```python
# Given
chars = ['h', '1', 'C', 'i', '9', 'True', '3.1', '8', 'F', '4', 'j']



# Solution
import string
chars = ['h', '1', 'C', 'i', '9', 'True', '3.1', '8', 'F', '4', 'j']

nums = string.digits
is_num = []

for char in chars:
    if char in nums:
        v = True
    else:
        v = False
    is_num.append((char, v))

print(is_num)
```

**Output** :

```
[('h', False), ('1', True), ('C', False), ('i', False), ('9', True), ('True', False), ('3.1', False), ('8', True), ('F', False), ('4', True), ('j', False)]
```


----

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




### Accumulating Lists and Strings




### The Way of the Programmer




### Python Basics - Final Course Assignment

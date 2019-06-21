# Python Basics
*Coursera | Python 3 Programming Specialization | Course 1*

## Week 2 : Sequences and Iteration
### Lists and Strings
#### Strings and Lists

In the real world most of the data we care about doesn’t exist on its own. Usually data is in the form of some kind of collection or sequence. For example, a grocery list helps us keep track of the individual food items we need to buy, and our todo list organizes the things we need to do each day. Notice that both the grocery list and the todo list are not even concerned with numbers as much as they are concerned with words. This is true of much of our daily life, and so Python provides us with many features to work with lists of all kinds of objects (numbers, words, etc.) as well as special kind of sequence, the character string, which you can think of as a sequence of individual letters.

So far we have seen built-in types like: `int`, `float`, and `str`. `int` and `float` are considered to be simple or primitive or atomic data types because their values are not composed of any smaller parts. They cannot be broken down.

On the other hand, strings and lists are different from the others because they are made up of smaller pieces. In the case of strings, they are made up of smaller strings each containing one **character**.

Types that are comprised of smaller pieces are called **collection data types**. Depending on what we are doing, we may want to treat a collection data type as a single entity (the whole), or we may want to access its parts. This ambiguity is useful.

In this chapter we will examine operations that can be performed on sequences, such as picking out individual elements or subsequences (called slices) or computing their length. In addition, we’ll examine some special functions that are defined only for strings, and we’ll find out one importance difference between strings and lists, that lists can be changed (or mutated) while strings are immutable.


### Strings
Strings can be defined as sequential collections of characters. This means that the individual characters that make up a string are in a particular order from left to right.

A string that contains no characters, often referred to as the **empty string**, is still considered to be a string. It is simply a sequence of zero characters and is represented by `‘’` or `“”` (two single or two double quotes with nothing in between).


### Lists
A **list** is a sequential collection of Python data values, where each value is identified by an index. The values that make up a list are called its **elements**. Lists are similar to strings, which are ordered collections of characters, except that the elements of a list can have any type and for any one list, the items can be of different types.

There are several ways to create a new list. The simplest is to enclose the elements in square brackets ( `[` and `]`).


```python
[10, 20, 30, 40]
["spam", "bungee", "swallow"]
```

The first example is a list of four integers. The second is a list of three strings. As we said above, the elements of a list don’t have to be the same type. The following list contains a string, a float, an integer, and another list.

```python
["hello", 2.0, 5, [10, 20]]
```

### Tuples

A **tuple**, like a list, is a sequence of items of any type. The printed representation of a tuple is a comma-separated sequence of values, enclosed in parentheses. In other words, the representation is just like lists, except with parentheses () instead of square brackets [].

One way to create a tuple is to write an expression, enclosed in parentheses, that consists of multiple other expressions, separated by commas.

```python
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
```

The key difference between lists and tuples is that a tuple is immutable, meaning that its contents can’t be changed after the tuple is created. We will examine the mutability of lists in detail in the chapter on Mutability.

To create a tuple with a single element (but you’re probably not likely to do that too often), we have to include the final comma, because without the final comma, Python treats the `(5)` below as an integer in parentheses:

```python
t = (5,)
print(type(t))

x = (5)
print(type(x))
```

**Output**:

```
<class 'tuple'>
<class 'int'>
```


#### The Index Operator

The **indexing operator** (Python uses square brackets to enclose the index) selects a single character from a string. The characters are accessed by their position or index value. For example, in the string shown below, the 14 characters are indexed left to right from postion 0 to position 13.

![](https://fopp.umsi.education/runestone/static/fopp/_images/indexvalues.png)

It is also the case that the positions are named from right to left using negative numbers where -1 is the rightmost index and so on. Note that the character at index 6 (or -8) is the blank character.

```python
school = "Luther College"
m = school[2]
print(m)

lastchar = school[-1]
print(lastchar)
```

**Output** :

```
t
e
```

The expression `school[2]` selects the character at index 2 from `school`, and creates a new string containing just this one character. The variable m refers to the result.

The letter at index zero of `"Luther College"` is `L`. So at position `[2]` we have the letter t.

If you want the zero-eth letter of a string, you just put 0, or any expression with the value 0, in the brackets. Give it a try.

The expression in brackets is called an **index**. An index specifies a member of an ordered collection. In this case the collection of characters in the string. The index indicates which character you want. It can be any integer expression so long as it evaluates to a valid index value.

Note that indexing returns a string — Python has no special type for a single character. It is just a string of length 1.


**Index Operator: Accessing Elements of a List or Tuple**

The syntax for accessing the elements of a list or tuple is the same as the syntax for accessing the characters of a string. We use the index operator ( `[]` – not to be confused with an empty list). The expression inside the brackets specifies the index. Remember that the indices start at 0. Any integer expression can be used as an index and as with strings, negative index values will locate items from the right instead of from the left.

When we say the first, third or nth character of a sequence, we generally mean counting the usual way, starting with 1. The nth character and the character AT INDEX n are different then: The nth character is at index n-1. Make sure you are clear on what you mean!

Try to predict what will be printed out by the following code, and then run it to check your prediction. (Actually, it’s a good idea to always do that with the code examples. You will learn much more if you force yourself to make a prediction before you see the output.)

```python
numbers = [17, 123, 87, 34, 66, 8398, 44]
print(numbers[2])
print(numbers[9-8])
print(numbers[-2])
```

**Output** :

```
87
123
8398
```


```python
prices = [1.99, 2.00, 5.50, 20.95, 100.98]
print(prices[0])
print(prices[-1])
print(prices[3-5])
```

**Output** :

```
1.99
100.98
20.95
```

-----

#### Disambiguation : []: creation vs indexing
Square brackets `[]` are used in quite a few ways in python. When you’re first learning how to use them it may be confusing, but with practice and repetition they’ll be easy to incorporate!

You have currently encountered two instances where we have used square brakets. The first is creating lists and the second is indexing. At first glance, creating and indexing are difficult to distinguish. However, indexing requires referencing an already created list while simply creating a list does not.

```python
new_lst = []
```

In the code above, a new list is created using the empty brackets. Since there’s nothing in it though, we can’t index into it.

```python
new_lst = ["NFLX", "AMZN", "GOOGL", "DIS", "XOM"]
part_of_new_lst = new_lst[0]
print(part_of_new_lst)
```

**Output** :

```
NFLX
```

In the code above, you’ll see how, now that we have elements inside of `new_lst`, we can index into it. In order to extract an element of the list, we do use `[]`, but we first have to specify which list we are indexing. Imagine if there was another list in the activecode. How would python know which list we want to index into if we don’t tell it? Additionally, we have to specify what element we want to extract. This belongs inside of the brakets.

Though it may be easier to distinguish in this above activecode, below may be a bit more difficult.

```python
lst = [0]
n_lst = lst[0]

print(lst)
print(n_lst)
```

**Output** :

```
[0]
0
```

Here, we see a list called `lst` being assigned to a list with one element, zero. Then, we see how `n_lst` is assigned the value associated with the first element of lst. Dispite the variable names, only one of the above variables is assigned to a list. Note that in this example, what sets creating appart from indexing is the reference to the list to let python know that you are extracting an element from another list.

-----
--------

**Check your understanding**

**E1** : What is printed by the following statements?

```python
s = "python rocks"
print(s[3])
```

A. t<br>
B. h ✅<br>
C. c<br>
D. Error, you cannot use the [ ] operator with a string.<br>


---

**E2** : What is printed by the following statements?

```python
s = "python rocks"
print(s[2] + s[-4])
```

A. tr <br>
B. to ✅ <br>
C. ps <br>
D. nn <br>
E. Error, you cannot use the [ ] operator with the + operator. <br>


---

**E3** : What is printed by the following statements?

```python
alist = [3, 67, "cat", [56, 57, "dog"], [], 3.14, False]
print(alist[5])
```

A. [ ] <br>
B. 3.14 ✅ <br>
C. False <br>
D. "dog" <br>


---

**E4** : Assign the value of the 34th element of `lst` to the variable `output`.

```python
lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
```


***Solution***:

```python
lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
output = lst[33]
print(output)
```

***Output*** :

```
laptop
```


---

**E5** : Assign the value of the 23rd element of `l` to the variable `checking`.

```python
l = ("hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones")
```


***Solution***:

```python
l = ("hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones")
checking = l[22]
print(checking)
```

***Output*** :

```
leaders and the best
```


---

**E6** : Assign the value of the last chacter of `lst` to the variable `output`. Do this so that the length of lst doesn’t matter.

```python
lst = "Every chess or checkers game begins from the same position and has a finite number of moves that can be played. While the number of possible scenarios and moves is quite large, it is still possible for computers to calculate that number and even be programmed to respond well against a human player..."
```


***Solution***:

```python
lst = "Every chess or checkers game begins from the same position and has a finite number of moves that can be played. While the number of possible scenarios and moves is quite large, it is still possible for computers to calculate that number and even be programmed to respond well against a human player..."
output = lst[-1]
print(output)
```

***Output*** :

```
.
```

---

**E7** : Which of the following correctly uses indexing? Assume that a is a list or string. Select as many as apply.

A. w = [a] <br>
B. y = a[] <br>
C. x = [8] <br>
D. t = a[0] ✅ <br>


---

**Note**

Why does counting start at 0 going from left to right, but at -1 going from right to left? Well, indexing starting at 0 has a long history in computer science having to do with some low-level implementation details that we won’t go into. For indexing from right to left, it might seem natural to do the analgous thing and start at -0. Unfortunately, -0 is the same as 0, so s[-0] can’t be the last item. Remember we said that programming languages are formal languages where details matter and everything is taken literally?

#### Length

The `len` function, when applied to a string, returns the number of characters in a string.

```python
fruit = "Banana"
print(len(fruit))
```

**Output** :

```
6
```

To get the last letter of a string, you might be tempted to try something like this:

```python
fruit = "Banana"
sz = len(fruit)
last = fruit[sz]
print(last)
```

**Output** :

```
IndexError: string index out of range on line 3
```

That won’t work. It causes the runtime error I`ndexError: string index out of range`. The reason is that there is no letter at index position 6 in `"Banana"`. Since we started counting at zero, the six indexes are numbered 0 to 5. To get the last character, we have to subtract 1 from the length. Give it a try in the example above.

```python
fruit = "Banana"
sz = len(fruit)
last = fruit[sz-1]
print(last)
```

**Output** :

```
a
```

Typically, a Python programmer will access the last character by combining the two lines of code from above.

```python
lastch = fruit[len(fruit)-1]
```

As with strings, the function `len` returns the length of a list (the number of items in the list). However, since lists can have items which are themselves sequences (e.g., strings), it important to note that `len` only returns the top-most length.

```python
alist = ["hello", 2.0, 5]
print(len(alist))
print(len(alist[0]))
```

**Output** :

```
3
5
```

Note that `alist[0]` is the string `"hello"`, which has length 5.



-----
--------

**Check your understanding**

**E1** : What is printed by the following statements?

```python
s = "python rocks"
print(len(s))
```

A. 11 <br>
B. 12 ✅<br>



---

**E2** : What is printed by the following statements?

```python
alist = [3, 67, "cat", 3.14, False]
print(len(alist))
```

A. 4 <br>
B. 5 ✅ <br>



---

**E3** : What is printed by the following statements?

```python
L = [0.34, '6', 'SI106', 'Python', -2]
print(len(L[1:-1]))
```

A. 2 <br>
B. 3 ✅ <br>
C. 4 <br>
D. 5 <br>


---

**E4** : Assign the number of elements in `lst` to the variable `output`.

```python
lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
```


***Solution***:

```python
lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
output = len(lst)
print(output)
```

***Output*** :

```
52
```


#### The Slice Operator

A substring of a string is called a slice. Selecting a slice is similar to selecting a character:

```python
singers = "Peter, Paul, and Mary"
print(singers[0:5])
print(singers[7:11])
print(singers[17:21])
```

**Output** :

```
Peter
Paul
Mary
```

The `slice` operator `[n:m]` returns the part of the string starting with the character at index n and go up to but not including the character at index m. Or with normal counting from 1, this is the (n+1)st character up to and including the mth character.

If you omit the first index (before the colon), the slice starts at the beginning of the string. If you omit the second index, the slice goes to the end of the string.

```python
fruit = "banana"
print(fruit[:3])
print(fruit[3:])
```

**Output** :

```
ban
ana
```

What do you think `fruit[:]` means?

```python
fruit = "banana"
print(fruit[:])
```

**Output** :

```
banana
```


**List Slices**

The slice operation we saw with strings also work on lists. Remember that the first index is the starting point for the slice and the second number is one index past the end of the slice (up to but not including that element). Recall also that if you omit the first index (before the colon), the slice starts at the beginning of the sequence. If you omit the second index, the slice goes to the end of the sequence.

```python
a_list = ["a", "b", "c", "d", "e", "f"]
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])
```

**Output** :

```
['b', 'c']
['a', 'b', 'c', 'd']
['d', 'e', 'f']
['a', 'b', 'c', 'd', 'e', 'f']
```

**Tuple Slices**

We can’t modify the elements of a tuple, but we can make a variable reference a new tuple holding different information. Thankfully we can also use the slice operation on tuples as well as strings and lists. To construct the new tuple, we can slice parts of the old tuple and join up the bits to make the new tuple. So `julia` has a new recent film, and we might want to change her tuple. We can easily slice off the parts we want and concatenate them with the new tuple.

```python
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])

print(len(julia))

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)
```

**Output** :

```
1967
(1967, 'Duplicity', 2009, 'Actress')
7
('Julia', 'Roberts', 1967, 'Eat Pray Love', 2010, 'Actress', 'Atlanta, Georgia')
```

-----
--------

**Check your understanding**

**E1** : What is printed by the following statements?

```python
s = "python rocks"
print(s[3:8])
```

A. python <br>
B. rocks <br>
C. hon r ✅<br>
D. Error, you cannot have two numbers inside the [ ]. <br>



---

**E2** : What is printed by the following statements?

```python
alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
print(alist[4:])
```

A. [ [ ], 3.14, False] ✅ <br>
B. [ [ ], 3.14] <br>
C. [ [56, 57, "dog"], [ ], 3.14, False] <br>



---

**E3** : Create a new list using the 9th through 12th elements (four items in all) of `new_lst` and assign it to the variable `sub_lst`.

```python
new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]
```


***Solution***:

```python
new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]
sub_lst = new_lst[8:12]
print(sub_lst)
```

***Output*** :

```
['sun', ['water', 'air', 'fire', 'earth'], 'games', 2.7]
```

#### Concatenation and Repetition

Again, as with strings, the `+` operator concatenates lists. Similarly, the `*` operator repeats the items in a list a given number of times.

```python
fruit = ["apple", "orange", "banana", "cherry"]
print([1, 2] + [3, 4])
print(fruit + [6, 7, 8, 9])

print([0] * 4)
print([0, 1] * 4)
print(fruit * 4)
print((fruit + [1] )* 4)
print(fruit + [1] * 4)
```

**Output** :

```
[1, 2, 3, 4]
['apple', 'orange', 'banana', 'cherry', 6, 7, 8, 9]
[0, 0, 0, 0]
[0, 1, 0, 1, 0, 1, 0, 1]
['apple', 'orange', 'banana', 'cherry', 'apple', 'orange', 'banana', 'cherry', 'apple', 'orange', 'banana', 'cherry', 'apple', 'orange', 'banana', 'cherry']
['apple', 'orange', 'banana', 'cherry', 1, 'apple', 'orange', 'banana', 'cherry', 1, 'apple', 'orange', 'banana', 'cherry', 1, 'apple', 'orange', 'banana', 'cherry', 1]
['apple', 'orange', 'banana', 'cherry', 1, 1, 1, 1]
```

It is important to see that these operators create new lists from the elements of the operand lists. If you concatenate a list with 2 items and a list with 4 items, you will get a new list with 6 items (not a list with two sublists). Similarly, repetition of a list of 2 items 4 times will give a list with 8 items.

![](https://media.giphy.com/media/H5BANbTgSGLupiwuZP/giphy.gif)


***Note***

WP: Adding types together

Beware when adding different types together! Python doesn’t understand how to concatenate different types together. Thus, if we try to add a string to a list with `['first'] + "second"` then the interpreter will return an error. To do this you’ll need to make the two objects the same type. In this case, it means putting the string into its own list and then adding the two together like so: `['first'] + ["second"]`. This process will look different for other types though. Remember that there are functions to convert types!


-----
--------

**Check your understanding**

**E1** : What is printed by the following statements?

```python
alist = [1,3,5]
blist = [2,4,6]
print(alist + blist)
```

A. 6 <br>
B. [1,2,3,4,5,6] <br>
C. [1,3,5,2,4,6] ✅ <br>
D. [3,7,11] <br>



---

**E2** : What is printed by the following statements?

```python
alist = [1,3,5]
print(alist * 3)
```

A. 9 <br>
B. [1,1,1,3,3,3,5,5,5] <br>
C. [1,3,5,1,3,5,1,3,5] ✅ <br>
D. [3,9,15] <br>



---

**E3** : Create a new list using the 9th through 12th elements (four items in all) of `new_lst` and assign it to the variable `sub_lst`.

```python
new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]
```


***Solution***:

```python
new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]
sub_lst = new_lst[8:12]
print(sub_lst)
```

***Output*** :

```
['sun', ['water', 'air', 'fire', 'earth'], 'games', 2.7]
```


#### Count and Index

As you create more complex programs, you will find that some tasks are commonly done. Python has some built-in functions and methods to help you with these tasks. This page will cover two helpful methods for both strings and lists: count and index.

You’ve learned about methods before when drawing with the turtle module. There, you used `.forward(50)` and `.color("purple")` to complete actions. We refer to forward and color as methods of the turtle class. Objects like strings and lists also have methods that we can use.


#### Count

The first method we’ll talk about is called `count`. It requires that you provide one argument, which is what you would like to count. The method then returns the number of times that the argument occured in the string/list the method was used on. There are some differences between count for strings and count for lists. When you use count on a string, the argument can only be a string. You can’t count how many times the integer 2 appears in a string, though you can count how many times the string “2” appears in a string. For lists, the argument is not restricted to just strings.



```python
a = "I have had an apple on my desk before!"
print(a.count("e"))
print(a.count("ha"))
```

**Output** :

```
5
2
```

```python
z = ["atoms", 4, "neutron", 6, "proton", 4, "electron", 4, "electron", "atoms"]
print(z.count("4"))
print(z.count(4))
print(z.count("a"))
print(z.count("electron"))
```

**Output** :

```
0
3
0
2
```

When you run the activecode window above, you’ll see how count with a list works. Notice how `“4”` has a count of zero but 4 has a count of three? This is because the list `z` only contains the integer 4. There are never any strings that are 4. Additionally, when we check the count of “a”, we see that the program returns zero. Though some of the words in the list contain the letter “a”, the program is looking for items in the list that are just the letter “a”.


#### Index

The other method that can be helpful for both strings and lists is the `index` method. The `index` method requires one argument, and, like the `count` method, it takes only strings when index is used on strings, and any type when it is used on lists. For both strings and lists, `index` returns the leftmost index where the argument is found. If it is unable to find the argument in the string or list, then an error will occur.

```python
music = "Pull out your music and dancing can begin"
bio = ["Metatarsal", "Metatarsal", "Fibula", [], "Tibia", "Tibia", 43, "Femur", "Occipital", "Metatarsal"]

print(music.index("m"))
print(music.index("your"))

print(bio.index("Metatarsal"))
print(bio.index([]))
print(bio.index(43))
```

**Output** :

```
14
9
0
3
6
```

All of the above examples work, but were you surprised by any of the return values? Remember that `index` will return the left most index of the argument. Even though `“Metatarsal”` occurs many times in `bio`, the method will only return the location of one of them.

Here’s another example.

```python
seasons = ["winter", "spring", "summer", "fall"]
print(seasons.index("autumn"))
```

**Output** :

```
ValueError: list.index(x): x not in list on line 3
```

In the above, we’re trying to see where “autumn” is in the list seasons. However, there is no string called autumn (though there is string called “fall” which is likely what the program is looking for). Remember that an error occurs if the argument is not in the string or list.


-----
--------

**Check your understanding**

**E1** : What will be stored in the variable ty below?

```python
qu = "wow, welcome week!"
ty = qu.index("we")
```

A. 5 ✅ <br>
B. 6 <br>
C. 13 <br>
D. 14 <br>
E. There is an error. <br>



---

**E2** : What will be stored in the variable ty below?

```python
qu = "wow, welcome week! Were you wanting to go?"
ty = qu.count("we")
```

A. 0 <br>
B. 2 ✅ <br>
C. 3 <br>
D. There is an error. <br>



---

**E3** : What will be stored in the variable ht below?

```python
rooms = ['bathroom', 'kitchen', 'living room', 'bedroom', 'closet', "foyer"]
ht = rooms.index("garden")
```

A. 0 <br>
B. -1 <br>
C. There is an error. ✅ <br>


Split and Join

#### `.split()`

Two of the most useful methods on strings involve lists of strings. The `split` method breaks a string into a list of words. By default, any number of whitespace characters is considered a word boundary.

![](https://fopp.umsi.education/runestone/static/fopp/_images/split_default.gif)

```python
song = "The rain in Spain..."
wds = song.split()
print(wds)
```

**Output** :

```
["The", "rain", "in", "Spain..."]
```

An optional argument called a **delimiter** can be used to specify which characters to use as word boundaries.

![](https://fopp.umsi.education/runestone/static/fopp/_images/split_on_e.jpeg)

The following example uses the string `ai` as the delimiter:

```python
song = "The rain in Spain..."
wds = song.split("ai")
print(wds)
```

**Output** :

```
['The r', 'n in Sp', 'n...']
```

Notice that the delimiter doesn’t appear in the result.

#### `.join()`

The inverse of the `split` method is `join`. You choose a desired **separator** string, (often called the *glue*) and join the list with the glue between each of the elements.


![](https://fopp.umsi.education/runestone/static/fopp/_images/join.gif)

```python
wds = ["red", "blue", "green"]
glue = ";"
s = glue.join(wds)
print(s)
print(wds)

print("***".join(wds))
print("".join(wds))
```

**Output** :

```
red;blue;green
["red", "blue", "green"]
red***blue***green
redbluegreen
```

The list that you glue together (`wds` in this example) is not modified. Also, you can use empty glue or multi-character strings as glue.


-----
--------

**Check your understanding**

**E1** : Create a new list of the 6th through 13th elements of `lst` (eight items in all) and assign it to the variable `output`.

```python
lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]
```

**Solution** :

```python
lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]

output = lst[5:13]
print(output)
```

**Output** :

```
['shine', 'marsh', 'winter', 'donkey', 'rain', ['Rio', 'Beijing', 'London'], [1, 2, 3], 'gold']
```


---

**E2** : Create a variable `output` and assign it to a list whose elements are the words in the string `str1`.



```python
str1 = "OH THE PLACES YOU'LL GO"
```

**Solution** :

```python
str1 = "OH THE PLACES YOU'LL GO"
output = str1.split()
print(output)
```

**Output** :

```
['OH', 'THE', 'PLACES', "YOU'LL", 'GO']
```

---

#### Split and Join

#### `.split()`

Two of the most useful methods on strings involve lists of strings. The `split` method breaks a string into a list of words. By default, any number of whitespace characters is considered a word boundary.

![](https://fopp.umsi.education/runestone/static/fopp/_images/split_default.gif)

```python
song = "The rain in Spain..."
wds = song.split()
print(wds)
```

**Output** :

```
["The", "rain", "in", "Spain..."]
```

An optional argument called a **delimiter** can be used to specify which characters to use as word boundaries.

![](https://fopp.umsi.education/runestone/static/fopp/_images/split_on_e.jpeg)

The following example uses the string `ai` as the delimiter:

```python
song = "The rain in Spain..."
wds = song.split("ai")
print(wds)
```

**Output** :

```
['The r', 'n in Sp', 'n...']
```

Notice that the delimiter doesn’t appear in the result.

#### `.join()`

The inverse of the `split` method is `join`. You choose a desired **separator** string, (often called the *glue*) and join the list with the glue between each of the elements.


![](https://fopp.umsi.education/runestone/static/fopp/_images/join.gif)

```python
wds = ["red", "blue", "green"]
glue = ";"
s = glue.join(wds)
print(s)
print(wds)

print("***".join(wds))
print("".join(wds))
```

**Output** :

```
red;blue;green
["red", "blue", "green"]
red***blue***green
redbluegreen
```

The list that you glue together (`wds` in this example) is not modified. Also, you can use empty glue or multi-character strings as glue.


-----
--------

**Check your understanding**

**E1** : Create a new list of the 6th through 13th elements of `lst` (eight items in all) and assign it to the variable `output`.

```python
lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]
```

**Solution** :

```python
lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]

output = lst[5:13]
print(output)
```

**Output** :

```
['shine', 'marsh', 'winter', 'donkey', 'rain', ['Rio', 'Beijing', 'London'], [1, 2, 3], 'gold']
```


---

**E2** : Create a variable `output` and assign it to a list whose elements are the words in the string `str1`.



```python
str1 = "OH THE PLACES YOU'LL GO"
```

**Solution** :

```python
str1 = "OH THE PLACES YOU'LL GO"
output = str1.split()
print(output)
```

**Output** :

```
['OH', 'THE', 'PLACES', "YOU'LL", 'GO']
```

---

Chapter Assessments & Exercises

#### Assessments

**A1**. What will the output be for the following code?


```python
let = "z"
let_two = "p"
c = let_two + let
m = c * 5
print(m)
```

A. zpzpzpzpzp <br>
B. zzzzzppppp <br>
C. pzpzpzpzpz ✅ <br>
D. pppppzzzzz <br>
E. None of the above, an error will occur. <br>



-----

**A2**. Write a program that extracts the last three items in the list sports and assigns it to the variable last. Make sure to write your code so that it works no matter how many items are in the list.


```python
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
```

**Solution** :

```python
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']

last = sports[-3:]
print(last)
```

**Output** :

```
['curling', 'ping pong', 'hockey']
```


-----

**A3**. Write code that combines the following variables so that the sentence “You are doing a great job, keep it up!” is assigned to the variable `message`. Do not edit the values assigned to `by`, `az`, `io`, or `qy`.


```python
by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"
```

**Solution** :

```python
by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"

message = by + " " + az + io + ", " + qy
print(message)
```

**Output** :

```
You are doing a great job, keep it up!
```



-----

**A4**. What will the output be for the following code?


```python
ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
new = ls[2:4]
print(new)
```

A. ['travel', 'lights', 'moon'] <br>
B. ['world', 'travel', 'lights'] <br>
C. ['travel', 'lights'] ✅ <br>
D. ['world', 'travel'] <br>


-----

**A5**. What is the type of `m`?


```python
l = ['w', '7', 0, 9]
m = l[1:2]
```

A. string <br>
B. integer <br>
C. float <br>
D. list ✅ <br>



-----

**A6**. What is the type of `m`?


```python
l = ['w', '7', 0, 9]
m = l[1]
```

A. string ✅ <br>
B. integer <br>
C. float <br>
D. list <br>


-----

**A7**. What is the type of `x`?


```python
b = "My, what a lovely day"
x = b.split(',')
```

A. string <br>
B. integer <br>
C. float <br>
D. list ✅ <br>



-----

**A8**. What is the type of `a`?


```python
b = "My, what a lovely day"
x = b.split(',')
z = "".join(x)
y = z.split()
a = "".join(y)
```

A. string ✅ <br>
B. integer <br>
C. float <br>
D. list <br>



-----

**A9**. Write code to determine how many 9’s are in the list `nums` and assign that value to the variable `how_many`. Do not use a for loop to do this.


```python
nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
```

**Solution** :

```python
nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]

how_many = nums.count(9)
print(how_many)
```

**Output** :

```
3
```

-----

**A10**. Write code that uses slicing to get rid of the the second 8 so that here are only two 8’s in the list bound to the variable nums.


```python
nums = [4, 2, 8, 23.4, 8, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
```

**Solution** :

```python
nums = [4, 2, 8, 23.4, 8, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]

nums = nums[:4] + nums[5:]
print(nums)
```

**Output** :

```
[4, 2, 8, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9, 34, 52, 1, -2, 9.1, 4]
```



-----

**A11**. Assign the last element of `lst` to the variable `end_elem`. Do this so that it works no matter how long lst is.


```python
lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

```

**Solution** :

```python
lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

end_elem = lst[-1]
print(end_elem)
```

**Output** :

```
26trombones
```


-----

**A12**. Assign the number of elements in `lst` to the variable `num_lst`.


```python
lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]
```

**Solution** :

```python
lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

num_lst = len(lst)
print(num_lst)
```

**Output** :

```
30
```



-----

**A13**. Create a variable called `wrds` and assign to it a list whose elements are the words in the string `sent`. Do not worry about punctuation.


```python
sent = "The bicentennial for our university was in 2017"
```

**Solution** :

```python
sent = "The bicentennial for our university was in 2017"
wrds = sent.split()
print(wrds)
```

**Output** :

```
['The', 'bicentennial', 'for', 'our', 'university', 'was', 'in', '2017']
```


----
----

#### Exercises

**Q1**. Write a program that will print out the length of each item in the list as well as the first and last characters of the item.

![](http://i67.tinypic.com/67kuw3.png)


----

**Q2**. Write code to determine how many t's are in the following sentences.

![](http://i63.tinypic.com/awfjer.png)

----



### Iteration



### The Way of the Programmer

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

#### 2.9. The For Loop

Back when we drew the images with turtle it could be quite tedious. If we wanted to draw a square then we had to move then turn, move then turn, etc. etc. four times. If we were drawing a hexagon, or an octagon, or a polygon with 42 sides, it would have been a nightmare to duplicate all that code.

A basic building block of all programs is to be able to repeat some code over and over again. We refer to this repetitive idea as **iteration**. In this section, we will explore some mechanisms for basic iteration.

In Python, the for statement allows us to write programs that implement iteration. As a simple example, let’s say we have some friends, and we’d like to send them each an email inviting them to our party. We don’t quite know how to send email yet, so for the moment we’ll just print a message for each friend.


```python
for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
	print("Hi", name, "Please come to my party on Saturday!")
```

**Output** :

```
Hi Joe Please come to my party on Saturday!
Hi Amy Please come to my party on Saturday!
Hi Brad Please come to my party on Saturday!
Hi Angelina Please come to my party on Saturday!
Hi Zuki Please come to my party on Saturday!
Hi Thandi Please come to my party on Saturday!
Hi Paris Please come to my party on Saturday!
```


Take a look at the output produced when you press the `run` button. There is one line printed for each friend. Here’s how it works:

* **name** in this `for` statement is called the **loop variable** or, alternatively, the **iterator variable**.
* The list of names in the square brackets is the sequence over which we will iterate.
* Line 2 is the **loop body**. The loop body is always indented. The indentation determines exactly what statements are “in the loop”. The loop body is performed one time for each name in the list.
* On each *iteration* or *pass* of the loop, first a check is done to see if there are still more items to be processed. If there are none left (this is called the **terminating condition** of the loop), the loop has finished. Program execution continues at the next statement after the loop body.
* If there are items still to be processed, the loop variable is updated to refer to the next item in the list. This means, in this case, that the loop body is executed here 7 times, and each time `name` will refer to a different friend.
* At the end of each execution of the body of the loop, Python returns to the `for` statement, to see if there are more items to be handled.

The overall syntax is `for <loop_var_name> in <sequence>:`

* Between the words `for` and `in`, there must be a variable name for the loop variable. You can’t put a whole expression there.
* A colon is required at the end of the line
* After the word in and before the colon is an expression that must evaluate to a sequence (e.g, a string or a list or a tuple). It could be a literal, or a variable name, or a more complex expression.


#### Flow of Execution of the `for` Loop

As a program executes, the interpreter always keeps track of which statement is about to be executed. We call this the **control flow**, or the **flow of execution** of the program. When humans execute programs, they often use their finger to point to each statement in turn. So you could think of control flow as “Python’s moving finger”.


Control flow until now has been strictly top to bottom, one statement at a time. We call this type of control **sequential**. Sequential flow of control is always assumed to be the default behavior for a computer program. The `for` statement changes this.


Flow of control is often easy to visualize and understand if we draw a flowchart. This flowchart shows the exact steps and logic of how the `for` statement executes.


![](https://fopp.umsi.education/runestone/static/fopp/_images/new_flowchart_for.png)

While loops may not seem to be necessary when you’re iterating over a few items, it is extremely helpful when iterating over lots of items. Imagine if you needed to change what happened in the code block. On the left, when you use iteration, this is easy. On the right, when you have hard coded the process, this is more difficult.


![](https://fopp.umsi.education/runestone/static/fopp/_images/iteration_vs_hardcoding.png)

#### Strings and `for` loops


Since a string is simply a sequence of characters, the `for` loop iterates over each character automatically.

```python
for achar in "Go Spot Go":
	print("char")
```

**Output** :

```
G
o

S
p
o
t

G
o
```

The loop variable `achar` is automatically reassigned each character in the string “Go Spot Go”. We will refer to this type of sequence iteration as **iteration by item**. Note that the for loop processes the characters in a string or items in a sequence one at a time from left to right.


#### Lists and `for` loops

It is also possible to perform **list traversal** using iteration by item. A list is a sequence of items, so the `for` loop iterates over each item in the list automatically.

```python
fruits = ["apple", "orange", "banana", "cherry"]

for afruit in fruits:
	print(afruit)
```

**Output** :

```
apple
orange
banana
cherry
```

It almost reads like natural language: For (every) fruit in (the list of) fruits, print (the name of the) fruit.


#### Iteration Simplifies our Turtle Program

To draw a square we’d like to do the same thing four times — move the turtle forward some distance and turn 90 degrees. We previously used 8 lines of Python code to have alex draw the four sides of a square. This next program does exactly the same thing but, with the help of the for statement, uses just three lines (not including the setup code). Remember that the for statement will repeat the forward and left four times, one time for each value in the list.

```python
import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(1)

for i in [0,1,2,3]:
	alex.forward(50)
	alex.left(90)

wn.exitonclick()
```

**Output** :

![](https://media.giphy.com/media/JNsxfnGjDxXiBFfah9/giphy.gif)


While “saving some lines of code” might be convenient, it is not the big deal here. What is much more important is that we’ve found a “repeating pattern” of statements, and we reorganized our program to repeat the pattern.

The values [0,1,2,3] were provided to make the loop body execute 4 times. We could have used any four values. For example, consider the following program.


```python
import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(1)

for i in ["yellow", "red", "purple", "blue"]:
	alex.forward(50)
	alex.left(90)

wn.exitonclick()
```

**Output** :

![](https://media.giphy.com/media/JNsxfnGjDxXiBFfah9/giphy.gif)


In the previous example, there were four integers in the list. This time there are four strings. Since there are four items in the list, the iteration will still occur four times. `aColor` will take on each color in the list. We can even take this one step further and use the value of `aColor` as part of the computation.


```python
import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(1)

for aColor in ["yellow", "red", "purple", "blue"]:
	alex.color(aColor)
	alex.forward(50)
	alex.left(90)

wn.exitonclick()
```

**Output** :

![](https://media.giphy.com/media/kaBYWace19K4sBiTty/giphy.gif)


In this case, the value of `aColor` is used to change the color attribute of `alex`. Each iteration causes `aColor` to change to the next value in the list.

The for-loop is our first example of a **compound statement**. Syntactically a compound statement is a statement. The level of indentation of a (whole) compound statement is the indentation of its heading. In the example above there are five statements with the same indentation, executed sequentially: the import, 2 assignments, the whole for-loop, and `wn.exitonclick()`. The for-loop compound statement is executed completely before going on to the next sequential statement, `wn.exitonclick()`.


-----
--------

**Check your understanding**

**E1** : How many times is the word HELLO printed by the following statements?

```python
s = "python rocks"
for ch in s:
	print("HELLO")
```


A. 10 <br>
B. 11 <br>
C. 12 ✅ <br>
D. Error, the for statement needs to use the range function.  <br>

---

**E2** : How many times is the word HELLO printed by the following statements?


```python
s = "python rocks"
for ch in s[3:8]:
	print("HELLO")
```


A. 4 <br>
B. 5 ✅ <br>
C. 6 <br>
D. Error, the for statement cannot use slice.  <br>

---


**E3** : How many times will the for loop iterate in the following statements?


```python
p = [3, 4, "Me", 3, [], "Why", 0, "Tell", 9.3]
for ch in p:
	print(ch)
```


A. 8 <br>
B. 9 ✅ <br>
C. 15 <br>
D. Error, the for statement needs to use the range function.  <br>

---

**E4** : How does python know what statements are contained in the loop body?


A. They are indented to the same degree from the loop header. ✅ <br>
B. There is always exactly one line in the loop body. <br>
C. 15 <br>
D. The loop body ends with a semi-colon (; ) which is not shown in the code above.  <br>

---


**E5** : Consider the following code:


```python
for aColor in ["yellow", "red", "green", "blue"]:
	alex.forward(50)
	alex.left(90)
```

What does each iteration through the loop do?

A. Draw a square using the same color for each side. <br>
B. Draw a square using a different color for each side. <br>
C. Draw one side of a square. ✅ <br>

---

#### The Accumulator Pattern and `range` Function

One common programming “pattern” is to traverse a sequence, accumulating a value as we go, such as the sum-so-far or the maximum-so-far. That way, at the end of the traversal we have accumulated a single value, such as the sum total of all the items or the largest item.

***The anatomy of the accumulation pattern includes:***
* initializing an “accumulator” variable to an initial value (such as 0 if accumulating a sum)
* iterating (e.g., traversing the items in a sequence)
* updating the accumulator variable on each iteration (i.e., when processing each item in the sequence)

For example, consider the following code, which computes the sum of the numbers in a list.


```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accum = 0
for w in nums:
	accum = accum + w
print(accum)
```

**Output** :

```
55
```

In the program above, notice that the variable `accum` starts out with a value of 0. Next, the iteration is performed 10 times. Inside the for loop, the update occurs. `w` has the value of current item (1 the first time, then 2, then 3, etc.). `accum` is reassigned a new value which is the old value plus the current value of `w`.

This pattern of iterating the updating of a variable is commonly referred to as the **accumulator pattern**. We refer to the variable as the **accumulator**. This pattern will come up over and over again. Remember that the key to making it work successfully is to be sure to initialize the variable before you start the iteration. Once inside the iteration, it is required that you update the accumulator.

We can utilize the range function in this situation as well. Previously, you’ve seen it used when we wanted to draw in turtle. There we used it to iterate a certain number of times. We can do more than that though. The `range` function takes at least one input - which should be an integer - and returns a list as long as your input. While you can provide two inputs, we will focus on using range with just one input. With one input, range will start at zero and go up to - but not include - the input. Here are the examples:

```python
print("range(5)")
for i in range(5):
	print(i)

print("range(0,5)")
for i in range(0,5):
	print(i)

print("range(1,5)")
for i in range(1,5):
	print(i)

print(list(range(5)))
print(list(range(0,5)))

print(range(5))
```

**Output** :

```
range(5)
0
1
2
3
4
range(0,5)
0
1
2
3
4
range(1,5)
1
2
3
4
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
range(0, 5)
```

One important thing to know about the range function in python3 is that if we want to use it outside of iteration, we have to cast it as a list using `list()`. Inside the textbook you’ll notice that `range` works with or without casting it as a list but it is best for you to try and get into the habit of casting it as a list. Here’s how you could use the range function in the previous problem.



```python
accum = 0
for w in range(11):
	accum = accum + w
print(accum)

sec_accum = 0
for w in range(1,11):
	sec_accum = sec_accum + w
print(sec_accum)
```

**Output** :

```
55
55
```


Because the range function is exclusive of the ending number, we have to use 11 as the function input.

We can use the accumulation pattern is count the number of something or to sum up a total. The above examples only covered how to get the sum for a list, but we can also count how many items are in the list if we wanted to.

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for w in nums:
	count = count + 1
print(count)
```

**Output** :

```
10
```

In this example we don’t make use of `w` even though the iterator variable (loop variable) is a necessary part of constructing a for loop. Instead of adding the value of `w` to `count` we add a 1 to it, because we’re incrementing the value of count when we iterate each time through the loop. Though in this scenario we could have used the `len` function, there are other cases later on where len won’t be useful but we will still need to count.

-----
--------

**Check your understanding**

**E1** : Consider the following code:

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for w in nums :
	accum = 0
	accum = accum + w
print(accum)
```

What happens if you put the initialization of accum inside the for loop as the first instruction in the loop?


A. It will print out 10 instead of 55 ✅ <br>
B. It will cause a run-time error <br>
C. It will print out 0 instead of 55 <br>

---

**E2** : Rearrange the code statements so that the program will add up the first n odd numbers where n is provided by the user.

![](http://i65.tinypic.com/rbkv20.png)

---

**E3** : Write code to create a list of integers from 0 through 52 and assign that list to the variable `numbers`. You should use a special Python function – do not type out the whole list yourself. HINT: You can do this in one line of code!

```python
numbers = list(range(53))
print(numbers)
```

**Output** :

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
```

----


**E4** : Count the number of characters in string `str1`. Do not use `len()`. Save the number in variable `numbs`.

```python
# Given
str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."


# Solution
numbs = 0
for char in str1:
    numbs += 1
print(numbs)
```

**Output** :

```
90
```

----


**E5** : Create a list of numbers 0 through 40 and assign this list to the variable `numbers`. Then, accumulate the total of the list’s values and assign that sum to the variable `sum1`.

```python
numbers = list(range(41))
sum1 = 0
for num in numbers:
    sum1 += num
print(sum1)
```

**Output** :

```
820
```

----

#### Traversal and the `for` Loop: By Index

It is also possible to iterate through the indexes of a string or sequence. The `for` loop can then be used to iterate over these positions. These positions can be used together with the indexing operator to access the individual characters in the string. We can use **Enumerate**, a built-in Python function, to make this process easier because it allows us to loop through something and have an automatic counter.



```python
for counter, item in enumerate(["apple", "pear", "apricot", "cherry", "peach"]):
	print(counter, item)
```

**Output** :

```
0 apple
1 pear
2 apricot
3 cherry
4 peach
```


By using the enumerate function, we can print out a counter that tells us the position of an item in a list. We could do this ourselves, but this saves us from having to do that. The index positions in the list are 0, 1 , 2, 3, and 4. This is exactly the same sequence of integers that are stored in `counter` each time the loop is iterated. The first time through the for loop, `counter` will be 0 and “apple” will be printed. Then, `counter` will be reassigned to 1 and “pear” will be displayed. This will continue until the list has ended, so that the final value for `counter` will be 4 and the final value of `item` will be “peach”.

Conveniently, we can also use the `range` function to automatically generate the indices of the characters.


```python
x = range(5)
print(type(x))
print(x)
print(list(x))
```

**Output** :

```
<class 'range'>
range(0, 5)
[0, 1, 2, 3, 4]
```

In order to make the iteration more general, we can use the `len` function to provide the bound for `range`. This is a very common pattern for traversing any sequence by position. Make sure you understand why the range function behaves correctly when using `len` of the string as its parameter value.


```python
fruit = ["apple", "pear", "apricot", "cherry", "peach"]
for n in range(len(fruit)):
	print(n, fruit[n])
```

**Output** :

```
0 apple
1 pear
2 apricot
3 cherry
4 peach
```

You may also note that iteration by position allows the programmer to control the direction of the traversal by changing the sequence of index values.


```python
fruit = ["apple", "pear", "apricot", "cherry", "peach"]
for idx in [0, 2, 4, 3, 1]:
	print(fruit[idx])
```

**Output** :

```
apple
apricot
peach
cherry
pear
```

-----
--------

**Check your understanding**

**E1** : How many times is the letter p printed by the following statements?

```python
s = "python"
for idx in range(len(s)):
	print(s[idx % 2])
```

A. 0 <br>
B. 1 <br>
C. 2 <br>
D. 3 ✅<br>
E. 6 <br>

---


#### Nested Iteration: Image Processing

Two dimensional tables have both rows and columns. You have probably seen many tables like this if you have used a spreadsheet program. Another object that is organized in rows and columns is a digital image. In this section we will explore how iteration allows us to manipulate these images.

A **digital image** is a finite collection of small, discrete picture elements called **pixels**. These pixels are organized in a two-dimensional grid. Each pixel represents the smallest amount of picture information that is available. Sometimes these pixels appear as small “dots”.

Each image (grid of pixels) has its own width and its own height. The width is the number of columns and the height is the number of rows. We can name the pixels in the grid by using the column number and row number. However, it is very important to remember that computer scientists like to start counting with 0! This means that if there are 20 rows, they will be named 0,1,2, and so on through 19. This will be very useful later when we iterate using range.

In the figure below, the pixel of interest is found at column `c` and row `r`.

![](https://fopp.umsi.education/runestone/static/fopp/_images/image.png)


#### The RGB Color Model

Each pixel of the image will represent a single color. The specific color depends on a formula that mixes various amounts of three basic colors: red, green, and blue. This technique for creating color is known as the **RGB Color Model**. The amount of each color, sometimes called the intensity of the color, allows us to have very fine control over the resulting color.

The minimum intensity value for a basic color is 0. For example if the red intensity is 0, then there is no red in the pixel. The maximum intensity is 255. This means that there are actually 256 different amounts of intensity for each basic color. Since there are three basic colors, that means that you can create 2563 distinct colors using the RGB Color Model.

Here are the red, green and blue intensities for some common colors. Note that “Black” is represented by a pixel having no basic color. On the other hand, “White” has maximum values for all three basic color components.


| Color | Red | Green | Blue |
|--|--|--|--|
| Red | 255 | 0 | 0 |
| Green | 0 | 255 | 0 |
| Blue | 0 | 0 | 255 |
| White | 255 | 255 | 255 |
| Black | 0 | 0 | 0 |
| Yellow | 255 | 255 | 0 |
| Magenta | 255 | 0 | 255 |

In order to manipulate an image, we need to be able to access individual pixels. This capability is provided by a module called **image**, provided in ActiveCode [1]. The image module defines two classes: `Image` and `Pixel`.

***If you want to explore image processing on your own outside of the browser you can install the cImage module from http://pypi.org.***


Each Pixel object has three attributes: the red intensity, the green intensity, and the blue intensity. A pixel provides three methods that allow us to ask for the intensity values. They are called `getRed`, `getGreen`, and `getBlue`. In addition, we can ask a pixel to change an intensity value using its `setRed`, `setGreen`, and `setBlue` methods.


| Color | Red | Green |
|--|--|--|
| `Pixel(r,g,b)` | `Pixel(20,100,50)` | Create a new pixel with 20 red, 100 green, and 50 blue. |
| `getRed()` | `r = p.getRed()` | Return the red component intensity. |
| `getGreen()` | `r = p.getGreen()` | Return the green component intensity. |
| `getBlue()` | `r = p.getBlue()` | Return the blue component intensity. |
| `setRed()` | `p.setRed(100)` | Set the red component intensity to 100. |
| `setGreen()` | `p.setGreen(45)` | Set the green component intensity to 45. |
| `setBlue()` | `p.setBlue(156` | Set the blue component intensity to 156. |


In the example below, we first create a pixel with 45 units of red, 76 units of green, and 200 units of blue. We then print the current amount of red, change the amount of red, and finally, set the amount of blue to be the same as the current amount of green.


```python
import image

p = image.Pixel(45, 76, 200)
print(p.getRed())

p.setRed(66)
print(p.getRed())

p.setBlue(p.getGreen())
print(p.getGreen(), p.getBlue())
```

**Output** :

```
45
66
76 76
```


#### Image Objects

To access the pixels in a real image, we need to first create an `Image` object. Image objects can be created in two ways. First, an Image object can be made from the files that store digital images. The image object has an attribute corresponding to the width, the height, and the collection of pixels in the image.

It is also possible to create an Image object that is “empty”. An `EmptyImage` has a width and a height. However, the pixel collection consists of only “White” pixels.

We can ask an image object to return its size using the `getWidth` and `getHeight` methods. We can also get a pixel from a particular location in the image using getPixel and change the pixel at a particular location using `setPixel`.

The Image class is shown below. Note that the first two entries show how to create image objects. The parameters are different depending on whether you are using an image file or creating an empty image.


| Method Name | Example | Explanation |
|--|--|--|
| `Image(filename)` | `img = image.Image(“cy.png”)` | Create an Image object from the file cy.png |
| `EmptyImage()` | `img = image.EmptyImage(100,200)` | Create an Image object that has all “White” pixels |
| `getWidth()` | `w = img.getWidth()` | Return the width of the image in pixels |
| `getHeight()` | `h = img.getHeight()` | Return the height of the image in pixels |
| `getPixel(col,row)` | `p = img.getPixel(35,86)` | Return the pixel at column 35, row 86 |
| `setPixel(col,row,p)` | `img.setPixel(100,50,mp)` | Set the pixel at column 100, row 50 to be mp |

Consider the image shown below. Assume that the image is stored in a file called “luther.jpg”. Line 2 opens the file and uses the contents to create an image object that is referred to by `img`. Once we have an image object, we can use the methods described above to access information about the image or to get a specific pixel and check on its basic color intensities.

![](https://fopp.umsi.education/runestone/static/fopp/_static/LutherBellPic.jpg)



```python
import image
img = image.Image("luther.jpg")

print(img.getWidth())
print(img.getHeight())

p = img.getPixel(45, 55)
print(p.getRed(), p.getGreen(), p.getBlue())
```

**Output** :

```
400
244
165 161 158
```

When you run the program you can see that the image has a width of 400 pixels and a height of 244 pixels. Also, the pixel at column 45, row 55, has RGB values of 165, 161, and 158. Try a few other pixel locations by changing the `getPixel` arguments and rerunning the program.


#### Image Processing and Nested Iteration

**Image processing** refers to the ability to manipulate the individual pixels in a digital image. In order to process all of the pixels, we need to be able to systematically visit all of the rows and columns in the image. The best way to do this is to use **nested iteration**.

Nested iteration simply means that we will place one iteration construct inside of another. We will call these two iterations the **outer iteration** and the **inner iteration**. To see how this works, consider the iteration below.

```python
for i in range(5):
  print(i)
```

We have seen this enough times to know that the value of i will be 0, then 1, then 2, and so on up to 4. The `print` will be performed once for each pass. However, the body of the loop can contain any statements including another iteration (another `for` statement). For example,

```python
for i in range(5):
  for j in range(3):
    print(i, j)
```

The `for i` iteration is the outer iteration and the `for j` iteration is the inner iteration. Each pass through the outer iteration will result in the complete processing of the inner iteration from beginning to end. This means that the output from this nested iteration will show that for each value of `i`, all values of `j` will occur.

Here is the same example in activecode. Try it. Note that the value of `i` stays the same while the value of `j` changes. The inner iteration, in effect, is moving faster than the outer iteration.

```python
for i in range(5):
  for j in range(3):
    print(i, j)
```

**Output** :

```
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
3 0
3 1
3 2
4 0
4 1
4 2
```

Another way to see this in more detail is to examine the behavior with codelens. Step through the iterations to see the flow of control as it occurs with the nested iteration. Again, for every value of `i`, all of the values of `j` will occur. You can see that the inner iteration completes before going on to the next pass of the outer iteration.


Our goal with image processing is to visit each pixel. We will use an iteration to process each row. Within that iteration, we will use a nested iteration to process each column. The result is a nested iteration, similar to the one seen above, where the outer `for` loop processes the rows, from 0 up to but not including the height of the image. The inner `for` loop will process each column of a row, again from 0 up to but not including the width of the image.

The resulting code will look like the following. We are now free to do anything we wish to each pixel in the image.


```python
for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        # do something with the pixel at position (col,row)
```

One of the easiest image processing algorithms will create what is known as a **negative** image. A negative image simply means that each pixel will be the opposite of what it was originally. But what does opposite mean?

In the RGB color model, we can consider the opposite of the red component as the difference between the original red and 255. For example, if the original red component was 50, then the opposite, or negative red value would be `255-50` or 205. In other words, pixels with a lot of red will have negatives with little red and pixels with little red will have negatives with a lot. We do the same for the blue and green as well.

The program below implements this algorithm using the previous image (luther.jpg). Run it to see the resulting negative image. Note that there is a lot of processing taking place and this may take a few seconds to complete. In addition, here are two other images that you can use (cy.png and goldygopher.png).

![](https://fopp.umsi.education/runestone/static/fopp/_static/cy.png)
**cy.py**

![](https://fopp.umsi.education/runestone/static/fopp/_static/goldygopher.png)
**goldygopher.png**


Change the name of the file in the `image.Image()` call to see how these images look as negatives. Also, note that there is an `exitonclick` method call at the very end which will close the window when you click on it. This will allow you to “clear the screen” before drawing the next negative.

```python
import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        newred = 255 - p.getRed()
        newgreen = 255 - p.getGreen()
        newblue = 255 - p.getBlue()

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()
```

Let’s take a closer look at the code. After importing the image module, we create an image object called `img` that represents a typical digital photo. We will update each pixel in this image from top to bottom, left to right, which you should be able to observe. You can change the values in `setDelay` to make the program progress faster or slower.

Lines 8 and 9 create the nested iteration that we discussed earlier. This allows us to process each pixel in the image. Line 10 gets an individual pixel.

Lines 12-14 create the negative intensity values by extracting the original intensity from the pixel and subtracting it from 255. Once we have the `newred`, `newgreen`, and `newblue` values, we can create a new pixel (Line 15).

Finally, we need to replace the old pixel with the new pixel in our image. It is important to put the new pixel into the same location as the original pixel that it came from in the digital photo.

Try to change the program above so that the outer loop iterates over the columns and the inner loop iterates over the rows. We still create a negative image, but you can see that the pixels update in a very different order.

-----
--------

**Check your understanding**

**E1** : If you have a pixel whose RGB value is (50, 0, 0), what color will this pixel appear to be?


A. 0 <br>
B. 1 <br>
C. 2 <br>
D. 3 ✅ <br>
E. 6 <br>

---

**E2** : Using the previous ActiveCode example, select the answer that is closest to the RGB values of the pixel at row 100, column 30? The values may be off by one or two due to differences in browsers.


A. 149 132 122 <br>
B. 183 179 170 ✅ <br>
C. 165 161 158 <br>
D. 201 104 115 <br>

---


**E3** : What will the following nested for-loop print?

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

```
a. ✅
    0 0
    0 1
    1 0
    1 1
    2 0
    2 1

b.
    0   0
    1   0
    2   0
    0   1
    1   1
    2   1

c.
    0   0
    0   1
    0   2
    1   0
    1   1
    1   2

d.
    0   1
    0   1
    0   1
```

---


**E4** : What would the image produced from ActiveCode box 16 look like if you replaced the lines:

```python
newred = 255 - p.getRed()
newgreen = 255 - p.getGreen()
newblue = 255 - p.getBlue()
```

with the lines :

```python
newred = p.getRed()
newgreen = 0
newblue = 0
```


A. It would look like a red-washed version of the bell image ✅ <br>
B. It would be a solid red rectangle the same size as the original image <br>
C. It would look the same as the original image <br>
D. It would look the same as the negative image in the example code  <br>


### The Way of the Programmer

# Basics of Programming III
## 3.1. Lists

### 3.1.1. Introduction to Lists

When we start writing more complex programs, we’ll start working with more pieces of data. But data can get messy real fast if we’re not careful.

To keep our data tidy, we’ll want to use *data structures*. Data structures are formats that we can use to keep track of our data in an organized fashion.

*Lists* are one very basic data structure. Programmers use lists as a container to store multiple pieces of information that relate to each other in some way. Like a list of the presidents of the US, types of cheeses in alphabetical order, and the finishing positions of runners in a race

What makes lists special is that they order our data in a specific, linear sequence.

Since our values are kept in order, it allows us to easily find the information we’re looking for; otherwise, we’d have a huge jumbled mess of data!

In this lesson, we’re going to cover:

* Accessing an item from a list
* Adding an item to a list
* Removing an item from a list


##### Instructions
Comic strips function in a similar way to lists. We can think of the strip as the list and each frame as a separate item in the list. The narrative that makes up a comic demonstrates that the items follow a specific order.

We create lists by adding items to an empty list. Right now we have a bunch of comic frames, but they’re not in any order and our comic strip is empty. Complete the comic strip by placing the frames in the correct order. Here’s how the story should go:

* Codey plants a seed
* Codey waters the seed
* Codey waits
* A sprout grows


![](http://i68.tinypic.com/55kya9.png)


### 3.1.2. Accessing List Items

Lists *order* items so that they’re in a specific sequence. For example the comic strip, as a list, stores frames in a specific order. Without an order, the story wouldn’t make sense!

This idea of sequence is important because it tells us that each value has a specific position in the list. The position of value in a list is known as its index. You can think of an index like an address - it’s what we use to locate an item in a list.

List indices (the plural of index) are numbers. Usually, lists will start their index at 0 and then add one for each value. So if you want to select the first item in the list, make sure to remember to use 0 in order to do so!

![](https://s3.amazonaws.com/codecademy-content/programs/code-foundations-path/bop-iii/lists/array_slice.svg)

Knowing an item’s index allows us to select a value from a list and do something with it, like save it to a variable. It can also be useful in modifying a list, whether by adding something or removing it.

##### Instructions

You’ve created a comic strip and sent it to an editor for review. Your editor has asked you to make some changes to the frame at index 1.

Click to select the frame that is at index 1.

Hint: index 1 is equivalent to the second position in the list.


![](http://i64.tinypic.com/2z74xsx.png)



### 3.1.3. Adding Items to a List

After a list is created, we’re able to add things to it.

When we add things to the end of an existing list, we say that we’re appending them to the end. Imagine we’re trying out different endings for our comic strip. We can try adding different frames to our current narrative and see which one we like the best.

```js
myList = ['apple', 'banana', 'pear']

myList.append('orange')

// now, myList == ['apple', 'banana', 'pear', 'orange']
```

In addition to adding things to the end of a list, we can also insert items in the existing list. We do so by using the index number for where we want to position our new value.

```js
myList = ['apple', 'banana', 'pear']

myList.splice(1, 0, 'mango') // make 'mango' the second item in the list

// now, myList = ['apple', 'mango', 'banana', 'pear']
```

In this line of code, we inserted the string `'mango'` at the index 1 position. But it’s important to be careful - adding something in the middle of a pre-existing list, or adding it to the beginning of a list, will alter the indices for all the following items. Notice that ‘banana’ was in the second position and is now in the third.

In JavaScript, we can edit lists with commands like `.splice` and `.pop`. You don’t need to memorize these commands – the important part is that you understand the ways in which lists can be edited!

##### Instructions

You’re finishing up a comic strip, but having a hard time figuring out how it should end! You’re stuck between three different options.

Try adding each option to the end of the comic strip and see which one you like the best!


### 3.1.4. Removing Items from a List

We’re also able to remove items from a list.

Similar to adding items, we can modify lists by taking off the last item, or we can use indexing to select a specific item and remove it from the list.


```js
myList = ['apple', 'banana', 'pear']

myList.pop() // returns 'pear'

// now, myList == ['apple', 'banana']
```


##### Instructions

After looking at your comic strip, you decide that you want the ending to be a cliffhanger. Take off the last frame from the comic.

![](http://i66.tinypic.com/166k5rr.png)


### 3.1.5. Lists: Putting it Together
Great! Now that you know all about lists, let’s write some code.

There are many ways to create lists and they can change depending on what language you are programming in. For this exercise, we’ll create lists using the following syntax:

```js
myList = ['apple', 'banana', 'pear']
```

This line of code will create a list called myList that includes three items in the list. Each item is separated by a comma:

* `'apple'`
* `'banana'`
* `'pear'`

You may have noticed that those were all strings. We can also put other data types in a list, including numbers and boolean values. We can even put other lists in a list!

To select an item from the list, we use the following syntax:

```js
myList = [0]
```

As we may remember, the first item is at the 0th index. So this code would grab the string, 'apple'. We could also save this selection to a variable, so we can use it later in our code:

```js
myFruit = myList[0]
```

##### Instructions
First, create a list called `comicStrip`.

Save the following strings to `comicStrip`:

* `'Codey sees the trail'`
* `'Codey starts the hike'`
* `'Codey is halfway'`
* `'Codey reaches the finish'`

Run the code to see the comic strip!

Hint: make sure to separate each item with a comma: `,`.

Select the 4th item from the list and save it to the variable `selection`.

Run the code. Did you select the correct frame? Try selecting other items in the list.

Hint: Remember that lists start at index 0!

```js
// SOLUTION

comicStrip = ['Codey sees the trail', 'Codey starts the hike', 'Codey is halfway', 'Codey reaches the finish']

selection = comicStrip[3]
```

### 3.1.6. Lists: Review
Congratulations! Now you’ve learned about another data type known as a list.

* A list is an ordered sequence of information
* You can access an item in a list by using its index position
* You can append items to the end of the list or insert them in the middle
* You can also remove an item from the end or middle of a list

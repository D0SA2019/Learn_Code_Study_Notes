# Basics of Programming III
## 3.3. Loops

### 3.3.1. Introduction to Loops

How do we use code to tell a computer this: “Create a variable and call a function 15 times”?

We could write it out 15 times:

```
create a variable
call a function
create a variable
call a function
create a variable
call a function....
```

…We’ll spare you the rest. This approach takes a long time and it can easily lead to mistakes. Instead, let’s give the instructions once and tell the computer how many times to repeat them:

```
Repeat this 15 times:
  create a variable
  call a function
```
This structure is called a *loop*, and you’ll learn all about them in this lesson. These special structures in programming will give you the ability to repeat instructions multiple times without writing the instructions out multiple times.

This lesson will cover:

* for loops
* while loops
* for each loops

By the way, we assume that you’re familiar with creating variables, using operators, calling functions, and working with lists.

##### Instructions
Create a pattern WITHOUT loops: In the text box, repeat these instructions 10 times, then run it:

1. Place a pink tile
2. Place a orange tile
3. Place a mint tile

If you did it correctly, you’ll see all 30 tiles placed on the board!

![](http://i66.tinypic.com/24d4lmw.png)

### 3.3.2. For Loops
When we give instructions once and tell the computer how many times to repeat them, we are using a for loop, or a count-controlled loop. It executes a set of instructions for a specified number of times:

```
For 10 times:
  placeTile('pink')
  placeTile('orange')
  placeTile('mint')
```

The tile-placing instructions are the same from the previous exercise – Place a pink tile, Place a orange tile, Place a mint tile – written as calls to the `placetile()` function.

When a computer receives this program it sets a counter to 0 and executes the instructions in the body of the loop. After each iteration (one pass through the instructions), it advances the counter by 1. The process repeats until the counter is 10, meaning 10 iterations are completed.

The for loop is good to use when you know the number of times you’d like to perform a task before you begin, like printing 3 copies of a document or inserting 8 rows into a table.

##### Instructions

Place the same 30 tiles as before, but now with a *for* loop!

* Insert the three instructions (pink, orange, mint)
* Select the number of times the loop should run (hint: 30 / 3 = 10)
* Run it

Much faster than the previous exercise, right? You got the same outcome in much less time! Additionally, using this method reduces your chance of making a mistake in the pattern.

![](http://i68.tinypic.com/axfr76.png)

### 3.3.3. While Loops
What if you approached tile-placing another way: you don’t know how many tiles to place, but you know when to stop. How could you communicate this type of command to a computer? Give it the instructions and a condition:

```
While there are pink tiles available:
  placeTile('pink')
  placeTile('orange')
  placeTile('mint')
```

This is a while loop, or condition-controlled loop. It repeats a set of instructions while that condition is true. In this case, the computer will place tiles while there are pink tiles available.

In a while loop, the computer checks if the condition is satisfied. If it is, it executes the tasks in the loop body. It checks the condition again, and repeats. This continues until the condition is not satisfied, and it stops executing the tasks.

Use while loops when you know when a program should stop, but not the number of times it should repeat.

[codepen](https://codepen.io/hevalhazalkurt/pen/GeXZvy)

##### Instructions
Try the same task with a *while* loop:

* Insert the three instructions (pink, orange, mint)
* Select a condition
* Run it

Be careful of infinite loops! If the condition is always true, the loop will never stop.


![](http://i63.tinypic.com/155juc8.png)

[codepen](https://codepen.io/hevalhazalkurt/pen/GeXZvy)


### 3.3.4. For Each Loops

There’s one more way to give looping instructions to a computer. We define a sequence of desired tile colors (a list), and tell the computer to repeat the instructions for each item in the sequence. Here’s an example list:

```js
festiveList = ['pink', 'green', 'red', 'pink', 'green', 'red' ]
```
and the loop would look like:

```
For each color in festiveList:
  placeTile(color)
```

Why does this program look shorter than the ones before it? We only need to write `placeTile()` once because the pink-green-red repetition is already described in the list.

`color` is a variable whose value changes each iteration. It represents each item in the list. On the first iteration, its value would be `'pink'`, then `'green'`, then `'red'`, and so on.

The sequence we used was a list, but we can use other similar data types. The umbrella term for those is collection, so we may also call for each loops collection loops.

Use this loop when you need to perform a task for every item in a list, or when the order of things must be maintained. In this case, both were important. A tile must be placed for each item in the list and the order of them is essential to the pattern.


##### Instructions

Place the same 30 tiles as before, but now with a for each loop!

* Select the collection (list) to use
* Run it


![](http://i66.tinypic.com/dm2v47.png)

[codepen](https://codepen.io/hevalhazalkurt/pen/YgOqBY)


### 3.3.5. Putting it All Together
Let’s combine all that we’ve learned so far:

* variables, operators, and data types
* functions and control flow
* lists and loops

Examples of for and while loops are provided below in JavaScript. Copy each one to the editor and run it! You’ll see that they do the same things.

In this for loop, the instructions are run 10 times.

```js
for (i = 0; i < 10; i++) {
  placeTile('mint')
  placeTile('orange')
  placeTile('mint')
}
```

In this while loop, we create a counter at 0 and add 1 to it every iteration. The loop is executed until the counter is 10 or more.

```js
let i = 0;
while (i < 10) {
  placeTile('mint')
  placeTile('orange')
  placeTile('mint')
  i++
}
```

##### Instructions
1. Copy the for loop to the text editor. Run it.
2. Delete the for loop and copy the while loop to the text editor. Run it.
3. Edit the condition in the while loop so that the loop is executed twice (only 6 tiles should be placed).

Well done. If you’re feeling creative, change the colors! You can replace the strings with any other color you’ve seen in this lesson, like `'purple'`.


### 3.3.6. Review
Well done! Loops are commonly used in programming because they save time, reduce error, and are easy to read. Being comfortable with each type of loop will make you a better programmer. In review:

* A loop is a structure in programming where the instructions are written once, but a computer can execute them multiple times
* Each execution of those instructions is called an iteration
* For loops (count-controlled loops) repeat for a specified number of times
* While loops (condition-controlled loops) repeat until a condition changes
* For each loops (collection-controlled loops) repeat for each item in a collection

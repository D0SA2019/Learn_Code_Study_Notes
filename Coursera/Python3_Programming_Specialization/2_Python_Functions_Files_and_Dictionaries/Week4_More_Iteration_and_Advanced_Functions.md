# Python Functions, Files, and Dictionaries
*Coursera | Python 3 Programming Specialization | Course 2*

## Week 4 : More Iteration and Advanced Functions

### While Loop

#### 4.1. The While Statement

Computers are often used to automate repetitive tasks. Repeating identical or similar tasks without making errors is something that computers do well and people do poorly.

Repeated execution of a sequence of statements is called **iteration**. Because iteration is so common, Python provides several language features to make it easier. We’ve already seen the `for` statement in a previous chapter. This is a very common form of iteration in Python. In this chapter we are going to look at the `while` statement — another way to have your program do iteration.

There is another Python statement that can also be used to build an iteration. It is called the `while` statement. The while statement provides a much more general mechanism for iterating. Similar to the `if` statement, it uses a boolean expression to control the flow of execution. The body of while will be repeated as long as the controlling boolean expression evaluates to `True`.

The following two figures show the flow of control. The first focuses on the flow inside the while loop and the second shows the while loop in context.


![](https://fopp.umsi.education/runestone/static/fopp/_images/while_flow.png)
![](https://fopp.umsi.education/runestone/static/fopp/_images/while_loop.png)

We can use the `while` loop to create any type of iteration we wish, including anything that we have previously done with a `for` loop. For example, the program in the previous section could be rewritten using `while`. Instead of relying on the `range` function to produce the numbers for our summation, we will need to produce them ourselves. To do this, we will create a variable called `aNumber` and initialize it to 1, the first number in the summation. Every iteration will add `aNumber` to the running total until all the values have been used. In order to control the iteration, we must create a boolean expression that evaluates to `True` as long as we want to keep adding values to our running total. In this case, as long as `aNumber` is less than or equal to the bound, we should keep going.

Here is a new version of the summation program that uses a while statement.

```python
def sumTo(aBound):
	"""Return the sum of 1+2+3 ... n"""
	theSum = 0
	aNumber = 1
	while aNumber <= aBound:
		theSum = theSum + aNumber
		aNumber = aNumber + 1
	return theSum

print(sumTo(4))
print(sumTo(1000))
```


**Output**:

```
10
500500
```

You can almost read the `while` statement as if it were in natural language. It means, while `aNumber` is less than or equal to `aBound`, continue executing the body of the loop. Within the body, each time, update `theSum` using the accumulator pattern and increment `aNumber`. After the body of the loop, we go back up to the condition of the `while` and reevaluate it. When `aNumber` becomes greater than `aBound`, the condition fails and flow of control continues to the `return` statement.

More formally, here is the flow of execution for a `while` statement:

1. Evaluate the condition, yielding `False` or `True`.
2. If the condition is `False`, exit the `while` statement and continue execution at the next statement.
3. If the condition is `True`, execute each of the statements in the body and then go back to step 1.

The body consists of all of the statements below the header with the same indentation.

This type of flow is called a **loop** because the third step loops back around to the top. Notice that if the condition is `False` the first time through the loop, the statements inside the loop are never executed.

The body of the loop should change the value of one or more variables so that eventually the condition becomes `False` and the loop terminates. Otherwise the loop will repeat forever. This is called an **infinite loop**. An endless source of amusement for computer scientists is the observation that the directions written on the back of the shampoo bottle (lather, rinse, repeat) create an infinite loop.

In the case shown above, we can prove that the loop terminates because we know that the value of `aBound` is finite, and we can see that the value of `aNumber` increments each time through the loop, so eventually it will have to exceed `aBound`. In other cases, it is not so easy to tell.


**Note** : Introduction of the while statement causes us to think about the types of iteration we have seen. The `for` statement will always iterate through a sequence of values like the list of names for the party or the list of numbers created by `range`. Since we know that it will iterate once for each value in the collection, it is often said that a `for` loop creates a **definite iteration** because we definitely know how many times we are going to iterate. On the other hand, the `while` statement is dependent on a condition that needs to evaluate to `False` in order for the loop to terminate. Since we do not necessarily know when this will happen, it creates what we call **indefinite iteration**. Indefinite iteration simply means that we don’t know how many times we will repeat but eventually the condition controlling the iteration will fail and the iteration will stop. (Unless we have an infinite loop which is of course a problem)

What you will notice here is that the `while` loop is more work for you — the programmer — than the equivalent `for` loop. When using a `while` loop you have to control the loop variable yourself. You give it an initial value, test for completion, and then make sure you change something in the body so that the loop terminates. That also makes a while loop harder to read and understand than the equivalent for loop. So, while you can implement definite iteration with a while loop, it’s not a good idea to do that. Use a for loop whenever it will be known at the beginning of the iteration process how many times the block of code needs to be executed.

----
----

**Check Your Understanding**

**Q1** : True or False: You can rewrite any for-loop as a while-loop.

A. True ✅ <br>
B. False <br>

-----

**Q2** : The following code contains an infinite loop. Which is the best explanation for why the loop does not terminate?

```python
n = 10
aswer = 1
while (n > 0):
	answer = answer + n
	n = n + 1
print(answer)
```

A. n starts at 10 and is incremented by 1 each time through the loop, so it will always be positive ✅ <br>
B. answer starts at 1 and is incremented by n each time, so it will always be positive <br>
C. You cannot compare n to 0 in while loop. You must compare it to another variable. <br>
D. In the while loop body, we must set n to False, and this code does not do that. <br>


----

**Q3** : Which type of loop can be used to perform the following iteration: You choose a positive integer at random and then print the numbers from 1 up to and including the selected integer.

A. a for-loop or a while-loop ✅ <br>
B. only a for-loop <br>
C. only a while-loop <br>


----

**Q4** : Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called `eve_nums`.

```python
eve_nums = []
counter = 0

while counter <= 15:
	if counter % 2 == 0:
		eve_nums.append(counter)
	counter += 1

print(eve_nums)
```

**Output** :

```
[0, 2, 4, 6, 8, 10, 12, 14]
```

----

**Q5** : Below, we’ve provided a for loop that sums all the elements of `list1`. Write code that accomplishes the same task, but instead uses a while loop. Assign the accumulator variable to the name `accum`.

```python
# Given
list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
for elem in list1:
    tot = tot + elem


# Solution
list1 = [8, 3, 4, 5, 6, 7, 9]
aNum = 0
accum = 0

while aNum < 10:
	if aNum in list1:
		accum += aNum
	aNum += 1

print(accum)
```

**Output** :

```
42
```

----


**Q6** : Write a function called `stop_at_four` that iterates through a list of numbers. Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.

```python
def stop_at_four(aList):
	ind = 0
	newList = []
	while ind < len(aList):
		if aList[ind] != 4:
			newList.append(aList[ind])
			ind += 1
		else:
			break
	return newList


blist = [1, 3, 6, 3, 7, 4, 8, 30]
clist = [0, 9, 4.5, 1, 7, 4, 8, 9, 3]
dlist = [4, 1, 2, 8]
elist = [4]
flist = [1,6,2,3,9]

print(stop_at_four(blist))
print(stop_at_four(clist))
print(stop_at_four(dlist))
print(stop_at_four(elist))
print(stop_at_four(flist))
```

**Output** :

```
[1, 3, 6, 3, 7]
[0, 9, 4.5, 1, 7]
[]
[]
[1, 6, 2, 3, 9]
```

----

#### 4.2. The Listener Loop

At the end of the previous section, we advised using a for loop whenever it will be known at the beginning of the iteration process how many times the block of code needs to be executed. Usually, in python, you will use a for loop rather than a while loop. When is it not known at the beginning of the iteration how many times the code block needs to be executed? The answer is, when it depends on something that happens during the execution.

One very common pattern is called a **listener loop**. Inside the while loop there is a function call to get user input. The loop repeats indefinitely, until a particular input is received.


```python
theSum = 0
x = -1
while (x != 0):
	x = int(input("next number to add up (enter 0 if no more numbers): "))
	theSum = theSum + x

print(theSum)
```


**Output**:

```
next number to add up (enter 0 if no more numbers): 2
next number to add up (enter 0 if no more numbers): 4
next number to add up (enter 0 if no more numbers): 5
next number to add up (enter 0 if no more numbers): 2
next number to add up (enter 0 if no more numbers): 5
next number to add up (enter 0 if no more numbers): 0
18
```

This is just our old friend, the accumulation pattern, adding each additional output to the sum-so-far, which is stored in a variable called theSum and reassigned to that variable on each iteration. Notice that theSum is initialized to 0. Also notice that we had to initialize x, our variable that stores each input that the user types, before the while loop. This is typical with while loops, and makes them a little tricky to read and write. We had to initialize it because the condition `x != 0` is checked at the very beginning, before the code block is ever executed. In this case, we picked an initial value that we knew would make the condition true, to ensure that the while loop’s code block would execute at least once.

If you’re at all unsure about how that code works, try adding print statements inside the while loop that print out the values of x and theSum.

#### Other uses of `while`

##### Sentinel Values

Indefinite loops are much more common in the real world than definite loops.

* If you are selling tickets to an event, you don’t know in advance how many tickets you will sell. You keep selling tickets as long as people come to the door and there’s room in the hall.
* When the baggage crew unloads a plane, they don’t know in advance how many suitcases there are. They just keep unloading while there are bags left in the cargo hold. (Why your suitcase is always the last one is an entirely different problem.)
* When you go through the checkout line at the grocery, the clerks don’t know in advance how many items there are. They just keep ringing up items as long as there are more on the conveyor belt.

Let’s implement the last of these in Python, by asking the user for prices and keeping a running total and count of items. When the last item is entered, the program gives the grand total, number of items, and average price. We’ll need these variables:

* `total` - this will start at zero
* `count` - the number of items, which also starts at zero
* `moreItems` - a boolean that tells us whether more items are waiting; this starts as True

The pseudocode (code written half in English, half in Python) for the body of the loop looks something like this:

```python
while moreItems
	ask for price
	add price to total
	add one to count
```

This pseudocode has no option to set `moreItems` to `False`, so it would run forever. In a grocery store, there’s a little plastic bar that you put after your last item to separate your groceries from those of the person behind you; that’s how the clerk knows you have no more items. We don’t have a “little plastic bar” data type in Python, so we’ll do the next best thing: we will use a `price` of zero to mean “this is my last item.” In this program, zero is a **sentinel value**, a value used to signal the end of the loop. Here’s the code:

```python
def checkout():
	total = 0
	count = 0
	moreItems = True
	while moreItems:
		price = float(input("Enter price of item (0 when done): "))
		if price != 0:
			count = count + 1
			total = total + price
			print("Subtotal: $", total)
		else:
			moreItems = False
	average = total / count
	print("Total items: ", count)
	print("Total $", total)
	print("Average price per item: $", average)

checkout()
```

**Output** :

```
Enter price of item (0 when done): 5.4
Subtotal: $ 5.4
Enter price of item (0 when done): 2.4
Subtotal: $ 7.800000000000001
Enter price of item (0 when done): 3
Subtotal: $ 10.8
Enter price of item (0 when done): 4.0
Subtotal: $ 14.8
Enter price of item (0 when done): 0
Total items:  4
Total $ 14.8
Average price per item: $ 3.7
```

There are still a few problems with this program.

* If you enter a negative number, it will be added to the total and count. Modify the code so that negative numbers give an error message instead (but don’t end the loop) Hint: `elif` is your friend.
* If you enter zero the first time you are asked for a price, the loop will end, and the program will try to divide by zero. Use an `if/else` statement outside the loop to avoid the division by zero and tell the user that you can’t compute an average without data.
* This program doesn’t display the amounts to two decimal places. You’ll be introduced to that in another chapter.


##### Validating Input

You can also use a `while` loop when you want to **validate** input; when you want to make sure the user has entered valid input for a prompt. Let’s say you want a function that asks a yes-or-no question. In this case, you want to make sure that the person using your program enters either a Y for yes or N for no (in either upper or lower case). Here is a program that uses a `while` loop to keep asking until it receives a valid answer. As a preview of coming attractions, it uses the `upper()` method which is described in String Methods to convert a string to upper case. When you run the following code, try typing something other than Y or N to see how the code reacts:

```python
def get_yes_or_no(message):
	valid_input = False
	while not valid_input:
		answer = input(message)
		answer = answer.upper()
		if answer == "Y" or answer == "N":
			valid_input = True
		else:
			print("Please enter Y for yes or N for no.")
	return answer

response = get_yes_or_no("Do you like lima beans? Y)es or N)o: ")
if response == "Y":
	print("Great! They are very healthy!")
else:
	print("Too bad. If cooked right, they are quite tasty.")
```

**Output** :

```
Do you like lima beans? Y)es or N)o: n
Too bad. If cooked right, they are quite tasty.
```

----
----

#### 4.3. Randomly Walking Turtles

Suppose we want to entertain ourselves by watching a turtle wander around randomly inside the screen. When we run the program we want the turtle and program to behave in the following way:

1. The turtle begins in the center of the screen.
2. Flip a coin. If it’s heads then turn to the left 90 degrees. If it’s tails then turn to the right 90 degrees.
3. Take 50 steps forward.
4. If the turtle has moved outside the screen then stop, otherwise go back to step 2 and repeat.

Notice that we cannot predict how many times the turtle will need to flip the coin before it wanders out of the screen, so we can’t use a for loop in this case. In fact, although very unlikely, this program might never end, that is why we call this indefinite iteration.

So based on the problem description above, we can outline a program as follows:


```python
create a window and a turtle

while the turtle is still in the window:
	generate a random number between 0 and 1
	if the number == 0 (heads):
		turn left
	else:
		turn right
	move the turtle forward 50
```


Now, probably the only thing that seems a bit confusing to you is the part about whether or not the turtle is still in the screen. But this is the nice thing about programming, we can delay the tough stuff and get something in our program working right away. The way we are going to do this is to delegate the work of deciding whether the turtle is still in the screen or not to a boolean function. Let’s call this boolean function `isInScreen` We can write a very simple version of this boolean function by having it always return `True`, or by having it decide randomly, the point is to have it do something simple so that we can focus on the parts we already know how to do well and get them working. Since having it always return True would not be a good idea we will write our version to decide randomly. Let’s say that there is a 90% chance the turtle is still in the window and 10% that the turtle has escaped.

```python
import random
import turtle


def isInScreen(w, t):
    if random.random() > 0.1:
        return True
    else:
        return False


t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn, t):
    coin = random.randrange(0, 2)
    if coin == 0:              # heads
        t.left(90)
    else:                      # tails
        t.right(90)

    t.forward(50)

wn.exitonclick()
```

**Output**:

![](https://media.giphy.com/media/XeuzHtQoXjWuajq9YI/giphy.gif)


Now we have a working program that draws a random walk of our turtle that has a 90% chance of staying on the screen. We are in a good position, because a large part of our program is working and we can focus on the next bit of work – deciding whether the turtle is inside the screen boundaries or not.

We can find out the width and the height of the screen using the `window_width` and `window_height` methods of the screen object. However, remember that the turtle starts at position 0,0 in the middle of the screen. So we never want the turtle to go farther right than width/2 or farther left than negative width/2. We never want the turtle to go further up than height/2 or further down than negative height/2. Once we know what the boundaries are we can use some conditionals to check the turtle position against the boundaries and return `False` if the turtle is outside or `True` if the turtle is inside.

Once we have computed our boundaries we can get the current position of the turtle and then use conditionals to decide. Here is one implementation:

```python
def isInScreen(wn, t):
	leftBound = -(wn.window_width() / 2)
	rightBound = wn.window_width() / 2
	topBound = wn.window_height() / 2
	bottomBound = -(wn.window_height() / 2)

	turtleX = t.xcor()
	turtleY = t.ycor()

	stillIn = True
	if turtleX > rightBound or turtleX < leftBound:
		stillIn = False
	if turtleY > topBound or turtleY > bottomBound:
		stillIn = False
	return stillIn
```

There are lots of ways that the conditional could be written. In this case we have given `stillIn` the default value of `True` and use two `if` statements to possibly set the value to `False`. You could rewrite this to use nested conditionals or `elif` statements and set `stillIn` to `True` in an else clause.

Here is the full version of our random walk program.


```python
import random
import turtle

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn,t):
    coin = random.randrange(0, 2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)

wn.exitonclick()
```


**Output**:

![](https://media.giphy.com/media/VJfFJ5bNBFyUGnBu8m/giphy.gif)

We could have written this program without using a boolean function. You might want to try to rewrite it using a complex condition on the while statement. However, using a boolean function makes the program much more readable and easier to understand. It also gives us another tool to use if this was a larger program and we needed to have a check for whether the turtle was still in the screen in another part of the program. Another advantage is that if you ever need to write a similar program, you can reuse this function with confidence the next time you need it. Breaking up this program into a couple of parts is another example of functional decomposition.


----
----

**Check Your Understanding**

**Q1** : In the random walk program in this section, what does the isInScreen function do?

A. Returns True if the turtle is still on the screen and False if the turtle is no longer on the screen. ✅ <br>
B. Uses a while loop to move the turtle randomly until it goes off the screen. <br>
C. Turns the turtle right or left at random and moves the turtle forward 50. <br>
D. Calculates and returns the position of the turtle in the window. <br>

-----


#### 4.4. Break and Continue

Python provides ways for us to control the flow of iteration with a two keywords: break and continue.

`break` allows the program to immediately ‘break out’ of the loop, regardless of the loop’s conditional structure. This means that the program will then skip the rest of the iteration, without rechecking the condition, and just goes on to the next outdented code that exists after the whole while loop.

![](https://fopp.umsi.education/runestone/static/fopp/_images/while_and_break.png)



```python
while True:
	print("This phrase will always print")
	break
	print("Does this phrase print?")

print("We are done with the while loop.")
```

**Output**:

```
This phrase will always print
We are done with the while loop.
```

We can see here how the print statement right after `break` is not executed. In fact, without using break, we have no way to stop the while loop because the condition is always set to True!

`continue` is the other keyword that can control the flow of iteration. Using `continue` allows the program to immediately “continue” with the next iteration. The program will skip the rest of the iteration, recheck the condition, and maybe does another iteration depending on the condition set for the while loop.

![](https://fopp.umsi.education/runestone/static/fopp/_images/while_and_continue.png)

```python
x = 0

while x < 10:
	print("We are incrementing x")
	if x % 2 == 0:
		x += 3
		continue
	if x % 3 == 0:
		x += 5
	x += 1

print("Done with our loop! X has the value: " + str(x))
```

**Output**:

```
We are incrementing x
We are incrementing x
We are incrementing x
Done with our loop! X has the value: 15
```

----
----

#### 4.5. Infinite Loops

Although the textbook has a time limit which prevents an active code window from running indefinitely, you’ll still have to wait a little while if your program has an ininite loop. If you accidentally make one outside of the textbook, you won’t have that same protection.

So how can you recognize when you are in danger of making an infinite loop?

First off, if the variable that you are using to determine if the while loop should continue is never reset inside the while loop, then your code will have an infinite loop. (Unless of course you use `break` to break out of the loop.)

Additionally, if the while condition is `while True:` and there is no break, then that is another case of an infinite loop!


```python
while True:
	print("Will this stop?")

print("We have escaped.")
```

Another case where an infinite loop is likely to occur is when you have reassiged the value of the variable used in the while statement in a way that prevents the loop from completing.

```python
b = 15

while b < 60:
	#b = 5 		# This makes infinite loop
	print("Bugs")
	b = b + 7
```

**Output**:

```
Bugs
Bugs
Bugs
Bugs
Bugs
Bugs
Bugs
```

Notice how in this case, b is initally set to 15 outside of the while loop, and then reassigned the value of 5 inside, on line 4. By the time 7 has been added to b on line 6, we then have to check if b is less than 60. Because it isn’t we again run line 4, and set the value of b to 5 again. There is no way to break out of this loop.

Sometimes programs can take a while to run, so how can you determine if your code is just talking a while or if it is stuck inside an infinite loop? Print statements are for people, so take advantage of them! You can add print statements to keep track of how your variables are changing as the program processes the instructions given to them. Below is an example of an infinite loop. Try adding print statments to see where it’s coming from. When you’re done, check out the answer to see what our solution was.


```python
d = {"x": []}

while len(d.keys()) <= 2:
	print("Dictionaries")
	d["x"].append("d")
```

**Output**:

```
Dictionaries
Dictionaries
Dictionaries
Dictionaries
...
...
TimeLimitError: Program exceeded run time limit.
```


```python
d = {"x": []}

while len(d.keys()) <= 2:
	print("Dictionaries")
	d["x"].append("d")
	print(d["x"])
```

**Output**:

```
starting the while loop
number of keys in d: 1
Dictionaries
number of keys in d after appending: 1
number of keys in d: 1
Dictionaries
number of keys in d after appending: 1
number of keys in d: 1
Dictionaries
number of keys in d after appending: 1
number of keys in d: 1
...
...
TimeLimitError: Program exceeded run time limit.
```
----
----


### Advanced Functions

#### 4.6. Optional Parameters

In the treatment of functions so far, each function definition specifies zero or more formal parameters and each function invocation provides exactly that many values. Sometimes it is convenient to have **optional parameters** that can be specified or omitted. When an optional parameter is omitted from a function invocation, the formal parameter is bound to a **default value**. When the optional parameter is included, then the formal parameter is bound to the value provided. Optional parameters are convenient when a function is almost always used in a simple way, but it’s nice to allow it to be used in a more complex way, with non-default values specified for the optional parameters.

Consider, for example, the `int` function, which you have used previously. Its first parameter, which is required, specifies the object that you wish to convert to an integer. For example, if you call in on a string, `int("100")`, the return value will be the integer 100.

That’s the most common way programmers want to convert strings to integers. Sometimes, however, they are working with numbers in some other “base” rather than base 10. For example, in base 8, the rightmost digit is ones, the next digit to the left is 8s, and the one to the left of that is the 64s place (8**2).

The int function provides an optional parameter for the base. When it is not specified, the number is converted to an integer assuming the original number was in base 10. We say that 10 is the default value. So `int("100")` is the same as invoking `int("100", 10)`. We can override the default of 10 by supplying a different value.

```python
print(int("100"))
print(int("100", 10))
print(int("100", 8))
```

**Output**:

```
100
100
64
```

When defining a function, you can specify a default value for a parameter. That parameter then becomes an optional parameter when the function is called. The way to specify a default value is with an assignment statement inside the parameter list. Consider the following code, for example.


```python
initial = 7
def f(x, y = 3, z = initial):
	print("x, y, z, are: " + str(x) + "," + str(y) + "," + str(z))

f(2)
f(2, 5)
f(2, 5, 8)
```

**Output**:

```
x, y, z, are: 2,3,7
x, y, z, are: 2,5,7
x, y, z, are: 2,5,8
```

Notice the different bindings of x, y, and z on the three invocations of f. The first time, y and z have their default values, 3 and 7. The second time, y gets the value 5 that is passed in, but z still gets the default value of 7. The last time, z gets the value 8 that is passed in.

If you want to provide a non-default value for the third parameter (z), you also need to provide a value for the second item (y). We will see in the next section a mechanism called keyword parameters that lets you specify a value for z without specifying a value for y.

**Note** : This is a second, related but slightly different use of = than we have seen previously. In a stand-alone assignment statement, not part of a function definition, `x=3` assigns 3 to the variable x. As part of specifying the parameters in a function definition, `x=3` says that 3 is the default value for x, used only when no value is provided during the function invocation.

There are two tricky things that can confuse you with default values. The first is that the default value is determined at the time that the function is defined, not at the time that it is invoked. So in the example above, if we wanted to invoke the function f with a value of 10 for z, we cannot simply set initial = 10 right before invoking f. See what happens in the code below, where z still gets the value 7 when f is invoked without specifying a value for z.

```python
initial = 7
def f(x, y = 3, z = initial):
	print("x, y, z, are: " + str(x) + "," + str(y) + "," + str(z))

initial = 10

f(2)
```

**Output**:

```
x, y, z, are: 2,3,7
```

The second tricky thing is that if the default value is set to a mutable object, such as a list or a dictionary, that object will be shared in all invocations of the function. This can get very confusing, so I suggest that you never set a default value that is a mutable object. For example, follow the exceution of this one carefully.

```python
def f(a, L=[]):
	L.append(a)
	return L

print(f(1))
print(f(2))
print(f(3))
print(f(4, ["Hello"]))
print(f(5, ["Hello"]))
```

**Output**:

```
[1]
[1, 2]
[1, 2, 3]
['Hello', 4]
['Hello', 5]
```

When the default value is used, the same list is shared. But on lines 8 and 9 two different copies of the list [“Hello”] are provided, so the 4 that is appended is not present in the list that is printed on line 9.

----
----

**Check Your Understanding**

**Q1** : What will the following code print?

```python
def f(x = 0, y = 1):
	return x * y

print(f())
```

A. 0 ✅ <br>
B. 1 <br>
C. None <br>
D. Runtime error since no parameters are passed in the call to f.  <br>

-----

**Q2** : What will the following code print?

```python
def f(x = 0, y = 1):
	return x * y

print(f(1))
```

A. 0 <br>
B. 1 ✅ <br>
C. None <br>
D. Runtime error since no parameters are passed in the call to f.  <br>

-----

**Q3** : Write a function called `str_mult` that takes in a required string parameter and an optional integer parameter. The default value for the integer parameter should be 3. The function should return the string multiplied by the integer parameter.

```python
def str_mult(x, y=3):
    return x * y

print(str_mult("ha"))
print(str_mult("ha", 9))
print(str_mult("hello "))
```

**Output** :

```
hahaha
hahahahahahahahaha
hello hello hello
```

-----

#### 4.7. Keyword Parameters

In the previous section, on Optional Parameters you learned how to define default values for formal parameters, which made it optional to provide values for those parameters when invoking the functions.

In this chapter, you’ll see one more way to invoke functions with optional parameters, with keyword-based parameter passing. This is particularly convenient when there are several optional parameters and you want to provide a value for one of the later parameters while not providing a value for the earlier ones.

The online official python documentation includes a tutorial on optional parameters which covers the topic quite well. Please read the content there: [Keyword arguments](http://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)

Don’t worry about the `def cheeseshop(kind, *arguments, **keywords):` example. You should be able to get by without understanding `*parameters` and `**parameters` in this course. But do make sure you understand the stuff above that.

The basic idea of passing arguments by keyword is very simple. When invoking a function, inside the parentheses there are always 0 or more values, separated by commas. With keyword arguments, some of the values can be of the form `paramname = <expr>` instead of just `<expr>`. Note that when you have `paramname = <expr>` in a function definition, it is defining the default value for a parameter when no value is provided in the invocation; when you have `paramname = <expr>` in the invocation, it is supplying a value, overriding the default for that paramname.

```python
def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"):
	print("-- This parrot wouldn't " + action,)
	print("if you put " + str(voltage) + " volts through it.")
	print("-- Lovely plumage, the " + type)
	print("-- It's " + state + "!")
	print("")

parrot(1000)																					# 1 positional argument
parrot(voltage=1000)																	# 1 keyword argument
parrot(voltage=1000000, action="VOOOOOM")							# 2 keyword arguments
parrot(action="VOOOOOM", voltage=1000000)							# 2 keyword arguments
parrot("a million", "bereft of life", "jump")					# 3 positional arguments
parrot("a thousand", state="pushing up the daisies")	# 1 positional, 1 keyword arguments
```

**Output**:

```
-- This parrot wouldn't voom
if you put 1000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff!

-- This parrot wouldn't voom
if you put 1000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff!

-- This parrot wouldn't VOOOOOM
if you put 1000000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff!

-- This parrot wouldn't VOOOOOM
if you put 1000000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff!

-- This parrot wouldn't jump
if you put a million volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's bereft of life!

-- This parrot wouldn't voom
if you put a thousand volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's pushing up the daisies!
```

**Note** : Note that we have yet another, slightly different use of the = sign here. As a stand-alone, top-level statement, `x=3`, the variable x is set to 3. Inside the parentheses that invoke a function, `x=3` says that 3 should be bound to the local variable x in the stack frame for the function invocation. Inside the parentheses of a function definition, `x=3` says that 3 should be the value for x in every invocation of the function where no value is explicitly provided for x.


#### Keyword Parameters with `.format`
Earlier you learned how to use the `format` method for strings, which allows you to structure strings like fill-in-the-blank sentences. Now that you’ve learned about optional and keyword parameters, we can introduce a new way to use the `format` method.

This other option is to specifically refer to keywords for interpolation values, like below.

```python
names_scores = [("Jack", [67, 89, 91]), ("Emily", [72, 95, 42]), ("Taylor", [83, 92, 86])]
for name, scores in names_scores:
	print("The scores {nm} gor were: {s1}, {s2}, {s3}".format(nm=name, s1=scores[0], s2=scores[1], s3=scores[2]))
```

**Output**:

```
The scores Jack gor were: 67, 89, 91
The scores Emily gor were: 72, 95, 42
The scores Taylor gor were: 83, 92, 86
```

Sometimes, you may want to use the `.format` method to insert the same value into a string multiple times. You can do this by simply passing the same string into the format method, assuming you have included `{}` s in the string everywhere you want to interpolate them. But you can also use positional passing references to do this! The order in which you pass arguments into the `format` method matters: the first one is argument `0`, the second is argument `1`, and so on.

For example,

```python
# this works
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{}!' she yelled. '{}! {}, {}!'".format(n,n,n,"say hello"))

print("")

# but this also works!
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n,"say hello"))
```

**Output**:

```
'Jack!' she yelled. 'Jack! Jack, say hello!'
'Jill!' she yelled. 'Jill! Jill, say hello!'
'Mary!' she yelled. 'Mary! Mary, say hello!'

'Jack!' she yelled. 'Jack! Jack, say hello!'
'Jill!' she yelled. 'Jill! Jill, say hello!'
'Mary!' she yelled. 'Mary! Mary, say hello!'
```

----
----

**Check Your Understanding**

**Q1** : What value will be printed for z?

```python
initial = 7
def f(x, y=3, z=initial):
	print("x, y, z are:", x, y, z)

f(2,5)
```

A. 2 <br>
B. 3 <br>
C. 5 <br>
D. 7 ✅  <br>
E. Runtime error since not enough values are passed in the call to f <br>


-----

**Q2** : What value will be printed for y?

```python
initial = 7
def f(x, y = 3, z = initial):
    print("x, y, z are:", x, y, z)

f(2, z = 10)
```

A. 2 <br>
B. 3 ✅ <br>
C. 5 <br>
D. 10 <br>
E. Runtime error since no value is provided for y, which comes before z <br>

-----

**Q3** : What value will be printed for x?

```python
initial = 7
def f(x, y = 3, z = initial):
    print("x, y, z are:", x, y, z)

f(2, x=5)
```

A. 2 <br>
B. 3 <br>
C. 5 <br>
D. 7 <br>
E. Runtime error since two different values are provided for x ✅  <br>

-----

**Q4** : What value will be printed for z?

```python
initial = 7
def f(x, y = 3, z = initial):
    print "x, y, z are:", x, y, z
initial = 0
f(2)
```

A. 2 <br>
B. 7 ✅  <br>
C. 0 <br>
D. Runtime error since two different values are provided for initial. <br>

-----

**Q5** : What value will be printed below?

```python
names = ["Alexey", "Catalina", "Mitsuki", "Pablo"]
print("'{first}!' she yelled. 'Come here, {first}! {f_one}, {f_two}, and {f_three} are here!'".format(first = names[1], f_one = names[0], f_two = names[2], f_three = names[3]))
```

A. 'first!' she yelled. 'Come here, first! f_one, f_two, and f_three are here!' <br>
B. 'Alexey!' she yelled. 'Come here, Alexey! Catalina, Misuki, and Pablo are here!' <br>
C. 'Catalina!' she yelled. 'Come here, Catalina! Alexey, Misuki, and Pablo are here!' ✅ <br>
D. There is an error. You cannot repeatedly use the keyword parameters. <br>

-----

**Q6** : Define a function called `multiply`. It should have one required parameter, a string. It should also have one optional parameter, an integer, named `mult_int`, with a default value of 10. The function should return the string multiplied by the integer. (i.e.: Given inputs “Hello”, mult_int=3, the function should return “HelloHelloHello”)

```python
def multiply(str, mult_int=10):
    return str * mult_int

print(multiply("hello "))
print(multiply("ha"))
print(multiply("Hello ", 3))
```

**Output** :

```
hello hello hello hello hello hello hello hello hello hello
hahahahahahahahahaha
Hello Hello Hello
```

-----

**Q7** : Currently the function is supposed to take 1 required parameter, and 2 optional parameters, however the code doesn’t work. Fix the code so that it passes the test. This should only require changing one line of code.

```python
# Given
def waste(var = "Water", mar, marble = "type"):
    final_string = var + " " + marble + " " + mar
    return final_string



# Solution
def waste(mar, var = "Water", marble = "type"):
    final_string = var + " " + marble + " " + mar
    return final_string

print(waste("Pokemon"))
```

**Output** :

```
Water type Pokemon
```

-----


#### 4.8. Anonymous Functions with Lambda Expressions

To further drive home the idea that we are passing a function object as a parameter to the sorted object, let’s see an alternative notation for creating a function, a **lambda expression**. The syntax of a lambda expression is the word “lambda” followed by parameter names, separated by commas but not inside (parentheses), followed by a colon and then an expression. `lambda arguments: expression` yields a function object. This unnamed object behaves just like the function object constructed below.


```python
def fname(arguments):
	return expression
```

![](https://fopp.umsi.education/runestone/static/fopp/_images/lambda.gif)

Consider the following code

```python
def f(x):
	return x -1

print(f)
print(type(f))
print(f(3))

print(lambda x: x-2)
print(type(lambda x: x-2))
print((lambda x: x-2)(6))
```

**Output**:

```
<function f at 0x1028b9400>
<class 'function'>
2
<function <lambda> at 0x102878c80>
<class 'function'>
4
```

Note the paralells between the two. At line 4, f is bound to a function object. Its printed representation is “<function f>”. At line 8, the lambda expression produces a function object. Because it is unnamed (anonymous), its printed representation doesn’t include a name for it, “<function <lambda>>”. Both are of type ‘function’.

A function, whether named or anonymous, can be called by placing parentheses () after it. In this case, because there is one parameter, there is one value in parentheses. This works the same way for the named function and the anonymous function produced by the lambda expression. The lambda expression had to go in parentheses just for the purposes of grouping all its contents together. Without the extra parentheses around it on line 10, the interpreter would group things differently and make a function of x that returns x - 2(6).

Some students find it more natural to work with lambda expressions than to refer to a function by name. Others find the syntax of lambda expressions confusing. It’s up to you which version you want to use though you will need to be able to read and understand lambda expressions that are written by others. In all the examples below, both ways of doing it will be illustrated.

Say we want to create a function that takes a string and returns the last character in that string. What might this look like with the functions you’ve used before?


```python
def last_char(s):
	return s[-1]

print(last_char("hello there"))
```

**Output**:

```
e
```

To re-write this using lambda notation, we can do the following:


```python
last_char = lambda s: s[-1]
print(last_char("hello there"))
```

**Output**:

```
e
```

Note that neither function is actually invoked. Look at the parallels between the two structures. The parameters are defined in both functions with the variable s. In the typical function, we have to use the keyword return to send back the value. In a lambda function, that is not necessary - whatever is placed after the colon is what will be returned.


----
----

**Check Your Understanding**

**Q1** : If the input to this lambda function is a number, what is returned?

```python
(lambda x: -x)
```

A. A string with a - in front of the number. <br>
B. A number of the opposite sign (positive number becomes negative, negative becomes positive). ✅ <br>
C. Nothing is returned because there is no return statement.  <br>

-----

#### 4.9. Method Invocations

There is one other special type of function called a **method**, which is invoked slightly differently. Some object types have methods defined for them. You have already seen some methods that operate on strings (e.g., `find`, `index`, `split`, `join`) and on lists (e.g., `append`, `pop`).

We will not learn about how to define methods until later in the course, when we cover Classes. But it’s worth getting a basic understanding now of how methods are invoked. To invoke a method, the syntax is `<expr>.<methodname>(<additional parameter values>)`.

The expression to the left of the dot should evaluate to an object of the correct type, an object for which <methodname> is defined. The method will be applied to that object (that object will be a parameter value passed to the function/method.) If the method takes additional parameters (some do, some don’t), additional expressions that evaluate to values are included inside the parentheses.

For example, let’s look at an invocation of the split method.

```python
y = "This is a sentence"
z = y.split()
print(type(z))
print(len(z))
print(z)
for w in z:
	print(w)
```

**Output**:

```
<class 'list'>
4
['This', 'is', 'a', 'sentence']
This
is
a
sentence
```


The split method operates on a string. Because it is a method rather than a regular function, the string it operates on appears to the left of the period, rather than inside the parentheses. The split method always returns a list. On line 2, that returned value is assigned to the variable z.

The split method actually takes an optional extra parameter. If no value is provided inside the parentheses, the split method chops up the list whenever it encounters a whitespace (a space, a tab, or a newline). But you can specifying a character or character string to split on. Try putting “s” inside the parentheses on line 2 above, make a prediction about what the output will be, and then check it. Try some other things inside the parentheses.

Note that the thing to the left of the period can be any expression, not just a variable name. It can even be a return value from some other function call or method invocation. For example, if we want to remove the s and t characters from a string, we can do it all on one line as show below.

```python
print("This is a sentence".replace("s", "").replace("t", ""))
```

**Output**:

```
Thi i a enence
```

What’s going on there? Start reading left to right. “This is a sentence” is a string, and the replace method is invoked on it. Two additional parameter values are provided, “s”, and an empty string. So, in the sentence, all occurrences of “s” are replaced with the empty string. A new string is returned, “Thi i a entence.” There is another period followed by the word replace, so the replace method is called again on that string, returning the shorter string, which is printed.


----
----

### 4.10. Chapter Assessments & Exercises

#### Assessments

**A1**. Write a function, `sublist`, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).


```python
def sublist(alist):
	n = 0
	sub_alist = []

	while n < len(alist):
		if alist[n] != 5:
			sub_alist.append(alist[n])
			n += 1
		else:
			break
	return sub_alist

print(sublist([1, 2, 3, 4, 5, 6, 7, 8]))
print(sublist([5]))
print(sublist([8, 6, 5]))
print(sublist([1, 6, 2, 3, 9]))
```

**Output** :

```
[1, 2, 3, 4]
[]
[8, 6]
[1, 6, 2, 3, 9]
```

-----

**A2**. Write a function called `check_nums` that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.


```python
print(def check_nums(alist):
    n = 0
    sevenless_list = []

    while n < len(alist):
        if alist[n] != 7:
            sevenless_list.append(alist[n])
            n += 1
        else:
            break
    return sevenless_list)

print(check_nums([0,2,4,9,2,3,6,8,12,14,7,9,10,8,3]))
print(check_nums([9,302,4,62,78,97,10,7,8,23,53,1]))
print(check_nums([7,8,3,2,4,51]))
print(check_nums([1, 6, 2, 3, 9]))
```

**Output** :

```
[0, 2, 4, 9, 2, 3, 6, 8, 12, 14]
[9, 302, 4, 62, 78, 97, 10]
[]
[1, 6, 2, 3, 9]
```

-----


**A3**. Write a function, `sublist`, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).


```python
def sublist(alist):
	n = 0
	stopless = []

	while n < len(alist):
		if alist[n] != "STOP":
			stopless.append(alist[n])
			n += 1
		else:
			break
	return stopless

lst1 = ['bob', 'joe', 'lucy', 'STOP', 'carol', 'james']
lst2 = ['STOP']
lst3 = ['jackie', 'paul', 'STOP']

print(sublist(lst1))
print(sublist(lst2))
print(sublist(lst3))
```

**Output** :

```
['bob', 'joe', 'lucy']
[]
['jackie', 'paul']
```

-----


**A4**. Write a function called `stop_at_z` that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.


```python
def stop_at_z(str):
	n = 0
	z_less = []

	while n < len(str):
		if str[n] != "z":
			z_less.append(str[n])
			n += 1
		else:
			break
	return z_less

print(stop_at_z(['c', 'b', 'd', 'zebra', 'h', 'r', 'z', 'm', 'a', 'k']))
print(stop_at_z(['zoo', 'zika', 'ozzie', 'pizzazz', 'z', 'pizza', 'zap', 'haze']))
print(stop_at_z(['z']))
```

**Output** :

```
['c', 'b', 'd', 'zebra', 'h', 'r']
['zoo', 'zika', 'ozzie', 'pizzazz']
[]
```

-----


**A5**. Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. Once complete, `sum2` should equal sum1.


```python
# Given
sum1 = 0
lst = [65, 78, 21, 33]
for x in lst:
    sum1 = sum1 + x



# Solution
sum1 = 0
lst = [65, 78, 21, 33]
for x in lst:
    sum1 = sum1 + x
print(sum1)

n = 0
sum2 = 0
while n < len(lst):
    sum2 += lst[n]
    n += 1
print(sum2)
```

**Output** :

```
197
197
```

-----

**A6**. Challenge: Write a function called `beginning` that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing


```python
def beginning(alist):
    n = 0
    first = []

    while n < len(alist):
        if alist[n] != "bye":
            first.append(alist[n])
            n += 1
        else:
            break
    return first[:10]

ls1 = ['water', 'phone', 'home', 'chapstick', 'market', 'headphones', 'bye', 'stickie notes', 'snapchat', 'facebook', 'social media']
ls2 = ['bye', 'no', 'yes', 'maybe', 'sorta']
ls3 = ['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup', 'see yah', 'toodel loo', 'night', 'until later', 'peace', 'bye', 'good-bye', 'g night']

print(beginning(ls1))
print(beginning(ls2))
print(beginning(ls3))
```

**Output** :

```
['water', 'phone', 'home', 'chapstick', 'market', 'headphones']
[]
['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup']
```

-----


**A7**. Create a function called `mult` that has two parameters, the first is required and should be an integer, the second is an optional parameter that can either be a number or a string but whose default is 6. The function should return the first parameter multiplied by the second.


```python
def mult(x, y=6):
	return x * y

print(mult(2))
print(mult(3, 5))
print(mult(4, "hello "))
```

**Output** :

```
12
15
hello hello hello hello
```

-----

**A8**. The following function, `greeting`, does not work. Please fix the code so that it runs without error. This only requires one change in the definition of the function.


```python
# Given
def greeting(greeting="Hello ", name, excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))


# Solution
def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))
```

**Output** :

```
Hello Bob!
Hello !
Hello Bob!!!
```

-----

**A9**. Below is a function, `sum`, that does not work. Change the function definition so the code works. The function should still have a required parameter, `intx`, and an optional parameter, `intz` with a defualt value of 5.


```python
# Given
def sum(intz=5, intx):
    return intz + intx


# Solution
def sum(intx, intz=5):
    return intz + intx

print(sum(8,2))
print(sum(12))
```

**Output** :

```
10
17
```

-----

**A10**. Write a function, `test`, that takes in three parameters: a required integer, an optional boolean whose default value is `True`, and an optional dictionary, called `dict1`, whose default value is `{2:3, 4:5, 6:8}`. If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.


```python
def test(x, boo=True, dict1={2:3, 4:5, 6:8}):
	if boo == True:
		if x in dict1.keys():
			return dict1[x]
		else:
			return False
	else:
		return False

print(test(2))
print(test(4, False))
print(test(5, dict1 = {5:4, 2:1}))
```

**Output** :

```
3
False
4
```

-----

**A11**. Write a function called `checkingIfIn` that takes three parameters. The first is a required parameter, which should be a string. The second is an optional parameter called `direction` with a default value of `True`. The third is an optional parameter called `d` that has a default value of `{'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}`. Write the function `checkingIfIn` so that when the second parameter is `True`, it checks to see if the first parameter is a key in the third parameter; if it is, return `True`, otherwise return `False`.

But if the second paramter is `False`, then the function should check to see if the first parameter is not a key of the third. If it’s not, the function should return `True` in this case, and if it is, it should return `False`.


```python
def checkingIfIn(str1, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
	if direction == True:
		if str1 in d.keys():
			return True
		else:
			return False
	else:
		if str1 not in d.keys():
			return True
		else:
			return False


print(checkingIfIn('grapes'))
print(checkingIfIn('carrots'))
print(checkingIfIn('grapes', False))
print(checkingIfIn('carrots', False))
print(checkingIfIn('grapes', d = {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1}))
print(checkingIfIn('peas', d = {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1}))
print(checkingIfIn('peas', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1}))
print(checkingIfIn('apples', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1}))
```

**Output** :

```
True
False
False
True
False
True
False
True
```

-----

**A11**. We have provided the function `checkingIfIn` such that if the first input parameter is in the third, dictionary, input parameter, then the function returns that value, and otherwise, it returns `False`. Follow the instructions in the active code window for specific variable assignmemts.


```python
def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn("beetroot")
print(c_false)
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn("beetroot", False)
print(c_true)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = checkingIfIn("fruit")
print(fruit_ans)
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn("apple", d = {'apple': 8, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7})
print(param_check)
```

**Output** :

```
False
True
19
8
```

-----

----
----

#### Exercises


**Q1**. Using a while loop, create a list `numbers` that contains the numbers 0 through 35. Your while loop should initialize a counter variable to 0. On each iteration, the loop should append the current value of the counter to the list and the counter should increase by 1. The while loop should stop when the counter is greater than 35.


```python
counter = 0
numbers = []

while counter < 36:
	numbers.append(counter)
	counter += 1

print(counter)
print(numbers)
```

**Output** :

```
36
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
```

-----

**Q2**. Using a while loop, create a list called `L` that contains the numbers 0 to 10. (i.e.: Your while loop should initialize a counter variable to 0. On each iteration, the loop should append the current value of the counter variable to L and then increase the counter by 1. The while loop should stop once the counter variable is greater than 10.)


```python
counter = 0
L = []

while counter < 11:
	L.append(counter)
	counter += 1

print(L)
```

**Output** :

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

-----

**Q3**. Using a while loop, create a list called `nums` that contains the numbers 0 though 20. (i.e: your while looop should initialize a counter variable on 0. During each iteration, the loop should append the current value of the counter variable to `nums` and then increase the counter by 1. The while loop should stop once the counter variable is greater than 20)


```python
counter = 0
nums = []

while counter < 21:
	nums.append(counter)
	counter += 1

print(nums)
```

**Output** :

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
```

-----

**Q4**. Modify the walking turtle program so that rather than a 90 degree left or right turn the angle of the turn is determined randomly at each step.


```python
import random
import turtle

sc = turtle.Screen()
steve = turtle.Turtle()
steve.speed(1)

step = 0

while step < 11:
    step += 1
    coin = random.randrange(0,2)
    angle = random.randrange(0, 360)
    if coin == 1:
        steve.left(angle)
        steve.forward(50)
    elif coin == 2:
        steve.right(angle)
        steve.forward(50)
    else:
        pass

sc.exitonclick()
```

**Output** :

![](https://media.giphy.com/media/ZbI8VYnpVwZjBoGGMZ/giphy.gif)


-----

**Q5**. Modify the turtle walk program so that you have two turtles each with a random starting location. Keep the turtles moving until one of them leaves the screen.


```python
import random
import turtle

def moveRandom(wn, t):
    coin = random.randrange(0,2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)

def areColliding(t1, t2):
    if t1.distance(t2) < 2:
        return True
    else:
        return False

def isInScreen(w, t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False
    return stillIn

t1 = turtle.Turtle()
t2 = turtle.Turtle()
wn = turtle.Screen()

t1.shape('turtle')
t2.shape('circle')

leftBound = -wn.window_width() / 2
rightBound = wn.window_width() / 2
topBound = wn.window_height() / 2
bottomBound = -wn.window_height() / 2

t1.up()
t1.goto(random.randrange(leftBound, rightBound),
        random.randrange(bottomBound, topBound))
t1.setheading(random.randrange(0, 360))
t1.down()

t2.up()
t2.goto(random.randrange(leftBound, rightBound),
        random.randrange(bottomBound, topBound))
t2.setheading(random.randrange(0, 360))
t2.down()


while isInScreen(wn, t1) and isInScreen(wn, t2):
    moveRandom(wn, t1)
    moveRandom(wn, t2)

wn.exitonclick()
```

**Output** :

![](https://media.giphy.com/media/JNlLx1aOvGHift2FFQ/giphy.gif)


-----

**Q6**. Create a while loop that initializes a counter at 0 and will run until the counter reaches 50. If the value of the counter is divisible by 10, append the value to the list, `tens`.


```python
counter = 0
tens = []

while counter < 51:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print(counter)
print(tens)
```

**Output** :

```
51
[0, 10, 20, 30, 40, 50]
```

-----

**Q7**. Use a while loop to iterate through the numbers 0 through 35. If a number is divisible by 3, it should be appended to a list called `three_nums`.


```python
counter = 0
three_nums = []

while counter < 36:
    if counter % 3 == 0:
        three_nums.append(counter)
    counter += 1

print(three_nums)
```

**Output** :

```
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33]
```

-----


**Q8**. Fill in the parameter list for g so that the invocations of g yield the return values specified.


```python
# Given
def g():
	return 2 * x + y + z

print(g(3))       # should output 10
print(g(3, 2))    # should output 8
print(g(3, 2, 1)) #should output 9



# Solution
def g(x, y=4, z=0):
	return 2 * x + y + z

print(g(3))
print(g(3, 2))    
print(g(3, 2, 1))
```

**Output** :

```
10
8
9
```

-----


**Q9**. Define a function called `nums` that has three parameters. The first parameter, an integer, should be required. A second parameter named `mult_int` should be optional with a default value of 5. The final parameter, `switch`, should also be optional with a default value of False. The function should multiply the two integers together, and if switch is True, should change the sign of the product before returning it.


```python
# Given
def nums():
    pass #remove this once you start writing the function


# Solution
def nums(x, mult_int = 5, switch = False):
	if switch == True:
		return -(x * mult_int)
	else:
		return x * mult_int

print(nums(5))
print(nums(2, mult_int=4))
print(nums(3, switch=True))
print(nums(4, mult_int=3, switch=True))
print(nums(0, switch=True))
```

**Output** :

```
25
8
-15
-12
0
```

-----

**Q10**. Write a function called `together` that takes three parameters, the first is a required parameter that is a number (integer or float), the second is a required parameter that is a string, and the third is an optional parameter whose default is ” “. What is returned is the first parameter, concatenated with the second, using the third.


```python
def together(num, st, space= " "):
	return str(num) + space + st

print(together(12, 'cats'))
print(together(17.3, 'birthday cakes'))
print(together(3, 'dogs', ': '))
print(together(493.3, 'beans', 'lima'))
```

**Output** :

```
12 cats
17.3 birthday cakes
3: dogs
493.3limabeans
```

-----

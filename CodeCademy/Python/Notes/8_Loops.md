# 8. Loops


### 8.1. While you're here
The `while` loop is similar to an `if` statement: it executes the code inside of it if some condition is true. The difference is that the `while` loop will continue to execute as long as the condition is true. In other words, instead of executing if something is true, it executes while that thing is true.

Line 6 decides when the loop will be executed. So, "as long as `count` is less than `5`," the loop will continue to execute. Line 8 increases `count` by 1. This happens over and over until `count` equals `5`.


##### Instructions

Change the loop so that it counts from `0` up to `9` (inclusive).

Be careful not to alter or remove the count `+= 1` statement. If your program has no way to increase `count`, your loop could go on forever and become an infinite loop which could crash your computer/browser!


```Python
# GIVEN
count = 0

if count < 5:
  print("Hello, I am an if statement and count is", count)

while count < 5:
  print("Hello, I am a while and count is", count)
  count += 1



# SOLUTION
count = 0

if count < 5:
  print("Hello, I am an if statement and count is", count)

while count < 10:
  print("Hello, I am a while and count is", count)
  count += 1


# OUTPUT
Hello, I am an if statement and count is 0
Hello, I am a while and count is 0
Hello, I am a while and count is 1
Hello, I am a while and count is 2
Hello, I am a while and count is 3
Hello, I am a while and count is 4
Hello, I am a while and count is 5
Hello, I am a while and count is 6
Hello, I am a while and count is 7
Hello, I am a while and count is 8
Hello, I am a while and count is 9
```

### 8.2. Condition
The *condition* is the expression that decides whether the loop is going to continue being executed or not. There are 5 steps to this program:

1. The `loop_condition` variable is set to `True`
2. The `while` loop checks to see if `loop_condition` is `True`. It is, so the loop is entered.
3. The `print` statement is executed.
4. The variable `loop_condition` is set to `False`.
5. The `while` loop again checks to see if `loop_condition` is `True`. It is not, so the loop is not executed a second time.


##### Instructions
See how the loop checks its condition, and when it stops executing? When you think you've got the hang of it, click Run to continue.


```Python
# GIVEN
loop_condition = True

while loop_condition:
  print("I am a loop")
  loop_condition = False


# OUTPUT
I am a loop
```

### 8.3. While you're at it
Inside a `while` loop, you can do anything you could do elsewhere, including arithmetic operations.


##### Instructions

Create a `while` loop that prints out all the numbers from 1 to 10 squared (1, 4, 9, 16, ... , 100), each on their own line.

* Fill in the blank space so that our `while` loop goes from `1` to `10` inclusive.
* Inside the loop, print the value of `num` squared. The syntax for squaring a number is `num ** 2`.
* Increment `num`.


```Python
# GIVEN
num = 1

while _______:



# SOLUTION
num = 1

while num < 11:
  print(num ** 2)
  num += 1



# OUTPUT
1
4
9
16
25
36
49
64
81
100
```

### 8.4. Simple errors

A common application of a `while` loop is to check user input to see if it is valid. For example, if you ask the user to enter `y` or `n` and they instead enter `7`, then you should re-prompt them for input.



##### Instructions

Fill in the loop condition so the user will be prompted for a choice over and over `while` choice does not equal `'y'` and choice does not equal `'n'`.


```Python
# GIVEN
choice = input('Enjoying the course? (y/n) ')

while _____ :  
  choice = input("Sorry, I didn't catch that. Enter again: ")



# SOLUTION
choice = input('Enjoying the course? (y/n) ')

while choice != "y" and choice != "n" :  
  choice = input("Sorry, I didn't catch that. Enter again: ")



# OUTPUT
Enjoying the course? (y/n) d
Sorry, I didn't catch that. Enter again: f
Sorry, I didn't catch that. Enter again: e
Sorry, I didn't catch that. Enter again: s
Sorry, I didn't catch that. Enter again: y
```

### 8.5. Infinite loops

An `infinite loop` is a loop that never exits. This can happen for a few reasons:

1. The loop condition cannot possibly be false (e.g. `while 1 != 2`)
2. The logic of the loop prevents the loop condition from becoming false.

Example:

```Python
count = 10
while count > 0:
  count += 1
```


##### Instructions
The loop in the editor has two problems: it's missing a colon (a syntax error) and `count` is never incremented (logical error). The latter will result in an infinite loop, so be sure to fix both before running!


```Python
# GIVEN
count = 0

while count < 10
  print(count)



# SOLUTION
count = 0

while count < 10:
  print(count)
  count += 1



# OUTPUT
0
1
2
3
4
5
6
7
8
9
```

### 8.6. Break
The `break` is a one-line statement that means "exit the current loop." An alternate way to make our counting loop exit and stop executing is with the `break` statement.

* First, create a while `with` a condition that is always true. The simplest way is shown.
* Using an `if` statement, you define the *stopping condition*. Inside the `if`, you write `break`, meaning "exit the loop."

The difference here is that this loop is guaranteed to run at least once.


##### Instructions
See what the `break` does? Feel free to mess around with it (but make sure you don't cause an infinite loop)! Click Run when you're ready to continue.


```Python
# GIVEN
count = 0

while True:
  print(count)
  count += 1
  if count >= 10:
    break



# SOLUTION
count = 0

while True:
  print(count)
  count += 1
  if count == 4:
    break



# OUTPUT
0
1
2
3
```

### 8.7. While / else

Something completely different about Python is the `while`/`else` construction. `while`/`else` is similar to `if`/`else`, but there is a difference: the `else` block will execute anytime the loop condition is evaluated to `False`. This means that it will execute if the loop is never entered or if the loop exits normally. If the loop exits as the result of a `break`, the `else` will not be executed.

In this example, the loop will `break` if a 5 is generated, and the `else` will not execute. Otherwise, after 3 numbers are generated, the loop condition will become false and the else will execute.



##### Instructions
Click Run to see while/else in action!


```Python
# GIVEN
import random

print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!")

count = 0
while count < 3:
  num = random.randint(1, 6)
  print(num)
  if num == 5:
    print("Sorry, you lose!")
    break
  count += 1
else:
  print("You win!")



# OUTPUT 1
Lucky Numbers! 3 numbers will be generated.
If one of them is a '5', you lose!
3
6
2
You win!



# OUTPUT 2
Lucky Numbers! 3 numbers will be generated.
If one of them is a '5', you lose!
5
Sorry, you lose!
```

### 8.8. Your own while / else
Now you should be able to make a game similar to the one in the last exercise. The code from the last exercise is below:

```Python
count = 0
while count < 3:
  num = random.randint(1, 6)
  print(num)
  if num == 5:
    print("Sorry, you lose!")
    break
  count += 1
else:
  print("You win!")
```

In this exercise, allow the user to guess what the number is `3` times.

```Python
guess = int(input("Your guess: "))
```

Remember, `input` turns user input into a string, so we use `int()` to make it a number again.


##### Instructions
Use a `while` loop to let the user keep guessing so long as `guesses_left` is greater than zero.

Ask the user for their `guess`, just like the second example above.

If they guess correctly, `print("You win!")` and `break`.

Decrement `guesses_left` by one.

Use an `else:` case after your `while` loop to print `"You lose."`.


```Python
# GIVEN
from random import randint
random_number = randint(1, 10)

guesses_left = 3



# SOLUTION
from random import randint
random_number = randint(1, 10)

guesses_left = 3

while guesses_left > 0 :
  guess = int(input("Make a guess! "))
  if guess == random_number:
    print("You win!")
    break
  guesses_left -= 1
else:
  print("You lose.")


# OUTPUT 1
Make a guess! 2
Make a guess! 3
Make a guess! 4
You lose.


# OUTPUT 2
Make a guess! 1
You win!
```

### 8.9. For your health
An alternative way to loop is the `for` loop. The syntax is as shown in the code editor. This example means "for each number `i` in the range 0 - 9, print `i`".


##### Instructions

Make the loop print the numbers from 0 to 19 instead of 0 to 9.

```Python
# GIVEN
print("Counting...")

for i in range(10):
  print(i)



# SOLUTION
print("Counting...")

for i in range(20):
  print(i)



# OUTPUT
Counting...
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
```

### 8.10. For your hobbies
This kind of loop is useful when you want to do something a certain number of times, such as append something to the end of a list.


##### Instructions
Create a `for` loop that prompts the user for a hobby 3 times.

Save the result of each prompt in a `hobby` variable

`append` each one to `hobbies`.

print `hobbies` after your `for` loop

Make sure to answer the prompts in the terminal when testing your code!


```Python
# GIVEN
hobbies = []


# SOLUTION
hobbies = []

for i in range(3):
    hobby = input("Enter one of your hobbies: ")
    hobbies.append(hobby)
print(hobbies)



# OUTPUT
Enter one of your hobbies: read
Enter one of your hobbies: think
Enter one of your hobbies: sleep
['read', 'think', 'sleep']
```

### 8.11. For your strings

Using a `for` loop, you can print out each individual character in a string.

The example in the editor is almost plain English: "for each character `c` in `thing`, print `c`".


##### Instructions

Add a second `for` loop so that each character in `word` is printed one at a time.


```Python
# GIVEN
thing = "spam!"

for c in thing:
  print(c)

word = "eggs!"



# SOLUTION
thing = "spam!"
for c in thing:
  print(c)

word = "eggs!"
for letter in word:
  print(letter)



# OUTPUT
s
p
a
m
!
```

### 8.12. For your A
String manipulation is useful in `for` loops if you want to modify some content in a string.

```Python
# Python 2
word = "Marble"
for char in word:
  print char,


# Python 3
word = "Marble"
for char in word:
  print(char, end =" ")


# OUTPUT
M a r b l e
```
The example above iterates through each character in `word` and, in the end, prints out `M a r b l e`.

The `,` character after our `print` statement means that our next `print` statement keeps printing on the same line.

##### Instructions
Let's filter out the letter `"A"` from our string.

* Do the following `for` each character in the `phrase`.
* If `char` is an `"A"` or `char` is an `"a"`, `print "X"`, instead of `char`. Make sure to include the trailing comma.
* Otherwise (`else:`), please `print char`, with the trailing comma.


```Python
# GIVEN
phrase = "A bird in the hand..."

print



# SOLUTION
phrase = "A bird in the hand..."

for char in phrase:
  if char == "A" or char == "a":
    print("X", end=" ")
  else:
    print(char, end=" ")


# OUTPUT
X   b i r d   i n   t h e   h X n d . . .
```

### 8.13. For your lists
Perhaps the most useful (and most common) use of `for` loops is to go through a list.

On each iteration, the variable `num` will be the next value in the list. So, the first time through, it will be `7`, the second time it will be `9`, then `12`, `54`, `99`, and then the loop will exit when there are no more values in the list.


##### Instructions

Write a second `for` loop that goes through the `numbers` list and prints each element squared, each on its own line.

```Python
# GIVEN
numbers  = [7, 9, 12, 54, 99]

print("This list contains: ")

for num in numbers:
  print(num)


# SOLUTION by add
for num in numbers:
  print(num**2)


# OUTPUT
This list contains:
7
9
12
54
99
49
81
144
2916
9801
```

### 8.14. Looping over a dictionary
You may be wondering how looping over a dictionary would work. Would you get the key or the value?

The short answer is: you get the key which you can use to get the value.

```Python
d = {'x': 9, 'y': 10, 'z': 20}
for key in d:
  if d[key] == 10:
    print("This dictionary has the value 10!")


# OUTPUT
This dictionary has the value 10!
```
1. First, we create a dictionary with strings as the keys and numbers as the values.
2. Then, we iterate through the dictionary, each time storing the key in `key`.
3. Next, we check if that key's value is equal to 10.
4. If so, we print `"This dictionary has the value 10!"`

##### Instructions

On line 5, print the key, followed by a space, followed by the value associated with that key.

```Python
# GIVEN
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:



# SOLUTION
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  print(key, d[key])



# OUTPUT
a apple
b berry
c cherry
```

### 8.15. Counting as you go
A weakness of using this for-each style of iteration is that you don't know the index of the thing you're looking at. Generally this isn't an issue, but at times it is useful to know how far into the list you are. Thankfully the built-in `enumerate` function helps with this.

`enumerate` works by supplying a corresponding index to each element in the list that you pass it. Each time you go through the loop, index will be one greater, and item will be the next item in the sequence. It's very similar to using a normal for loop with a list, except this gives us an easy way to count how many items we've seen so far.


##### Instructions
We don't want the user to see things listed from index 0, since this looks unnatural. Instead, the items should appear to start at index 1. Modify the print statement to reflect this behavior. See the Hint for help.


```Python
# GIVEN
choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')
for index, item in enumerate(choices):
  print(index, item)


# SOLUTION
choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')
for index, item in enumerate(choices):
  print(index + 1, item)



# OUTPUT
Your choices are:
1 pizza
2 pasta
3 salad
4 nachos
```

### 8.16. Multiple lists
It's also common to need to iterate over two lists at once. This is where the built-in zip function comes in handy.

`zip` will create pairs of elements when passed two lists, and will stop at the end of the shorter list.

`zip` can handle three or more lists as well!


##### Instructions
Compare each pair of elements and print the larger of the two.


```Python
# GIVEN
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):



# SOLUTION
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  if a > b:
    print(a)
  else:
    print(b)



# OUTPUT
3
9
17
15
30
```

### 8.17. For / else
Just like with `while`, `for` loops may have an `else` associated with them.

In this case, the `else` statement is executed after the `for`, but only if the `for` ends normally—that is, not with a `break`. This code will `break` when it hits `'tomato'`, so the `else` block won't be executed.


##### Instructions
Click Run to see how `for` and `else` work together.


```Python
# GIVEN
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
  if f == 'tomato':
    print('A tomato is not a fruit!') # (It actually is.)
    break
  print('A', f)
else:
  print('A fine selection of fruits!')




# OUTPUT
You have...
A banana
A apple
A orange
A tomato is not a fruit!
```

### 8.18. Change it up
As mentioned, the `else` block won't run in this case, since `break` executes when it hits `'tomato'`.


##### Instructions
Modify the code in the editor such that the `for` loop's else statement is executed.


```Python
# GIVEN
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
  if f == 'tomato':
    print('A tomato is not a fruit!') # (It actually is.)
    break
  print('A', f)
else:
  print('A fine selection of fruits!')



# SOLUTION
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
  if f == 'tomato':
    print('A tomato is not a fruit!') # (It actually is.)
    continue
  print('A', f)
else:
  print('A fine selection of fruits!')



# OUTPUT
You have...
A banana
A apple
A orange
A tomato is not a fruit!
A pear
A grape
A fine selection of fruits!
```

### 8.19. Create your own

To wrap up this lesson, let's create our own `for`/`else` statement from scratch.



##### Instructions
Build your `for`/`else` statement in the editor. Execution of the else branch is optional, but your code should print a string of your choice to the editor regardless.


```Python
# SOLUTION
breakfast_order = ["coffee", "tea", "beer", "chocolate", "cheese", "pancake", "egg"]

for i in breakfast_order:
  if i == "beer":
    print("A", i, end=" ")
    print("Not a good choice for breakfast! I won't give you it.")
    continue
  else:
    print("A", i)
else :
  print("Good choice! It'll be perfect Sunday breakfast!")



# OUTPUT
A coffee
A tea
A beer Not a good choice for breakfast! I won't give you it.
A chocolate
A cheese
A pancake
A egg
Good choice! It'll be perfect Sunday breakfast!
```

# Battleship

### 1. Welcome to Battleship!
In this project you will build a simplified, one-player version of the classic board game Battleship! In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid. The player will have 10 guesses to try to sink the ship.

To build this game we will use our knowledge of lists, conditionals and functions in Python. When you're ready to get started, click Next to continue.

##### Instructions
Click Next to get started with Battleship!


### 2. Getting Our Feet Wet
The first thing we need to do is to set up the game board.

##### Instructions

Create a variable `board` and set it equal to an empty list.

```Python
# SOLUTION
board = list()
```


### 3. Make a List
Good! Now we'll use a built-in Python function to generate our board, which we'll make into a 5 x 5 grid of all `"0"`s, for "ocean".

```Python
print(["0"]*5)
```
will print out `["O", "O", "O", "O", "O"]`, which is the basis for a wor of our board.

We'll do this five times to make fice rows. (Since we have to do this five times, it sounds like a loop might be in order.)

##### Instructions
Create a 5 x 5 grid initialized to all 'O's and store it in `board`.

* Use `range()` to loop `5` times.
* Inside the loop, `.append()` a list containing 5 `"O"`s to `board`, just like in the example above.

Note that these are capital etter "O" and not zeros.


```Python
# GIVEN
board = list()


# SOLUTION
board = list()

for x in range(5):
  board.append(["O"] * 5)
```

### 4. Check it Twice
Great job! Now that we've built our board, let's show it off.

Throughout our game, we'll want to print the game board so that the player can see which locations they have already guessed. Regularly printing the board will also help us debug our program.

The easiest way to `print` the board would be to have Python display it for us using the print command. Let's give that a try and see what the results look like—is this a useful way to print our board for Battleship?

##### Instructions

Use the `print` command to display the contents of the `board` list.

```Python
# GIVEN
board = list()

for x in range(5):
  board.append(["O"] * 5)
print(board)

# OUTPUT
# [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
```

### 5. Custom Print
Now we can see the contents of our list, but clearly it would be easier to play the game if we could print the board out like a grid with each row on its own line.

We can use the fact that our board is a list of lists to help us do this. Let's set up a `for` loop to go through each of the elements in the outer list (each of which is a row of our board) and print them.

##### Instructions
First, delete your existing `print` statement.

Then, define a function named `print_board` with a single argument, `board_in`.

Inside the function, write a `for` loop to iterates through each `row` in `board` and `print` it to the screen.

Call your function with `board` to make sure it works.


```Python
# GIVEN
board = list()

for x in range(5):
  board.append(["O"] * 5)



# SOLUTION by add
board = list()

for x in range(5):
  board.append(["O"] * 5)

def print_board(board_in):
  for row in board_in:
    print(row)

print(print_board(board))



# OUTPUT
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
None
```


### 6. Printing Pretty
We're getting pretty close to a playable board, but wouldn't it be nice to get rid of those quote marks and commas? We're storing our data as a list, but the player doesn't need to know that!

```Python
letters = ['a', 'b', 'c', 'd']
print(" ".join(letters))
print("---".join(letters))
```

1. In the example above, we create a list called `letters`.
2. Then, we print `a b c d`. The `.join` method uses the string to combine the items in the list.
3. Finally, we print `a---b---c---d`. We are calling the `.join` function on the `"---"` string.

We want to turn each row into `"O O O O O"`.

##### Instructions

Inside your function, inside your `for` loop, use `" "` as the separator to `.join` the elements of each `row`.

```Python
# GIVEN
board = list()

for x in range(5):
  board.append(["O"] * 5)

def print_board(board_in):
  for row in board_in:
    print(row)

print(print_board(board))



# SOLUTION
board = list()

for x in range(5):
  board.append(["O"] * 5)

def print_board(board_in):
  for row in board_in:
    print(" ".join(row))

print(print_board(board))



# OUTPUT
O O O O O
O O O O O
O O O O O
O O O O O
O O O O O
None
```


### 7. Hide...
Excellent! Now, let's hide our battleship in a random location on the board.

Since we have a 2-dimensional list, we'll use two variables to store the ship's location, `ship_row` and `ship_col`.


```python
from random import randint
coin = randint(0, 1)
dice = randint(1, 6)
```
1. In the above example, we first import the `randint(low, high)` function from the `random` module.
2. Then, we generate either zero or one and store it in `coin`.
3. Finally, we generate a number from one to six inclusive.

Let's generate a `random_row` and `random_col` from zero to four!


##### Instructions
Define two new functions, `random_row` and `random_col`, that each take `board_in` as input.

These functions should `return` a random row index and a random column index from your board, respectively. Use `randint(0, len(board_in) - 1)`.

Call each function on `board`.


```Python
# GIVEN
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)



# SOLUTION by add
def random_row(board_in):
  return randint(0, len(board_in) - 1)

def random_col(board_in):
  return randint(0, len(board_in) - 1)

```


### 8. ...and Seek!
Good job! For now, let's store coordinates for the ship in the variables `ship_row` and `ship_col`. Now you have a hidden battleship in your ocean! Let's write the code to allow the player to guess where it is.

```python
number = input("Enter a number: ")
if int(number) == 0:
  print("You entered 0")
```

`input` asks the user for input and returns it as a string. But we're going to want to use integers for our guesses! To do this, we'll wrap the `input`s with `int()` to convert the string to an integer.

##### Instructions
Create a new variable called `guess_row` and set it to `int(input("Guess Row: "))`.

Create a new variable called `guess_col` and set it to `int(input("Guess Col: "))`.

Click Run and then answer the prompts by typing in a number and pressing Enter (or Return on some computers).




```Python
# GIVEN
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)



# SOLUTION by add
guess_row = int(input("Guess Row:"))
guess_col = int(input("Guess Col:"))
```


### 9. It's Not Cheating—It's Debugging!
Awesome! Now we have a hidden battleship and a guess from our player. In the next few steps, we'll check the user's guess to see if they are correct.

While we're writing and debugging this part of the program, it will be helpful to know where that battleship is hidden. Let's add a `print` statement that displays the location of the hidden ship.

Of course, we'll remove this output when we're finished debugging since if we left it in, our game wouldn't be very challenging. :)


##### Instructions

Before the lines prompting the user for input:

Print the value of `ship_row`.

Print the value of `ship_col`.


```Python
# GIVEN
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

guess_row = int(input("Guess Row:"))
guess_col = int(input("Guess Col:"))




# SOLUTION
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)

guess_row = int(input("Guess Row:"))
guess_col = int(input("Guess Col:"))



# OUTPUT
4
0
Guess Row:
Guess Col:
```

### 10. You win!
Okay—now for the fun! We have the actual location of the ship and the player's guess so we can check to see if the player guessed right.

For a guess to be right, `guess_col` should be equal to `ship_col` and `guess_row` should be equal to `ship_row`.

```python
if guess_col == 0 and guess_row == 0:
  print("Top-left corner.")
```
The example above, is just a reminder about `if` statements.

##### Instructions
On line 29, add an `if` to check if `guess_row` equals `ship_row` and `guess_col` equals `ship_col`.

If that is the case, please `print` out `"Congratulations! You sank my battleship!"`

When you run this code, be sure to enter integer guesses in the panel where it asks for "Guess Row" and then "Guess Col".


```Python
# GIVEN
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))



# SOLUTION by add
if guess_row == ship_row and guess_col == ship_col:
  print("Congratulations! You sank my battleship!")



# OUTPUT
O O O O O
O O O O O
O O O O O
O O O O O
O O O O O
3
2
Guess Row: 3
Guess Col: 2
Congratulations! You sank my battleship!
```


### 11. Danger, Will Robinson!!
Great! Of course, the player isn't going to guess right all the time, so we also need to handle the case where the guess is wrong.

```python
print(board[2][3])
```
The example above prints out `"O"`, the element in the 3rd row and 4th column.

##### Instructions
Add an `else` under the `if` we wrote in the previous step.

Print out `"You missed my battleship!"`

Set the list element at `guess_row`, `guess_col` to `"X"`.

As the last line in your `else` statement, call `print_board(board)` again so you can see the `"X"`.Make sure to enter a col and row that is on the board!


```Python
# GIVEN
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)

guess_row = int(input("Guess Row:"))
guess_col = int(input("Guess Col:"))

if guess_row == ship_row and guess_col == ship_col:
  print("Congratulations! You sank my battleship!")



# SOLUTION by add
if guess_row == ship_row and guess_col == ship_col:
  print("Congratulations! You sank my battleship!")
else :
  print("You missed my battleship!")
  board[guess_row][guess_col] = "X"
  print(print_board(board))



# OUTPUT
O O O O O
O O O O O
O O O O O
O O O O O
O O O O O
1
2
Guess Row:2
Guess Col:4
You missed my battleship!
O O O O O
O O O O O
O O O O X
O O O O O
O O O O O
```


### 12. Bad Aim
Great job! Now we can handle both correct and incorrect guesses from the user. But now let’s think a little bit more about the "miss" condition.

1. They can enter a guess that's off the board.
2. They can guess a spot they’ve already guessed.
3. They can just miss the ship.

We'll add these tests inside our else condition. Let's build the first case now!


```python
if x not in range(8) or \
   y not in range(3):
  print("Outside the range")
```
The example above checks if either `x` or `y` are outside those ranges. The `\` character just continues the if statement onto the next line.

##### Instructions

Add a new `if` statement that is nested under the `else`.

Like the example above, it should check if `guess_row` is not in `range(5)` or `guess_col` is not in `range(5)`.

If that is the case, print out `"Oops, that's not even in the ocean."`

After your new `if` statement, add an `else` that contains your existing handler for an incorrect guess. Don't forget to indent the code!


```Python
# GIVEN
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)

guess_row = int(input("Guess Row:"))
guess_col = int(input("Guess Col:"))

if guess_row == ship_row and guess_col == ship_col:
  print("Congratulations! You sank my battleship!")


if guess_row == ship_row and guess_col == ship_col:
  print("Congratulations! You sank my battleship!")
else :
  print("You missed my battleship!")
  board[guess_row][guess_col] = "X"
  print(print_board(board))



# SOLUTION by add
if guess_row == ship_row and guess_col == ship_col:
  print("Congratulations! You sank my battleship!")
else :
  if guess_row not in range(5) or guess_col not in range(5):
    print("Oops, that's not even in the ocean.")
  else:
  	print("You missed my battleship!")
  	board[guess_row][guess_col] = "X"
  	print(print_board(board))



# OUTPUT
O O O O O
O O O O O
O O O O O
O O O O O
O O O O O
4
3
Guess Row: 6
Guess Col: 6
Oops, that's not even in the ocean.
```

### 13. Not Again!
Great! Now let's handle the second type of incorrect guess: the player guesses a location that was already guessed. How will we know that a location was previously guessed?

```python
print(board[guess_row][guess_col])
```

The example above will print an `"X"` if already guessed or an `"O"`


##### Instructions
Add an `elif` to see if the guessed location already has an 'X' in it.

If it has, `print("You guessed that one already.")`


```Python
# GIVEN
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
  print("Congratulations! You sank my battleship!")
else :
  if guess_row not in range(5) or guess_col not in range(5):
    print("Oops, that's not even in the ocean.")
  else:
  	print("You missed my battleship!")
  	board[guess_row][guess_col] = "X"
  	print(print_board(board))



# SOLUTION by add
if guess_row == ship_row and guess_col == ship_col:
  print("Congratulations! You sank my battleship!")
else :
  if guess_row not in range(5) or guess_col not in range(5):
    print("Oops, that's not even in the ocean.")
  elif board[guess_row][guess_col] == "X":
    print("You guessed that one already.")
  else:
  	print("You missed my battleship!")
  	board[guess_row][guess_col] = "X"
  	print(print_board(board))

# OUTPUT

```
### 14. Test Run
Congratulations! Now you should have a game of Battleship! that is fully functional for one guess.

Make sure you play it a couple of times and try different kinds of incorrect guesses. This is a great time to stop and do some serious debugging.

In the next step, we'll move on and look at how to give the user 4 guesses to find the battleship.

##### Instructions
Thoroughly test your game. Make sure you try a variety of different guesses and look for any errors in the syntax or logic of your program.



### 15. Play It, Sam
You can successfully make one guess in Battleship! But we’d like our game to allow the player to make up to 4 guesses before they lose.

```python
for turn in range(4):
  # Make a guess
  # Test that guess
```
We can use a `for` loop to iterate through a range. Each iteration will be a turn.

##### Instructions
Add a `for` loop that repeats the guessing and checking part of your game for 4 turns, like the example above.

At the beginning of each iteration, `print("Turn", turn + 1)` to let the player know what `turn` they are on.

Indent everything that should be repeated.

```Python
# GIVEN
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

if guess_row == ship_row and guess_col == ship_col:
  print("Congratulations! You sank my battleship!")
else :
  if guess_row not in range(5) or guess_col not in range(5):
    print("Oops, that's not even in the ocean.")
  elif board[guess_row][guess_col] == "X":
    print("You guessed that one already.")
  else:
  	print("You missed my battleship!")
  	board[guess_row][guess_col] = "X"
  	print(print_board(board))



# SOLUTION by add
for turn in range(4):
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sunk my battleship!")
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print("Oops, that's not even in the ocean.")
    elif(board[guess_row][guess_col] == "X"):
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      print("Turn", turn + 1)
    print_board(board)



# OUTPUT
O O O O O
O O O O O
O O O O O
O O O O O
O O O O O
3
3
Guess Row: 2
Guess Col: 3
You missed my battleship!
Turn 1
O O O O O
O O O O O
O O O X O
O O O O O
O O O O O
Guess Row: 4
Guess Col: 5
Oops, that's not even in the ocean.
O O O O O
O O O O O
O O O X O
O O O O O
O O O O O
Guess Row: 2
Guess Col: 3
You guessed that one already.
O O O O O
O O O O O
O O O X O
O O O O O
O O O O O
Guess Row: 2
Guess Col: 3
You guessed that one already.
O O O O O
O O O O O
O O O X O
O O O O O
O O O O O
```

### 16. Game Over
If someone runs out of guesses without winning right now, the game just exits. It would be nice to let them know why.

Since we only want this message to display if the user guesses wrong on their last turn, we need to think carefully about where to put it.

1. We’ll want to put it under the `else` that accounts for misses
2. We’ll want to print the message no matter what the cause of the miss
3. Since our `turn` variable starts at 0 and goes to 3, we will want to end the game when `turn` equals `3`.

##### Instructions
Add an `if` statement that checks to see if the user is out of guesses.

* Put it under the `else` that accounts for misses.
* Put it after the `if/elif/else` statements that check for the reason the player missed. We want `"Game Over"` to print regardless of the reason.

If turn equals 3, `print("Game Over")`.


```Python
# GIVEN
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

for turn in range(4):
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sunk my battleship!")
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print("Oops, that's not even in the ocean.")
    elif(board[guess_row][guess_col] == "X"):
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      print("Turn", turn + 1)
    print_board(board)



# SOLUTION by add
for turn in range(4):
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sunk my battleship!")
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print("Oops, that's not even in the ocean.")
      print("Game Over")
    elif(board[guess_row][guess_col] == "X"):
      print("You guessed that one already.")
      print("Game Over")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      print("Turn", turn + 1)
      if turn == 3:
          print("Game Over")
    print_board(board)



# OUTPUT
O O O O O
O O O O O
O O O O O
O O O O O
O O O O O
0
2
Guess Row: 2
Guess Col: 3
You missed my battleship!
Turn 1
O O O O O
O O O O O
O O O X O
O O O O O
O O O O O
Guess Row: 2
Guess Col: 1
You missed my battleship!
Turn 2
O O O O O
O O O O O
O X O X O
O O O O O
O O O O O
Guess Row: 3
Guess Col: 4
You missed my battleship!
Turn 3
O O O O O
O O O O O
O X O X O
O O O O X
O O O O O
Guess Row: 2
Guess Col: 3
You guessed that one already.
Game Over
O O O O O
O O O O O
O X O X O
O O O O X
O O O O O
```


### 17. A Real Win

Almost there! We can play Battleship!, but you’ll notice that when you win, if you haven’t already guessed 4 times, the program asks you to enter another guess. What we’d rather have happen is for the program to end—it’s no fun guessing if you know you’ve already sunk the Battleship!

We can use the `break` command to get out of a `for` loop.


##### Instructions
Add a `break` under the win condition to end the loop after a win.


```Python
# GIVEN
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

for turn in range(4):
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sunk my battleship!")
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print("Oops, that's not even in the ocean.")
      print("Game Over")
    elif(board[guess_row][guess_col] == "X"):
      print("You guessed that one already.")
      print("Game Over")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      print("Turn", turn + 1)
      if turn == 3:
          print("Game Over")
    print_board(board)



# SOLUTION by add
if guess_row == ship_row and guess_col == ship_col:
  print("Congratulations! You sunk my battleship!")
  break
else:
  if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
    print("Oops, that's not even in the ocean.")
    print("Game Over")
  elif(board[guess_row][guess_col] == "X"):
    print("You guessed that one already.")
    print("Game Over")
  else:
    print("You missed my battleship!")
    board[guess_row][guess_col] = "X"
    print("Turn", turn + 1)
    if turn == 3:
        print("Game Over")
  print_board(board)



# OUTPUT
O O O O O
O O O O O
O O O O O
O O O O O
O O O O O
3
0
Guess Row: 3
Guess Col: 0
Congratulations! You sunk my battleship!
```

### 18. To Your Battle Stations!
Congratulations! You have a fully functional Battleship game! Play it a couple of times and get your friends to try it out, too. (Don’t forget to go back and remove the debugging output that gives away the location of the battleship!)

You may want to take some time to clean up and document your code as well.

##### Instructions
When you are done playing Battleship! and are ready to move on, click Run.


### 19. Extra Credit
You can also add on to your Battleship! program to make it more complex and fun to play. Here are some ideas for enhancements—maybe you can think of some more!

Make multiple battleships: you'll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.

Make your game a two-player game.

Use functions to allow your game to have more features like rematches, statistics and more!

Some of these options will be easier after we cover loops in the next lesson. Think about coming back to Battleship! after a few more lessons and see what other changes you can make!

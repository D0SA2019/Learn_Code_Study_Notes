# Python Basics
*Coursera | Python 3 Programming Specialization | Course 1*

## Week 3 : Booleans and Conditionals
### Boolean Expressions

#### 3.1. Boolean Expressions

The Python type for storing true and false values is called `bool`, named after the British mathematician, George Boole. George Boole created **Boolean Algebra**, which is the basis of all modern computer arithmetic.

There are only two **boolean values**. They are `True` and `False`. Capitalization is important, since `true` and `false` are not boolean values (remember Python is case sensitive).


```python
print(True)
print(type(True))
print(type(False))
```


**Output** :

```
True
<class 'bool'>
<class 'bool'>
```


***Note*** : Boolean values are not strings! It is extremely important to realize that True and False are not strings. They are not surrounded by quotes. They are the only two values in the data type `bool`. Take a close look at the types shown below.


```python
print(type(True))
print(type("True"))
```


**Output** :

```
<class 'bool'>
<class 'str'>
```

A **boolean expression** is an expression that evaluates to a boolean value. The equality operator, `==`, compares two values and produces a boolean value related to whether the two values are equal to one another.

```python
print(5 == 5)
print(5 == 6)
```


**Output** :

```
True
False
```

In the first statement, the two operands are equal, so the expression evaluates to `True`. In the second statement, 5 is not equal to 6, so we get `False`.

The `==` operator is one of six common **comparison operators**; the others are:


```python
x == y				# x is equal to y
x != y				# x is not equal to y
x > y					# x is greater than y
x < y					# x is less than y
x >= y				# x is greater than or equal to y
x <= y				# x is less than or equal to y
```

Although these operations are probably familiar to you, the Python symbols are different from the mathematical symbols. A common error is to use a single equal sign (`=`) instead of a double equal sign (`==`). Remember that `=` is an assignment operator and `==` is a comparison operator. Also, there is no such thing as `=<` or `=>`.

Note too that an equality test is symmetric, but assignment is not. For example, if `a == 7` then `7 == a`. But in Python, the statement `a = 7` is legal and `7 = a` is not.

----
-----

**Check Your Understanding**


**E1** : Which of the following is a Boolean expression? Select all that apply.

A. True ✅ <br>
B. 3 == 4 ✅<br>
C. 3 + 4 <br>
D. 3 + 4 == 7 ✅ <br>
E. "False" <br>


#### Logical Operators

There are three logical operators: `and`, `or`, and `not`. The semantics (meaning) of these operators is similar to their meaning in English. For example, `x > 0 and x < 10` is true only if `x` is greater than 0 and at the same time, x is less than 10. How would you describe this in words? You would say that x is between 0 and 10, not including the endpoints.

`n % 2 == 0 or n % 3 == 0` is true if either of the conditions is true, that is, if the number is divisible by 2 or divisible by 3. In this case, one, or the other, or both of the parts has to be true for the result to be true.

Finally, the `not` operator negates a boolean expression, so `not  x > y` is true if `x > y` is false, that is, if `x` is less than or equal to `y`.


```python
x = 5
print(x>0 and x<10)

n = 25
print(n%2 == 0 or n%3 == 0)
```


**Output** :

```
True
False
```


**Common Mistake!**

There is a very common mistake that occurs when programmers try to write boolean expressions. For example, what if we have a variable `number` and we want to check to see if its value is 5, 6, or 7? In words we might say: “number equal to 5 or 6 or 7”. However, if we translate this into Python, `number == 5 or 6 or 7`, it will not be correct. The `or` operator must join the results of three equality checks. The correct way to write this is `number == 5 or number == 6 or number == 7`.

This may seem like a lot of typing but it is absolutely necessary. You cannot take a shortcut.

Well, actually, you can take a shortcut but not that way. Later `in` this chapter you’ll learn about the in operator for strings and sequences: you could write `number in [5, 6, 7]`.

----
-----

**Check Your Understanding**


**E1** : What is the correct Python expression for checking to see if a number stored in a variable x is between 0 and 5.

A. x > 0 and < 5 <br>
B. 0 < x < 5 <br>
C. x > 0 or x < 5 <br>
D. x > 0 and x < 5 ✅ <br>


#### The in and not in Operators

The `in` operator tests if one string is a substring of another:


```python
print("p" in "apple")
print("i" in "apple")
print("ap" in "apple")
print("pa" in "apple")
```


**Output** :

```
True
False
True
False
```


Note that a string is a substring of itself, and the empty string is a substring of any other string. (Also note that computer scientists like to think about these edge cases quite carefully!)


```python
print("a" in "a")
print("apple" in "apple")
print("" in "a")
print("" in "apple")
```


**Output** :

```
True
True
True
True
```

The `not in` operator returns the logical opposite result of `in`.

```python
print("x" not in "apple")
```


**Output** :

```
True
```

We can also use the `in` and `not in` operators on lists!

```python
print("a" in ["a", "b", "c", "d"])
print(9 in [3, 2, 9, 10, 9.0])
print("wow" not in ["gee wiz", "gosh golly", "wow", "amazing"])
```


**Output** :

```
True
True
False
```

However, remember how you were able to check to see if an “a” was in “apple”? Let’s try that again to see if there’s an “a” somewhere in the following list.

```python
print("a" in ["apple", "absolutely", "application", "nope"])
```


**Output** :

```
False
```

Clearly, we can tell that a is in the word apple, and absolutely, and application. For some reason though, the Python interpreter returns False. Why is that? When we use the `in` and `not in` operators on lists, Python checks to see if the item on the left side of the expression is equivalent to an element in the item on the right side of the expression. In this case, Python is checking whether or not an element of the list is the string “a” - nothing more or less than that.


#### Precedence of Operators

Arithmetic operators take precedence over logical operators. Python will always evaluate the arithmetic operators first (** is highest, then multiplication/division, then addition/subtraction). Next comes the relational operators. Finally, the logical operators are done last. This means that the expression `x*5 >= 10 and y-6 <= 20` will be evaluated so as to first perform the arithmetic and then check the relationships. The and will be done last. Many programmers might place parentheses around the two relational expressions, `(x*5 >= 10) and (y-6 <= 20)`. It is not necessary to do so, but causes no harm and may make it easier for people to read and understand the code.

The following table summarizes the operator precedence from highest to lowest. A complete table for the entire language can be found in the [Python Documentation](http://docs.python.org/py3k/reference/expressions.html#expression-lists).

| Level | Category | Operators |
|--|--|--|
| 7 (high) | exponent | `**` |
| 6 | multiplication | `*`, `/`, `//`, `%` |
| 5 | addition | `+`, `-` |
| 4 | relational | `==`, `!=`, `<=`, `>=`, `<`, `>` |
| 3 | logical | `not` |
| 2 | logical | `and` |
| 1 (low) | logical | `or` |


***Common Mistake!***

Students often incorrectly combine the in and or operators. For example, if they want to check that the letter x is inside of either of two variables then they tend to write it the following way: `'x' in y or z`

Written this way, the code would not always do what the programmer intended. This is because the in operator is only on the left side of the or statement. It doesn’t get implemented on both sides of the or statement. In order to properly check that x is inside of either variable, the in operator must be used on both sides which looks like this:

`'x' in y or 'x' in z`


----
----

**Check Your Understanding**

**E1** : Which of the following properly expresses the precedence of operators (using parentheses) in the following expression: `5*3 > 10 and 4+6==11`

A. `((5*3) > 10) and ((4+6) == 11)` ✅ <br>
B. `(5*(3 > 10)) and (4 + (6 == 11))` <br>
C. `((((5*3) > 10) and 4)+6) == 11` <br>
D. `((5*3) > (10 and (4+6))) == 11` <br>


### Conditional Execution

#### Conditional Execution


In order to write useful programs, we almost always need the ability to check conditions and change the behavior of the program accordingly. **Selection statements**, sometimes also referred to as **conditional statements**, give us this ability. The simplest form of selection is the **if statement**. This is sometimes referred to as **binary selection** since there are two possible paths of execution.

```python
x = 15

if x % 2 == 0:
	print(x, "is even")
else:
	print(x, "is odd")
```

**Output** :

```
15 is odd
```

The syntax for an `if` statement looks like this:


```python
if BOOLEAN EXPRESSION :
	STATEMENTS_1					# executed if condition evaluates to True
else :
	STATEMENTS_2					# executes if condition evaluates to False
```

The boolean expression after the `if` statement is called the **condition**. If it is true, then the indented statements get executed. If not, then the statements indented under the `else` clause get executed.

Flowchart of a if statement with an else
![](https://fopp.umsi.education/runestone/static/fopp/_images/flowchart_if_else.png)

As with the function definition from the last chapter and other compound statements like `for`, the `if` statement consists of a header line and a body. The header line begins with the keyword `if` followed by a boolean expression and ends with a colon (:).

The indented statements that follow are called a **block**. The first unindented statement marks the end of the block.

Each of the statements inside the first block of statements is executed in order if the boolean expression evaluates to `True`. The entire first block of statements is skipped if the boolean expression evaluates to `False`, and instead all the statements under the `else` clause are executed.

There is no limit on the number of statements that can appear under the two clauses of an `if` statement, but there has to be at least one statement in each block.

----
----

**Check Your Understanding**

**E1** : How many lines of code can appear in the indented code block below the if and else lines in a conditional?

A. Just one. <br>
B. Zero or more. <br>
C. One or more. ✅ <br>
D. One or more, and each must contain the same number. <br>


----

**E2** : What does the following code print? (choose from output a, b, c or nothing)

```python
if (4 + 5 == 10):
	print("TRUE")
else:
	print("FALSE")
```

A. TRUE <br>
B. FALSE ✅ <br>
C. TRUE on one line and FALSE on the next <br>
D. Nothing will be printed <br>



----

**E3** : What does the following code print?

```python
if (4 + 5 == 10):
	print("TRUE")
else:
	print("FALSE")
print("TRUE")
```

```
a. TRUE

b.
   TRUE
   FALSE

c.
   FALSE
   TRUE
d.
   TRUE
   FALSE
   TRUE
```

A. Output a <br>
B. Output b <br>
C. Output c ✅ <br>
D. Output d <br>



----

**E4** : Write code to assign the string `"You can apply to SI!"` to output if the string `"SI 106"` is in the list courses. If it is not in `courses`, assign the value `"Take SI 106!"` to the variable `output`.

```python
courses = ["ENGR 101", "SI 110", "ENG 125", "SI 106", "CHEM 130"]

if "SI 106" in courses:
    output = "You can apply to SI!"
else :
    output = "Take SI 106!"
print(output)
```


**Output** :

```
You can apply to SI!
```


----

**E5** : Create a variable, `b`, and assign it the value of `15`. Then, write code to see if the value `b` is greater than that of `a`. If it is, `a`’s value should be multiplied by 2. If the value of `b` is less than or equal to `a`, nothing should happen. Finally, create variable `c` and assign it the value of the sum of `a` and `b`.

```python
# Given
a = 20


# Solution
b = 15

if b > a :
	a = a * 2
else:
	pass

c = a + b
print(c)
```

**Output** :

```
35
```


#### Unary Selection

Another form of the `if` statement is one in which the `else` clause is omitted entirely. This creates what is sometimes called **unary selection**. In this case, when the condition evaluates to `True`, the statements are executed. Otherwise the flow of execution continues to the statement after the body of the `if`.

Flowchart of an if with no else :

![](https://fopp.umsi.education/runestone/static/fopp/_images/flowchart_if_only.png)

```python
x = 10
if x < 0:
	print("The negative number ", x, " is not valid here.")
print("This is always printed.")
```

**Output** :

```
This is always printed.
```

What would be printed if the value of x is negative?

```python
x = -10
if x < 0:
	print("The negative number ", x, " is not valid here.")
print("This is always printed.")
```

**Output** :

```
The negative number  -10  is not valid here.
This is always printed.
```

----
----

**Check Your Understanding**

**E1** : What does the following code print?

```python
x = -10
if x < 0:
	print("The negative number ", x, " is not valid here.")
print("This is always printed.")
```

```
a.
This is always printed

b.
The negative number -10 is not valid here
This is always printed

c.
The negative number -10 is not valid here
```

A. Output a <br>
B. Output b ✅ <br>
C. Output c <br>
D. It will cause an error because every if must have an else clause. <br>


----


**E2** : Will the following code cause an error?

```python
x = -10
if x < 0:
	print("The negative number ", x, " is not valid here.")
else:
	print(x, " is a positive number")
else:
	print("This is always printed")
```


A. No <br>
B. Yes ✅ <br>


#### Nested Conditionals

One conditional can also be **nested** within another. For example, assume we have two integer variables, `x` and `y`. The following pattern of selection shows how we might decide how they are related to each other.

```python
if x < y :
	print("x is less than y")
else:
	if x > y :
		print("x is greater than y")
	else:
		print("x and y must be equal")
```

The outer conditional contains two branches. The second branch (the else from the outer) contains another `if` statement, which has two branches of its own. Those two branches could contain conditional statements as well.

The flow of control for this example can be seen in this flowchart illustration.

![](https://fopp.umsi.education/runestone/static/fopp/_images/flowchart_nested_conditional.png)

Here is a complete program that defines values for `x` and `y`. Run the program and see the result. Then change the values of the variables to change the flow of control.

```python
x = 10
y = 10

if x < y:
    print("x is less than y")
else:
    if x > y:
        print("x is greater than y")
    else:
        print("x and y must be equal")
```

**Output** :

```
x and y must be equal
```


----
----

**Check Your Understanding**

**E1** : Will the following code cause an error?

```python
x = -10
if x < 0:
	print("The negative number ", x, " is not valid here.")
else:
	if x > 0 :
		print(x, " is a positive number")
	else:
		print(x, " is 0")
```


A. No ✅ <br>
B. Yes <br>


#### Chained Conditionals

Python provides an alternative way to write nested selection such as the one shown in the previous section. This is sometimes referred to as a **chained conditional**.

```python
if x < y :
	print("x is less than y")
elif x > y :
	print("x is greater than y")
else:
	print("x and y must be equal")
```

The flow of control can be drawn in a different orientation but the resulting pattern is identical to the one shown above.

![](https://fopp.umsi.education/runestone/static/fopp/_images/flowchart_chained_conditional.png)

`elif` is an abbreviation of `else if`. Again, exactly one branch will be executed. There is no limit of the number of `elif` statements but only a single (and optional) final `else` statement is allowed and it must be the last branch in the statement.

![](https://fopp.umsi.education/runestone/static/fopp/_images/conditionals_overview.png)

Each condition is checked in order. If the first is false, the next is checked, and so on. If one of them is true, the corresponding branch executes, and the statement ends. Even if more than one condition is true, only the first true branch executes.

Here is the same program using `elif`.

```python
x = 10
y = 10

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")
```

**Output** :

```
x and y must be equal
```

The following image highlights different kinds of valid conditionals that can be used. Though there are other versions of conditionals that Python can understand (imagine an if statement with twenty elif statements), those other versions must follow the same order as seen below.

![](https://fopp.umsi.education/runestone/static/fopp/_images/valid_conditionals.png)


----
----

**Check Your Understanding**

**E1** : Which of I, II, and III below gives the same result as the following nested if?

```python
# nested if-else statement

x = -10
if x < 10:
	print("The negative number ",  x, " is not valid here.")
else:
	if x > 0 :
		print(x, " is a positive number")
	else:
		print(x, " is 0")
```

```python
I.

if x < 0:
    print("The negative number ",  x, " is not valid here.")
else (x > 0):
    print(x, " is a positive number")
else:
    print(x, " is 0")
```

```python
II.

if x < 0:
    print("The negative number ",  x, " is not valid here.")
elif (x > 0):
    print(x, " is a positive number")
else:
    print(x, " is 0")
```


```python
III.

if x < 0:
    print("The negative number ",  x, " is not valid here.")
if (x > 0):
    print(x, " is a positive number")
else:
    print(x, " is 0")
```

A. I only  <br>
B. II only ✅ <br>
C. III only  <br>
D. II and III  <br>
E. I, II, and III  <br>

---

**E2** : What will the following code print if x = 3, y = 5, and z = 2?

```python
if x < y and x < z:
    print("a")
elif y < x and y < z:
    print("b")
else:
    print("c")
```

A. a <br>
B. b <br>
C. c ✅ <br>


---

**E3** : Create one conditional to find whether `“false”` is in string `str1`. If so, assign variable `output` the string `“False. You aren’t you?”`. Check to see if `“true”` is in string `str1` and if it is then assign `“True! You are you!”` to the variable `output`. If neither are in `str1`, assign `“Neither true nor false!”` to `output`.

```python
str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"

if "false" in str1:
    output = "False. You aren’t you?"
elif "true" in str1:
	output = "True! You are you!"
else:
	output = "Neither true nor false!"
print(output)
```

**Output** :

```
True! You are you!
```


---

**E4** : Create an empty list called `resps`. Using the list `percent_rain`, for each percent, if it is above 90, add the string `‘Bring an umbrella.’` to `resps`, otherwise if it is above 80, add the string `‘Good for the flowers?’` to `resps`, otherwise if it is above 50, add the string `‘Watch out for clouds!’` to `resps`, otherwise, add the string `‘Nice day!’` to `resps`. Note: if you’re sure you’ve got the problem right but it doesn’t pass, then check that you’ve matched up the strings exactly.

```python
percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = []

for rain in percent_rain:
	if rain > 90:
		resps.append("Bring an umbrella.")
	elif rain > 80:
		resps.append("Good for the flowers?")
	elif rain > 50:
		resps.append("Watch out for clouds!")
	else:
		resps.append("Nice day!")
print(resps)
```

**Output** :

```
['Bring an umbrella.', 'Nice day!', 'Bring an umbrella.', 'Watch out for clouds!', 'Nice day!', 'Nice day!', 'Watch out for clouds!', 'Good for the flowers?']
```


---

**E5** : We have created conditionals for you to use. Do not change the provided conditional statements. Find an integer value for `x` that will cause `output` to hold the values `True` and `None`.

```python
# Given
x =
output = []

if x > 63:
    output.append(True)
elif x > 55:
    output.append(False)
else:
    output.append("Neither")

if x > 67:
    output.append(True)
else:
    output.append(None)


# Solution
x = 64
...
print(output)
```

**Output** :

```
[True, None]
```


#### Setting Up Conditionals

Before writing your conditionals, it can be helpful to make your own flowchart that will plot out the flow of each condition. By writing out the flow, you can better determine how complex the set of conditionals will be as well as check to see if any condition is not taken care of before you begin writing it out.

To make sure that your code covers all of the conditions that you intend for it to cover, you should add comments for each clause that explains what that clause is meant to do. Then, you should add tests for each possible path that the program could go though. What leads to certain conditional statements being executed? Is that what you intended?


#### Choosing your type of Conditional

When adding conditionals to your program, you should also consider the kinds of conditionals that are at your disposal and what would fit best.

![](https://fopp.umsi.education/runestone/static/fopp/_images/valid_conditionals.png)

Though you’ll use them often, remember that conditional statements don’t always need an else clause. When deciding the flow, ask yourself what you want to have happen under a certain condition. For example, if you wanted to find all of the words that have the letter ‘n’ in them. If there’s nothing that needs to happen when a word does not contain the letter ‘n’ then you won’t need an else clause. The program should just continue onward!



----
----

**Check Your Understanding**

**E1** : What is the best set of conditonal statements provided based on the following prompt? You want to keep track of all the words that have the letter ‘t’ and in a separate variable you want to keep track of all the words that have the letter ‘z’ in them.

A. If statement - Else statement <br>
B. If statement - Elif statement <br>
C. If statement - If statement ✅  <br>
D. If statement - Elif statemenet - Else statement <br>

---

**E2** : Select the most appropriate set of conditonal statements for the situation described: You want to keep track of all the words that contain both “t” and “z”.

A. If statement - Elif statemenet - Else statement <br>
B. If statement - Else statement <br>
C. If statement - Nested If statement <br>
D. If statement ✅ <br>
E. If statement - Nested If statement - Else statement <br>


#### The Accumulator Pattern with Conditionals

Sometimes when we’re accumulating, we don’t want to add to our accumulator every time we iterate. Consider, for example, the following program which counts the number of letters in a phrase.

```python
phrase = "What a wonderful day to program"
tot = 0

for char in phrase:
	if char != " ":
		tot = tot + 1

print(tot)
```

**Output** :

```
26
```

Here, we **initialize** the accumulator variable to be zero on line two.

We **iterate** through the sequence (line 3).

The **update** step happens in two parts. First, we check to see if the value of `char` is not a space. If it is not a space, then we update the value of our accumulator variable `tot` (on line 6) by adding one to it. If that conditional proves to be False, which means that char is a space, then we don’t update `tot` and continue the for loop. We could have written `tot = tot + 1` or `tot += 1`, either is fine.

At the end, we have accumulated a the total number of letters in the phrase. Without using the conditional, we would have only been able to count how many characters there are in the string and not been able to differentiate between spaces and non-spaces.

We can use conditionals to also count if particular items are in a string or list. The following code finds all occurrences of vowels in the following string.


```python
s = "what if we went to the zoo"
x = 0

for i in s:
	if i in ["a", "e", "i", "o", "u"]:
		x += 1

print(x)
```

**Output** :

```
8
```

We can also use `==` to execute a similar operation. Here, we’ll check to see if the character we are iterating over is an “o”. If it is an “o” then we will update our counter.

![](https://fopp.umsi.education/runestone/static/fopp/_images/accum_o.gif)


#### Accumulating the Max Value

We can also use the accumulation pattern with conditionals to find the maximum or minimum value. Instead of continuing to build up the accumulator value like we have when counting or finding a sum, we can reassign the accumulator variable to a different value.

The following example shows how we can get the maximum value from a list of integers.


```python
nums = [9, 3, 8, 11, 5, 29, 2]
best_num = 0

for n in nums:
	if n > best_num:
		best_num = n

print(best_num)
```

**Output** :

```
29
```

Here, we initialize best_num to zero, assuming that there are no negative numbers in the list.

In the for loop, we check to see if the current value of n is greater than the current value of `best_num`. If it is, then we want to **update** `best_num` so that it now is assigned the higher number. Otherwise, we do nothing and continue the for loop.

You may notice that the current structure could be a problem. If the numbers were all negative what would happen to our code? What if we were looking for the smallest number but we initialized `best_num` with zero? To get around this issue, we can initialize the accumulator variable using one of the numbers in the list.

```python
nums = [9, 3, 8, 11, 5, 29, 2]
best_num = nums[0]

for n in nums:
	if n > best_num:
		best_num = n

print(best_num)
```

**Output** :

```
29
```

The only thing we changed was the value of `best_num` on line 2 so that the value of `best_num` is the first element in `nums`, but the result is still the same!

```python
nums = [-9, -3, -8, -11, -5, -29, -2]
best_num = nums[0]

for n in nums:
	if n > best_num:
		best_num = n

print(best_num)
```

**Output** :

```
-2
```

----
----

**Check Your Understanding**

**E1** : What is printed by the following statements?

```python
s = "We are learning!"
x = 0

for i in s:
	if i in ["a", "b", "c", "d", "e"]:
		x += 1

print(x)
```

A. 2 <br>
B. 5 ✅ <br>
C. 0 <br>
D. There is an error in the code so it cannot run. <br>


---

**E2** : What is printed by the following statements?

```python
list = [5, 2, 1, 4, 9, 10]
min_value = 0

for item in list:
	if item < min_value:
		min_value = item

print(min_value)
```

A. 10 <br>
B. 1 <br>
C. 0 ✅ <br>
D. There is an error in the code so it cannot run. <br>



---

**E3** : For each string in the list `words`, find the number of characters in the string. If the number of characters in the string is greater than 3, add 1 to the variable `num_words` so that `num_words` should end up with the total number of words with more than 3 characters.

```python
# Given
words = ["water", "chair", "pen", "basket", "hi", "car"]



# Solution
words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0

for word in words:
    len_word = len(word)
    if len_word > 3:
        num_words += 1

print(num_words)
```

**Output** :

```
3
```


---

**E4** : For each word in `words`, add ‘d’ to the end of the word if the word ends in “e” to make it past tense. Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called `past_tense`.

```python
# Given
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]



# Solution
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = list()

for word in words:
    if word[-1] == "e":
        word = word + "d"
        past_tense.append(word)
    else:
        word = word + "ed"
        past_tense.append(word)

print(past_tense)
```

**Output** :

```
['adopted', 'baked', 'beamed', 'confided', 'grilled', 'planted', 'timed', 'waved', 'wished']
```


#### Chapter Assessments & Exercises

#### Assessments

**A1**. `rainfall_mi` is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable `num_rainy_months`. In other words, count the number of items with values `> 3.0.`

Hard-coded answers will receive no credit.


```python
# Given
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"


# Solution
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rains = rainfall_mi.split(",")
num_rainy_months = 0
for rain in rains:
    if float(rain) > 3.0 :
        num_rainy_months += 1

print(num_rainy_months)
```


**Output** :

```
5
```


-----

**A2**. The variable `sentence` stores a string. Write code to determine how many words in `sentence` start and end with the same letter, including one-letter words. Store the result in the variable `same_letter_count`.

Hard-coded answers will receive no credit.


```python
# Given
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"


# Solution
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
sliced = sentence.split()
same_letter_count = 0

for word in sliced:
	if word[0] == word[-1]:
		same_letter_count += 1

print(same_letter_count)
```


**Output** :

```
2
```


-----

**A3**. Write code to count the number of strings in list `items` that have the character w in it. Assign that number to the variable `acc_num`.

HINT 1: Use the accumulation pattern!

HINT 2: the in operator checks whether a substring is present in a string.

Hard-coded answers will receive no credit.

```python
# Given
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]


# Solution
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0

for item in items:
	w_num = item.count("w")
	if w_num > 0:
		acc_num +=1
print(acc_num)
```


**Output** :

```
4
```



-----

**A4**. Write code that counts the number of words in `sentence` that contain either an “a” or an “e”. Store the result in the variable `num_a_or_e`.

Note 1: be sure to not double-count words that contain both an a and an e.

HINT 1: Use the `in` operator.

HINT 2: You can either use `or` or `elif`.

Hard-coded answers will receive no credit.


```python
# Given
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."



# Solution
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
sliced = sentence.split()
num_a_or_e = 0

for word in sliced:
    num_a = word.count("a")
    num_e = word.count("e")

    if num_a > 0 or num_e > 0:
        num_a_or_e += 1

print(num_a_or_e)
```

**Output** :

```
14
```


-----

**A5**. Write code that will count the number of vowels in the sentence `s` and assign the result to the variable `num_vowels`. For this problem, vowels are only a, e, i, o, and u.
Hint: use the `in` operator with `vowels`.


```python
# Given
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']


# Solution
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

num_vowels = 0
sliced = s.split()

for word in sliced:
    for letter in word:
        if letter in vowels:
            num_vowels += 1

print(num_vowels)
```

**Output** :

```
32
```


-----

**A6**. Create one conditional so that if “Friendly” is in `w`, then “Friendly is here!” should be assigned to the variable `wrd`. If it’s not, check if “Friend” is in `w`. If so, the string “Friend is here!” should be assigned to the variable `wrd`, otherwise “No variation of friend is in here.” should be assigned to the variable `wrd`. (Also consider: does the order of your conditional statements matter for this problem? Why?)


```python
# Given
w = "Friendship is a wonderful human experience!"



# Solution
w = "Friendship is a wonderful human experience!"

if "Friendly" in w:
    wrd = "Friendly is here!"

elif "Friend" in w:
    wrd = "Friend is here!"
else:
    wrd = "No variation of friend is in here."
print(wrd)
```


**Output** :

```
Friend is here!
```


-----

**A7**. We have written conditionals for you to use. Create the variable `x` and assign it some integer so that at the end of the code, `output` will be assigned the string `"Consistently working"`.


```python
# Given
if x >= 10:
    output = "working"
else:
    output = "Still working"
if x > 12:
    output = "Always working"
elif x < 7:
    output = "Forever working"
else:
    output = "Consistently working"



# Solution
x = 9
```

-----

**A8**. Write code so that if `"STATS 250"` is in the list `schedule`, then the string `"You could be in Information Science!"` is assigned to the variable `resp`. Otherwise, the string `"That's too bad."` should be assigned to the variable `resp`.


```python
# Given
schedule = ["SI 106", "STATS 250", "SI 110", "ENGLISH 124/125"]


# Solution
schedule = ["SI 106", "STATS 250", "SI 110", "ENGLISH 124/125"]
if "STATS 250" in schedule:
    resp = "You could be in Information Science!"
else:
    resp = "That's too bad."

print(resp)
```

**Output** :

```
You could be in Information Science!
```


-----

**A9**. Create the variable `z` whose value is `30`. Write code to see if `z` is greater than `y`. If so, add 5 to `y`’s value, otherwise do nothing. Then, multiply `z` and `y`, and assign the resulting value to the variable `x`.


```python
# Given
y = 22



# Solution
y = 22
z = 30

if z > y:
    y += 5

x = z * y
print(x)
```

**Output** :

```
810
```

-----

**A10**. For each string in `wrd_lst`, find the number of characters in the string. If the number of characters is less than 6, add 1 to `accum` so that in the end, `accum` will contain an integer representing the total number of words in the list that have fewer than 6 characters.


```python
# Given
wrd_lst = ["Hello", "activecode", "Java", "C#", "Python", "HTML and CSS", "Javascript", "Swift", "php"]



# Solution
wrd_lst = ["Hello", "activecode", "Java", "C#", "Python", "HTML and CSS", "Javascript", "Swift", "php"]
accum = 0

for word in wrd_lst:
    len_word = len(word)

    if len_word < 6:
        accum += 1

print(accum)
```


**Output** :

```
5
```


----
----

#### Exercises

**Q1**. Write code that asks the user to enter a numeric score (0-100). In response, it should print out the score and corresponding letter grade, according to the table below.

| Score | Grade |
|--|--|
| >= 90 | A |
| [80-90]| B |
| [70-80]| C |
| [60-70]| D |
| < 60 | F |

The square and round brackets denote closed and open intervals. A closed interval includes the number, and open interval excludes it. So 79.99999 gets grade C , but 80 gets grade B.

```python
score = int(input("Enter the score: "))

if score >= 90:
	grade = "A"
elif 80 <= score < 90:
	grade = "B"
elif 70 <= score < 80:
	grade = "C"
elif 60 <= score < 70:
	grade = "D"
else:
	grade = "F"

print(grade)
```

**Output** :

```
Enter the score: 80
B
```


----

**Q2**. A year is a **leap year** if it is divisible by 4. If the year can be evenly divided by 100, it is NOT a leap year, unless the year is **also** evenly divisible by 400. Then it is a leap year. Write code that asks the user to input a year and output True if it’s a leap year, or False otherwise. Use if statements.

| Year | Leap? |
|--|--|
| 1944 | True |
| 2011 | False |
| 1986 | False |
| 1800 | False |
| 1900 | False |
| 2000 | True |
| 2056 | True |

Above are some examples of what the output should be for various inputs.

```python
year = int(input("Enter the year: "))

if year % 100 == 0:
	if year % 400 == 0:
		is_leap = True
	else:
		is_leap = False
elif year % 4 == 0:
	is_leap = True
else:
	is_leap = False

print(is_leap)
```

----

**Q3**. What do these expressions evaluate to?

1. `3 == 3`
2. `3 != 3`
3. `3 >= 4`
4. `not (3 < 4)`

```python
print(3 == 3)
print(3 != 3)
print(3 >= 4)
print(not (3 < 4))
```

**Output** :

```
True
False
False
False
```

----


**Q4**. Give the **logical opposites** of these conditions, meaning an expression that would produce `False` whenever this expression produces `True`, and vice versa. You are not allowed to use the not operator.

1. `a > b`
2. `a >= b`
3. `a >= 18  and  day == 3`
4. `a >= 18  or  day != 3`


```
a < b
a < b
a < 18 and day != 3
a < 18 or day == 3
```


----

**Q5**. Provided are the lengths of two sides of a right-angled triangle. Assign the length of the hypotenuse the the variable `hypo_len`. (Hint: `x ** 0.5` will return the square root, or use `sqrt` from the math module)


```python
# Given
side1 = 3
side2 = 4


# Solution
hypo_len = ((side1 ** 2 ) * (side2 ** 2)) ** 0.5
print(hypo_len)
```

**Output** :

```
5.0
```

----

**Q6**. Provided is a list of numbers. For each of the numbers in the list, determine whether they are even. If the number is even, add `True` to a new list called `is_even`. If the number is odd, then add `False`.


```python
# Given
num_lst = [3, 20, -1, 9, 10]


# Solution
is_even = list()

for num in num_lst:
    if num % 2 == 0 :
        num_even = True
        is_even.append(num_even)
    else:
        num_even = False
        is_even.append(num_even)

print(is_even)
```

**Output** :

```
[False, True, False, False, True]
```

----


**Q7**. Provided is a list of numbers. For each of the numbers in the list, determine whether they are odd. If the number is odd, add `True` to a new list called `is_odd`. If the number is even, then add `False`.


```python
# Given
num_lst = [3, 20, -1, 9, 10]


# Solution
is_odd = list()

for num in num_lst:
	if num % 2 != 0:
		num_odd = True
		is_odd.append(num_odd)
	else:
		num_odd = False
		is_odd.append(num_odd)

print(is_odd)
```

**Output** :

```
[True, False, True, True, False]
```

----


**Q8**. Given the lengths of three sides of a triange, determine whether the triangle is right angled. If it is, the assign `True` to the variable `is_rightangled`. If it’s not, then assign `False` to the variable `is_rightangled`.

Hint: floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for equality. If a good programmer wants to know whether `x` is equal or close enough to `y`, they would probably code it up as

```python
if  abs(x - y) < 0.001:      # if x is approximately equal to y
    ...
```

```python
# Given
a = 5
b = 6
c = 8


# Solution
if (((b**2) + (c**2)) ** 0,5) == a:
	is_rightangled = True
elif (((a**2) + (c**2)) ** 0,5) == b:
	is_rightangled = True
elif (((a**2) + (b**2)) ** 0,5) == c:
	is_rightangled = True
else:
	is_rightangled = False

print(is_rightangled)
```

**Output** :

```
False
```

----

**Q9**. Implement the calculator for the date of Easter.

The following algorithm computes the date for Easter Sunday for any year between 1900 to 2099.

Ask the user to enter a year. Compute the following:

1. a = year % 19
2. b = year % 4
3. c = year % 7
4. d = (19 * a + 24) % 30
5. e = (2 * b + 4 * c + 6 * d + 5) % 7
6. dateofeaster = 22 + d + e

Special note: The algorithm can give a date in April. You will know that the date is in April if the calculation gives you an answer greater than 31. (You’ll need to adjust) Also, if the year is one of four special years (1954, 1981, 2049, or 2076) then subtract 7 from the date.

Your program should print an error message if the user provides a date that is out of range.


```python
year = int(input("Enter the year between 1900-2099: "))

if year not in list(range(1900, 2100)):
	print("The year isnt'n between 1900-2099")
else:
	a = year % 19
	b = year % 4
	c = year % 7
	d = (19 * a + 24) % 30
	e = (2 * b + 4 * c + 6 * d + 5) % 7
	dateofeaster = 22 + d + e

	if year in [1954, 1981, 2049, 2076]:
		dateofeaster -= 7
	if dateofeaster > 31:
		print("April", dateofeaster - 31)
	else:
		print("March", dateofeaster)
```

**Output** :

```
Enter the year between 1900-2099: 1957
April 21
```

----


**Q10**. Get the user to enter some text and print out True if it’s a palindrome, False otherwise. (Hint: reuse some of your code from the last question. The == operator compares two values to see if they are the same)


```python
text = input("Enter a word or text: ")
count = 0

for char in text:
	ind = text.find(char)
	if char == text[(-ind)-1]:
		count += 1

if count >= 2:
	is_pal = True
else :
	is_pal = False

print(is_pal)
```

**Output** :

```
Enter a word or text: Red rum, sir, is murder
True
```

----

**Q11**. Write a program that will print out a greeting to each student in the list. This list should also keep track of how many students have been greeted and note that each time a new student has been greeted. When only one student has entered, the program should say "The first student has entered!". Afterwards, the program should say "There are {number here} students in the classroom!".


**Output** :

![](http://i66.tinypic.com/zwfeop.png)

----

**Q12**. Piece together a program so that it can successfully print out one print statement, given the value of x.


**Output** :

![](http://i68.tinypic.com/10h6o80.png)

----

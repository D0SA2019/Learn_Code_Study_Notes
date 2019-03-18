# Basics of Programming I
## 1.5. Operators


### 1.5.1. Introduction

In computing, we work with lots of different forms of data. But the real fun comes when we can *do* something with this data.

In this lesson, we’ll look at how we can write short computer programs using *operators*.

Operators are different symbols that represent an *operation*, such as the plus sign (`+`) as a symbol for addition. Operations enable us to *process* our data, to transform it into something else.

You may already be familiar with operators and operations from other contexts. This lesson looks at different ways we can use operators in programming, including:

* Making calculations using *arithmetic* operators.
* Comparing information using *comparison* operators.
* Creating logical expressions using *logical* (aka Boolean) operators.


##### Instructions

We can think of writing a program as similar to following a recipe.

In this lesson, we’ll look at how we can use operators to make a fruit salad.

To make the salad, we’ll use operators to:

* Calculate the fruit needed
* Compare the different fruits
* Determine if we have the right ingredients

Right now, we can only add or take away data points by manually including them or deleting them from our code, sort of like adding and subtracting.

When you’re ready, move to the next exercise.


**GIVEN**

![](http://i68.tinypic.com/qyhf02.png)

[codepen](https://codepen.io/hevalhazalkurt/pen/RdBboQ)

### 1.5.2. Using Operators to Make Calculations
Think about the last time you needed to perform long division — did you write it out on paper or reach for a calculator? We can actually write computer programs that perform calculations for us. In fact, that was their original purpose!

If we want to write a program that performs calculations, we need to use arithmetic operators. They include addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).

* Addition adds an amount to a number: `2 + 3 = 5`
* Subtraction takes away an amount from a number: `10 - 3 = 7`
* Multiplication takes a number and repeats it a specified number of times: `5 * 2 = 10`
* Division takes a number and divides it by another number: `15 / 3 = 5`

How does this work in real life? Let’s say we need to buy some apples for the fruit salad recipe. The recipe calls for six apples, but we can only find bags of five. If we buy just enough bags for your recipe, how many extra apples will you have?

Since one bag isn’t enough, we need to buy two bags with five apples each, which would equal 10. Then, we’d subtract the six apples that we need for our recipe to find our answer:

```
apples = 5
my_apples = apples * 2
answer = my_apples - 6
```

If we were to print out `answer`, it would equal `4`.

You may notice that unlike in math class, we put the “answer” on the left-hand side of the equals sign, rather than to the right. That’s because we’re saving the value of our answer to a new variable! So, `apples`, `my_apples`, and `answer` are all variables.

##### Instructions
Let’s calculate how many apples we need for our fruit salad!

The recipe says that for a fruit salad that serves 2-4 people you will need four apples. But you’re making a fruit salad for a party, so you need to double the recipe. Use the buttons to calculate the correct amount of apples to use in the fruit salad.

**GIVEN**

![](http://i64.tinypic.com/23u22d4.png)

[codepen](https://codepen.io/hevalhazalkurt/pen/RdBboQ)

### 1.5.3. Using Operators to Make Comparisons
When writing a program, we often need to check if a value is correct or compare two values.

Comparison operators allow us to compare values and evaluate their relationship. Rather than evaluating to an integer, they evaluate to `true` or `false`, AKA boolean values. Expressions that evaluate to boolean values are known as boolean expressions.

Comparison operators include:

* Less than `<` — value to the left is **less than** the value to the right: `2 < 6`
* Greater than `>` — value to the left is **more than** the value to the right: `14 > 5`
* Equals `==` — value to the left is **equal to** the value to the right: `3 == 3`

Note: we use a double-equal sign to show that we’re checking a value, rather than setting it equal to something, like we would with a variable. Some languages even use a triple-equal sign `===` to super-triple-check!

There are two main instances where we use comparison operators:

**If we have an unknown quantity.** What if we knew that we needed a half pound of strawberries, but we didn’t know the weight of each strawberry? We could weigh the strawberries and see if the total weight equals a half pound.

```
strawberry_weight = ?
is (strawberry_weight == .5lb)? => true
```

**If we need to compare two known values.** If we’re making a salad that’s super citrusy, then we need to make sure we have more oranges than bananas. If that’s false, I’ll have to add more oranges.

```
bananas = 5
oranges = 3

is (oranges > bananas)? => false
```

##### Instructions
For once, let’s compare apples and oranges.

Our fruit salad recipe gives us a couple options for apple to orange ratios.

* If we want a balanced salad, we should have three apples and three oranges.

* If we want a more citrusy salad, we should have five oranges and three apples.

* If we want a less citrusy salad, we should have four apples and two oranges.

From left to right, follow the provided recipes and select the correct comparison operator for each one.

Why is it helpful to be able to check or compare different values?

**GIVEN**

![](http://i67.tinypic.com/29yjldx.png)

[codepen](https://codepen.io/hevalhazalkurt/pen/GeBKeP)

### 1.5.4. Using Operators to Get Different Outcomes
As we saw, comparison operators allow us to examine the relationship of two values. But what if we’re looking at more than two values?

*Logical operators*, also known as boolean operators, evaluate multiple boolean expressions. Rather than determining if one relationship is true or false, it looks at several relationships by connecting them with logical operators and then determining the logic/validity of the overall expression.

Logical operators include:

* *AND* — both expressions evaluate to true, so the final result is true:
	* `((4 > 1) AND (2 < 7))` is the same as `(TRUE AND TRUE)`. Evaluates to true.
* OR — one of the expressions evalutes to true, so the final result is true:
	* `((8 > 6) OR (3 > 6))` is the same as `(TRUE OR FALSE)`. Evaluates to true.
* NOT — an expression, no matter its logical value, evaluates to the opposite:
	* `NOT (1 < 3)` evaluates to `NOT (TRUE)`. Evaluates to false.

The examples given are only a few of the outcomes that you can reach using logical operators. Using logical operators and boolean expressions enable us to handle different scenarios in our program. For example, what if we only had apples in our fridge? If a recipe asked for either apples OR pears, we could still make the recipe. But if a recipe requires both apples AND pears, we wouldn’t be able to make it.

##### Instructions
Take a look at these following recipes and determine if you can make them with the fruit on hand:

* You have a fruit salad recipe that calls for seven apples and four oranges.
* You have a juice recipe that asks for eight apples, but you could also just use eight oranges.
* You have a recipe that is for applesauce.

How do boolean operators allow us to make our programs more flexible or more strict? Can we start to see ways we can write programs that can handle different scenarios?

**GIVEN**

![](http://i66.tinypic.com/547iuu.png)

[codepen](https://codepen.io/hevalhazalkurt/pen/JzBjzx)

### 1.5.5. Putting it All Together
Now that we know a bit about different operators, let’s try writing our own expressions!

As we’ve seen, we can use operators to change something’s value, add other things to our program, to take them away, or to perform calculations. We can also use operators to compare statements or determine whether they are true or false.

One important thing about operators when you program is that they may look different from language to language. That’s because different programming languages have different syntax, or rules for how they are written.

##### Instructions
Let’s use the operators that we’ve learned to add different fruits to the screen and determine their relationships.

* Create a variable named `orange` and set it equal to 4.

* **Decrease** the number of oranges from 4 to 2. Save the result to the orange variable again.

* Run the code and see how many oranges appear on the screen.

**GIVEN**

```
// Create an apple variable and set it to 1
apple = 1

// Increase the amount of apples from 1 to 3
apple = apple + 2


// Create an orange variable and set it to 4


// Decrease the amount of oranges from 4 to 2
```

**SOLUTION**

```
apple = 1

apple = apple + 2

orange = 4

orange = orange - 2
```

![](http://i66.tinypic.com/rsrk0m.png)



### 1.5.6. Review

Congrats! Now you know about different operators and how they can be used to build simple programs.

In this lesson, we learned:

* *Operators* are symbols that represent different ways of modifying, comparing, and evaluating information.
* *Arithmetic operators* are used to make calculations.
* *Comparison operators* determine the relationship between two values, which results in a boolean.
* *Logical operators* determine the logical state of multiple boolean values or expressions, which results in another boolean.

Now that you know the building blocks of operators, how can you further combine them to write programs?

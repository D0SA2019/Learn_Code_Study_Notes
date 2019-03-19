# Basics of Programming I
## 2.1. Functions


### 2.1.1. Functions

This lesson requires you to know the basics of hamburger-making:

* Place the bread down
* Add the burger patty
* Add the pickles
* Place the bread on top

What if you had to say each step every time you ordered a hamburger? It’s tedious. It takes a long time. (How do you fit that on a menu?) And it risks making mistakes.

In this lesson you will learn a solution to that problem: functions. You’ll learn how and why they are used in programming and be able to communicate their benefits to other programmers!

Functions are used throughout programming — in fact, some styles of programming rely completely on functions. Knowing this information will be useful for anywhere your programming path takes you.


##### Instructions

Build hamburgers without a function: make three hamburgers by clicking on each instruction.

Hint: Add bread – Add burger patty – Add pickles – Add bread.


**GIVEN**

![](https://media.giphy.com/media/3h3GQIMSckKTBzvE1u/giphy.gif)


### 2.1.2. Functions for Reusability

Instead of giving those instructions for every hamburger, we can group and name them as a single function:

```
function makeHamburger() {
  Add bread
  Add burger patty
  Add pickles
  Add bread
}
```

A function is a sequence of instructions that performs a specific task, packaged as a unit.

We’ve *defined* the function by giving it instructions and a name, but how do we use it? We use a function by *calling* it. When we call `makeHamburger()` we expect all of its steps to be executed.

##### Instructions
Build hamburgers with a function: In this example you can call the function by clicking the button `makeHamburger()`. Make three hamburgers by calling the function three times.



![](https://media.giphy.com/media/5nrZeSbpt6d1RusDuz/giphy.gif)


### 2.1.3. Functions for Flexibility

Not everyone wants to eat hamburgers.

We could write a new function for each new sandwich type, but that takes a lot of work and risks making mistakes.

Instead we’ll generalize the hamburger function to a sandwich function. This new sandwich function will still make a bread-topping-topping-bread combination, but the toppings may change based on inputs to the function:

```
function makeSandwich(topping1, topping2) {
  Add bread
  Add topping1
  Add topping2
  Add bread
}
```

We’ve renamed the function `makeSandwich()` and given it two inputs, or *parameters*. Each time we call the function, we’ll give actual values for each input, called *arguments*.

For example, we make a ham-and-cheese sandwich with `makeSandwich("ham", "cheese")`. We call the function with the arguments “ham” and “cheese”. Those will be the values for the `topping1` and `topping2` parameters.

Instead of writing a different function for each type of sandwich, we have one function that can make them all!


##### Instructions

Call the `makeSandwich()` function with the arguments `"ham"` and `"cheese"`.

Notice how the instructions change with different inputs.


![](https://media.giphy.com/media/7YDd9BcI2TffEOGk8m/giphy.gif)



### 2.1.4. Functions for organization

A sandwich wouldn’t be complete without fries and dessert!

Here are the instructions to make the complete meal:

* Add bread, Add burger patty, Add fried potatoes, Add pickles, Add bread, Add salt, Add chocolate scoop, Add ketchup, Add vanilla scoop, Add strawberry scoop

Oof. All of the instructions are there, but they’re confusing and hard to edit. If you decide to ask for a fruit salad instead of fries, you would have to find all of the fries-related instructions and replace every line.

To make it easier to read, we’ll separate and organize our instructions:

* Add bread, Add burger patty, Add pickles, Add bread

* Add fried potatoes, Add salt, Add ketchup

* Add chocolate scoop, Add vanilla scoop, Add strawberry scoop

Better… Now let’s group these instructions into three functions:

* makeSandwich()
* makeSomeFries()
* makeIceCream()

We can easily substitute one line, `makeSomeFries()`, for a different function, like `makeFruitSalad()`. And if there’s an error, we know where to look for the recipe for each part of the meal.

The new instructions are starting to look like a program! By using functions, we made it easier to read, reusable, and *modular*: each set of related instructions (sandwich, fries, dessert) is grouped into its own function, which we can easily add, remove, and swap to make a diversity of meals.


##### Instructions

*“I’d like a sandwich, fries, and triple ice cream scoop, please!”*

1. Make this lunch WITHOUT functions
2. Make this lunch again WITH functions

Questions: Which approach was easier? Which approach was less prone to error?

------

*“I’d like 3 sandwiches, 2 fries, and 2 triple ice cream scoop, please!”*

1. Click the reset icon
2. Make this lunch WITHOUT the functions
3. Make this lunch WITH functions

Questions: Which approach was easier this time?


[codepen](https://codepen.io/hevalhazalkurt/pen/JzBVyq)


### 2.1.5. Putting It All Together
Time to get coding! It’s okay if you don’t recognize all the symbols in this code: we’ll walk you through the parts you need to know.

The `makeSandwich()` function is provided in **main.js**. It is defined with two parameters, `topping1` and `topping2`. By reading the instructions inside the function, we can see that it is constructing a string of words that represent the ingredients in the sandwich. For example, the first ingredient is `'bread'`.

Below the function definition, the function is called. When called, the function outputs a string representing a custom sandwich. We say that the function *returns* a string. The value of that string is stored in the variable `result`.

We’ve set up the workspace so that the value of `result` is translated to ingredients drawn in the app to the far right. With the below code…

```
result = makeSandwich('burger patty', 'pickles')
```

…the app will interpret `result` as a bread-patty-pickles-bread sandwich and draw one to the screen.


##### Instructions

Make a sandwich of your own by calling the function with different arguments:

* At the bottom of the code, change `'burger patty'` and `'pickles'` to `'peanut butter'` and `'jelly'`, then
* Run the code

Congrats, you’re coding with JavaScript! Feel free to try other toppings you’ve seen throughout this lesson.


**GIVEN**

```js
// Define the 'makeSandwich()' function
function makeSandwich(topping1, topping2) {
  sandwich = 'bread' + ','
  sandwich += topping1 + ','
  sandwich += topping2 + ','
  sandwich += 'bread'
  return sandwich
}

// Call the function and store the returned value in 'result'
result = makeSandwich('burger patty', 'pickles')
```


**SOLUTION**

```js
// Define the 'makeSandwich()' function
function makeSandwich(topping1, topping2) {
  sandwich = 'bread' + ','
  sandwich += topping1 + ','
  sandwich += topping2 + ','
  sandwich += 'bread'
  return sandwich
}

// Call the function and store the returned value in 'result'
result = makeSandwich('peanut butter', 'jelly')
```


### 2.1.6. Review

Well done! Functions are a fundamental concept in programming, and learning the basics will serve you wherever your path leads, regardless of language or domain. To review:

* A *function* is a sequence of instructions that performs a specific task, packaged as a unit.
* When we *define* a function, we specify the instructions, inputs, and name of the function.
* When we *call* a function, all of its instructions are executed.
* Functions can be executed many times, making its instructions *reusable*.
* Functions can have *parameters*, which accept input values, making its instructions *flexible*.
* Functions organize a program into distinct units, making interchanging and editing them easier. This makes your entire program organized and *modular*.


##### Instructions

Make sure you’re comfortable with the above concepts before moving on!


[codepen](https://codepen.io/hevalhazalkurt/pen/JzBVyq)

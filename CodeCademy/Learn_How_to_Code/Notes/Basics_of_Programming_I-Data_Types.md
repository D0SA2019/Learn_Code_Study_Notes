# Basics of Programming I
## 1.3. Data Types


### 1.3.1. Introduction to Data Types
*Data* is a basic unit in programming. Without data, we couldn’t write any programs! But what is data? We may be familiar with data as information, or facts. In computing, data is the pieces of information that we use to build programs, like the numbers in a calculation, or the text printed to a screen.

*Data types* are exactly what they sound like: different types of data. Data types tell us about the data, including how it can be stored and what types of operations we can perform. For example, we can write a program that squares numbers, but it wouldn’t be able to square a word.

In programming, there’s a special group of data types called *primitives*. Primitives are the most basic data types, so basic that you can find them in pretty much every programming language. They include:

* Numbers
* Strings
* Boolean values (True or False)

In the following exercises, we’ll dig a little deeper into each primitive data type and what you generally can (and can’t do) with each one.

##### Instructions
Computers can do different things with different kinds of data. This computer will process data according to the function that you give it. If the function matches the data type, you will get an answer! If it doesn’t, you’ll see an error.

The functions do the following:

* **capitalize**: will turn lowercase characters into uppercase characters
* **square**: will square a number
* **evaluate**: will determine if an input is true or false

**GIVEN**

![](http://i66.tinypic.com/vrzqiv.png)

[codepen](https://codepen.io/hevalhazalkurt/pen/XGYQOr/)

### 1.3.2. Numbers
*Numbers* are the original data type. The earliest computers communicated only in numbers, using binary computation.

We no longer just program using numbers, but numbers still have special properties and are used to do the following:

* *Describe* — numbers are used to express value: what is the frequency of a sound wave? We can express that in a number, such as 800hz.
* *Calculate* — numbers are used in calculations: what’s the distance between the earth and mars?
* *Count* — numbers are used to keep track: how many times did the car go around the track?

While we can do a lot of things with numbers, there are a few things we can’t do with them. For example, say we have the number 20 and the text, “I am 20 years old.” While both deal with the idea of 20 as a value, a computer could perform mathematical operations on the first piece of data, but not on the second.


##### Instructions
Numbers allows us to write programs that store values, count, and make calculations. This program calculates the numerical distance between different points in space and keeps count of how far we’ve gone!

**GIVEN**

![](http://i67.tinypic.com/sd1jk7.png)

[codepen](https://codepen.io/hevalhazalkurt/pen/JzZqRE)

### 1.3.3. Strings
But what if we want to work with data that isn’t a number? We can represent other forms of data as a *string*.

Strings are any sequence of characters (letters, spaces, numbers, or symbols). While almost anything can be a string, they are typically used to represent text or speech. Similar to how we represent speech in writing, we surround strings with single (`'...'`) or double quotes (`"..."`).

But why the name strings? Strings are a sequence of symbols, so we can think of each characters being strung together, like beads in a necklace.

So, what can we use strings for?

* To display data that uses text or symbols, like printing our name to the screen.
To add or remove text. Since strings are a linear sequence of characters, we can break strings into even smaller strings, or combine strings to make longer ones.
* To modify characters. For example, we could capitalize the first letter of every word in a string if wanted to turn it into a title.
* To let the computer communicate with us in a “human-readable” way, like displaying the rules of an online game.

Strings may sometimes look similar to other data types. But it’s important to remember that even if a number looks like a number, or a boolean looks like a boolean, it’s good to check that it’s not a string — or else you won’t be able to use it correctly!

Take the following string: `'20'`. The string `'20'` is different from the numerical value of `20`. While they appear to be the same, a computer would see the first as two characters: `'2'` and `'0'`, while the second contains the numerical value of `20`.

##### Instructions

While we can think of strings as chunks of text, it’s also useful to remember that they’re just a collection of individual characters, like letters in a banner.

Type a word into the box and see the result. Notice how each character is separate from the ones around it, but they come together to make a word!

**GIVEN**

![](http://i64.tinypic.com/2im3tb5.png)

[codepen](https://codepen.io/hevalhazalkurt/pen/ZPRNwp)

### 1.3.4. Boolean
This next data type has a special importance to computing. *Boolean values* represent the logical ideas of true and false.

Booleans, unlike numbers or strings, only have two values: `true` and `false`. The term boolean comes from the inventor of a specific form of logic, George Boole. Logic is important to computer science because it is an early attempt at translating the human capacity for reason to computers.

So, what do we use booleans for?

* To determine validity. For example, we want to know whether a meme is viral. If it’s been viewed more than 50 million times in less than a week, we’d say that it’s true that it went viral.
* To make decisions. For example, if I get an email, the program checks that the email is new and it displays at the top of my inbox.
Because booleans act as binary opposites, we can think of them in a myriad of ways, like on and off, yes and no, sometimes even 1 and 0.

While we use the words `true` and `false` to represent boolean values, it’s important to remember that they are different from the strings `'true'` and `'false'`.


##### Instructions
Programmers first were able to illustrate the idea of binary logic through turning on and off electric circuits, where on equaled `true` and off equaled `false`. In fact, the relationship between electricity and logic is the basis for digitization!

Flip the switch to see the scene change from day to night and watch the lights turn on and off. Notice how the variable `LightsOn` stays the same, but its value changes from `true` to `false`.

**GIVEN**

![](http://i64.tinypic.com/8yf7ly.png)

[codepen](https://codepen.io/hevalhazalkurt/pen/OqEePK)

### 1.3.5. Putting it All Together

So far you’ve learned about three different data types:

* numbers
* strings
* booleans

Let’s put your knowledge to work!

In the code editor, we’ve listed three variables, each equal to a different datatype. Try choosing a function and see what it outputs.

##### Instructions
Now, let’s change the values of the variables! Press the run button, then select a function from the dropdown menu and see how it evaluates each value.

* What happens if you change the value, but keep the data type?
* What happens if you swap out the data type?

Any time that you change the code, make sure to run your code again! Otherwise, the computer won’t know that you made a change.


**GIVEN**

```js
myNumber = 150;

myString = 'hello';

myBool = true;
```

![](http://i67.tinypic.com/1z2mvzk.png)

### 1.3.6. Data Types Review

Congrats! Now you know the building blocks of most programming languages and should start to have an idea about the types of simple programs that you could write.

In this lesson, we learned:

* Categorizing information using data types is a way for a computer to distinguish different types of input.
* Primitives are the simplest data types and are shared across many programming languages. They include:
	* Numbers — values that allow us to do calculations and keep count.
	* Strings — a sequence of characters or symbols often used to denote text.
	* Booleans — logical values that represent the idea of true or false.


**GIVEN**

```js
myNumber = 150;

myString = 'hello';

myBool = true;
```
![](http://i67.tinypic.com/1z2mvzk.png)

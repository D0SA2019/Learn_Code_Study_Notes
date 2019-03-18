# Basics of Programming I
## 1.1 Variables


### 1.1.1. Introduction to Variables

In programming, we have a way of storing values so that we can reuse them throughout our program or change them, if necessary. This concept is known as a ***variable***.

Maybe you’re familiar with the math term *variable*, or the word *variability*. Programming variables share qualities with each. Similar to a variable in math, a variable is a way of saving a piece of information with a specific name. By giving a value a name, we can easily reuse that value over and over again in our code. Like the idea of variability, a programming variable allows us to easily change a value throughout our code.

Variables are an important first step in coding because with variables we can start using an important programming tool: repetition. Rather than writing out a piece of data every time we need it, we write it out once and the computer remembers it and can repeat that information back.

In this lesson, we’ll explore why variables are an important part of programming, including:

* Using variables to reuse a value
* Using variables to change a value


##### Instructions
Imagine that you’re building a game using tiles with different patterns, representing different terrains.

The tiles need to be placed in the following order:

First row:

* grass
* rocks
* grass

Second row:

* forest
* rocks
* forest

Third row:

* rocks
* grass
* rocks

In each box, enter the type of terrain that should go in the accompanying tile. Continue until the entire board is filled.

**GIVEN**

[source code](https://s3.amazonaws.com/codecademy-content/programs/code-foundations-path/bop-i/variables/exercise_1/index.html)

![](http://i65.tinypic.com/4he4yh.png)

![](http://i66.tinypic.com/2ic0cno.png)

<iframe height="265" style="width: 100%;" scrolling="no" title="Terrain Pattern with Rock, Forest and Grass" src="//codepen.io/hevalhazalkurt/embed/PLaxzY/?height=265&theme-id=0&default-tab=html,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/hevalhazalkurt/pen/PLaxzY/'>Terrain Pattern with Rock, Forest and Grass</a> by Heval Hazal Kurt
  (<a href='https://codepen.io/hevalhazalkurt'>@hevalhazalkurt</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>


### 1.1.2. Reusing Values in Variables
One reason we use variables is that they allow us to easily *reuse* values in different parts of our code.

When we reuse a value, it will appear in multiple places in our code. Re-typing that value becomes tedious, which leads to errors, and without a variable name, it becomes unclear as to what the value represents. It may also be unclear as to what that value is meant to represent.

Let’s take a look at the following piece of code. Here we have a number that we reuse in order to make some calculations:

```
847595593392818109495
847595593392818109495 * 2
847595593392818109495 / 4
```
Rather than writing the same number over and over again, we can save it to a variable named my_number:

```
my_number = 847595593392818109495
my_number * 2
my_number / 4
```

You may be thinking, “But what if my variable name is longer than the value it stores? What’s the point of a variable?”

When we use a value without assigning it to a variable, that’s known as *hardcoding*. While it’s sometimes faster to initially hardcode values in your program, in the long run you’ll run into trouble — especially if you need to change what those values are.

##### Instructions
The last time we built our game, we repeated ourselves a lot. Instead of writing out the pattern for each tile, let’s save the types of terrain we want to use to a set of variables that we can use across the board.

Replicate the previous design by making each variable equal to one of the following:

* grass
* rocks
* forest

As you enter your choices, what do you notice about the board that changes?

How was this process different from the last exercise? Did variables make this process more efficient?

**GIVEN**

[source code](https://s3.amazonaws.com/codecademy-content/programs/code-foundations-path/bop-i/variables/exercise_2/index.html)

![](http://i65.tinypic.com/t6q742.png)

![](http://i67.tinypic.com/2ihrqle.png)


<iframe height="265" style="width: 100%;" scrolling="no" title="Terrain Pattern with Rock, Forest and Grass 1" src="//codepen.io/hevalhazalkurt/embed/zbayWg/?height=265&theme-id=0&default-tab=js,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/hevalhazalkurt/pen/zbayWg/'>Terrain Pattern with Rock, Forest and Grass 1</a> by Heval Hazal Kurt
  (<a href='https://codepen.io/hevalhazalkurt'>@hevalhazalkurt</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>


### 1.1.3. Changing the Value of a Variable

The strong selling point of using a variable is that we can easily change their value, making our programs flexible.

As we saw in the last exercise, we can save a number to a variable and reuse it throughout a program:

```
my_number = 847595593392818109495
my_number * 2
my_number / 4
```

We could easily switch out the value of my_number, without having to change that number in multiple places in our code.


```
my_number = 1
my_number * 2
my_number / 4
```

We could also change the value of `my_number` part way through our program:


```
my_number = 1
my_number * 2

my_number = 3
my_number / 4
```


##### Instructions
You’d like there to be options for an expansion pack, and that means — more terrains!

Use the drop-down menus to explore the different options for the board and try creating new game designs by swapping out the different terrains.

**GIVEN**

[source code](https://s3.amazonaws.com/codecademy-content/programs/code-foundations-path/bop-i/variables/exercise_3/index.html)

![](http://i68.tinypic.com/k3kmr9.png)

<iframe height="265" style="width: 100%;" scrolling="no" title="Terrain Patterns" src="//codepen.io/hevalhazalkurt/embed/jJKdVo/?height=265&theme-id=0&default-tab=js,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/hevalhazalkurt/pen/jJKdVo/'>Terrain Patterns</a> by Heval Hazal Kurt
  (<a href='https://codepen.io/hevalhazalkurt'>@hevalhazalkurt</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>


### 1.1.4. Putting it All Together



##### Instructions


### 1.1.5. Review - Variables



##### Instructions

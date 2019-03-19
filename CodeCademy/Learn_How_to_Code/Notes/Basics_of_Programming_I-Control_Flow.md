# Basics of Programming III
## 2.3. Control Flow

### 2.3.1. Control Flow

How do computers make decisions? Here are a few examples:

* Web surfing: Open the browser, load the text, load the images.
* Social media: If the user’s profile is private, hide their posts. Otherwise, make them visible.
* Electronic music: Repeat a note four times a measure.
* Shopping: Collect shipping and contact information. Reject a purchase if either is incorrect.

Each of these *programs* is a set of instructions, executed in a certain order. This order, called *control flow*, is just as important as the instructions themselves.

Programmers use *control structures* to alter control flow. Control structures include conditionals — “do these instructions if Z is true”, loops — “do these instructions X many times”, and exceptions — “do instruction set A, but if an error occurs switch to instruction set B”. Programmers use these structures in their code to tell a computer which instructions (or in which order) to execute.

In this lesson you will learn the fundamental concepts of control flow and three essential control structures. By the end of the lesson you should be able to:

* Define control flow
* Explain the difference between conditional, loop, and exception control structures
* Give examples for each


##### Instructions

There are five steps in this program, which loads a basic website. Execute the steps in the correct order by clicking each one.

In what order are the instructions executed?


![](https://media.giphy.com/media/1iwvLM68hI6Wr5wu4a/giphy.gif)

[codepen](https://codepen.io/hevalhazalkurt/pen/qvyzZp)


### 2.3.2. Conditional
*If the user’s profile is private, hide their posts. Otherwise, make them visible.*

Computers can run instructions on their own, leaving us to work on more interesting and creative problems. But computers can’t make decisions on their own. Programmers can give them multiple sets of instructions and describe the right conditions in which to use each set. They can describe a structure like the quoted program above: “if X, then do instruction set 1. Otherwise do instruction set 2.” This structure is called a *conditional* control structure because the computer’s instructions depend on some *condition(s)*.

In our social media example, all the instructions are shown in the diagram, but only some of them will be executed each time. Here they are in text form:

1. Check profile privacy
2. Hide the post
3. Show the post

When is step 2 executed and when is 3 executed? The answer is: it depends. The control flow is 1-2 if the profile is private and 1-3 if the profile is public. The condition is the privacy setting on the profile.

Conditional control structures, or just conditionals, allow programs to do different things in different scenarios. As you can see, they follow a logic similar to how humans think, making it easy to write clear code while still handling complex processes.


##### Instructions

Select “Make Profile Public”, then click through each step of the conditional structure.

Select “Make Profile Private”, then click through each step of the conditional structure.

What’s the control flow for each?

![](https://media.giphy.com/media/LwIUYSMcyTVbpVyLr7/giphy.gif)

![](https://media.giphy.com/media/ywSfnrtp68y9dqPSS5/giphy.gif)


[codepen](https://codepen.io/hevalhazalkurt/pen/MxBNvX)

### 2.3.3. Loop
*Repeat a sound four times a measure.*

Computers are good at repetitive tasks: they exactly follow instructions and perform them quickly. But if the programmer has to write the same instructions for every repetition, they waste time and increase the chances of a mistake.

In our example, instead of literally writing “play a sound, play a sound, play a sound, play a sound”, programmers can use a loop structure. A loop is a sequence of instructions which is specified once but which may be carried out several times in a row. In this case there is one instruction (play a sound) and it should be carried out 4 times.

Loop structures can also specify that the instructions are repeated until a certain condition is met. For example, “Repeat a sound until you are booed off stage”.


##### Instructions

Click the shapes in the diagram to move through each step of the loop structure.

What is the condition or count that must be met to stop looping?


![](https://media.giphy.com/media/8cfGpSfCrqoLBS9uih/giphy.gif)



### 2.3.4. Exception
*Collect shipping and email address. Reject a purchase if either is incorrect.*

Errors, or exceptions, happen all the time in programming. You can’t escape them. But you can handle them gracefully.

In exception handling, two sets of instructions are defined. The first set is executed, and if an exception occurs, the first set is stopped and the second set of instructions is executed.

In this example,

* The first set is “collect shipping address”, “collect email address”
* The second set is “reject the purchase”

If any errors occur in executing the first set — maybe the address is incorrectly formatted, or fake — it is stopped and the the second set is executed.

These statements are useful if you know an exception may occur in a set of instructions but you don’t know in which one, or you expect the same exception might occur in multiple, sequential instructions.


##### Instructions

Set the shipping and contact information, then click through the exception structure.

What happens when you select a fake address and a real email?

What happens when you select a real address and a fake email?

![](https://media.giphy.com/media/4TeA7gXJDn6fuM3olI/giphy.gif)

![](https://media.giphy.com/media/9VaGmpgjKm5BmI1d0l/giphy.gif)


### 2.3.5. Putting It All Together

Let’s recreate the conditional control structure using JavaScript! (The one about social media posts, remember?)

![](https://s3.amazonaws.com/codecademy-content/programs/code-foundations-path/bop-ii/conditional-control-flow-4.png)

The control flow shown above is written as a conditional control structure in **main.js**. It looks something like this:

```js
if (condition) {
  DO SOMETHING
} else {
  DO SOMETHING DIFFERENT
}
```

If the `condition` evaluates to true, the computer will execute the body of that statement. In this case, it’s `DO SOMETHING`.

If the `condition` is false, the computer will execute the body of the `else` statement. In this case, it’s `DO SOMETHING DIFFERENT`.

Let’s adapt this general template to our example:

1. The `condition` is true when the privacy `mode` is set to `'public'`. This is already written for you in **main.js**.
2. You’ll replace `DO SOMETHING` with a JavaScript function: `showDetails()`.
3. You’ll replace `DO SOMETHING DIFFERENT` with another function: `hideDetails()`.

The instructions below will show you how to do this in code!


##### Instructions

Complete the control structure by calling the functions below. If the mode is 'public', call:

```js
showDetails();
```

Else, call :

```js
hideDetails();
```

Run the code and test the website.

If done correctly, the content of the post should be visible when you choose “Make Profile Public” in the dropdown, and the content of the post should be hidden when you choose “Make Profile Private”.


**GIVEN**

```js
if (mode === 'public') {
  // Call a function here to show the post details

} else {
  // Call a function here to hide the post details

}
```


**SOLUTION**

```js
if (mode === 'public') {
  showDetails();

} else {
  hideDetails();
}
```


### 2.3.6. Review
Well done! Control flow is a fundamental concept in programming, and learning the basics will serve you wherever your path leads, regardless of language or domain. In review:

* *Control flow* is the order in which instructions are executed.
* *Control structures* alter control flow in a program. You learned three structures, each suited for a different scenario:
	* *Conditional*: “if some condition is met, then do X. Otherwise, do Y”.
	* *Loop*: “do something Z number of times” or “do something repeatedly until some condition is met”.
	* *Exception*: “do steps A, B, C. If an error occurs, stop, and do steps J, K, L”.

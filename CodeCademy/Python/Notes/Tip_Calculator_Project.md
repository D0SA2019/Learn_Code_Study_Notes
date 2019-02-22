# 1. Python Tip Calculator Project
### The Meal
Now let's apply the concepts from the previous section to a real wordl example.

You've finished easting at a restaurant, and received this bill :

- **Cost of meal** : $44.50
- **Restaurant tax** : 6.75%
- **Tip** : 15%

You'll apply the tip to the overall cost of the meal (including tax).

First, let's declare the variable `meal` and assign it the value `44.50`

```python
# Assign the variable meal the value 44.50 on line 3!

meal = 44.50
```

### The Tax
Good! Now let's create a variable for the tax percentage.

The tax on your receipt is 6.75%. You'll have to divide 6.75 by 100 in order to get the decimal form of the percentage.

Create the variable `tax` and set it equal to the decimal value of 6.75%.

```python
meal = 44.50
tax = 6.75/100
```

### The Tip
Nice work! You received good service, so you'd like to leave a 15% tio on top of the cost of the meal, including tax.

Before we compute the tip for your bill, let's set a variable for the tip. Again we need to get the decimal form of the tip, so we divide 15.0 by 100.

Set the variable tip to decimak value of 15% on line 5.

```python
meal = 44.50
tax = 6.75/100
tip = 15/100
```

### Reassign in a Single Line
Okay! We've got the three variables we need to perform our calculation, and we know some arithmetic operators that can help us out.

We saw Lesson 1 that we can reassign variables. For example, we could say `spam = 7` then later change our minds and say `spam = 3`

On line 7, reassign `meal` to the value itself + itself * tax. And yes you're allowed to reassign a variable in terms of itself.

We're only calculating the cost of meal and tax here. We'll get to the tip soon.

```python
meal = 44.50
tax = 6.75/100
tip = 15/100
meal += meal * tax
```


### The Total
Now that `meal` has the cost of the food plus tax, let's introduce on line 8 a new variable, `total`, equal to the new `meal + meal * tip`.

The code on line 10 formats and prints to the console the value of total with exactly two numbers after the decimal. (We'll learn about string formatting, the concole, and print in Unit 2!)

Assign the variable `total` to the sum of `meal + meal * tip` on line 8. Now you have the total cost of your meal!

```python
meal = 44.50
tax = 6.75/100
tip = 15/100
meal += meal * tax
meal += meal * tip
print(meal)
print("%.2f" % meal)

# Output :
54.6293125
54.63
```

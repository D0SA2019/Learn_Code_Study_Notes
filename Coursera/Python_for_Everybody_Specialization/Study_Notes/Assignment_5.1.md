# Assignment 5.1

Write a program that repeatedly prompts a user for integer numbers until the user enters "done". Once "done" is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

Desired Output :
```
Invalid input
Maximum is 10
Minimum is 2
```
<br>

## My solution

```python
largest = None
smallest = None

while True:
    try:
        num = raw_input("Enter a number: ")
        if num == "done":
            break
        if largest is None:
            largest = int(num)
        if int(num) > largest:
            largest = int(num)
        if smallest is None:
            smallest = int(num)
        if int(num) < smallest:
            smallest = int(num)
    except:
        print("Invalid input")
print("Maximum is", largest)
print("Minimum is", smallest)

# Output
# Invalid input
# Maximum is 10
# Minimum is 2
```

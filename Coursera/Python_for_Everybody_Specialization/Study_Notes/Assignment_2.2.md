# Assignment 2.2
*Course 01 : Getting Started With Python*


2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use **input** to read a string and **float()** to convert the string to an number. Do not worry about error checking or bad user data. 


`Desired Output --> Pay: 96.25`

<br>

## My solution 
  
```python
hrs = input("Enter Hours:")       # Output : Enter Hours:  / User answer : 35
rat = input("Enter Rate:")        # Output : Enter Rate:  / User answer : 2.75
hour = float(hrs)
rate = float(rat)
gross = hour * rate
print("Pay:", gross)              # Output : Pay: 96.25
```

<br>

## Dr. Chuck's solution

```python
xh = input("Enter Hours: ")       # Output : Enter Hours:  / User answer : 35
xr = input("Enter Rate: ")        # Output : Enter Rate:  / User answer : 2.75
xp = float(xh) * float(xr)        # Output : Pay: 96.25
print("Pay:", xp)
```

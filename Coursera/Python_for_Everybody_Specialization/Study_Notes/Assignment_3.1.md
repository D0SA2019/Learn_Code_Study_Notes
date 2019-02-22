# Assignment 3.1

3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75) You should use `input` to read a string and `float()` to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.


`Desired Output --> Pay: 498.75`

<br>

## My solution

```python
hrs = input("Enter Hours:")
rt = input("Enter Rate:")
h = float(hrs)
r = float(rt)
if hrs <= 40 :
  grsl = h * r
  print(grsl)
if hrs > 40 :
  grs2 = (40 * r) + (h - 40) * (r * 1.5)
  print(grs2)
```

## Dr Chuck's solution

```python
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
if fh > 40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else :
    xp = fh * fr
print("Pay:",xp)
```

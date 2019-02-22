# Assignment 6.5
Take the following Python code that stores a string:

`str = 'X-DSPAM-Confidence:0.8475'`

Write code using `find()` and string slicing (see section 6.10) to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.

## My solution
```Python
str = 'X-DSPAM-Confidence:0.8475'
colon = str.find(":")
number = int(colon) + 1
find = str[number:]
print(find)
```

## Dr. Chuck's solution
```Python
str = 'X-DSPAM-Confidence:0.8475'
ipos = str.find(":")
piece = str[ipos+1:]
value = float(piece)
print(value)
```

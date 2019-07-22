# 002 - Python If-Else
## Problem

Given an integer, `n`, perform the following conditional actions:

If `n` is odd, print `Weird`

If `n` is even and in the inclusive range of 2 to 5, print `Not Weird`

If `n` is even and in the inclusive range of 6 to 20, print `Weird`

If `n` is even and greater than 20, print `Not Weird`

#### Input Format
A single line containing a positive integer, `n`.

#### Constraints
1 <= n <= 100

#### Output Format
Print `Weird` if the number is weird; otherwise, print `Not Weird`.

```
Sample Inputs
3
24
```

```
Sample Output
Weird
Not Weird
```

#### Given Code

```python
N = int(input())
```

## Solution 1

```python
N = int(input())
if N % 2 == 0 and 2 < N < 5 :
    print("Not Weird")
elif N % 2 == 0 and 6 < N < 20 :
    print("Weird")
elif N % 2 == 0 and N > 20 :
    print("Not Weird")
else :
    print("Weird")
```



## Solution 2

```python
def odd(num):
    if num % 2 != 0:
        return "Weird"
    else:
        return even(num)

def even(num):
    if 2 <= num <= 5:
        return "Not Weird"
    elif 6 <= num <= 20:
        return "Weird"
    elif num > 20:
        return "Not Weird"

N = int(input())
print(odd(N))
```

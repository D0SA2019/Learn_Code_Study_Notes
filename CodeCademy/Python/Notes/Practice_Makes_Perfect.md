# Practice Makes Perfect


### 1. Practice! Practice Practice!
The best way to get good at anything is a lot of practice. This lesson is full of practice problems for you to work on. Each exercise will contain minimal instructions to help you solve these problems. The goal is to help you take your programming skills and apply them to real life problems.

The more challenging programs will contain some helpful hints to nudge you in the right direction.

##### Instructions

Hit Run to continue.


### 2. is_even
All right! Let's get started.

Remember how an even number is a number that is divisible by 2?


##### Instructions

Define a function `is_even` that will take a number `x` as input.

If `x` is even, then `return True`.

Otherwise, `return False`.


```Python
# SOLUTION
def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False


print(is_even(5))
print(is_even(284))


# OUTPUT
False
True
```

### 3. is_int
An integer is just a number without a decimal part (for instance, `-17`, `0`, and `42` are all integers, but `98.6` is not).

For the purpose of this lesson, we'll also say that a number with a decimal part that is all 0s is also an integer, such as 7.0.

This means that, for this lesson, you can't just test the input to see if it's of type `int`.

If the difference between a number and that same number rounded is greater than zero, what does that say about that particular number?


##### Instructions
Define a function `is_int` that takes a number `x` as an input.

Have it `return True` if the number is an integer (as defined above) and `False` otherwise.

For example:


```Python
is_int(7.0)   # True    
is_int(7.5)   # False    
is_int(-1)    # True
```


```Python
# SOLUTION 1
def is_int(x):
  if x == int(x):
    return True
  else:
    return False


print(is_int(7))
print(is_int(7.0))
print(is_int(7.7))
print(is_int(-7))


# SOLUTION 2
def is_int(x):
  return not bool(x%1)

print(is_int(7))
print(is_int(7.0))
print(is_int(7.7))
print(is_int(-7))


# OUTPUT
True
True
False
True
```

### 4. digit_sum
Awesome! Now let's try something a little trickier. Try summing the digits of a number.


##### Instructions
Write a function called `digit_sum` that takes a positive integer `n` as input and returns the sum of all that number's digits. For example: `digit_sum(1234)` should return `10` which is `1 + 2 + 3 + 4`. (Assume that the number you are given will always be positive.)

Check the hint if you need help!



```Python
# SOLUTION
def digit_sum(x):
    sum = 0
    x = str(x)
    for c in x:
        sum += int(c)
    return sum


print(digit_sum(1234))
print(digit_sum(434))


# OUTPUT
10
11
```

### 5. factorial

All right! Now we're cooking. Let's try a factorial problem.

To calculate the factorial of a non-negative integer `x`, just multiply all the integers from 1 through `x`. For example:

* `factorial(4)` would equal `4 * 3 * 2 * 1`, which is 24.
* `factorial(1)` would equal `1`.
* `factorial(3)` would equal `3 * 2 * 1`, which is 6.



##### Instructions
Define a function `factorial` that takes an integer `x` as input.

Calculate and return the factorial of that number.



```Python
# SOLUTION
def factorial(x):
    mul = 1
    for num in range(1, x + 1):
        mul *= num
    return mul


# OUTPUT
24
6
1
```


### 6. is_prime
A *prime number* is a positive integer greater than 1 that has no positive divisors other than 1 and itself. (That's a mouthful!)

In other words, if you want to test if a number in a variable `x` is prime, then no other number should go into `x` evenly besides 1 and `x`. So `2` and `5` and `11` are all prime, but `4` and `18` and `21` are not.

If there is a number between 1 and `x` that goes in evenly, then `x` is not prime.




##### Instructions
Define a function called `is_prime` that takes a number `x` as input.

For each number `n` from 2 to `x - 1`, test if `x` is evenly divisible by `n`.

If it is, `return False`.

If none of them are, then `return True`.



```Python
# SOLUTION
def is_prime(x):
    if x < 2 :
        return False
    for n in range(2, x-1):
        if x % n == 0:
            return False
    else:
        return True

print(is_prime(5))
print(is_prime(8))
print(is_prime(23))
print(is_prime(205))

primes = []
for num in range(20):
  if is_prime(num):
    primes.append(num)
print(primes)

for num in range(20):
    print(num, "is prime?", is_prime(num))

```

OUTPUT :
```
True
False
True
False
[2, 3, 5, 7, 11, 13, 17, 19]
0 is prime? False
1 is prime? False
2 is prime? True
3 is prime? True
4 is prime? False
5 is prime? True
6 is prime? False
7 is prime? True
8 is prime? False
9 is prime? False
10 is prime? False
11 is prime? True
12 is prime? False
13 is prime? True
14 is prime? False
15 is prime? False
16 is prime? False
17 is prime? True
18 is prime? False
19 is prime? True
```

### 7. reverse
Great work so far! Let's practice writing some functions that work with strings.


##### Instructions

Define a function called `reverse` that takes a string `text` and returns that string in reverse. For example: `reverse("abcd")` should return `"dcba"`.

You may not use `reversed` or `[::-1]` to help you with this.

You may get a string containing special characters (for example, !, @, or #).


```Python
# SOLUTION
# simple version
def reverse_basic(text):
    return text[::-1]

print(reverse_basic("Hello"))


# long version
def reverse(text):
    word = ""
    i = len(text) - 1
    while i >= 0:
        word = word + text[i]
        i -= 1
    return word

print(reverse("Hello World!"))



# OUTPUT
olleH
!dlroW olleH
```

### 8. anti_vowel
Nice work. Next up: vowels!


##### Instructions
Define a function called `anti_vowel` that takes one string, `text`, as input and returns the text with all of the vowels removed.

For example: `anti_vowel("Hey You!")` should return `"Hy Y!"`. Don't count Y as a vowel. Make sure to remove lowercase and uppercase vowels.



```Python
# SOLUTION
vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

def anti_vowel(text):
    for vowel in vowels:
        if vowel in text:
            text = text.replace(vowel, "")
    return text

print(anti_vowel("Hey you!"))
print(anti_vowel("Your weekly writer summary for March 1"))
print(anti_vowel("An app meticulously crafted for people who love to read. It’s the perfect companion for wherever your day takes you."))



# OUTPUT
Hy y!
Yr wkly wrtr smmry fr Mrch 1
n pp mtclsly crftd fr ppl wh lv t rd. t’s th prfct cmpnn fr whrvr yr dy tks y.
```

### 9. scrabble_score

Scrabble is a game where players get points by spelling words. Words are scored by adding together the point values of each individual letter (we'll leave out the double and triple letter and word scores for now).

To the right is a dictionary containing all of the letters in the alphabet with their corresponding Scrabble point values.

For example: the word `"Helix"` would score `15` points due to the sum of the letters: `4 + 1 + 1 + 1 + 8`.


##### Instructions
Define a function `scrabble_score` that takes a string `word` as input and returns the equivalent scrabble score for that word.

* Assume your input is only one word containing no spaces or punctuation.
* As mentioned, no need to worry about score multipliers!
* Your function should work even if the letters you get are uppercase, lowercase, or a mix.
* Assume that you're only given non-empty strings.



```Python
# GIVEN
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


# SOLUTION by adding
def scrabble_score(word):
    index = 0
    word_score = 0
    word = word.lower()
    while index < len(word):
        word_score += score[word[index]]
        index += 1
    return word_score

print(scrabble_score("Hello"))
print(scrabble_score("HevalHazalKurt"))


# OUTPUT
8
36
```

### 10. censor
You're doing great with these string function challenges. Last one!


##### Instructions
Write a function called `censor` that takes two strings, `text` and `word`, as input. It should return the `text` with the `word` you chose replaced with asterisks. For example:

```python
censor("this hack is wack hack", "hack") ```

should return:

```py
"this **** is wack ****"
```

* Assume your input strings won't contain punctuation or upper case letters.
* The number of asterisks you put should correspond to the number of letters in the censored word.

```Python
# SOLUTION 1
def cencor(text, word):
    if word in text:
        text = text.replace(word, "****")
    return text

print(cencor("this hack is wack hack", "hack"))


# SOLUTION 2
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result

print(censor("this hack is wack hack", "hack"))


# OUTPUT
this **** is wack ****
this **** is wack ****
```

### 11. count
Great work so far. Let's finish up by practicing with a few functions that take lists as arguments.


##### Instructions
Define a function called `count` that has two arguments called `sequence` and `item`.

Return the number of times the item occurs in the list.

For example: `count([1, 2, 1, 1], 1)` should return `3` (because `1` appears `3` times in the list).

* There is a list method in Python that you can use for this, but you should do it the long way for practice.
* Your function should return an integer.
* The item you input may be an integer, string, float, or even another list!
* Be careful not to use `list` as a variable name in your code—it's a reserved word in Python!



```Python
# SOLUTION
def count(sequence, item):
    total = 0
    for i in sequence:
        if i == item:
            total += 1
        else:
            continue
    return total

print(count([1, 2, 1, 1], 1))
print(count([1],7))



# OUTPUT
3
0
```

### 12. purify
Awesome! Now let's practice filtering a list.


##### Instructions
Define a function called `purify` that takes in a list of numbers, removes all odd numbers in the list, and `return`s the result. For example, `purify([1,2,3])` should return `[2]`.

Do not directly modify the list you are given as input; instead, return a new list with only the even numbers.



```Python
# SOLUTION
def purify(numbers):
    odds = []
    for num in numbers:
        if num % 2 == 0:
            odds.append(num)
        else:
            continue
    return odds

print(purify([1,2,3]))
print(purify([4,6,11,24,23]))



# OUTPUT
[2]
[4, 6, 24]
```

### 13. product
Great! Now let's try a little multiplication.


##### Instructions
Define a function called `product` that takes a list of integers as input and returns the product of all of the elements in the list. For example: `product([4, 5, 5])` should return `100` (because `4 * 5 * 5` is `100`).

* Don't worry about the list being empty.
* Your function should return an integer



```Python
# SOLUTION
def product(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

print(product([4, 5, 5]))



# OUTPUT
100
```

### 14. remove_duplicates

Awesome! Now for something a bit trickier.

##### Instructions
Write a function `remove_duplicates` that takes in a list and removes elements of the list that are the same.

For example: `remove_duplicates([1, 1, 2, 2])` should return `[1, 2]`.

* Don't remove every occurrence, since you need to keep a single occurrence of a number.
* The order in which you present your output does not matter. So returning [1, 2, 3] is the same as returning [3, 1, 2].
* Do not modify the list you take as input! Instead, return a new list.



```Python
# SOLUTION
def remove_duplicates(numbers):
    uniques = []
    for num in numbers:
        if num in uniques:
            continue
        else:
            uniques.append(num)
    return uniques

print(remove_duplicates([1, 1, 2, 2]))


# OUTPUT
[1, 2]
```

### 15. median
Great work! You've covered a lot in these exercises. Last but not least, let's write a function to find the median of a list.

The *median* is the middle number in a sorted sequence of numbers.

Finding the median of `[7, 12, 3, 1, 6]` would first consist of sorting the sequence into `[1, 3, 6, 7, 12]` and then locating the middle value, which would be `6`.

If you are given a sequence with an even number of elements, you must average the two elements surrounding the middle.

For example, the median of the sequence `[7, 3, 1, 4]` is `3.5`, since the middle elements after sorting the list are `3` and `4` and `(3 + 4) / (2.0)` is `3.5`.

You can sort the sequence using the `sorted()` function, like so:

```Python
sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]
```

##### Instructions

Write a function called `median` that takes a list as an input and returns the median value of the list. For example: `median([1, 1, 2])` should return `1`.

* The list can be of any size and the numbers are not guaranteed to be in any particular order. Make sure to sort it!
* If the list contains an even number of elements, your function should return the average of the middle two.


```Python
# SOLUTION
def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean

print(median([2, 4, 5, 9]))
```

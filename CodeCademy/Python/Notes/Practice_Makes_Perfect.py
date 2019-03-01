print("")
print("------ Practice Makes Perfect ------")

print("")
print("------ 2. is_even ------")
def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False


print(is_even(5))
print(is_even(284))




print("")
print("------ 3. is_int ------")
def is_int(x):
  if x == int(x):
    return True
  else:
    return False


print(is_int(7))
print(is_int(7.0))
print(is_int(7.7))
print(is_int(-7))

print("")

def is_int(x):
  return not bool(x%1)

print(is_int(7))
print(is_int(7.0))
print(is_int(7.7))
print(is_int(-7))




print("")
print("------ 4. digit_sum ------")
def digit_sum(x):
    sum = 0
    x = str(x)
    for c in x:
        sum += int(c)
    return sum


print(digit_sum(1234))
print(digit_sum(434))




print("")
print("------ 5. factorial ------")
def factorial(x):
    mul = 1
    for num in range(1, x + 1):
        mul *= num
    return mul

print(factorial(4))
print(factorial(3))
print(factorial(1))




print("")
print("------ 6. is_prime ------")
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




print("")
print("------ 7. reverse ------")
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




print("")
print("------ 8. anti_vowel ------")

vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

def anti_vowel(text):
    for vowel in vowels:
        if vowel in text:
            text = text.replace(vowel, "")
    return text

print(anti_vowel("Hey you!"))
print(anti_vowel("Your weekly writer summary for March 1"))
print(anti_vowel("An app meticulously crafted for people who love to read. It’s the perfect companion for wherever your day takes you."))




print("")
print("------ 9. scrabble_score ------")

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

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




print("")
print("------ 10. censor ------")

def cencor(text, word):
    if word in text:
        text = text.replace(word, "****")
    return text

print(cencor("this hack is wack hack", "hack"))


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




print("")
print("------ 11. count ------")
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




print("")
print("------ 12. purify ------")

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




print("")
print("------ 13. product ------")

def product(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

print(product([4, 5, 5]))




print("")
print("------ 14. remove_duplicates ------")
def remove_duplicates(numbers):
    uniques = []
    for num in numbers:
        if num in uniques:
            continue
        else:
            uniques.append(num)
    return uniques

print(remove_duplicates([1, 1, 2, 2]))




print("")
print("------ 15. median ------")

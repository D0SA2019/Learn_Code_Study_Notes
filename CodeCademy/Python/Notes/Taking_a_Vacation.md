# Taking a Vacation
### 1. Before We Begin
Let's first quickly review functions in Python.

```python
def bigger(first, second):
  print(max(first, second))
  return True

bigger(37,29)

# Output : 37
```

In the example above:

1. We define a function called `bigger` that has two arguments called `first` and `second`.
2. Then, we print out the larger of the two arguments using the built-in function `max`.
3. Finally, the `bigger` function returns `True`.

Now try creating a function yourself!

##### Instructions
Write a function called `answer` that takes no arguments and returns the value `42`.

Even without arguments, you will still need parentheses.Don't forget the colon at the end of the function definition!


```Python
# SOLUTION
def answer():
  return 42
```



### 2.Planning Your Trip
When planning a vacation, it's very important to know exactly how much you're going to spend.

```python
def wages(hours):
  # If I make $8.35/hour...
  return 8.35 * hours

print(wages(65))

# Output : 542.75
```
The above example is just a refresher in how functions are defined.

Let's use functions to calculate your trip's costs.

##### Instructions
Define a function called `hotel_cost` with one argument `nights` as input.

The hotel costs $140 per night. So, the function `hotel_cos`t should `return 140 * nights`.

```Python
# SOLUTION
def hotel_cost(nights):
  return 140 * nights
```



### 3. Getting There
You're going to need to take a plane ride to get to your location.

```python
def fruit_color(fruit):
  if fruit == "apple":
    return "red"
  elif fruit == "banana":
    return "yellow"
  elif fruit == "pear":
    return "green"
```

1. The example above defines the function `fruit_color` that accepts a string as the argument `fruit`.
2. The function returns a string if it knows the color of that `fruit`.

##### Instructions
Below your existing code, define a function called `plane_ride_cost` that takes a string, `city`, as input.

The function should `return` a different price depending on the location, similar to the code example above. Below are the valid destinations and their corresponding round-trip prices.

* `"Charlotte": 183`
* `"Tampa": 220`
* `"Pittsburgh": 222`
* `"Los Angeles": 475`

```Python
# GIVEN
def hotel_cost(nights):
  return 140 * nights


# SOLUTION
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
```



### 4. Transportation
You're also going to need a rental car in order for you to get around.

```python
def finish_game(score):
  tickets = 10 * score
  if score >= 10:
    tickets += 50
  elif score >= 7:
    tickets += 20
  return tickets
```
In the above example, we first give the player 10 tickets for every point that the player scored. Then, we check the value of `score` multiple times.

1. First, we check if `score` is greater than or equal to 10. If it is, we give the player 50 bonus tickets.
2. If `score` is just greater than or equal to 7, we give the player 20 bonus tickets.
3. At the end, we return the total number of tickets earned by the player.

Remember that an elif statement is only checked if all preceding `if/elif` statements fail.


##### Instructions
Below your existing code, define a function called `rental_car_cost` with an argument called `days`.

Calculate the cost of renting the car:

1. Every day you rent the car costs $40.
2. `if` you rent the car for 7 or more days, you get $50 off your total.
3. Alternatively (`elif`), if you rent the car for 3 or more days, you get $20 off your total.
3. You cannot get both of the above discounts.

Return that cost.

Just like in the example above, this check becomes simpler if you make the 7-day check an `if` statement and the 3-day check an `elif` statement.

```Python
# GIVEN
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475


# SOLUTION
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  if days >= 7 :
    return 40 * days - 50
  elif days >= 3 and days < 7:
    return 40 * days - 20
  else :
    return 40 * days
```


### 5. Pull it Together
Great! Now that you've got your 3 main costs figured out, let's put them together in order to find the total cost of your trip.

```python
def double(n):
  return 2 * n

def triple(p):
  return 3 * p

def add(a, b):
  return double(a) + triple(b)
```
1. We define two simple functions, `double(n)` and `triple(p)` that return 2 times or 3 times their input. Notice that they have `n` and `p` as their arguments

2. We define a third function, `add(a, b)` that returns the sum of the previous two functions when called with `a` and `b`, respectively. Notice that even though the names of the parameters for `add(a, b)` are different than the names of the parameters for `double(n)` and `triple(p)` we can still pass them into those functions as arguments


##### Instructions
Below your existing code, define a function called `trip_c`ost that takes two parameters, `city` and `days` and returns the sum of calling the `rental_car_cost(days)`, `hotel_cost(days - 1)`, and `plane_ride_cost(city)` functions.

Notice that we changed the argument of `hotel_costs()` from `nights` to `days - 1`. Since we want `trip-cost` to only depend on two parameters, we have to convert the variable nights into days. If you are going to be staying somewhere, the number of nights you stay there is one less than the number of days you were there (imagine a weekend trip to visit family, you leave Saturday and return Sunday, so you visit for two days, but only stay for one night).

```Python
# GIVEN
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  if days >= 7 :
    return 40 * days - 50
  elif days >= 3 and days < 7:
    return 40 * days - 20
  else :
    return 40 * days

# SOLUTION
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  if days >= 7 :
    return 40 * days - 50
  elif days >= 3 and days < 7:
    return 40 * days - 20
  else :
    return 40 * days

def trip_cost(city,days):
  return rental_car_cost(days) + hotel_cost(days-1) + plane_ride_cost(city)
```

### 6. Hey, You Never Know!
You can't expect to only spend money on the plane ride, hotel, and rental car when going on a vacation. There also needs to be room for additional costs like fancy food or souvenirs.


##### Instructions
Modify your `trip_cost` function definition. Add a third argument, `spending_money`.

Modify what the `trip_cost` function does. Add the variable `spending_money` to the sum that it returns.

```Python
# SOLUTION
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  if days >= 7 :
    return 40 * days - 50
  elif days >= 3 and days < 7:
    return 40 * days - 20
  else :
    return 40 * days

def trip_cost(city,days,spending_money):
  return rental_car_cost(days) + hotel_cost(days-1) + plane_ride_cost(city) + spending_money
```


### 7. Plan Your Trip!
Nice work! Now that you have it all together, let's take a trip.

What if we went to Los Angeles for 5 days and brought an extra 600 dollars of spending money?

##### Instructions
After your previous code, `print` out the `trip_cost`( to `"Los Angeles"` for `5` days with an extra `600` dollars of spending money.

Don't forget the closing `)` after passing in the 3 previous values!

```Python
# SOLUTION
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  if days >= 7 :
    return 40 * days - 50
  elif days >= 3 and days < 7:
    return 40 * days - 20
  else :
    return 40 * days

def trip_cost(city,days,spending_money):
  return rental_car_cost(days) + hotel_cost(days-1) + plane_ride_cost(city) + spending_money

print(trip_cost("Los Angeles",5,600))


# Output : 1815
```

print("")
print("------ 1 : Hello World ------")
# From notes :
print("Hello, world!")
print("Water—there is not a drop of water there! Were Niagara but a cataract of sand, would you travel your thousand miles to see it?")

# Exercise :
print("Hi there!")
print("")


print("")
print("------ 2 : Print Statements ------")
# From notes :
print("Hello World!")
print("Deep into distant woodlands winds a mazy way, reaching to overlapping spurs of mountains bathed in their hill-side blue.")

# Exercise :
print("Hi there!")
print("")


print("")
print("------ 3 : Strings ------")
# From notes :
print("This is a good string")
print('You can use single quotes or double quotes for a string')
print("This is " + "a good string")

# Exercise :
print("Hello " + "Heval")

print("")
print("------ 4 : Handling Errors ------")
print("How do you make a hot dog stand?")
print("You take away its chair!")


print("")
print("------ 5 : Variables ------")
todays_date = "17 December 2018"
print(todays_date)


print("")
print("------ 6 : Arithmetic ------")
mirthful_addition = 12381 + 91817
amazing_subtraction = 981 - 312
trippy_multiplication = 38 * 902
happy_division = 540 / 45
sassy_combinations = 129 * 1345 + 120 / 6 - 12

product = 2 * 6
remainder = 1398 % 11

print(mirthful_addition)
print(amazing_subtraction)
print(trippy_multiplication)
print(happy_division)
print(sassy_combinations)
print(product)
print(remainder)


print("")
print("------ 7 : Updating Variables ------")
fish_in_clarks_pond = 50
print("Before we have 0 fish." )
print("Catching fish")

number_of_fish_caught = 10
fish_in_clarks_pond = fish_in_clarks_pond - number_of_fish_caught

print("Now we have", fish_in_clarks_pond, "fish." )
print("")

money_in_wallet = 40
sandwich_price = 7.50
sales_tax = .08 * sandwich_price
print("We have", money_in_wallet, "$ in the wallet." )
print("The sandwich is",sandwich_price, "$ without tax." )
sandwich_price += sales_tax
money_in_wallet -= sandwich_price
print("After the tax the sandwich will be",sandwich_price, "$ and there will be", money_in_wallet, "$ in my wallet." )

print("")
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06
september_to_december_rainfall = september_rainfall + october_rainfall + november_rainfall + december_rainfall

annual_rainfall += september_to_december_rainfall
print(annual_rainfall)


print("")
print("------ 8 : Comments ------")
city_name = "St. Potatosburg"
# The city population
city_pop = 340000
print("Check the code to see comments!")


print("")
print("------ 9 : Numbers ------")
# this evaluates to 150:
float4 = 1.5e2
print(float4)

print("")
cucumbers = 5
price_per_cucumber = 3.25
total_cost = cucumbers * price_per_cucumber
print(total_cost)


print("")
print("------ 10 : Two Types of Division ------")
quotient1 = 6/2
quotient2 = 7/2
print(quotient1)
print(quotient2)

print("")
cucumbers = 100
num_people = 6
whole_cucumbers_per_person = cucumbers / num_people
print(whole_cucumbers_per_person)



print("")
print("------ 11 : Multi-line Strings ------")
address_string = """136 Whowho Rd
Apt 7
Whosville, WZ 44494"""
print(address_string)

print("")
string1 = """The following piece of code does the following steps:
takes in some input
does An Important Calculation
returns the modified input and a string that says "Success!" or "Failure..."
"""
print(string1)

print("")
haiku = """The old pond,
A frog jumps in:
Plop!"""
print(haiku)



print("")
print("------ 12 : Booleans ------")
a = True
b = False
print(a, b)

print("")
age_is_12 = False
name_is_maria = True

print(age_is_12, name_is_maria)




print("")
print("------ 13 : ValueError ------")
age = 13
print("I am " + str(age) + " years old!")

print("")
number1 = "100"
number2 = "10"

string_addition = number1 + number2
int_addition = int(number1) + int(number2)
print(string_addition)
print(int_addition)

print("")
string_num = "7.5"
print(float(string_num))

print("")
float_1 = 0.25
float_2 = 40.0

product = float_1 * float_2
big_string = "The product was " + str(product)
print(big_string)



print("")
print("------ 14 : Review ------")
skill_completed = "Python Syntax"
exercises_completed = 13
# The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5
point_total = 100
point_total += exercises_completed*points_per_exercise

print("I got "+str(point_total)+" points!")

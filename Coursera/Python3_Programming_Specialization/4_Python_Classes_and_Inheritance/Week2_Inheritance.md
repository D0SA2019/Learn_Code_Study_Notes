# Python Classes and Inheritance
*Coursera | Python 3 Programming Specialization | Course 4*

## Week 2 : Inheritance

#### 2.1. Introduction: Class Inheritance

Classes can “inherit” methods and class variables from other classes. We’ll see the mechanics of how this works in subsequent sections. First, however, let’s motivate why this might be valuable. It turns out that inheritance doesn’t let you do anything that you couldn’t do without it, but it makes some things a lot more elegant. You will also find it’s useful when someone else has defined a class in a module or library, and you just want to override a few things without having to reimplement everything they’ve done.

Consider our Tamagotchi game. Suppose we wanted to make some different kinds of pets that have the same structure as other pets, but have some different attributes or behave a little differently. For example, suppose that dog pets should show their emotional state a little differently than cats or act differently when they are hungry or when they are asked to fetch something.

You could implement this by making instance variable for the pet type and dispatching on that instance variable in various methods.

```python
from random import randrange

class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty", pet_type="dog"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class
        self.pet_type = pet_type

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            if self.pet_type == "dog": # if the pet is a dog, it will express its mood in different ways from a cat or any other type of animal
                return "happy"
            elif self.pet_type == "cat":
                return "happy, probably"
            else:
                return "HAPPY"
        elif self.hunger > self.hunger_threshold:
            if self.pet_type == "dog": # same for hunger -- dogs and cats will express their hunger a little bit differently in this version of the class definition
                return "hungry, arf"
            elif self.pet_type == "cat":
                return "hungry, meeeeow"
            else:
                return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)
```

**That code is exactly the same as the code defining the `Pet` class that you saw in the Tamagotchi section, except that we’ve added a few things.**
* A new input to the constructor – the `pet_type` input parameter, which defaults to `"dog"`, and the `self.pet_type` instance variable.
* if..elif..else in the `self.mood()` method, such that different types of pets (a dog, a cat, or any other type of animal) express their moods and their hunger in slightly different ways.

But that’s not an elegant way to do it. It obscures the parts of being a pet that are common to all pets and it buries the unique stuff about being a dog or a cat in the middle of the mood method. What if you also wanted a dog to reduce boredom at a different rate than a cat, and you wanted a bird pet to be different still? Here, we’ve only implemented **dogs**, **cats**, and **other** – but you can imagine the possibilities.

If there were lots of different types of pets, those methods would start to have long and complex if..elif..elif code clauses, which can be confusing. And you’d need that in every method where the behavior was different for different types of pets. Class inheritance will give us a more elegant way to do it.

-------
--------

#### 2.2. Inheriting Variables and Methods

We said that inheritance provides us a more elegant way of, for example, creating `Dog` and `Cat` types, rather than making a very complex `Pet` class. In the abstract, this is pretty intuitive: all pets have certain things, but dogs are different from cats, which are different from birds. Going a step further, a Collie dog is different from a Labrador dog, for example. Inheritance provides us with an easy and elegant way to represent these differences.

Basically, it works by defining a new class, and using a special syntax to show what the new sub-class **inherits from** a super-class. So if you wanted to define a `Dog` class as a special kind of `Pet`, you would say that the `Dog` type inherits from the `Pet` type. In the definition of the inherited class, you only need to specify the methods and instance variables that are different from the parent class (the **parent class**, or the **superclass**, is what we may call the class that is *inherited from*. In the example we’re discussing, `Pet` would be the superclass of `Dog` or `Cat`).

Here is an example. Say we want to define a class `Cat` that inherits from `Pet`. Assume we have the Pet class that we defined earlier.

We want the `Cat` type to be exactly the same as `Pet`, except we want the sound cats to start out knowing “meow” instead of “mrrp”, and we want the `Cat` class to have its own special method called `chasing_rats`, which only `Cat` s have.

For reference, here’s the original Tamagotchi code

```python
from random import randrange

# Here's the original Pet class
class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

# Here's the new definition of class Cat, a subclass of Pet.
class Cat(Pet): # the class name that the new class inherits from goes in the parentheses, like so.
    sounds = ['Meow']

    def chasing_rats(self):
        return "What are you doing, Pinky? Taking over the world?!"

branson = Cat("Branson")
print(branson)
print(branson.chasing_rats())
print(branson.hunger)
branson.feed()
print(branson.hunger)
print(branson.sounds)
branson.hi()
```

**Output** :

```
I'm Branson.  I feel happy.
What are you doing, Pinky? Taking over the world?!
7
1
['Meow']
Meow
```

All we need is the few extra lines at the bottom of our code! The elegance of inheritance allows us to specify just the differences in the new, inherited class. In that extra code, we make sure the `Cat` class inherits from the `Pet` class. We do that by putting the word Pet in parentheses, `class Cat(Pet)`:. In the definition of the class `Cat`, we only need to define the things that are different from the ones in the `Pet` class.

In this case, the only difference is that the class variable `sounds` starts out with the string `"Meow"` instead of the string `"mrrp"`, and there is a new method `chasing_rats`.

We can still use all the `Pet` methods in the `Cat` class, this way. You can call the` __str__` method on an instance of `Cat` to `print` an instance of `Cat`, the same way you could call it on an instance of `Pet`, and the same is true for the `hi` method – it’s the same for instances of `Cat` and `Pet`. But the `chasing_rats` method is special: it’s only usable on `Cat` instances, because `Cat` is a subclass of `Pet` which has that additional method.

In the original Tamagotchi game in the last chapter, you saw code that created instances of the `Pet` class. Now let’s write a little bit of code that uses instances of the `Pet` class AND instances of the `Cat` class.


```python
p1 = Pet("Fido")
print(p1)

p1.feed()
p1.hi()
print(p1)

print("")

cat1 = Cat("Fluffy")
print(cat1)

cat1.feed()
cat1.hi()
print(cat1)
print(cat1.chasing_rats())
```

**Output** :

```
I'm Fido.  I feel happy.
Mrrp
I'm Fido.  I feel happy.


I'm Fluffy.  I feel happy.
Meow
I'm Fluffy.  I feel happy.
What are you doing, Pinky? Taking over the world?!
```

And you can continue the inheritance tree. We inherited `Cat` from `Pet`. Now say we want a subclass of `Cat` called `Cheshire`. A Cheshire cat should inherit everything from `Cat`, which means it inherits everything that `Cat` inherits from `Pet`, too. But the `Cheshire` class has its own special method, `smile`.


```python
class Cheshire(Cat):
    def smile(self):
        print(":D :D :D")

cat1 = Cat("Fluffy")
cat1.feed()
cat1.hi()
print(cat1)
print(cat1.chasing_rats())

print("")
print("")


new_cat = Cheshire("Pumpkin")
new_cat.hi()
new_cat.chasing_rats()
new_cat.smile()

print("")
print("")

p1 = Pet("Teddy")
p1.hi()
```

**Output** :

```
Meow
I'm Fluffy.  I feel happy.
What are you doing, Pinky? Taking over the world?!


Meow
:D :D :D


Mrrp
```


#### How the interpreter looks up attributes

So what is happening in the Python interpreter when you write programs with classes, subclasses, and instances of both parent classes and subclasses?

**This is how the interpreter looks up attributes:**

1. First, it checks for an instance variable or an instance method by the name it’s looking for.
2. If an instance variable or method by that name is not found, it checks for a class variable. (See the previous chapter for an explanation of the difference between *instance variables* and *class variables*.)
3. If no class variable is found, it looks for a class variable in the parent class.
4. If no class variable is found _there_, the interpreter looks for a class variable in THAT class’s parent, if it exists – the “grandparent” class.
5. This process goes on until the last ancestor is reached, at which point Python will signal an error.

Let’s look at this with respect to some code.

Say you write the lines:

```python
new_cat = Cheshire("Pumpkin")
print(new_cat.name)
```

**Output** :

```
Pumpkin
```

In the second line, after the instance is created, Python looks for the instance variable `name` in the `new_cat` instance. In this case, it exists. The name on this instance of `Cheshire` is `Pumpkin`. There you go!

When the following lines of code are written and executed:

```python
cat1 = Cat("Sepia")
cat1.hi()
```

**Output** :

```
Meow
```

The Python interpreter looks for `hi` in the instance of `Cat`. It does not find it, because there’s no statement of the form `cat1.hi = ....` (Be careful here – if you had set an instance variable on Cat called hi it would be a bad idea, because you would not be able to use the **method** that it inherited anymore. We’ll see more about this later.)

Then it looks for hi as a class variable (or method) in the class `Cat`, and still doesn’t find it.

Next, it looks for a class variable `hi` on the parent class of `Cat`, `Pet`. It finds that – there’s a method called hi on the class `Pet`. Because of the `()` after `hi`, the method is invoked. All is well.

However, for the following, it won’t go so well


```python
p1 = Pet("Teddy")
p1.chasing_rats()
```

The Python interpreter looks for an instance variable or method called `chasing_rats` on the `Pet` class. It doesn’t exist. `Pet` has no parent classes, so Python signals an error.

-------
--------

**Check your understanding**

**Q1** : After you run the code, `new_cat = Cheshire("Pumpkin")`, how many instance variables exist for the new_cat instance of Cheshire?

A. 1 <br>
B. 2 <br>
C. 3 <br>
D. 4 ✅ <br>

*Explanation : Neither `Cheshire` nor Cat `defines` an `__init__` constructor method, so the grandaprent class, `Pet`, will have it's `__init__` method called. That constructor method sets the instance variables name, hunger, boredom, and sounds.*

----

**Q2** : What would print after running the following code:

```python
new_cat = Cheshire("Pumpkin")
class Siamese(Cat):
  def song(self):
    print("We are Siamese if you please. We are Siamese if you don’t please.")
another_cat = Siamese("Lady")
another_cat.song()
```

A. We are Siamese if you please. We are Siamese if you don’t please.  ✅ <br>
B. Error  <br>
C. Pumpkin  <br>
D. Nothing. There’s no print statement.  <br>


----

**Q3** : What would print after running the following code:

```python
new_cat = Cheshire("Pumpkin")
class Siamese(Cat):
  def song(self):
    print("We are Siamese if you please. We are Siamese if you don’t please.")
another_cat = Siamese("Lady")
new_cat.song()
```


A. We are Siamese if you please. We are Siamese if you don’t please. <br>
B. Error ✅ <br>
C. Pumpkin <br>
D. Nothing. There’s no print statement. <br>


---------

#### 2.3. Overriding Methods

If a method is defined for a class, and also defined for its parent class, the subclass’ method is called and not the parent’s. This follows from the rules for looking up attributes that you saw in the previous section.

We can use the same idea to understand overriding methods.

Let’s return to our idea of making Cats, Dogs, and other pets generate a string for their “mood” differently.

Here’s the original Pet class again.

```python
from random import randrange

# Here's the original Pet class
class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)
```

Now let’s make two subclasses, Dog and Cat. Dogs are always happy unless they are bored and hungry. Cats, on the other hand, are happy only if they are fed and if their boredom level is in a narrow range and, even then, only with probability 1/2.


```python
class Cat(Pet):
    sounds = ["Meow"]

    def mood(self):
        if self.hunger > self.hunger_threshold:
            return "hungry"
        if self.boredom < 2:
            return "grumpy; leave me alone"
        elif self.boredom > self.boredom_threshold:
            return "bored"
        elif randrange(2) == 0:
            return "randomly annoyed"
        else:
            return "happy"

class Dog(Pet):
    sounds = ["Woof", "Ruff"]

    def mood(self):
        if (self.hunger > self.hunger_threshold) and (self.boredom > self.boredom_threshold):
            return "bored and hungry"
        else:
            return "happy"


c1 = Cat("Fluffy")
d1 = Dog("Astro")

c1.boredom = 1
print(c1.mood())

c1.boredom = 3
for i in range(10):
    print(c1.mood())
print(d1.mood())
```

**Output** :

```
grumpy; leave me alone
happy
happy
randomly annoyed
happy
happy
randomly annoyed
randomly annoyed
randomly annoyed
happy
happy
happy
```


-------
--------


#### 2.4. Invoking the Parent Class's Method

Sometimes the parent class has a useful method, but you just need to execute a little extra code when running the subclass’s method. You can override the parent class’s method in the subclass’s method with the same name, but also invoke the parent class’s method. Here’s how.

Say you wanted the `Dog` subclass of `Pet` to say “Arf! Thanks!” when the `feed` method is called, as well as executing the code in the original method.

Here’s the original `Pet` class again.


```python
from random import randrange

# Here's the original Pet class
class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)
```

And here’s a subclass that overrides `feed()` by invoking the the parent class’s `feed()` method; it then also executes an extra line of code. Note the somewhat inelegant way of invoking the parent class’ method. We explicitly refer to `Pet.feed` to get the method/function object. We invoke it with parentheses. However, since we are not invoking the method the normal way, with `<obj>.methodname`, we have to explicitly pass an instance as the first parameter. In this case, the variable self in `Dog.feed()` will be bound to an instance of `Dog`, and so we can just pass self: `Pet.feed(self)`.

```python
from random import randrange

class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def feed(self):
        Pet.feed(self)
        print("Arf! Thanks!")

d1 = Dog("Astro")

d1.feed()
```

**Output** :

```
Arf! Thanks!
```

**Note** : There’s a better way to invoke a superclass’s method. In that alternative method, we would call `super().feed()`. This is nice because it’s easier to read, and also because it puts the specification of the class that Dog inherits from in just one place, `class Dog(Pet)`. Elsewhere, you just refer to `super()` and python takes care of looking up that the parent (super) class of `Dog` is `Pet`.


This technique is very often used with the `__init__` method for a subclass. Suppose that some extra instance variables are defined for the subclass. When you invoke the constructor, you pass all the regular parameters for the parent class, plus the extra ones for the subclass. The subclass’ `__init__` method then stores the extra parameters in instance variables and calls the parent class’ `__init__` method to store the common parameters in instance variables and do any other initialization that it normally does.

Let’s say we want to create a subclass of `Pet`, called `Bird`, and we want it to take an extra parameter, `chirp_number`, with a default value of 2, and have an extra instance variable, `self.chirp_number`. Then, we’ll use this in the `hi` method to make more than one sound.


```python
class Bird(Pet):
    sounds = ["chirp"]
    def __init__(self, name="Kitty", chirp_number=2):
        Pet.__init__(self, name)
        self.chirp_number = chirp_number

    def hi(self):
        for i in range(self.chirp_number):
            print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

b1 = Bird("tweety", 5)
b1.teach("Polly wanna cracker")
b1.hi()
```

**Output** :

```
chirp
Polly wanna cracker
Polly wanna cracker
Polly wanna cracker
Polly wanna cracker
```

-------
--------

**Check your understanding**

**Q1** : What will print when `print(b1.sounds)` is run?

A. 5 <br>
B. ["Mrrp"] <br>
C. ["chirp"] ✅  <br>
D. Error <br>

----

**Q2** : For the Dog class defined in the earlier activecode window, what would happen when `d1.feed()` is run if the `Pet.feed(self)` line was deleted?

A. Error when invoked <br>
B. The string would not print out but d1 would have its hunger reduced. <br>
C. The string would print but d1 would not have its hunger reduced. ✅ <br>
D. Nothing would be different. It is the same as the current code. <br>


------
-------


#### 2.5. Tamagotchi Revisited

Using what we know about class inheritance, we can make a new version of the Tamagotchi game, where you can adopt different types of pets that are slightly different from one another.

And now we can play the Tamagotchi game with some small changes, such that we can adopt different types of pets.



```python
import sys
sys.setExecutionLimit(60000)
from random import randrange

class Pet(object):
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.update_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.update_boredom()

    def feed(self):
        self.update_hunger()

    def update_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def update_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

class Cat(Pet):
    sounds = ['Meow']

    def mood(self):
        if self.hunger > self.hunger_threshold:
            return "hungry"
        if self.boredom <2:
            return "grumpy; leave me alone"
        elif self.boredom > self.boredom_threshold:
            return "bored"
        elif randrange(2) == 0:
            return "randomly annoyed"
        else:
            return "happy"

class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def mood(self):
        if (self.hunger > self.hunger_threshold) and (self.boredom > self.boredom_threshold):
            return "bored and hungry"
        else:
            return "happy"

    def feed(self):
        Pet.feed(self)
        print("Arf! Thanks!")

class Bird(Pet):
    sounds = ["chirp"]
    def __init__(self, name="Kitty", chirp_number=2):
        Pet.__init__(self, name) # call the parent class's constructor
        # basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
        self.chirp_number = chirp_number # now, also assign the new instance variable

    def hi(self):
        for i in range(self.chirp_number):
            print(self.sounds[randrange(len(self.sounds))])
        self.update_boredom()

class Lab(Dog):
    def fetch(self):
        return "I found the tennis ball!"

    def hi(self):
        print(self.fetch())
        print(self.sounds[randrange(len(self.sounds))])

class Poodle(Dog):
    def dance(self):
        return "Dancin' in circles like poodles do."

    def hi(self):
        print(self.dance())
        Dog.hi(self)

def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None # no pet matched

pet_types = {'dog': Dog, 'lab': Lab, 'poodle': Poodle, 'cat': Cat, 'bird': Bird}
def whichtype(adopt_type="general pet"):
    return pet_types.get(adopt_type.lower(), Pet)

def play():
    animals = []

    option = ""
    base_prompt = """
        Quit
        Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: """
    feedback = ""
    while True:
        action = input(feedback + "\n" + base_prompt)
        feedback = ""
        words = action.split()
        if len(words) > 0:
            command = words[0]
        else:
            command = None
        if command == "Quit":
            print("Exiting...")
            return
        elif command == "Adopt" and len(words) > 1:
            if whichone(animals, words[1]):
                feedback += "You already have a pet with that name\n"
            else:
                # figure out which class it should be
                if len(words) > 2:
                    Cl = whichtype(words[2])
                else:
                    Cl = Pet
                # Make an instance of that class and append it
                animals.append(Cl(words[1]))
        elif command == "Greet" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again.\n"
                print()
            else:
                pet.hi()
        elif command == "Teach" and len(words) > 2:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.teach(words[2])
        elif command == "Feed" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.feed()
        else:
            feedback+= "I didn't understand that. Please try again."

        for pet in animals:
            pet.clock_tick()
            feedback += "\n" + pet.__str__()

play()
```

**Output** :

```

        Quit
        Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: Adopt Weirdo cat

     I'm Weirdo.  I feel happy.

        Quit
        Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: Greet Weirdo
Meow

     I'm Weirdo.  I feel happy.

        Quit
        Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: Teach Weirdo Puff

     I'm Weirdo.  I feel grumpy; leave me alone.

        Quit
        Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: Feed Weirdo

     I'm Weirdo.  I feel happy.

        Quit
        Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: Greet Weirdo
Puff

     I'm Weirdo.  I feel grumpy; leave me alone.

        Quit
        Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: Greet Weirdo
Meow

     I'm Weirdo.  I feel grumpy; leave me alone.

        Quit
        Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: Teach Weirdo Hofff

     I'm Weirdo.  I feel grumpy; leave me alone.

        Quit
        Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: Feed Weirdo

     I'm Weirdo.  I feel happy.

        Quit
        Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: Quit
Exiting...
```


-------
--------

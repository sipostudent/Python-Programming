### Introducing Lists ###

## What is a list? ##

""" A list is a collection of items in a particular order. You can make a list that
includes the letters of the alphabet, the digits from 0–9, or the names of
all the people in your family. You can put anything you want into a list, and 
the items in your list don’t have to be related in any particular way. Because
a list usually contains more than one element, it’s a good idea to make the
name of your list plural, such as letters, digits, or names.
In Python, square brackets ([]) indicate a list, and individual elements
in the list are separated by commas. Here’s a simple example of a list that
contains a few kinds of bicycles: """

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)

# Result: ['trek', 'cannondale', 'redline', 'specialized']


## Accessing Elements in a List ##

""" Lists are ordered collections, so you can access any element in a list by
telling Python the position, or index, of the item desired. To access an element in a list, 
write the name of the list followed by the index of the item
enclosed in square brackets.
For example, let’s pull out the first bicycle in the list bicycles: """

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

# Result: trek


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

# Result: Trek

""" This example produces the same output as the preceding example
except 'Trek' is capitalized. """


# Index Positions Start at 0, Not 1

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])

# This code returns the second and fourth bicycles in the list:

""" Result: 
cannondale
specialized
"""

""" Python has a special syntax for accessing the last element in a list. 
By asking for the item at index -1, Python always returns the last item in the list: """

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

""" This code returns the value 'specialized'. This syntax is quite useful,
because you’ll often want to access the last items in a list without knowing
exactly how long the list is. This convention extends to other negative index
values as well. The index -2 returns the second item from the end of the list,
the index -3 returns the third item from the end, and so forth. """

## Using Individual Values from a List ##

""" You can use individual values from a list just as you would any other variable. 
For example, you can use f-strings to create a message based on a
value from a list.
Let’s try pulling the first bicycle from the list and composing a message
using that value. """

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)

""" Here, we build a sentence using the value at bicycles[0] and assign it to
the variable message. The output is a simple sentence about the first bicycle
in the list: """

# Result: My first bicycle was a Trek.


# TRY IT YOURSELF

""" 3-1. Names: Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time. """

friend_name = ['harry', 'sally', 'bill', 'jill']
print(friend_name[0].title())
print(friend_name[1].title())
print(friend_name[2].title())
print(friend_name[3].title())

""" 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the
person’s name. """

friend_name = ['harry', 'sally', 'bill', 'jill']
message = f"In year 7, {friend_name[0].title()} was a good friend of mine."
print(message)

message = f"In year 7, {friend_name[1].title()} was a good friend of mine."
print(message)

message = f"In year 7, {friend_name[2].title()} was a good friend of mine."
print(message)

message = f"In year 7, {friend_name[3].title()} was a good friend of mine."
print(message)

""" 3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.” """

transportation_mode = ['planes', 'cars', 'ships']

favorite = transportation_mode[0].title()
print(favorite + ", are my first favorite mode of transportation.")

favorite = transportation_mode[1].title()
print(favorite + ", are my second favorite mode of transportation.")

favorite = transportation_mode[2].title()
print(favorite + ", are my third favorite mode of transportation.")

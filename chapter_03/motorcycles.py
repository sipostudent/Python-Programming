### Changing, Adding, and Removing Elements ###

""" Most lists you create will be dynamic, meaning you’ll build a list and
then add and remove elements from it as your program runs its course. For
example, you might create a game in which a player has to shoot aliens out
of the sky. You could store the initial set of aliens in a list and then remove
an alien from the list each time one is shot down. Each time a new alien
appears on the screen, you add it to the list. Your list of aliens will increase
and decrease in length throughout the course of the game.  """

## Modifying Elements in a List ##

""" The syntax for modifying an element is similar to the syntax for accessing
an element in a list. To change an element, use the name of the list followed
by the index of the element you want to change, and then provide the new
value you want that item to have. """

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

""" The code at defines the original list, with 'honda' as the first element.
The code changes the value of the first item to 'ducati'. The output
shows that the first item has indeed been changed, and the rest of the list
stays the same: """

""" Result: 
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki'] """

# You can change the value of any item in a list, not just the first item.


# Adding Elements to a List

""" You might want to add a new element to a list for many reasons. For
example, you might want to make new aliens appear in a game, add new
data to a visualization, or add new registered users to a website you’ve
built. Python provides several ways to add new data to existing lists. """

# Appending Elements to the End of a List

""" The simplest way to add a new element to a list is to append the item to the
list. When you append an item to a list, the new element is added to the end
of the list. Using the same list we had in the previous example, we’ll add the
new element 'ducati' to the end of the list: """

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

""" The append() method at u adds 'ducati' to the end of the list without
affecting any of the other elements in the list: """

""" Result: 
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']
"""

""" The append() method makes it easy to build lists dynamically. For
example, you can start with an empty list and then add items to the list
using a series of append() calls. Using an empty list, let’s add the elements
'honda', 'yamaha', and 'suzuki' to the list: """

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# The resulting list looks exactly the same as the lists in the previous examples:

# Result: ['honda', 'yamaha', 'suzuki']

""" Building lists this way is very common, because you often won’t know
the data your users want to store in a program until after the program is
running. To put your users in control, start by defining an empty list that
will hold the users’ values. Then append each new value provided to the list
you just created. """

# Inserting Elements into a List

""" You can add a new element at any position in your list by using the insert()
method. You do this by specifying the index of the new element and the
value of the new item. """

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

""" In this example, the code inserts the value 'ducati' at the beginning of the list. The insert() method opens a space at position 0 and stores
the value 'ducati' at that location. This operation shifts every other value
in the list one position to the right: """

# Result: ['ducati', 'honda', 'yamaha', 'suzuki']


# Removing Elements from a List

""" Often, you’ll want to remove an item or a set of items from a list. For
example, when a player shoots down an alien from the sky, you’ll most
likely want to remove it from the list of active aliens. Or when a user 
decides to cancel their account on a web application you created, you’ll
want to remove that user from the list of active users. You can remove an
item according to its position in the list or according to its value. """


# Removing an Item Using the del Statement

""" If you know the position of the item you want to remove from a list, you can
use the del statement. """

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

""" The code uses del to remove the first item, 'honda', from the list of
motorcycles: """

""" Result:
['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki'] 
"""

""" You can remove an item from any position in a list using the del statement if you know its index. 
For example, here’s how to remove the second item, 'yamaha', in the list: """

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# The second motorcycle is deleted from the list:

""" Result:
['honda', 'yamaha', 'suzuki']
['honda', 'suzuki']
"""

""" In both examples, you can no longer access the value that was removed
from the list after the del statement is used. """


# Removing an Item Using the pop() Method

""" Sometimes you’ll want to use the value of an item after you remove it from a
list. For example, you might want to get the x and y position of an alien that
was just shot down, so you can draw an explosion at that position. In a web
application, you might want to remove a user from a list of active members
and then add that user to a list of inactive members.
The pop() method removes the last item in a list, but it lets you work
with that item after removing it. The term pop comes from thinking of a
list as a stack of items and popping one item off the top of the stack. In
this analogy, the top of a stack corresponds to the end of a list. """

# Let’s pop a motorcycle from the list of motorcycles:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

""" We start by defining and printing the list motorcycles. We pop
a value from the list and store that value in the variable popped_motorcycle.
We print the list to show that a value has been removed from the list.
Then we print the popped value to prove that we still have access to
the value that was removed.
The output shows that the value 'suzuki' was removed from the end of
the list and is now assigned to the variable popped_motorcycle: """

['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
# suzuki

""" How might this pop() method be useful? Imagine that the motorcycles
in the list are stored in chronological order according to when we owned
them. If this is the case, we can use the pop() method to print a statement
about the last motorcycle we bought: """

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# The output is a simple sentence about the most recent motorcycle we owned:

# Result: The last motorcycle I owned was a Suzuki.


# Popping Items from any Position in a List

""" You can use pop() to remove an item from any position in a list by including
the index of the item you want to remove in parentheses. """

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

""" We start by popping the first motorcycle in the list, and then we
print a message about that motorcycle. The output is a simple sentence
describing the first motorcycle I ever owned: """


# Result: The first motorcycle I owned was a Honda.

""" Remember that each time you use pop(), the item you work with is no
longer stored in the list.
If you’re unsure whether to use the del statement or the pop() method,
here’s a simple way to decide: when you want to delete an item from a list
and not use that item in any way, use the del statement; if you want to use an
item as you remove it, use the pop() method. """


# Removing an Item by Value

""" Sometimes you won’t know the position of the value you want to remove
from a list. If you only know the value of the item you want to remove, you
can use the remove() method.
For example, let’s say we want to remove the value 'ducati' from the list of
motorcycles. """

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

""" The code Python to figure out where 'ducati' appears in the
list and remove that element: """

""" Result:
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki'] 
"""

""" You can also use the remove() method to work with a value that’s being
removed from a list. Let’s remove the value 'ducati' and print a reason for
removing it from the list: """

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

""" After defining the list, we assign the value 'ducati' to a variable
called too_expensive. We then use this variable to tell Python which value
to remove from the list. The value 'ducati' has been removed 
from the list but is still accessible through the variable too_expensive, 
allowing us to print a statement about why we removed 'ducati' from the list of
motorcycles: """

""" Result: 
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']

A Ducati is too expensive for me."""


""" Note: 
The remove() method deletes only the first occurrence of the value you specify. If there’s
a possibility the value appears more than once in the list, you’ll need to use a loop
to make sure all occurrences of the value are removed. You’ll learn how to do this in
Chapter 7. 
"""

# TRY IT YOURSELF

""" 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner. """

guests = ['sam', 'pam', 'tam']

name = guests[0].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")

name = guests[1].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")

name = guests[2].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")


""" 3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.

•	 Start with your program from Exercise 3-4. Add a print() call at the end
of your program stating the name of the guest who can’t make it.
•	 Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
•	 Print a second set of invitation messages, one for each person who is still
in your list. """

guests = ['sam', 'pam', 'tam']

name = guests[0].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")

name = guests[1].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")

name = guests[2].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")

name = guests[1].title()
print(
    f"\nDue to prior engagements, {name.title()} will not be in attendance.\n")

del(guests[1])
guests.insert(1, 'Jimmy')

name = guests[0].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")

name = guests[1].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")

name = guests[2].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")


""" 3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.

Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
call to the end of your program informing people that you found a bigger
dinner table.

•	 Use insert() to add one new guest to the beginning of your list.
•	 Use insert() to add one new guest to the middle of your list.
•	 Use append() to add one new guest to the end of your list.
•	 Print a new set of invitation messages, one for each person in your list. """

name = guests[0].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")

name = guests[1].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")

name = guests[2].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")

# Extra dining table seats available, so let's add some more people to the list.
print(f"\nNews just in, extra dining seats are now available.\n")

guests.insert(0, 'timmy')
guests.insert(2, 'billy')
guests.append('jilly')
print(guests)

name = guests[0].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")

name = guests[1].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")

name = guests[2].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")

name = guests[3].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")

name = guests[4].title()
print(f"Dear {name.title()}, you are invited to dinner at my house.")


""" 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.

•	 Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.

•	 Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.

•	 Print a message to each of the two people still on your list, letting them
know they’re still invited.

•	 Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program. """

name = guests.pop()
print(f"Sorry {name.title()}, but I can invite only two people for dinner.")

name = guests.pop()
print(f"Sorry {name.title()}, but I can invite only two people for dinner.")

name = guests.pop()
print(f"Sorry {name.title()}, but I can invite only two people for dinner.")


# There should be two people left. Let's invite them.
name = guests[0].title()
print(f"Dear {name.title()}, please consider yourself still invited to my dinner party.")

name = guests[1].title()
print(f"Dear {name.title()}, please consider yourself still invited to my dinner party.")

del(guests[0])
del(guests[0])
del(guests[0])

print(guests)
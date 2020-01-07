# Looping Through an Entire List

""" Let’s say we have a list of magicians’ names, and we want to print out
each name in the list. We could do this by retrieving each name from the
list individually, but this approach could cause several problems. For one,
it would be repetitive to do this with a long list of names. Also, we’d have to
change our code each time the list’s length changed. A for loop avoids both
of these issues by letting Python manage these issues internally.
Let’s use a for loop to print out each name in a list of magicians: """

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

""" 
# 1. We begin by defining a list, just as we did in Chapter 3.

# 2. We define a for loop. This line tells Python to pull a name from the list
magicians, and associate it with the variable magician. 

# 3. We tell Python to print the name that’s just been assigned to magician. 
Python then repeats lines v and w, once for each name in the list. 

It might help to read this code as “For every magician in the list of magicians, 
print the magician’s name.” The output is a simple printout of each name in the list:
"""

""" Result:
alice
david
carolina
"""

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

# A Closer Look at Looping

""" 
The concept of looping is important because it’s one of the most common
ways a computer automates repetitive tasks. For example, in a simple loop
like we used in magicians.py, Python initially reads the first line of the loop:

for magician in magicians:

    This line tells Python to retrieve the first value from the list magicians
and associate it with the variable magician. This first value is 'alice'. Python
then reads the next line:

print(magician)

    Python prints the current value of magician, which is still 'alice'. Because
the list contains more values, Python returns to the first line of the loop:

for magician in magicians:

    Python retrieves the next name in the list, 'david', and associates that
value with the variable magician. Python then executes the line:

print(magician)
 """

""" Also keep in mind when writing your own for loops that you can choose
any name you want for the temporary variable that will be associated with
each value in the list. However, it’s helpful to choose a meaningful name
that represents a single item from the list. For example, here’s a good way to
start a for loop for a list of cats, a list of dogs, and a general list of items:

for cat in cats:
for dog in dogs:
for item in list_of_items: """

# Doing More Work Within a for Loop

""" You can do just about anything with each item in a for loop. Let’s build on
the previous example by printing a message to each magician, telling them
that they performed a great trick: """

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

""" The only difference in this code is where we compose a message to
each magician, starting with that magician’s name. The first time through
the loop the value of magician is 'alice', so Python starts the first message
with the name 'Alice'. The second time through the message will begin with
'David', and the third time through the message will begin with 'Carolina'.
The output shows a personalized message for each magician in the list: """

""" Result:
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick! """


""" You can also write as many lines of code as you like in the for loop.
Every indented line following the line for magician in magicians is considered inside the loop, 
and each indented line is executed once for each value in the list. 
Therefore, you can do as much work as you like with each value in the list.
Let’s add a second line to our message, telling each magician that we’re
looking forward to their next trick: """

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

""" Because we have indented both calls to print(), each line will be executed
once for every magician in the list. The newline ("\n") in the second print()
call inserts a blank line after each pass through the loop. This creates a set
of messages that are neatly grouped for each person in the list: """


""" Result:
Alice, that was a great trick!
I can't wait to see your next trick, Alice.
David, that was a great trick!
I can't wait to see your next trick, David.
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina. """


# Doing Something After a for Loop

""" What happens once a for loop has finished executing? Usually, you’ll want
to summarize a block of output or move on to other work that your program must accomplish.
    Any lines of code after the for loop that are not indented are executed
once without repetition. Let’s write a thank you to the group of magicians
as a whole, thanking them for putting on an excellent show. To display this
group message after all of the individual messages have been printed, we
place the thank you message after the for loop without indentation: """


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you, everyone. That was a great magic show!")

""" Result:
Alice, that was a great trick!
I can't wait to see your next trick, Alice.
David, that was a great trick!
I can't wait to see your next trick, David.
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
Thank you, everyone. That was a great magic show!
"""

# Forgetting to Indent

""" Always indent the line after the for statement in a loop. If you forget, Python
will remind you: """

""" The call to print() u should be indented, but it’s not. When Python
expects an indented block and doesn’t find one, it lets you know which line
it had a problem with. """

""" LACKS INDENTATION - INCORRECT
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)
"""

""" HAS INDENTATION - CORRECT
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
"""

# Forgetting to Indent Additional Lines

""" Sometimes your loop will run without any errors but won’t produce the
expected result. This can happen when you’re trying to do several tasks in
a loop and you forget to indent some of its lines.
For example, this is what happens when we forget to indent the second
line in the loop that tells each magician we’re looking forward to their next
trick: """

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

""" The call to print() u is supposed to be indented, but because Python
finds at least one indented line after the for statement, it doesn’t report an
error. As a result, the first print() call is executed once for each name in the
list because it is indented. The second print() call is not indented, so it is
executed only once after the loop has finished running. Because the final
value associated with magician is 'carolina', she is the only one who receives
the “looking forward to the next trick” message: """

""" Result:
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina. """

""" This is a logical error. The syntax is valid Python code, but the code does
not produce the desired result because a problem occurs in its logic. If you
expect to see a certain action repeated once for each item in a list and it’s
executed only once, determine whether you need to simply indent a line or
a group of lines. """


# Indenting Unnecessarily After the Loop

""" If you accidentally indent code that should run after a loop has finished, that
code will be repeated once for each item in the list. Sometimes this prompts
Python to report an error, but often this will result in a logical error.
For example, let’s see what happens when we accidentally indent the
line that thanked the magicians as a group for putting on a good show: """

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you everyone, that was a great magic show!")

""" Because the last print line is indented, it’s printed once for each person in
the list, as shown here: """


""" Result:
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

Thank you everyone, that was a great magic show!
David, that was a great trick!
I can't wait to see your next trick, David.

Thank you everyone, that was a great magic show!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you everyone, that was a great magic show! """


""" This is another logical error, similar to the one in “Forgetting to Indent
Additional Lines” on page 54. Because Python doesn’t know what you’re
trying to accomplish with your code, it will run all code that is written in
valid syntax. If an action is repeated many times when it should be executed
only once, you probably need to unindent the code for that action. """


# Forgetting the Colon

""" The colon at the end of a for statement tells Python to interpret the next
line as the start of a loop. """

magicians = ['alice', 'david', 'carolina']
for magician in magicians
    print(magician)

""" Result:
  File "magicians.py", line 251
    for magician in magicians
                            ^
SyntaxError: invalid syntax 
"""

""" If you accidentally forget the colon, as shown at u, you’ll get a syntax
error because Python doesn’t know what you’re trying to do. Although
this is an easy error to fix, it’s not always an easy error to find. You’d be
surprised by the amount of time programmers spend hunting down singlecharacter errors like this. Such errors are difficult to find because we often
just see what we expect to see. """


# TRY IT YOURSELF

""" 4-1. Pizzas:  Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza. 

# Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza you should
have one line of output containing a simple statement like I like pepperoni
pizza.

# Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza! """

favorite_pizza = [chicken, hawaiian, beef]



""" 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.

# Modify your program to print a statement about each animal, such as
A dog would make a great pet.

# Add a line at the end of your program stating what these animals have in
common. You could print a sentence such as Any of these animals would
make a great pet! """

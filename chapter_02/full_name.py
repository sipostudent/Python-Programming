### Sipo Charles - 25/12/2019 ###

## Variables and Simple Data Types ##

""" In some situations, you’ll want to use a variable’s value inside a string. For
example, you might want two variables to represent a first name and a last
name respectively, and then want to combine those values to display someone’s full name: """

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# Result : ada lovelace

""" To insert a variable’s value into a string, place the letter f immediately
before the opening quotation mark. Put braces around the name or names
of any variable you want to use inside the string. Python will replace each
variable with its value when the string is displayed.
These strings are called f-strings. The f is for format, because Python
formats the string by replacing the name of any variable in braces with its
value.  """


""" You can do a lot with f-strings. For example, you can use f-strings to
compose complete messages using the information associated with a variable, as shown here: """

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

""" The full name is used in a sentence that greets the user, and the
title() method changes the name to title case. This code returns a simple
but nicely formatted greeting: """

# Result: Hello, Ada Lovelace!


""" You can also use f-strings to compose a message, and then assign the
entire message to a variable: """

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

""" This code displays the message Hello, Ada Lovelace! as well, but by
assigning the message to a variable we make the final print() call much
simpler """

""" F-strings were first introduced in Python 3.6. If you’re using Python 3.5 or earlier,
you’ll need to use the format() method rather than this f syntax. To use format(), list
the variables you want to use in the string inside the parentheses following format.
Each variable is referred to by a set of braces; the braces will be filled by the values
listed in parentheses in the order provided: """

full_name = "{} {}".format(first_name, last_name)

""" For additional information, refer to official Python documentation 
which is located at www.python.org """
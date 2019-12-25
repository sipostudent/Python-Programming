### Sipo Charles - 25/12/2019 ###

## Variables and Simple Data Types ##

name = "Ada Lovelace"
print(name.upper())
print(name.lower())
print(name.title())

""" Result:
ADA LOVELACE
ada lovelace
Ada Lovelace """

""" The title() method changes each word to title case, where each word
begins with a capital letter. This is useful because you’ll often want to think
of a name as a piece of information. For example, you might want your program to recognize the input values Ada, ADA, and ada as the same name, and
display all of them as Ada. """

""" The lower() method is particularly useful for storing data. Many times
you won’t want to trust the capitalization that your users provide, so you’ll
convert strings to lowercase before storing them. Then when you want to
display the information, you’ll use the case that makes the most sense for
each string. """
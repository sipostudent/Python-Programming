### Sipo Charles - 25/12/2019 ###

## Variables and Simple Data Types ##

""" 2-7. Stripping Names: Use a variable to represent a person’s name, and include
some whitespace characters at the beginning and end of the name. Make sure
you use each character combination, "\t" and "\n", at least once.
    Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip(). """

name = ' jon \t"bones" \njones  '
print(name.title)
print(name.title().rstrip())
print(name.title().lstrip())
print(name.title().strip())
# Indenting Unnecessarily

""" If you accidentally indent a line that doesn’t need to be indented, Python
informs you about the unexpected indent: """

message = "Hello Python world!"
    print(message)

""" We don’t need to indent the print() call u, because it isn’t part of a
loop; hence, Python reports that error: """

""" Error message:
  File "hello_world.py", line 7
    print(message)
    ^
IndentationError: unexpected indent """

""" You can avoid unexpected indentation errors by indenting only when
you have a specific reason to do so. In the programs you’re writing at this
point, the only lines you should indent are the actions you want to repeat
for each item in a for loop. """


# Sipo Charles - 24/12/2019

# Avoiding Type Errors with the str() Function

# age = 23
# message = "Happy " + age + "rd Birthday!"

# print(message)

# Result: TypeError: can only concatenate str (not "int") to str

age = 23
message = "Happy " + str(age) + "rd Birthday!"

print(message)

# Result: Happy 23rd Birthday!

# TRY IT YOURSELF

""" 2-8. Number Eight:
Write addition, subtraction, multiplication, and division operations 
that each result in the number 8. Be sure to enclose your operations in print statements 
to see the results. 
You should create four lines that look like this: print(5 + 3) """

print(5 + 3)
print(16 - 8)
print(4 * 2)
print(48 / 6)

""" 2-9. Favourite Number: Store your favorite number in a variable. 
Then, using that variable, create a message that reveals your favorite number. 
Print that message """

favorite_number = 32
message = "My favorite number is " + str(favorite_number)

print(message)

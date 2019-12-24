# Sipo Charles - 24/12/2019

# Changing Case in a String with Methods

name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())

"""Result: 
1. Ada Lovelace
2. ADA LOVELACE
3. ada lovelace"""

# Combining or Concatenating Strings

# Example 1:

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

# Result: ada lovelace


# Example 2: message not stored inside a variable

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print("Hello, " + full_name.title() + "!")

# Result: Hello, Ada Lovelace!


# Example 3: message is stored inside a variable

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

message = "Hello, " + full_name.title() + "!"
print(message)

# Result: Hello, Ada Lovelace!

# Sipo Charles - 24/12/2019

# TRY IT YOURSELF

# 1. Personal Message

first_name = "steve"
last_name = "johnson"
full_name = first_name + " " + last_name

message = "Hello, " + full_name.title() + ", " + \
    "would you like to learn some Python today?"
print(message)

# 2. Name cases

name = "betty rogers"
print(name.title())
print(name.upper())
print(name.lower())

# 3. Famous Quote 1:

famous_forename = "muhammed"
famous_surname = "ali"
famous_quote = "'float like a butterfly, sting like a bee'"

print(famous_forename.title() + " " + famous_surname.title() + " once said " + famous_quote.format(famous_quote))

# 4. Famous Quote 2:

famous_forename = "muhammed"
famous_surname = "ali"
famous_person = famous_forename + " " + famous_surname
famous_quote = "'float like a butterfly, sting like a bee'"

famous_quote = famous_person.title() + " once said " + famous_quote.format(famous_quote)

print(famous_quote)

# 5. Stripping Names:

person_name = " John Smith  "

print(person_name)

person_name = " John Smith  "
person_name = person_name.lstrip()

print(person_name)

person_name = " John Smith  "
person_name = person_name.rstrip()

print(person_name)

person_name = " John Smith  "
person_name = person_name.strip()

print(person_name)



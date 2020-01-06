### Sipo Charles - 25/12/2019 ###

### Organizing a List ###

""" Often, your lists will be created in an unpredictable order, because you can’t always control 
the order in which your users provide their data. Although this is unavoidable in most circumstances, 
you’ll frequently want to present your information in a particular order. Sometimes you’ll want to 
preserve the original order of your list, and other times you’ll want to change the original order. 
Python provides a number of different ways to organize your lists, depending on the situation. """


# Sorting a List Permanently with the sort() Method

""" Python’s sort() method makes it relatively easy to sort a list. 
Imagine we have a list of cars and want to change the order of the list 
to store them alphabetically. To keep the task simple, let’s assume that 
all the values in the list are lowercase. """

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

""" The sort() method, changes the order of the list permanently. 
The cars are now in alphabetical order, and we can never revert to
the original order: """

""" Result:
['audi', 'bmw', 'subaru', 'toyota'] 
"""

""" You can also sort this list in reverse alphabetical order by passing the
argument reverse=True to the sort() method. The following example sorts
the list of cars in reverse alphabetical order: """

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Again, the order of the list is permanently changed:

""" Result:
['toyota', 'subaru', 'bmw', 'audi'] 
"""


print("______________________________")  # Separator


# Sorting a List Temporarily with the sorted() Function

""" To maintain the original order of a list but present it in a sorted order, you
can use the sorted() function. The sorted() function lets you display your list
in a particular order but doesn’t affect the actual order of the list.
Let’s try this function on the list of cars. """

# List: cars
cars = ['bmw', 'audi', 'toyota', 'subaru']

# 1. We first print the list in its original order
print("Here is the original list:")
print(cars)

# 2. Then in alphabetical order. 
print("\nHere is the sorted list:")
print(sorted(cars))

# 3. After the list is displayed in the new order, we show that the list is still stored in its original order. 
print("\nHere is the original list again:")
print(cars)

""" Result:
Here is the original list:
['bmw', 'audi', 'toyota', 'subaru']
Here is the sorted list:
['audi', 'bmw', 'subaru', 'toyota']
x Here is the original list again:
['bmw', 'audi', 'toyota', 'subaru']
"""

""" Notice that the list still exists in its original order at after the sorted()
function has been used. The sorted() function can also accept a reverse=True
argument if you want to display a list in reverse alphabetical order. """

# Printing a List in Reverse Order

""" To reverse the original order of a list, you can use the reverse() method.
If we originally stored the list of cars in chronological order according to
when we owned them, we could easily rearrange the list into reverse chronological order: """

# List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

""" Notice that reverse() doesn’t sort backward alphabetically; it simply
reverses the order of the list: """

""" Result: 
['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw'] 
"""

""" The reverse() method changes the order of a list permanently, but you
can revert to the original order anytime by applying reverse() to the same
list a second time. """

# Finding the Length of a List

""" You can quickly find the length of a list by using the len() function. The list
in this example has four items, so its length is 4: """

""" Result:
>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> len(cars)
4   
"""

""" You’ll find len() useful when you need to identify the number of aliens
that still need to be shot down in a game, determine the amount of data
you have to manage in a visualization, or figure out the number of registered 
users on a website, among other tasks. """



### Changing, Adding, and Removing Elements ###

""" Most lists you create will be dynamic, meaning you’ll build a list and
then add and remove elements from it as your program runs its course. For
example, you might create a game in which a player has to shoot aliens out
of the sky. You could store the initial set of aliens in a list and then remove
an alien from the list each time one is shot down. Each time a new alien
appears on the screen, you add it to the list. Your list of aliens will increase
and decrease in length throughout the course of the game.  """

## Modifying Elements in a List ##

""" The syntax for modifying an element is similar to the syntax for accessing
an element in a list. To change an element, use the name of the list followed
by the index of the element you want to change, and then provide the new
value you want that item to have. """

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

""" The code at defines the original list, with 'honda' as the first element.
The code changes the value of the first item to 'ducati'. The output
shows that the first item has indeed been changed, and the rest of the list
stays the same: """

""" Result: 
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki'] """

# You can change the value of any item in a list, not just the first item.


## Adding Elements to a List

""" You might want to add a new element to a list for many reasons. For
example, you might want to make new aliens appear in a game, add new
data to a visualization, or add new registered users to a website you’ve
built. Python provides several ways to add new data to existing lists. """

## Appending Elements to the End of a List

""" The simplest way to add a new element to a list is to append the item to the
list. When you append an item to a list, the new element is added to the end
of the list. Using the same list we had in the previous example, we’ll add the
new element 'ducati' to the end of the list: """

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

""" For additional information, refer to official Python documentation 
which is located at www.python.org """
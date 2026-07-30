st = ()
# empty {} will result in the creation of an empty dictionary, not an empty set. To create an empty set, you must use the set() function.

fruits = {"lime", "cherry", "banana", "pear"}
len(fruits)  # Output: 4

# c checking if an item is in a set
fruits = {"lime", "cherry", "banana", "pear"}
print("lime" in fruits)  # Output: True
print("apple" in fruits)  # Output: False

# adding an item to a set
fruits.add("apple")
print(fruits)  # Output: {'apple', 'cherry', 'banana', 'pear', 'lime'}
# once a set is created, you cannot change its items, but you can add new items.

# update()
fruits = {"lime", "cherry", "banana", "pear"}
veg = {"carrot", "broccoli", "spinach", "cabbage"}
fruits.update(veg)
print(fruits)
print(fruits | veg)  # Output: {'lime', 'cherry', 'banana', 'pear', 'carrot', 'broccoli', 'spinach', 'cabbage'}

# removing an item from a set
fruits.remove("lime")
print(fruits)  # Output: {'cherry', 'banana', 'pear', 'carrot', 'broccoli', 'spinach', 'cabbage'}

# pop. it pops a random item from the set, since sets are unordered, you will not know which item that gets removed.
fruits.pop()
popped = fruits.pop()
print(popped)  # Output: 'cherry'

# clear. it clears or empties the set. it does not delete the set itself, but it removes all items from the set.
fruits.clear()
print(fruits)  # Output: set()

# del
del fruits

# intersection. it returns a set that contains the items that exist in both sets.
whole = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even = {0, 2, 4, 6, 8, 10}
print(whole.intersection(even))  # Output: {0, 2, 4, 6, 8, 10}

# issubset. it returns True if all items in the set exist in the specified set, otherwise it returns False.
# issuperset. it returns True if all items in the specified set exist in the original set, otherwise it returns False.
whole.issubset(even)  # Output: False
whole.issuperset(even)  # Output: True

# difference. it returns a set that contains the items that exist in the original set
whole.difference(even)  # Output: {1, 3, 5, 7, 9}

# symmetric difference returns a set that contains all items in both sets except items that are present in both sets
# opposite of intersection
whole = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some = {1, 2, 3, 4, 5}
whole.symmetric_difference(some)  # Output: {0, 6, 7, 8, 9, 10}

# disjoint. it returns True if 2 sets have no common items set,it returns False.
even = {0, 2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9}
even.isdisjoint(odd)  # Output: True

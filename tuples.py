empty_tuple = ()
# or
tuple = tuple()

# accessing elements inside of a tuple by index
fruits = ("lime", "cheryy", "banana", "pear")
f_fruit = fruits[0]
print(f_fruit)  # Output: lime
s_fruit = fruits[1]
print(s_fruit)  # Output: cheryy
l_index = len(fruits) - 1
l_fruit = fruits[l_index]
print(l_fruit)  # Output: pear

# negative indexing
l_fruit = fruits[-1]
print(l_fruit)  # Output: pear
f_fruit = fruits[-4]
print(f_fruit)  # Output: lime
s_fruit = fruits[-3]
print(s_fruit)  # Output: cheryy
t_fruit = fruits[-2]
print(t_fruit)  # Output: banana

# slicing a tuple
fruits = ("lime", "cherry", "banana", "pear")
all_fruits = fruits[0:4]
print(all_fruits)  # Output: ('lime', 'cherry', 'banana', 'pear')
cb = fruits[1:3]
print(cb)  # Output: ('cherry', 'banana')
cba = fruits[1:4]
print(cba)  # Output: ('cherry', 'banana', 'pear')
lb = fruits[::2]
print(lb)  # Output: ('lime', 'banana')
all_fruits = fruits[-4:]
print(all_fruits)  # Output: ('lime', 'cherry', 'banana', 'pear')
cb = fruits[-3:-1]
print(cb)  # Output: ('cherry', 'banana')
cbp = fruits[-3:]
print(cbp)  # Output: ('cherry', 'banana', 'pear')
reverse = fruits[::-1]
print(reverse)  # Output: ('pear', 'banana', 'cherry', 'lime')

# converting a list to a tuple
fruits = list(fruits)
fruits[0] = "apple"
fruits = tuple(fruits)
print(fruits)  # Output: ('apple', 'cherry', 'banana', 'pear')

# joining tuple
fruits = ("lime", "cherry", "banana", "pear")
vegetables = ("carrot", "broccoli", "spinach", "cabbage")
fruits_and_vegetables = fruits + vegetables
print(
    fruits_and_vegetables
)  # Output: ('lime', 'cherry', 'banana', 'pear', 'carrot', 'broccoli', 'spinach')

# deleting tuple
del fruits
del vegetables
del fruits_and_vegetables
# print(fruits)  # Output: NameError: name 'fruits' is not defined
# print(vegetables)  # Output: NameError: name 'vegetables' is not defined

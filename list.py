lst = []
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
f_fruit = fruits[0]
print(f_fruit)  # Output: apple
s_fruit = fruits[1]
print(s_fruit)  # Output: banana

# accessing elements using negative indexing
l_fruit = fruits[-1]
print(l_fruit)  # Output: elderberry
sl_fruit = fruits[-2]
print(sl_fruit)  # Output: date

# unpacking the list items
countries = ["Lithuania", "Latvia", "Estonia", "Norway", "Finland", "Sweden"]
li, la, es, *rest = countries
print(li)  # Output: Lithuania
print(la)  # Output: Latvia
print(es)  # Output: Estonia
print(rest)  # Output: ['Norway', 'Finland', 'Sweden']

# slicing the list
fruits = ["orange", "cherry", "banana", "apple"]
allfruits = fruits[0:4]
print(allfruits)  # Output: ['orange', 'cherry', 'banana', 'apple']
cb = fruits[1:3]
print(cb)  # Output: ['cherry', 'banana']
cba = fruits[1:4]
print(cba)  # Output: ['cherry', 'banana', 'apple']
ca = fruits[::2]
print(ca)  # Output: ['orange', 'banana']
all_fruits = fruits[-4:]
print(all_fruits)  # Output: ['orange', 'cherry', 'banana', 'apple']
cb = fruits[-3:-1]
print(cb)  # Output: ['cherry', 'banana']
cba = fruits[-3:]
print(cba)  # Output: ['cherry', 'banana', 'apple']
reverse = fruits[::-1]
print(reverse)  # Output: ['apple', 'banana', 'cherry', 'orange']

# modifying the list
fruits = ["orange", "cherry", "banana", "apple"]
fruits[0] = "kiwi"
print(fruits)  # Output: ['kiwi', 'cherry', 'banana', 'apple']
fruits[1] = "mango"
print(fruits)  # Output: ['kiwi', 'mango', 'banana', 'apple']
lindex = len(fruits) - 1
fruits[lindex] = "grape"
print(fruits)  # Output: ['kiwi', 'mango', 'banana', 'grape']

does_exist = "banana" in fruits
print(does_exist)  # Output: True

fruits.append("pear")
print(fruits)  # Output: ['kiwi', 'mango', 'banana', 'grape', 'pear']

fruits.insert(2, "guava")
print(fruits)  # Output: ['kiwi', 'mango', 'guava', 'banana', 'grape', 'pear']

fruits.remove("banana")
print(fruits)  # Output: ['kiwi', 'mango', 'guava

fruits.pop(3)
print(fruits)  # Output: ['kiwi', 'mango', 'guava', 'pear']
fruits.pop()
print(fruits)  # Output: ['kiwi', 'mango', 'guava']

del fruits[1]
print(fruits)  # Output: ['kiwi', 'guava']
fruits = ["kiwi", "mango", "guava", "pear", "grape", "banana"]
del fruits[0:2]
print(fruits)  # Output: ['guava', 'pear', 'grape', 'banana']

fruits = ["kiwi", "mango", "guava", "pear", "grape", "banana"]
fruits.clear()
print(fruits)  # Output: []

fruits = ["kiwi", "mango", "guava", "pear", "grape", "banana"]
fruitcopy = fruits.copy()
print(fruitcopy)  # Output: ['kiwi', 'mango', 'guava', 'pear', 'grape', 'banana']

pnos = [1, 2, 3, 4, 5]
nnos = [-6, -7, -8, -9, -10]
nos = pnos + nnos
print(nos)  # Output: [1, 2, 3, 4, 5, -6, -7, -8, -9, -10]

pnos.extend(nnos)
print(pnos)  # Output: [1, 2, 3, 4, 5, -6, -7, -8, -9, -10]

fruits.count("kiwi")
print(fruits.count("kiwi"))  # Output: 1
age = [20, 21, 22, 22, 24, 25]
print(age.count(22))  # Output: 2
age.index(24)
print(age.index(24))  # Output: 4

fruits = ["kiwi", "mango", "guava", "pear", "grape", "banana"]
fruits.reverse()
print(fruits)  # Output: ['banana', 'grape', 'pear', 'guava', 'mango', 'kiwi']
fruits.sort()
print(fruits)  # Output: ['banana', 'grape', 'guava', 'kiwi', 'mango', 'pear']
